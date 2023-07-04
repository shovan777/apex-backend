def fizzBuzz(n: int):
    def replaceBuzz(pos_num):
        if pos_num % 3 == 0 and pos_num % 5 == 0:
            return "FizzBuzz"
        if pos_num % 3 == 0:
            return "Fizz"
        if pos_num % 5 == 0:
            return "Buzz"
        return str(pos_num)

    # return map(replaceBuzz, range(1, n+1))
    return map(replaceBuzz, range(1, n + 1))
