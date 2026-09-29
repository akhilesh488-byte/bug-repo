def calculate_total(items: list[dict]) -> float:
    """Sum up (price * quantity) for each item in the invoice."""
    total = 0.0
    for item in items:
        total += item["price"] * item["quantity"]
    return total