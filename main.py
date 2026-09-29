from calculator import calculate_total
from discount import apply_discount
from utils import format_currency

def process_invoice():
    items = [
        {"name": "Widget", "price": 20.0, "quantity": 3},
        {"name": "Gadget", "price": 50.0, "quantity": 2},
    ]
    subtotal = calculate_total(items)
    final = apply_discount(subtotal, 10)
    print(f"Subtotal: {format_currency(subtotal)}")
    print(f"Final (after 10% discount): {format_currency(final)}")

if __name__ == "__main__":
    process_invoice()