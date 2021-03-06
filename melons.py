"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    order_type = None
    tax = None
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

        
    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        tax_and_qty = (1 + self.tax) * self.qty

        #If international increase base price for xmas melons and add #3 if qty less than 10 
 
        if self.species == 'christmas melons': 
            if self.order_type == 'international' and self.qty <10:
                total = tax_and_qty * base_price * 1.5 + 3
            else: 
                total = tax_and_qty * base_price + 3
        else: 
            total = tax_and_qty * base_price


        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty) 
        self.country_code = country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    passed_inspection = False
    order_type = "government"
    tax = 0.0

    def mark_inspection(self, passed_or_not): #submit if True or False as boolean
        self.passed_inspection = passed_or_not
