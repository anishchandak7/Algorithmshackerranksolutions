s = input()


def timeConversion(s):
    time = ""
    hrs = int(s[0:2])
    if s[-2:] == "AM" and hrs < 13:
        if hrs == 12:
            hrs = 00
            hrs = str(hrs).zfill(2)
            time = hrs + s[2:8]
            return time
        else:
            hrs = str(hrs).zfill(2)
            time = hrs + s[2:8]
            return time
    elif s[-2:] == "PM" and hrs < 24:
        if hrs == 12:
            return s[0:8]
        else:
            hrs = hrs + 12
            hrs = str(hrs)
            time = hrs + s[2:8]
            return time


result = timeConversion(s)
print(result)
