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
    search_again = input("Press any key for search again or 'q' for quit: ")
    if search_again=='q':
        print("Thanks for using my program. Good luck and safe travels!")
        return False
    else:
        return True

def line_num():
    while True:
        num = input("Please enter line number: ")
        if num.isalpha():
            print("You should enter only digits!")
            print("*******************************")
        elif num not in list(week.keys()):
            print("There's no such line. Maybe in future. But now...")
            print("*******************************")
        else:
            if len(num)<=2:
                print("*******************************")
                print(f"Good! Your tram line is {num}.")
                print("*******************************")
                break
            else:
                print("*******************************")
                print(f"Good! Your bus line is {num}.")
                print("*******************************")
                break
    return num

def dir_num():
    print(f"Now you can choose between the directions.\nEither {list(week[ask_line])[0]} or {list(week[ask_line])[1]}.")
    while True:
        dir = input('Choose one: ').title()
        if dir.isdigit():
            print("*******************************")
            print("Please enter direction's name. Not numer!")
            print(f"It's '{list(week[ask_line])[0]}' or '{list(week[ask_line])[1]}'.")
            print("*******************************")
        elif dir not in week[ask_line]:
            print("*******************************")
            print('Wrong direction. Try again!')
            print(f"It's '{list(week[ask_line])[0]}' or '{list(week[ask_line])[1]}'.")
            print("*******************************")
        else:
            break
    return dir

def station_select():
    print("*******************************")
    print(f"Here's the list of stations on this line.\nChoose the one from list below:")
    print("*******************************")
    index = 1
    for station in week[ask_line][ask_dir]:
        print(index,station)
        index += 1
    while True:
        print("*******************************")
        line = input("So, where do we start? ==> ").title()
        if line not in list(week[ask_line][ask_dir]):
            print("*******************************")
            print("There's no such station. Be careful and enter correct name!")
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
                            print(f"Your next tram of line {self.number} departs from {self.station} at {i.strftime('%H:%M')} o'clock")
                            print(f"It's {str(time_interval(current_time,i))[:-3]} left! Enjoy your journey!")
                            break
                        else:
                            print(f"Your next bus of line {self.number} departs from {self.station} at {i.strftime('%H:%M')} o'clock")
                            print(f"It's {str(time_interval(current_time,i))[:-3]} left! Enjoy your journey!")
                            break                    
                    elif sun[self.number][self.direction][self.station][-1]<current_time:
                        next_day = week[self.number][self.direction][self.station][0].strftime('%H:%M')
                        last = sun[self.number][self.direction][self.station][-1].strftime('%H:%M')
                        print(f"Unfortunately the last trip from {self.station} for today was at {last}.\nNext is at {next_day} o'clock tomorrow.\nGood night and safe travels!")
                        break
        elif check_weekday()=='Saturday':
            for i in sat[self.number][self.direction][self.station]:
                if i > current_time:            
                    if len(self.number)<=2:
                        print(f"Your next tram of line {self.number} departs from {self.station} at {i.strftime('%H:%M')} o'clock")
                        print(f"It's {time_interval(current_time,i)} left! Enjoy your journey!")
                        break
                    else:
                        print(f"Your next bus of line {self.number} departs from {self.station} at {i.strftime('%H:%M')} o'clock")
                        print(f"It's {time_interval(current_time,i)} left! Enjoy your journey!")
                        break                    
                elif current_time > sat[self.number][self.direction][self.station][-1]:
                    next_day = sun[self.number][self.direction][self.station][0].strftime('%H:%M')
                    last = sat[self.number][self.direction][self.station][-1].strftime('%H:%M')
                    print(f"Unfortunately the last trip from {self.station} for today was at {last}.\nNext is at {next_day} o'clock tomorrow.\nGood night and safe travels!")
                    break
        else:
            for i in week[self.number][self.direction][self.station]:                
                if i > current_time:            
                    if len(self.number)<=2:
                        print(f"Your next tram of line {self.number} departs from {self.station} at {i.strftime('%H:%M')} o'clock")
                        print(f"It's {str(time_interval(current_time, i))[:-3]} left! Enjoy your journey!")
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
    print("Welcome to the interactive timetable application for Cracow public transport!\nHope you enjoy it. Let's get started!")
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