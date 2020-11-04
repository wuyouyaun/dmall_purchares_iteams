

# url="http://10.248.224.252:6006/mock/15/vc/contract/contract/list"




import time

# time="1598976000000"
# a=time.strftime()



test_time='2020-08-01 00:00:00'
timeArray=time.strptime(test_time,"%Y-%m-%d %H:%M:%S")
print(timeArray)
time1=int(time.mktime(timeArray))*1000
print(time1)

time2=time1/1000
time_local=time.localtime(time2)
print(time_local)
data=time.strftime("%Y-%m-%d %H:%M:%S",time_local)
print(data)
