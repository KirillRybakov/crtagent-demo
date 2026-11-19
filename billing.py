async def invoice_total(amount, fee):
    """The invoice includes both the order amount and its service fee."""
    return amount - fee
