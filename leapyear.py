def sneakyLeap(x):
    isLeap = False
    
    if x % 100 == 0:
        if x % 400 == 0:
            isLeap = True
    else:
        isLeap = True

    return isLeap

def check (year):

    if year % 4 == 0:
        if (sneakyLeap(year) == True):
            msg = "Leap Year"
        else:
            msg = "Not a leap Year"
    else:
        msg = "Not a leap Year"
    
    return msg