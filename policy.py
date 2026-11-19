"""Business rules shared by pricing and the repository-context demo."""
def loyalty_threshold():
    """The inclusive loyalty-discount threshold is 100 currency units."""
    return 100

def loyalty_discount():
    """The fixed loyalty discount is 10 currency units."""
    return 10
