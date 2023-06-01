def how_long(dis, frac, s):
    c=186000
    lightYear =c*60*60*24*365
    speed = frac*c
    times = dis/speed
    minutes = times/60
    hours = minutes/60
    days = hours/24
    years = days/365
    
    if s == "M":
        return minutes
    if s == "H":
        return hours
    if s == "D":
        return days
    if s == "Y":
        return years
        
print(how_long(238900, 0.01, 'M'))
print(how_long(45594000, 0.01, 'H'))
print(how_long(93000000, 1.0, 'M'))
print(how_long(9000000000, 0.01, 'D'))
print(how_long(25000000000000, 0.01, 'Y'))