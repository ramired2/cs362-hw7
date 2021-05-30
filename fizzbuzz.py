def check(x):
    if x % 5 == 0 and x % 3 == 0:
        msg = "FizzBuzz"
        return msg

def check3(x):
    if x % 3 == 0 and x % 5 != 0:
        msg = "Fizz"
        return msg