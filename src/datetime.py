from datetime import datetime

now = datetime.now()

print now



from datetime import datetime

now = datetime.now()

print now.month
print now.day
print now.year




from datetime import datetime

now = datetime.now()

print now.month
print now.day
print now.year

print str(now.month) + "/" + str(now.day) + "/" + str(now.year)
print str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)