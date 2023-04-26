# from players.player import Player
from simulation.players.player import Player
import cv2

class SimplePlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def behave(self):
        # while True:
        #     img_top = self.getCameraFrame("top")
        #     cv2.imshow("Top", img_top)
        #     cv2.waitKey(1)

        for i in range(6):
            self.move("Forwards")
        for i in range(2):
            self.move("Backwards")

        return
