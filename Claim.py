import Day
import Line
import datetime
from datetime import timedelta
from typing import List
from prettytable import PrettyTable

class Claim:
    days: List[Day.Day] = []
    path: str = ""
    name: str = ""
    startdate: datetime.date = ""
    enddate: datetime.date = ""
    perdiem: float = ""
    hasflight: bool = ""

    def __init__(self, path, name, startdate, enddate):
        self.path = path
        self.name = name
        self.startdate = startdate
        self.enddate = enddate
        print(self.enddate-self.startdate)
        currdate = startdate
        while currdate != enddate+timedelta(days=1):
            self.days.append(Day.Day(currdate))
            currdate = currdate+timedelta(days=1)

    def add_day(self):
        pass
    def show_claim(self):
        tables = []
        for day in self.days:
            x = PrettyTable()
            x.field_names = ["Date", "Cost", "Category", "Billable", "Explanation"]
            for line in day.lines:
                x.add_row([day.date.strftime("%m/%d/%y"), line.cost, line.category, line.billable, line.explanation])
            tables.append(x)
        for table in tables:
            print(table)
