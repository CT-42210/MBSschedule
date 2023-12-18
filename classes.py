class Period:
    def __init__(self, title, color, start_time, end_time, teacher, period_num):
        self.title = title
        self.color = color
        self.start_time = start_time
        self.end_time = end_time
        self.teacher = teacher
        self.period_num = period_num

        self.check_attributes()

    def __repr__(self):
        return "Period()"

    def __str__(self):
        return f"Period() obj: {self.title}"

    def check_attributes(self):
        check = lambda name, d_type: True if type(name) is not type(d_type) else False
        if check(self.title, ""):
            raise TypeError("attribute \'title\' must be string")
        if check(self.color, ""):
            raise TypeError("attribute \'color\' must be string")
        if check(self.start_time, ""):
            raise TypeError("attribute \'start_time\' must be string")
        if check(self.end_time, ""):
            raise TypeError("attribute \'end_time\' must be string")
        if check(self.teacher, ""):
            raise TypeError("attribute \'teacher\' must be string")
        if check(self.period_num, int):
            raise TypeError("attribute \'period_num\' must be int")


class SchoolDay:

    def __init__(self, title, color, periods=None):
        if periods is None:
            periods = []
        self.title = title
        self.color = color
        self.periods = periods

        self.check_attributes()

    def __repr__(self):
        return "SchoolDay()"

    def __str__(self):
        return f"SchoolDay() obj: {self.title}"

    def check_attributes(self):
        check = lambda name, d_type: True if type(name) is not type(d_type) else False
        if check(self.title, ""):
            raise TypeError("attribute \'title\' must be string")
        if check(self.color, ""):
            raise TypeError("attribute \'color\' must be string")
        if check(self.periods, []):
            raise TypeError("attribute \'periods\' must be list")
        if self.periods.__len__() > 0:
            if check(self.periods, Period):
                raise TypeError("attributes within \'periods\' are not Period objects")


day_A = SchoolDay("Day A", "Red")
print(day_A)
