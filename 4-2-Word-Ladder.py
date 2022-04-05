

def find_neighbors(word_list, word1):
    neighbors = []
    for word2 in word_list:
        count = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                count += 1
        if count == 1:
            neighbors.append(word2)
    return neighbors


def find_neighbors_v2(word_list, word):
    neighbors = []
    chars = [c for c in word]
    for i in range(len(chars)):
        tmp = chars.copy()
        for j in range(ord('a'), ord('z' ) +1):
            tmp[i] = chr(j)
            neighbors.append(''.join(tmp))
    return neighbors


def solution1(beginWord: str, endWord: str, wordList: list) -> int:
    if endWord not in wordList:
        return 0
    queue = []
    word_set = set(wordList)
    queue.append((beginWord, 1))
    if beginWord in word_set:
        word_set.remove(beginWord)
    # level = 0
    while queue:
        node, level = queue.pop(0)
        if node == endWord:
            return level
        neighbors = find_neighbors_v2(word_set, node)
        for neighbor in neighbors:
            if neighbor in word_set:
                word_set.remove(neighbor)
                queue.append((neighbor, level +1))
    return 0


def solution2(beginWord: str, endWord: str, wordList: list) -> int:
    if endWord not in wordList:
        return 0
    queue_left = []
    queue_right = []
    word_set = set(wordList)
    queue_left.append((beginWord, 1))
    queue_right.append((endWord, 1))
    if beginWord in word_set:
        word_set.remove(beginWord)
    # level = 0
    neighbors_left, neighbors_right = [], []
    while queue_left:
        node, level = queue_left.pop(0)
        if node == endWord:
            return level
        if neighbors_left:
            neighbors_left = find_neighbors_v2(word_set, node)
        if neighbors_right:
            neighbors_right = find_neighbors_v2(word_set, node)
        if len(neighbors_left) < len(neighbors_right):
            neighbors = neighbors_left
            neighbors_left = []
        else:
            neighbors = neighbors_right
            neighbors_right = []
        for neighbor in neighbors:
            if neighbor in word_set:
                word_set.remove(neighbor)
                queue_left.append((neighbor, level +1))
    return 0
