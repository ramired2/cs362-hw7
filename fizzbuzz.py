def check(x):
    msg = ""
    if x % 5 == 0 and x % 3 == 0:
        msg = "FizzBuzz"
        print(msg)
    return msg

def check3(x):
    msg = ""
    if x % 3 == 0 and x % 5 != 0:
        msg = "Fizz"
        print(msg)
    return msg

def check5(x):
    msg = ""
    if x % 3 != 0 and x % 5 == 0:
        msg = "Buzz"
        print(msg)
    return msg

count = 0
while count < 100:
    count += 1

    res = check(count)
    res1 = check3(count)
    res2 = check5(count)

    if res == "" and res1 == "" and res2 == "":
        print (count)