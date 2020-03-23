class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        print(res)
        # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
        # str.join(sequence)
        return "".join(res)


if __name__ == '__main__':
    test = Solution()
    s = "LEETCODEISHIRING"
    print(test.convert(s, 3))


if __name__ == '__main__':
    test = Solution()
    s = "LEETCODEISHIRING"
    print(test.convert(s, 3))
