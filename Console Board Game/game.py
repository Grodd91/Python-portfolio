import random
import os
import time

class Game:
    def __init__(self):
        self.board_size = 10
        self.player_position = [0, 0]
        self.goal_position = [random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)]
        self.obstacle_positions = [[random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)] for _ in range(5)]
        self.score = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self):
        self.clear_screen()
        print("Score:", self.score)
        for i in range(self.board_size):
            for j in range(self.board_size):
                if [i, j] == self.player_position:
                    print("P", end=" ")
                elif [i, j] == self.goal_position:
                    print("G", end=" ")
                elif [i, j] in self.obstacle_positions:
                    print("O", end=" ")
                else:
                    print("-", end=" ")
            print()

    def move_player(self, direction):
        steps = 5  # Number of steps for the animation
        delta = [0, 0]  # Change in position for animation
        if direction == "up" and self.player_position[0] > 0:
            delta[0] = -1
        elif direction == "down" and self.player_position[0] < self.board_size - 1:
            delta[0] = 1
        elif direction == "left" and self.player_position[1] > 0:
            delta[1] = -1
        elif direction == "right" and self.player_position[1] < self.board_size - 1:
            delta[1] = 1

        for _ in range(steps):
            # Update player position for animation
            self.player_position[0] += delta[0] / steps
            self.player_position[1] += delta[1] / steps
            self.display_board()
            time.sleep(0.05)  # Adjust animation speed

        # Round player position to integer values
        self.player_position = [round(self.player_position[0]), round(self.player_position[1])]

    def check_collision(self):
        if self.player_position in self.obstacle_positions:
            return True
        return False

    def check_goal(self):
        if self.player_position == self.goal_position:
            return True
        return False

    def play(self):
        print("Welcome to the game!")
        while True:
            self.display_board()

            direction = input("Enter direction (up/down/left/right): ").lower()
            if direction in ["up", "down", "left", "right"]:
                self.move_player(direction)
                if self.check_collision():
                    print("Game over! You hit an obstacle.")
                    break
                elif self.check_goal():
                    print("Congratulations! You reached the goal!")
                    self.score += 1
                    self.goal_position = [random.randint(0, self.board_size-1), random.randint(0, self.board_size-1)]
            else:
                print("Invalid direction! Please enter up/down/left/right.")

if __name__ == "__main__":
    game = Game()
    game.play()
