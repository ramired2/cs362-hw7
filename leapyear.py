def check ():
    msg = "Please enter a year: "
    year = input(msg)

    year = int(year)

    if year % 4 == 0:
        return "Leap Year"
    else:
        return "Not a leap Year"