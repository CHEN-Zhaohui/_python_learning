class Solution:
    def reverse(self, x: int) -> int:
        num, temp = 0, abs(x)
        while temp > 0:
            num = num*10 + temp % 10
            temp //= 10
        if x < 0:
            num = -num
        return num if -2**31 < num < 2**31-1 else 0


if __name__ == '__main__':
    x = -123
    test = Solution()
    print(test.reverse(x))

