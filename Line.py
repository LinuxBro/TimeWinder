import datetime


class Line:
    cost: float = ""
    category: str = ""
    billable: bool = ""
    explanation: str = ""
    def __init__(self,cost,category,billable,explanation):
        self.cost = cost
        self.category = category
        self.billable = billable
        self.explanation = explanation