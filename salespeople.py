"""A hierarchy of classes for salespeople."""

class Salesperson():
    """A salesperson at Ubermelon."""
    base_salary = 50000
    commission_rate = 0.05 
    def __init__(self):
        """Initialize salesperson attributes."""

    def calculate_monthly_pay(self, total_sales):
        """Calculate the person's monthly pay.

        Use the person's base salary and commissions.
        """

        commission = self.commission_rate * total_sales
        monthly_salary = self.base_salary / 12

        return "${:.2f}".format(monthly_salary + commission)


class InternSalesperson(Salesperson):
    """A college intern at Ubermelon working in sales."""
    base_salary = 20000