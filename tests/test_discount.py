from discount import apply_discount

def test_apply_discount_basic():
    # $200 with a 10% discount should return $180 (10% of 200 = 20 off)
    assert apply_discount(200, 10) == 180

if __name__ == "__main__":
    result = apply_discount(200, 10)
    expected = 180
    print(f"apply_discount(200, 10) = {result}, expected {expected}")
    assert result == expected, "TEST FAILED"
    print("TEST PASSED")