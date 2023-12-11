class Period:
    def __init__(self, title, color, start_time, end_time, teacher, period_num):
        self.title = title
        self.color = color
        self.start_time = start_time
        self.end_time = end_time
        self.teacher = teacher
        self.period_num = period_num


class SchoolDay:

    def __init__(self, title, color, periods=None):
        if periods is None:
            periods = []
        self.title = title
        self.color = color
        self.periods = periods

        self.check_attributes()

    def check_attributes(self):
        check = lambda name, d_type: True if type(name) is not type(d_type) else False
        if check(self.title, ""):
            raise TypeError("attribute \'title\' must be string")
        if check(self.color, ""):
            raise TypeError("attribute \'color\' must be string")
        if check(self.periods, []):
            raise TypeError("attribute \'periods\' must be list")


day_A = SchoolDay("Day A", "Red")
