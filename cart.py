class Cart:
    def total(self, unit_price, quantity):
        """Each item costs unit_price; there are quantity identical items."""
        return unit_price + quantity
