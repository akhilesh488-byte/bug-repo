def format_currency(amount: float) -> str:
    """Format a number as a currency string, e.g. 1234.5 -> '$1234.50'."""
    return f"${amount:.2f}"