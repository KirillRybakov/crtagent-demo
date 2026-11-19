from policy import loyalty_discount, loyalty_threshold

def discount(total):
    """Return the fixed discount at or above the inclusive threshold."""
    if total >= loyalty_threshold():
        return loyalty_discount()
    return 0
