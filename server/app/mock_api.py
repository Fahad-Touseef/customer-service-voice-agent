def get_past_orders():
    return [
        {
            "order_date": "2024-01-01",
            "order_number": "AB472",
            "order_description": "Patagonia jacket - red",
            "order_status": "fulfilled",
        },
        {
            "order_date": "2024-01-05",
            "order_number": "AC859",
            "order_description": "Patagonia fleece pullover - navy",
            "order_status": "fulfilled",
        },
        {
            "order_date": "2024-01-10",
            "order_number": "AF103",
            "order_description": "Patagonia down vest - black",
            "order_status": "fulfilled",
        },
        {
            "order_date": "2024-01-15",
            "order_number": "AD620",
            "order_description": "Patagonia rain jacket - green",
            "order_status": "fulfilled",
        },
        {
            "order_date": "2024-01-20",
            "order_number": "AC391",
            "order_description": "Patagonia hiking pants - khaki",
            "order_status": "fulfilled",
        },
        {
            "order_date": "2024-01-25",
            "order_number": "AE746",
            "order_description": "Patagonia beanie - grey",
            "order_status": "fulfilled",
        },
        {
            "order_date": "2024-01-30",
            "order_number": "AB285",
            "order_description": "Patagonia backpack - blue",
            "order_status": "fulfilled",
        },
        {
            "order_date": "2024-02-04",
            "order_number": "AF934",
            "order_description": "Patagonia gloves - black",
            "order_status": "fulfilled",
        },
        {
            "order_date": "2024-02-09",
            "order_number": "AD507",
            "order_description": "Patagonia shorts - olive",
            "order_status": "fulfilled",
        },
    ]


def submit_refund_request(order_number: str):
    """Confirm with the user first"""
    return "success"
