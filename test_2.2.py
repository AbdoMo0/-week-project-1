import math

def min_board_size(w, h, n):
    rows = math.ceil(math.sqrt(n * h / w))
    cols = math.ceil(math.sqrt(n * w / h))
    board_size = max(w * cols / h, h * rows / w)
    return math.ceil(board_size)

w, h, n = map(int, input().split())
print(min_board_size(w, h, n))

##Sorry, but the algorithm is not correct. and answer is also incorrect.

