import datetime as dt

# Inside the datetime module there is a datetime class.  I created a dt alias above for 
# datetime so I don't have to use datetime.datetime.
dt.datetime

# Inside the datetime class is a method called now that gets you the current date and time in the form of a datetime object.
now = dt.datetime.now()

print(now)

year = now.year
month = now.month
day = now.day

# 0=Mon, 1=Tues, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun 
day_of_the_week = now.weekday()

if year == 2020: 
    print("Its COVID time")
else:
    print("No COVID yay!")

print(f"{day} {month} {year}")
print(day_of_the_week)