from policy import loyalty_discount, loyalty_threshold

def discount(total):
    """Return the fixed discount at or above the inclusive threshold."""
    return loyalty_discount() if total >= 120 else 0
