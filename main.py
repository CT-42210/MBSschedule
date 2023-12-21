class Period:
    def __init__(self, className, teacher, number, color):
        self.name = className
        self.teacher = teacher
        self.number = number
        self.color = color


class SchoolDay:
    def __init__(self):
        self.blocks = []


class Block(Period):
    def __init__(self, className, color, teacher, number, start_time, end_time):
        super().__init__(className, teacher, number, color)
        self.start_time = start_time
        self.end_time = end_time


# Create 8 periods
periods = [
    Period("Period 1", "Teacher1", 1, "Red"),
    Period("Period 2", "Teacher2", 2, "Blue"),
    Period("Period 3", "Teacher3", 3, "Green"),
    Period("Period 4", "Teacher4", 4, "Yellow"),
    Period("Period 5", "Teacher5", 5, "Orange"),
    Period("Period 6", "Teacher6", 6, "Purple"),
    Period("Period 7", "Teacher7", 7, "Pink"),
    Period("Period 8", "Teacher8", 8, "Brown"),
]

# Create a SchoolDay with 5 blocks using the periods
school_day = SchoolDay()
school_day.blocks.append(Block(periods[0].name, periods[0].color, periods[0].teacher, periods[0].number, "8:00 AM", "9:00 AM"))
school_day.blocks.append(Block(periods[1].name, periods[1].color, periods[1].teacher, periods[1].number, "9:00 AM", "10:00 AM"))
school_day.blocks.append(Block(periods[2].name, periods[2].color, periods[2].teacher, periods[2].number, "10:00 AM", "11:00 AM"))
school_day.blocks.append(Block(periods[3].name, periods[3].color, periods[3].teacher, periods[3].number, "11:00 AM", "12:00 PM"))
school_day.blocks.append(Block(periods[4].name, periods[4].color, periods[4].teacher, periods[4].number, "1:00 PM", "2:00 PM"))

# Repeat the process for the other 4 days of the week
# ...
x = 6
# Example usage:
print(f"{school_day.blocks[x].name} with {school_day.blocks[x].teacher} starts at {school_day.blocks[x].start_time}")
