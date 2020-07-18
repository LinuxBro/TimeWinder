import datetime
import Line
from typing import List

class Day:
    lines: List[Line.Line] = []
    date: datetime.date = ""

    def __init__(self, date):
        self.date = date

    def add_line(self, line):
        self.lines.append(line)
