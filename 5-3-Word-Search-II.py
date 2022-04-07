from collections import defaultdict


class Solution:
    def findWords(self, board: list, words: list) -> list:
        self.result = set()
        self.char_dict = defaultdict(set)
        self.y_max = len(board)
        self.x_max = len(board[0])
        for y in range(len(board)):
            for x in range(len(board[0])):
                self.char_dict[board[y][x]].add((y, x))

        for word in words:
            if all([c in self.char_dict for c in word]):
                for yx in self.char_dict[word[0]]:
                    road_list = [yx]
                    tmp_list = []
                    self.backtracking(road_list, word, board)
        return self.result

    def backtracking(self, road_list, word, board):
        if len(road_list) == len(word):
            self.result.add(word)
            return

        for yx in self.valid_roads(road_list, word, board):
            road_list.append(yx)
            self.backtracking(road_list, word, board)
            road_list.pop()

    def valid_roads(self, road_list, word, board):
        next_char = word[len(road_list)]
        cur_y, cur_x = road_list[-1]
        tmp = []

        next_y = cur_y - 1
        if next_y >= 0 and board[next_y][cur_x] == next_char and (next_y, cur_x) not in road_list:
            tmp.append((next_y, cur_x))
        next_y = cur_y + 1
        if next_y < self.y_max and board[next_y][cur_x] == next_char and (next_y, cur_x) not in road_list:
            tmp.append((next_y, cur_x))
        next_x = cur_x - 1
        if next_x >= 0 and board[cur_y][next_x] == next_char and (cur_y, next_x) not in road_list:
            tmp.append((cur_y, next_x))
        next_x = cur_x + 1
        if next_x < self.x_max and board[cur_y][next_x] == next_char and (cur_y, next_x) not in road_list:
            tmp.append((cur_y, next_x))
        return tmp
