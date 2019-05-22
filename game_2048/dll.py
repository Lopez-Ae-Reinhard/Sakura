import random
import copy


class GameCoreController:
    """
        游戏核心算法
    """

    def __init__(self):
        self.__map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.map_check = False

    @property
    def map_check(self):
        return self.__map_check

    @map_check.setter
    def map_check(self, value):
        self.__map_check = value

    @property
    def map(self):
        return self.__map

    @staticmethod
    def list_sort(list_target):
        """
            将零元素移动到末尾
        :return:
        """
        for max01 in range(len(list_target) - 1):
            for min01 in range(max01 + 1, len(list_target)):
                if list_target[min01] != 0:
                    list_target[min01], list_target[max01] = list_target[max01], list_target[min01]

    def merge(self, list_target):
        """
            合并相邻函数
        :return:
        """
        GameCoreController.list_sort(list_target)
        for i in range(len(list_target) - 1):
            if list_target[i] == list_target[i + 1]:
                list_target[i] += list_target[i + 1]
                list_target[i + 1] = 0
        GameCoreController.list_sort(list_target)

    def __move_left(self):
        """
            左移
        :return:
        """
        for x in range(len(self.__map)):
            self.merge(self.__map[x])
        return self.__map

    def __move_right(self):
        for x in range(len(self.__map)):
            self.__map[x] = self.__map[x][::-1]
            self.merge(self.__map[x])
            self.__map[x][::-1] = self.__map[x]
        return self.__map

    def __move_up(self):
        """
            上移
        :param list02:
        :return:
        """
        for y in range(len(self.__map)):
            list01 = []
            for x in range(len(self.__map)):
                list01.append(self.__map[x][y])
            self.merge(list01)
            for x in range(len(self.__map)):
                self.__map[x][y] = list01[x]
        return self.__map

    def __move_down(self):
        """
            下移
        :param list02:
        :return:
        """
        for y in range(len(self.__map)):
            list01 = []
            for x in range(len(self.__map)):
                list01.append(self.__map[len(self.__map) - x - 1][y])
            self.merge(list01)
            for x in range(len(self.__map)):
                self.__map[len(self.__map) - x - 1][y] = list01[x]
        return self.__map

    def move(self,dir):
        self.map_check = False
        map01 = self.__map_judge()
        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.right:
            self.__move_right()
        self.map_check = self.map_control(map01)

    def map_control(self,map):
        if self.map != map:
            return True

    def __point_zero(self):
        """
            查找所有0的位置
        :return:
        """
        list01 = []
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    list01.append((r, c))
        return list01

    def __random_num(self):
        """
            随机选择一个为0的位置
        :return:
        """
        end_num = len(self.__point_zero())
        num = random.randint(0, end_num - 1)
        return self.__point_zero()[num]

    def probability_random(self):
        """
            如果有为0的随机选择2或4替换
            #4的概率为10%,2的概率为90%
        :return:
        """
        if len(self.__point_zero()) == 0:
            return
        rand_num = self.__random_num()
        list01 = [4, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        end_num = len(list01)
        num = random.randint(0, end_num - 1)
        pro_num = list01[num]
        self.__map[rand_num[0]][rand_num[1]] = pro_num

    def __map_judge(self):
        """
            对二维列表进行深拷贝
        :return:
        """
        map01 = copy.deepcopy(self.map)
        return map01

    def game_over(self):
        if len(self.__point_zero()) == 0:
            print("游戏结束")


class Direction:
    up = "w"
    down = "s"
    left = "a"
    right = "d"
