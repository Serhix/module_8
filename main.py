from datetime import datetime, timedelta


users = [
          {'name': 'Serhiy', 'birthday': datetime(year=1989, month=5, day=15)},
          {'name': 'Olya', 'birthday': datetime(year=1992, month=5, day=16)},
          {'name': 'Taras', 'birthday': datetime(year=1998, month=5, day=14)},
          {'name': 'Volodymyr', 'birthday': datetime(year=1985, month=5, day=18)},
          {'name': 'Oleg', 'birthday': datetime(year=1999, month=5, day=13)},
          {'name': 'Nadiya', 'birthday': datetime(year=2001, month=5, day=14)},
          {'name': 'Oleksandr', 'birthday': datetime(year=1988, month=5, day=17)},
          {'name': 'Vasyl', 'birthday': datetime(year=2000, month=5, day=19)},
          {'name': 'Anatoliy', 'birthday': datetime(year=1983, month=5, day=18)},
          {'name': 'Oksana', 'birthday': datetime(year=1993, month=5, day=20)},
          {'name': 'Nataliya', 'birthday': datetime(year=2002, month=5, day=21)},
          {'name': 'Vita', 'birthday': datetime(year=1978, month=5, day=19)},
          {'name': 'Nastya', 'birthday': datetime(year=1989, month=5, day=21)},
          {'name': 'Kateryna', 'birthday': datetime(year=1998, month=5, day=19)},
          {'name': 'Andriy', 'birthday': datetime(year=1999, month=5, day=13)},
          {'name': 'Matviy', 'birthday': datetime(year=1996, month=5, day=17)},  
        ]


def get_birthdays_per_week(users):

    delta = timedelta(days = 1)
    # week_day = datetime.now()
    week_day = datetime(year=2023, month=5, day=13) #для зручності тестування можна вибирати не поточний день а будь-який 
    list_day = []

    for _ in range(7):
        for key in users:
            if key['birthday'].day == week_day.day:
                list_day.append(key["name"])
        if list_day and week_day.weekday() != 5 and week_day.weekday() != 6:
            print(f'{week_day.strftime("%A")}: {", ".join(list_day)}')
            list_day = [] # обнуляємо лише по буднях
        week_day = week_day + delta

get_birthdays_per_week(users)