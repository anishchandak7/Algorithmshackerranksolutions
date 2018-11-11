import calendar as cal
date = input()
month,day,year = date.split(" ")
day = int(day)
month = int(month)
year = int(year)
weekday = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
index = cal.weekday(year,month,day)
for pos in range(len(weekday)):
    if(index == pos):
        print(weekday[index])
