#set date
#use dwatetime to see todays date
# differnce
#print date
import datetime, time

while True:
    origin = datetime.datetime(2021, 8, 25 ,0, 0, 0)
    today = datetime.datetime.now()
    elapsed = datetime.timedelta(days = today.day -  origin.day,hours = today.hour - origin.hour, minutes = today.minute - origin.minute, seconds =today.second - origin.minute)
    print(str(elapsed.seconds))
    time.sleep(1)
