class Solution:
    # count = 0
    def __init__(self):
        self.num_arr = []
        self.print_arr = []

    # fire_bool = True

    def isPalindrome(self, head) -> bool:
        # fire_bool = True
        self.num_arr.append(head.val)
        self.print_arr.append(head.val)

        if head.next:
            # if head.val == num_arr.pop(0):
            print("i am execured")
            # return False
            # self.num_arr.append(head.val)
            # self.print_arr.append(head.val)
            # fire_bool = self.isPalindrome(head.next)
            self.isPalindrome(head.next)
        # if not recurse_bool:
        #     return recurse_bool
        if self.num_arr:
            print("hello", head.val, self.num_arr[0])
            if head.val == self.num_arr.pop(0):
                print(" I am same")
                # fire_bool = True
                return True
                # return fire_bool
        print("I am different ")
        # fire_bool = False
        self.num_arr = []
        return False

    def isPalindrome2(self, head):
        norm_arr = []
        count = 0
        while head:
            norm_arr.append(head.val)
            head = head.next
            count = count + 1
        mid_count = count // 2
        odd_off = count % 2
        # print(norm_arr, norm_arr[:mid_count:1], norm_arr[:mid_count-1+odd_off:-1]
        # , count, mid_count)
        return norm_arr[:mid_count:1] == norm_arr[: mid_count - 1 + odd_off : -1]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


fire = ListNode(val=0)
length = 7
mid_val = length / 2
for i in range(1, length):
    # print(fire.val)
    if i >= mid_val:
        fire = ListNode(val=length - i - 1, next=fire)
    else:
        fire = ListNode(val=i, next=fire)


water = ListNode(val=1)
water = ListNode(2, water)
# water = ListNode(2, water)
# water = ListNode(1, water)
sol = Solution()
print(sol.isPalindrome2(fire))
# print(sol.num_arr)
# print(sol.isPalindrome(water))
# print(sol.num_arr)

# dark = ListNode(val=1)
# print(sol.isPalindrome(dark))

# # print(sol.print_arr)
# print(sol.num_arr)
