import datetime
import Line
from typing import List

class Day:

    def __init__(self, date):
        self.date = date
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)
