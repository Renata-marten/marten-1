import datetime
import locale
locale.setlocale(locale.LC_ALL, "ru")
userData = datetime.datetime.strptime(input('Введите дату в формате дд.мм.гг \n'), '%d.%m.%Y')

schedule = []
schedule.append(datetime.datetime.strftime(userData, '%d.%m.%Y - %A'))
delta = datetime.timedelta(days=2)
for i in range(15):
    schedule.append(datetime.datetime.strftime(userData + delta, '%d.%m.%Y - %A'))
    delta += datetime.timedelta(days=2)
print('Ваше расписание на ближайший месяц:')
for j in schedule:
    print(j)