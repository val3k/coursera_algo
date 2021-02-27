import heapq


class Solver():
    def __init__(self, board):
        self.board = board
        self.moves = 0
        self.minpq = []
        self.game_tree = []
        self.loops = 0

    def isSolvable(self):
        if self.loops > 3:
            return False
        else:
            return True

    def moves(self):
        return self.moves

    def solution(self):
        prior = self.moves + self.board.hamming()
        heapq.heappush(self.minpq, (prior, self.board))
        while True:
            self.game_tree.append(heapq.heappop(self.minpq))
            self.minpq = []
            self.moves += 1
            last_board = self.game_tree[-1][1]
            prev_board = self.game_tree[1-self.moves][1]
            possible_boards = last_board.neighbors()
            third_board = self.game_tree[1-self.moves-1][1]

            if third_board.tiles == last_board.tiles:
                self.loops += 1

            if last_board.isGoal():
                return self.game_tree

            if not self.isSolvable():
                return None

            for brd in possible_boards:
                if not last_board.equals(brd) and not prev_board.equals(brd):
                    prior = self.moves + brd.hamming()
                    heapq.heappush(self.minpq, (prior, brd))
