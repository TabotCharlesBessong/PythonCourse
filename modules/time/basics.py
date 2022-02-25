
import time


print(time.ctime(0)) #Thu Jan  1 01:00:00 1970
     
print(time.time()) #1645747097.385027  
print(time.ctime(time.time())) #Fri Feb 25 00:58:17 2022
# print(time.localtime())

timeObject = time.localtime()

localTime = time.strftime("%B %d %Y %H:%M:%S",timeObject)
print(localTime)
utc = time.gmtime()
print(utc)
# localTime =  time.strftime(format,time.localtime().tm_sec())
# dayOfTheYear = time.strftime(format,time.localtime().tm_yday())
# weekDay = time.strftime(format,time.localtime().tm_wday())

# print(localTime)