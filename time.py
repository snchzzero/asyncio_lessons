import datetime

# datestring for which datetime_obj required
date_string = '2021-09-01 15:27:05 +0530'
# using strptime() to get datetime object
datetime_obj = datetime.datetime.strptime(
    date_string, '%Y-%m-%d %H:%M:%S %z')

print(datetime_obj)

some_time = "2023-12-19 08:00:29+03:00"
iso_f = datetime.datetime.fromisoformat(some_time)
print(iso_f)
print(type(iso_f))
time_without_z = iso_f.replace(tzinfo=None)
print(time_without_z)

time_now = datetime.datetime.now()
print('time_now ', time_now)


delta_second = abs((time_without_z - time_now).total_seconds())
print('delta_second', delta_second)
