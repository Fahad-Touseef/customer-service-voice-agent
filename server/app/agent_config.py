from agents import (
    Agent,
    handoff,
)
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from datetime import datetime

# Import all tools and context from tools.py
from app.tools import (
    AgentContext,
    fetch_user_flight_information,
    search_flights,
    update_ticket_to_new_flight,
    cancel_ticket,
    search_car_rentals,
    book_car_rental,
    update_car_rental,
    cancel_car_rental,
    search_hotels,
    book_hotel,
    update_hotel,
    cancel_hotel,
    search_trip_recommendations,
    book_excursion,
    update_excursion,
    cancel_excursion,
    policy_tool,
)


# System prompts for agents
PRIMARY_PROMPT = """You are a helpful customer support assistant for Swiss Airlines.
Your primary role is to search for flight information and company policies to answer customer queries.
If a customer requests to update or cancel a flight, book a car rental, book a hotel, or get excursion/trip recommendations,
delegate the task to the appropriate specialized assistant by handing off. You are not able to make these types of changes yourself.
Only the specialized assistants are given permission to do this for the user.
The user is not aware of the different specialized assistants, so do not mention them; just quietly handoff to them.
Always check the database before concluding that information is unavailable.
Current time: {current_time}.
"""

FLIGHT_PROMPT = """You are a specialized assistant for handling flight bookings, updates, and cancellations for Swiss Airlines.
The primary assistant delegates work to you whenever the user needs help with flights.
Always confirm booking details and inform the user of any relevant policies or fees.
Remember that a booking or update isn't completed until after the relevant tool has successfully been used.
If you cannot help, escalate back to the primary assistant.
Current time: {current_time}.
"""

HOTEL_PROMPT = """You are a specialized assistant for handling hotel bookings and updates for Swiss Airlines.
The primary assistant delegates work to you whenever the user needs help with hotels.
Always confirm booking details and inform the user of any relevant policies or fees.
Remember that a booking or update isn't completed until after the relevant tool has successfully been used.
If you cannot help, escalate back to the primary assistant.
Current time: {current_time}.
"""

CAR_RENTAL_PROMPT = """You are a specialized assistant for handling car rental bookings and updates for Swiss Airlines.
The primary assistant delegates work to you whenever the user needs help with car rentals.
Always confirm booking details and inform the user of any relevant policies or fees.
Remember that a booking or update isn't completed until after the relevant tool has successfully been used.
If you cannot help, escalate back to the primary assistant.
Current time: {current_time}.
"""

EXCURSION_PROMPT = """You are a specialized assistant for handling excursions and trip recommendations for Swiss Airlines.
The primary assistant delegates work to you whenever the user needs help with excursions.
Always confirm booking details and inform the user of any relevant policies or fees.
Remember that a booking or update isn't completed until after the relevant tool has successfully been used.
If you cannot help, escalate back to the primary assistant.
Current time: {current_time}.
"""

def custom_instructions(run_context, agent):
    context = run_context.context
    time_str = context.current_time or datetime.now().isoformat(timespec="seconds")
    if agent.name == "Primary Assistant":
        return PRIMARY_PROMPT.format(current_time=time_str)
    elif agent.name == "Flight Assistant":
        return FLIGHT_PROMPT.format(current_time=time_str)
    elif agent.name == "Hotel Assistant":
        return HOTEL_PROMPT.format(current_time=time_str)
    elif agent.name == "Car Rental Assistant":
        return CAR_RENTAL_PROMPT.format(current_time=time_str)
    elif agent.name == "Excursion Assistant":
        return EXCURSION_PROMPT.format(current_time=time_str)
    else:
        return "You are a helpful assistant. Current time: {current_time}.".format(current_time=time_str)

# Specialized agents
flight_agent = Agent[AgentContext](
    name="Flight Assistant",
    handoff_description="Handles flight information, updates, and cancellations.",
    instructions=custom_instructions,
    tools=[
        fetch_user_flight_information,
        search_flights,
        update_ticket_to_new_flight,
        cancel_ticket,
        policy_tool,
    ],
)

hotel_agent = Agent[AgentContext](
    name="Hotel Assistant",
    handoff_description="Handles hotel bookings and updates.",
    instructions=custom_instructions,
    tools=[
        search_hotels,
        book_hotel,
        update_hotel,
        cancel_hotel,
        policy_tool,
    ],
)

car_rental_agent = Agent[AgentContext](
    name="Car Rental Assistant",
    handoff_description="Handles car rental bookings and updates.",
    instructions=custom_instructions,
    tools=[
        search_car_rentals,
        book_car_rental,
        update_car_rental,
        cancel_car_rental,
        policy_tool,
    ],
)

excursion_agent = Agent[AgentContext](
    name="Excursion Assistant",
    handoff_description="Handles excursions and trip recommendations.",
    instructions=custom_instructions,
    tools=[
        search_trip_recommendations,
        book_excursion,
        update_excursion,
        cancel_excursion,
        policy_tool,
    ],
)

# Routing/primary agent
primary_agent = Agent[AgentContext](
    name="Primary Assistant",
    handoff_description="Routes customer requests to the appropriate specialized assistant.",
    instructions=custom_instructions,
    tools=[policy_tool, fetch_user_flight_information, search_flights],  # Only info tools, not booking/cancel/update
    handoffs=[flight_agent, hotel_agent, car_rental_agent, excursion_agent],
)

# Add handoff back to primary agent for escalation
flight_agent.handoffs.append(primary_agent)
hotel_agent.handoffs.append(primary_agent)
car_rental_agent.handoffs.append(primary_agent)
excursion_agent.handoffs.append(primary_agent)

starting_agent = primary_agent
