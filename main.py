months = [['january', 31], ['february', 28], ['march', 31], ['april', 30], ['may', 31], ['june', 30],
          ['july', 31], ['august', 31], ['september', 30], ['october', 31], ['november', 30], ['december', 31]]
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

schoolYear = {'start': '9-11-2023', 'end': '6-6-2024'}
schoolDays = [1, 2, 3, 4, 5]
divisionStopStartDates = [{'start': '9-11-2023', 'end': '1-12-2024'}, {'start': '1-15-2024', 'end': '6-6-2024'}]
scheduleData = [8, 'letters']
defaultSchedule = [
    {'name': 'Advisory', 'type': 'advisory', 'time': {'start': '8:00', 'end': '8:05'}},
    {'name': 'Block 1', 'type': 'class', 'time': {'start': '8:10', 'end': '9:10'}},
    {'name': 'Block 2', 'type': 'class', 'time': {'start': '9:15', 'end': '10:15'}},
    {'name': 'Block 3', 'type': 'class', 'time': {'start': '10:20', 'end': '11:20'}},
    {'name': 'Flex', 'type': 'free', 'time': {'start': '11:25', 'end': '11:55'}},
    {'name': 'Lunch', 'type': 'lunch', 'time': {'start': '12:00', 'end': '12:25'}},
    {'name': 'Block 4', 'type': 'class', 'time': {'start': '12:30', 'end': '1:30'}},
    {'name': 'Block 5', 'type': 'class', 'time': {'start': '1:35', 'end': '2:35'}},
    {'name': 'Collab', 'type': 'free', 'time': {'start': '2:40', 'end': '3:15'}}
]

classes = [
    {'name': 'Advisory', 'teacher': 'Markolovic', 'room': 'MSC 201'},
    {'name': 'Math', 'teacher': 'Marone', 'room': 'MSC 204', 'color': 'blue'},
    {'name': 'Health', 'teacher': 'Coates', 'room': 'GH 204', 'color': 'purple'},
    {'name': 'English', 'teacher': 'Horan', 'room': 'GH 104', 'color': 'yellow'},
    {'name': 'Spanish', 'teacher': 'Toscano', 'room': 'BH 203', 'color': 'orange'},
    {'name': 'History', 'teacher': 'Kamil', 'room': 'GH 207', 'color': 'red'},
    {'name': 'Biology', 'teacher': 'Milinkovic', 'room': 'MSC 203', 'color': 'green'},
    {'name': 'Jazz Band', 'teacher': 'Girvin', 'room': 'FH 105', 'color': 'silver'}
]


def dateRange(date, startRange, endRange):
    a, b, c = int(date.split('-')[0]), int(date.split('-')[1]), int(date.split('-')[2])
    f, g, h = int(startRange.split('-')[0]), int(startRange.split('-')[1]), int(startRange.split('-')[2])
    x, y, z = int(endRange.split('-')[0]), int(endRange.split('-')[1]), int(endRange.split('-')[2])

    if z > h:
        y = y + months[(x - 1)][1]
        x = x - 1
        x = x + 12
        z = z - 1

    if c > h:
        b = b + months[(a - 1)][1]
        a = a - 1
        a = a + 12
        c = c - 1

    if f <= a <= x:
        if g <= b <= y:
            return True
        else:
            return False


def func(date, a):
    if dateRange('3-13-2024', '9-11-2023', '6-6-2024'):
        if a in schoolDays:
            print("school day")


def main(q, i, z):
    q = q - 1
    i = i - 1
    x, y = 0, 0
    while True:
        if x == 12:
            break
        else:
            if (q % 12) == 0:
                if i == 0:
                    z = z + 1
                    q = 0

            if i == months[(q % 12)][1]:
                i = 0
                q = q + 1
                x = x + 1
            else:
                month = months[(q % 12)][0]
                date = (i + 1)
                day = days[(y % 7)]
                year = z
                print(f"{q + 1}-{date}-{year}, {day}")
                func(f"{q + 1}-{date}-{year}", (y % 7))
                i = i + 1
                y = y + 1


startDate = '9-1-2023'
#main(int(startDate.split('-')[0]), int(startDate.split('-')[1]), int(startDate.split('-')[2]))

func()
