import datetime
import locale
locale.setlocale(locale.LC_ALL, "ru")
userData = datetime.datetime.strptime(input('Введите дату в формате дд.мм.гг \n'), '%d.%m.%Y')

schedule = []
schedule.append(datetime.datetime.strftime(userData, '%d.%m.%Y - %A'))
delta = datetime.timedelta(days=2)
while delta <= datetime.timedelta(days=30):
    if datetime.datetime.weekday(userData + delta) == 6:
        delta += datetime.timedelta(days=1)
    schedule.append(datetime.datetime.strftime(userData + delta, '%d.%m.%Y - %A'))
    delta += datetime.timedelta(days=2)
print('Ваше расписание на ближайший месяц:')
for j in schedule:
    print(j)