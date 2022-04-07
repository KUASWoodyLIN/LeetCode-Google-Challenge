from utils.timer import timer


class Solution:
    @timer
    def findStrobogrammatic(self, n: int) -> list:
        middle_pair = ["0", "1", "8"]
        self.other_pair = {"1": "1", "6": "9", "9": "6", "8": "8", "0": "0"}
        self.first_pair = {"1": "1", "6": "9", "9": "6", "8": "8"}
        self.n = n
        self.output_list = []
        if n == 1:
            return middle_pair
        elif n % 2:
            for i in middle_pair:
                tmp_list = [i]
                self.recursion(0, tmp_list)
        else:
            tmp_list = []
            self.recursion(0, tmp_list)
        return self.output_list

    def recursion(self, n, tmp_list):
        if n == self.n // 2:
            self.output_list.append(''.join(tmp_list))
            return
        elif n == self.n // 2 - 1:
            for start, end in self.first_pair.items():
                tmp_list.insert(0, start)
                tmp_list.append(end)
                self.recursion(n + 1, tmp_list)
                tmp_list.pop()
                tmp_list.pop(0)
        else:
            for start, end in self.other_pair.items():
                tmp_list.insert(0, start)
                tmp_list.append(end)
                self.recursion(n + 1, tmp_list)
                tmp_list.pop()
                tmp_list.pop(0)


s = Solution()
s.findStrobogrammatic(1)
s.findStrobogrammatic(2)
s.findStrobogrammatic(3)
s.findStrobogrammatic(4)
