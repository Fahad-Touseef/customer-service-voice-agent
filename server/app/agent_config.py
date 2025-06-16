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

# Import prompts from prompts.py
from app.prompts import (
    voice_system_prompt,
    PRIMARY_PROMPT,
    FLIGHT_PROMPT,
    HOTEL_PROMPT,
    CAR_RENTAL_PROMPT,
    EXCURSION_PROMPT,
)

def custom_instructions(run_context, agent):
    context = run_context.context
    time_str = context.current_time or datetime.now().isoformat(timespec="seconds")
    if agent.name == "Primary Assistant":
        return voice_system_prompt + PRIMARY_PROMPT.format(current_time=time_str)
    elif agent.name == "Flight Assistant":
        return voice_system_prompt + FLIGHT_PROMPT.format(current_time=time_str)
    elif agent.name == "Hotel Assistant":
        return voice_system_prompt + HOTEL_PROMPT.format(current_time=time_str)
    elif agent.name == "Car Rental Assistant":
        return voice_system_prompt + CAR_RENTAL_PROMPT.format(current_time=time_str)
    elif agent.name == "Excursion Assistant":
        return voice_system_prompt + EXCURSION_PROMPT.format(current_time=time_str)

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
