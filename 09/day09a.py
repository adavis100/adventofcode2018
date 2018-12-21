PLAYER_COUNT = 9
HIGHEST_MARBLE = 25

def main():
    play_game()
    return

def play_game():
    scores = [0] * PLAYER_COUNT
    game = Game()
    for marble in range(HIGHEST_MARBLE):
        for player in range(PLAYER_COUNT):
            scores[player] += game.play_marble(marble)
            print('{}: ({}, {})'.format(player, scores[player], game.current))
            print(player)
    print(max(scores))


class Game:
    def __init__(self):
        self.current = Marble(0)

    def play_marble(self, value):
        if value % 23 == 0:
            return self.play_scoring_marble(value)
        else:
            return self.play_normal_marble(value)

    def play_scoring_marble(self, value):
        to_remove = self.current.left.left.left.left.left.left.left
        score = value + to_remove.value
        position = to_remove.right
        position.left = to_remove.left
        to_remove.left.right = position
        self.current = position
        return score

    def play_normal_marble(self, value):
        insert_pos = self.current.right
        next = insert_pos.right
        new_marble = Marble(value, insert_pos, next)
        insert_pos.right.left = new_marble
        insert_pos.right = new_marble
        return (0, new_marble)
        

class Marble:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left or self
        self.right = right or self




class Circle:
    def __init__(self):
        return

if __name__ == '__main__':
    main()