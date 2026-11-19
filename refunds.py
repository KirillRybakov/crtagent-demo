def refund_amount(total, fee):
    """Refund policy depends on the contract; ask whether the fee is retained."""
    return total - fee
