class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


count = 0
num_arr = []
print_arr = []
recurse_bool = True


def isPalindrome(head: ListNode) -> bool:
    # count = 0
    # num_arr = []
    # cur_val = head.val
    # head = head.next
    # count += 1
    # print(cur_val)
    fire_bool = True
    num_arr.append(head.val)
    print_arr.append(head.val)
    if head.next:
        # if head.val == num_arr.pop(0):
        #     print('i am execured')
        # return False
        # num_arr.append(head.val)
        # print_arr.append(head.val)
        fire_bool = isPalindrome(head.next)
    # if not recurse_bool:
    #     return recurse_bool
    if fire_bool and num_arr:
        print(head.val, num_arr[0])
        if head.val == num_arr.pop(0):
            print("I am same")
            return True
    print("I am not same")
    return False

    # head = head.next()

    # while head:
    #     cur_val = head.val
    #     head = head.next
    #     count += 1
    #     print(cur_val)
    # for i in iter(head):
    #     print(i.val)


fire = ListNode(val=0)
length = 7
mid_val = length / 2
for i in range(1, length):
    # print(fire.val)
    if i >= mid_val:
        fire = ListNode(val=length - i - 1, next=fire)
    else:
        fire = ListNode(val=i, next=fire)
# print(fire.val)
# fire.val = 9
water = ListNode(val=1)
water = ListNode(2, water)
# water = ListNode(2, water)
# water = ListNode(1, water)
# isPalindrome(fire)
print(isPalindrome(water))
print(num_arr)
print(print_arr)
