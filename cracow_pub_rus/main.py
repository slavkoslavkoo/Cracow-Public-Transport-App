from datetime import datetime
from lines import week, sat, sun

# function to check the day of the week
def check_weekday():
        from datetime import date
        today = date.today()
        if today.isoweekday()==7:
            return 'Sunday'
        elif today.isoweekday()==6:
            return 'Saturday'
        elif today.isoweekday()==5:
            return 'Friday'
        else:
           return 'Weekdays'

#function to show time imterval between depart and current time
def time_interval(low,high):
    lower = datetime.strptime(low.strftime('%H%M'), '%H%M')
    higher = datetime.strptime(high.strftime('%H%M'), '%H%M')
    return higher - lower

# function that calls search again message after succesful operation
def search_again():
    search_again = input("Нажми любую кнопку чтобы искать еще или 'q' чтобы выйти: ")
    if search_again=='q':
        print("Спасибо за использование моей программы. Удачи и счастливой дороги!")
        return False
    else:
        return True

# function for managing user's choice of line numer
def line_num():
    while True:
        num = input("Введи номер маршрута: ")
        if num.isalpha():
            print("Вводить нужно только цифры!")
            print("*******************************")
        elif num not in list(week.keys()):
            print("Нет такой линии. Может в будуещем. Ну а пока...")
            print("*******************************")
        else:
            if len(num)<=2:
                print("*******************************")
                print(f"Отлично! Маршрут твоего трамвая - это {num}.")
                print("*******************************")
                break
            else:
                print("*******************************")
                print(f"Отлично! Маршрут твоего автобуса - это {num}.")
                print("*******************************")
                break
    return num

# function for managing user's direction choice
def dir_num():
    print(f"Теперь ты можешь выбрать направление.\nЭто будет {list(week[ask_line])[0]} или {list(week[ask_line])[1]}.")
    while True:
        dir = input('Выбери одно из них: ').title()
        if dir.isdigit():
            print("*******************************")
            print("Нужно ввести название. Не номер!")
            print(f"'{list(week[ask_line])[0]}' или '{list(week[ask_line])[1]}'.")
            print("*******************************")
        elif dir not in week[ask_line]:
            print("*******************************")
            print('Неправильное направлени. Попробуй еще!')
            print(f"Введи '{list(week[ask_line])[0]}' или '{list(week[ask_line])[1]}'.")
            print("*******************************")
        else:
            break
    return dir

# function to correctly choose station
def station_select():
    print("*******************************")
    print(f"Ниже приведен список остановок на данной линии.\nВыбери одну из них:")
    print("*******************************")
    index = 1
    for station in week[ask_line][ask_dir]:
        print(index,station)
        index += 1
    while True:
        print("*******************************")
        line = input("Ну что, откуда стартуем? ==> ").title()
        if line.isdigit():
            print("*******************************")
            print("Введи название остановки. Не цифры")
        elif line not in list(week[ask_line][ask_dir]):
            print("*******************************")
            print("Нет такой остановки. Будь внимателен и попробуй еще!")
        else:
            break
    return line

# creating class to operate user's entries and timetables from Line.py
class Ttable:

    def __init__(self,number, direction, station):
        self.number = number
        self.direction = direction
        self.station = station

    # function that determines day of the week, current time and accept user enties in order to process through Lines.py and show
    # the closest trip for each line and how many time left untill it departs
    # also it finds out if there's no trip for today and informs user about it showing message
    # about closest trip for tomorrow on current line

    def closest(self):
        #accessing to the local time
        current_time = datetime.now().time()
        if check_weekday()=='Sunday':
                for i in sun[self.number][self.direction][self.station]:
                    if i > current_time:            
                        if len(self.number)<=2:
                            print(f"Твой следующий трамвай маршрута {self.number} отправляется с {self.station} в {i.strftime('%H:%M')}")
                            print(f"Осталось {str(time_interval(current_time,i))[:-3]}! Счастливого пути!")
                            break
                        else:
                            print(f"Твой следующий автобус маршрута {self.number} отправляется с {self.station} в {i.strftime('%H:%M')}")
                            print(f"Осталось {str(time_interval(current_time,i))[:-3]}! Счастливого пути!")
                            break                    
                    elif sun[self.number][self.direction][self.station][-1]<current_time:
                        next_day = week[self.number][self.direction][self.station][0].strftime('%H:%M')
                        last = sun[self.number][self.direction][self.station][-1].strftime('%H:%M')
                        print(f"К сожалению последний маршрут отъехал с {self.station} в {last}.\nСледующий будет завтра в {next_day}.\nСпокойной ночи и приятных поездок!")
                        break
        elif check_weekday()=='Saturday':
            for i in sat[self.number][self.direction][self.station]:
                if i > current_time:            
                    if len(self.number)<=2:
                        print(f"Твой следующий трамвай маршрута {self.number} отправляется с {self.station} в {i.strftime('%H:%M')}")
                        print(f"Осталось {time_interval(current_time,i)}! Счастливого пути!")
                        break
                    else:
                        print(f"Твой следующий автобус маршрута {self.number} отправляется с {self.station} в {i.strftime('%H:%M')}")
                        print(f"Осталось {time_interval(current_time,i)}! Счтастливого пути!")
                        break                    
                elif current_time > sat[self.number][self.direction][self.station][-1]:
                    next_day = sun[self.number][self.direction][self.station][0].strftime('%H:%M')
                    last = sat[self.number][self.direction][self.station][-1].strftime('%H:%M')
                    print(f"К сожалению последний маршрут отъехал с {self.station} в {last}.\nСледующий будет завтра в {next_day}.\nGпокойной ночи и приятных поездок!")
                    break
        else:
            for i in week[self.number][self.direction][self.station]:                
                if i > current_time:            
                    if len(self.number)<=2:
                        print(f"Твой следующий трамвай маршрута {self.number} отправляется с {self.station} в {i.strftime('%H:%M')}")
                        print(f"Осталось {str(time_interval(current_time, i))[:-3]}! Счастливого пути!")
                        break
                    else:
                        print(f"Your next bus of line {self.number} departs from {self.station} at {i.strftime('%H:%M')} o'clock")
                        print(f"It's {str(time_interval(current_time,i))[:-3]} left! Enjoy your journey!")
                        break                    
                elif current_time > week[self.number][self.direction][self.station][-1]:
                    if check_weekday()=='Friday':
                        next_day = sat[self.number][self.direction][self.station][0].strftime('%H:%M')
                        last = week[self.number][self.direction][self.station][-1].strftime('%H:%M')
                        print(f"Unfortunately the last trip from {self.station} for today was at {last}.\nNext is at {next_day} o'clock tomorrow.\nGood night and safe travels!")
                        break
                    else:
                        next_day = week[self.number][self.direction][self.station][0].strftime('%H:%M')
                        last = week[self.number][self.direction][self.station][-1].strftime('%H:%M')
                        print(f"Unfortunately the last trip from {self.station} for today was at {last}.\nNext is at {next_day} o'clock tomorrow.\nGood night and safe travels!")
                        break


if __name__=='__main__':
    print("Добро пожаловать в интерактивное приложение Краковского общественного транспорта!\nКак говорил дядя Юра:'Поехали'!")
    while True:        
        try:
            ask_line = line_num()
            ask_dir = dir_num()
            ask_station = station_select()
            # asign entries to class object Ttable for further maintaining
            line = Ttable(ask_line, ask_dir, ask_station)
            # call function to show closest line trip
            line.closest()
                
            if not search_again():
                break
        except KeyError:
            pass