def apply_discount(total: float, discount_percent: float) -> float:
    """Apply a percentage discount to the total invoice amount.

    discount_percent is a percentage (e.g. 10 means 10% off), not a flat amount.
    """
    return total - discount_percent  # bug is here