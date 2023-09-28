# Enter your code here. Read input from STDIN. Print output to STDOUT
class Date:
    def __init__(self, date_arr):
        self.day = int(date_arr[0])
        self.month = int(date_arr[1])
        self.year = int(date_arr[2])


def get_fine(ret_date, exp_date):
    rdate = Date(ret_date)
    edate = Date(exp_date)
    if rdate.year == edate.year:
        if rdate.month == edate.month:
            if rdate.day <= edate.day:
                return 0
            else:
                return 15 * (rdate.day - edate.day)
        elif rdate.month < edate.month:
            return 0
        else:
            return 500 * (rdate.month - edate.month)
    elif rdate.year < edate.year:
        return 0
    else:
        return 10000


if __name__ == "__main__":
    ret_date = input().strip().split(" ")
    exp_date = input().strip().split(" ")
    # print(ret_date)
    print(get_fine(ret_date, exp_date))
