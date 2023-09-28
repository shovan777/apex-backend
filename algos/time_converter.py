def timeConversion(s):
    # Write your code here
    am_pm = s[-2:]
    s_hour = int(s[:2])
    if am_pm == "PM" and s_hour != 12:
        s_hour += 12
        print(str(s_hour) + s[2:-2])
    elif am_pm == "AM" and s_hour == 12:
        print("00" + s[2:-2])
    else:
        print(s[:-2])


timeConversion("12:05:45PM")
