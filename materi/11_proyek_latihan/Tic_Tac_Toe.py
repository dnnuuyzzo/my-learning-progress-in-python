from typing import List, Optional


class Board:
    def __init__(self):
        self.cells: List[str] = [" "] * 9

    def display(self) -> None:
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.cells[i]} | {self.cells[i+1]} | {self.cells[i+2]} ")
            if i < 6:
                print("---+---+---")
        print("\n")

    def make_move(self, index: int, player: str) -> bool:
        if self.cells[index] == " ":
            self.cells[index] = player
            return True
        return False

    def is_full(self) -> bool:
        return " " not in self.cells

    def check_winner(self) -> Optional[str]:
        win_patterns = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]

        for a, b, c in win_patterns:
            if self.cells[a] == self.cells[b] == self.cells[c] != " ":
                return self.cells[a]
        return None

    def reset(self) -> None:
        self.cells = [" "] * 9


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = "X"

    def switch_player(self) -> None:
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self) -> None:
        while True:
            self.board.display()
            print(f"Player {self.current_player}'s turn")

            try:
                move = int(input("Choose position (1-9): ")) - 1
                if move not in range(9):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please choose 1-9.")
                continue

            if not self.board.make_move(move, self.current_player):
                print("Cell already taken. Try again.")
                continue

            winner = self.board.check_winner()
            if winner:
                self.board.display()
                print(f"🎉 Player {winner} wins!")
                self.board.reset()
                break

            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                self.board.reset()
                break

            self.switch_player()


if __name__ == "__main__":
    Game().play()