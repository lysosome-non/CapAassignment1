from operator import truediv


def chek_value(s):
    try:
        s=float(s)
        return True
    except:
        return False


print("Celsius-Fahrenheit conversion sys")
while True:
    a= input("insert your temperature (eg: 34F,12C)")

    if a[-1] in ['F','f'] and chek_value(a[:-1]):
        C = (eval(a[:-1])-32)/1.8
        print(C,'Celsius')
    elif a[-1] in ['C','c'] and chek_value(a[:-1]):
        F = (eval(a[:-1])*1.8)+32
        print(F,'fahrenherit')
        break
    else:
        print("wrong")
    print("Hello")