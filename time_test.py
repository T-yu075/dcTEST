import datetime

# now_time = datetime.datetime.now()
now_time = datetime.datetime.now().strftime("%H:%M")
print(now_time)

#a = str(now_time).split(' ')
#dateee = date.fromisoformat(a[0])
#print(date.isoweekday(dateee))  # 星期N


weekk = datetime.datetime.today().isoweekday()
print(weekk)