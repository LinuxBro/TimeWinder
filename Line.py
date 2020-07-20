import datetime


class Line:

    def __init__(self,cost,category,billable,explanation):
        self.cost = cost
        self.category = category
        self.billable = billable
        self.explanation = explanation