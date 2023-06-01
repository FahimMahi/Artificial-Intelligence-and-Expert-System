def getSeconds(hours, minutes, seconds):
    
    hours = int(hours) * 3600
    minutes = int(minutes) * 60
    seconds = int(seconds)
    return hours + minutes + seconds

print(getSeconds("11", "11", "14"))
print(getSeconds("00", "01", "02"))
print(getSeconds("05", "00", "30"))
print(getSeconds("00", "00", "00"))
print(getSeconds("02", "18", "49"))