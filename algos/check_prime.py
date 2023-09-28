# Enter your code here. Read input from STDIN. Print output to STDOUT
def check_prime(num):
    if num in [0, 1]:
        return "Not Prime"
    num_sqrt = int(num ** (0.5))
    if num % 2 == 0:
        return "Not prime"
    for i in range(3, num_sqrt + 1, 2):
        if num % i == 0:
            return "Not prime"
    return "Prime"


if __name__ == "__main__":
    n = int(input())
    tobe_checked = []
    for i in range(n):
        tobe_checked.append(int(input()))

    for num in tobe_checked:
        print(check_prime(num))
