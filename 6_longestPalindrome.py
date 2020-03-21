class Solution:
    def force(self, s):
        length, longest = 0, []
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if s[j] == s[i]:
                    # 判断是否为回文字符串
                    if s[i:j+1] == s[i:j+1][::-1]:
                        if length <= j - i + 1:
                            length = j - i + 1
                            longest += [s[i:j+1]]
        return longest

    def spread(self, s, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def spread_from_center(self, s: str):

        if s == s[::-1]:
            return s
        longest = s[:1]
        for i in range(len(s)):
            palindrome_odd = self.spread(s, i, i)
            palindrome_even = self.spread(s, i, i + 1)
            # 当前找到的最长回文子串
            longest = max(palindrome_odd, palindrome_even, longest, key=len)
        return longest
    def longestPalindrome(self, s: str):
        return{
            1: lambda s:self.force(s),
            2: lambda s:self.spread_from_center(s),
        }[2](s)


if __name__ == '__main__':
    s = "babad"
    test = Solution()
    print(test.longestPalindrome(s))

