from game_2048.dll import GameCoreController
from game_2048.dll import Direction
import os


class GameConsoleView:
    """
        控制台视图
    """

    def __init__(self):
        self.__controller = GameCoreController()

    def start(self):
        """
            游戏开始
        :return:
        """
        self.__controller.probability_random()
        self.__controller.probability_random()
        self.print_map()

    def print_map(self):
        """
            打印界面
        :return:
        """
        os.system("clear")
        print("----------------")
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(self.__controller.map[r][c], end="\t")
            print()

    def update(self):
        """
            更新逻辑
        :return:
        """
        while True:
            self.move_map()
            if self.__controller.map_check:
                self.__controller.probability_random()
            self.__controller.game_over()
            self.print_map()

    def move_map(self):
        dir = input("w,s,a,d")
        if dir == "w":
            self.__controller.move(Direction.up)
        elif dir == "s":
            self.__controller.move(Direction.down)
        elif dir == "a":
            self.__controller.move(Direction.left)
        elif dir == "d":
            self.__controller.move(Direction.right)



