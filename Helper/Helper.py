class Vector2:
    """
       向量
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 将函数转移到类中，就是静态方法．
    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)

    @staticmethod
    def left_up():
        return Vector2(-1, -1)

    @staticmethod
    def left_down():
        return Vector2(1, -1)

    @staticmethod
    def right_up():
        return Vector2(-1, 1)

    @staticmethod
    def right_down():
        return Vector2(1, 1)


class DoubleListHelper:
    """
        二维列表助手类
            定义：在开发过程中，所有对二维列表的常用操作．
    """

    @staticmethod
    def get_elements(list_target, v_pos, v_dir, count):
        result = []
        for i in range(count):
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            result.append(list_target[v_pos.x][v_pos.y])
        return result

#
# # 测试．．．．．．．．．．．．．
# list01 = [
#     ["00", "01", "02", "03"],
#     ["10", "11", "12", "13"],
#     ["20", "21", "22", "23"],
# ]
#
# # 10               向右　　　　　3　　　　－－> 11 12  13
# re01 = DoubleListHelper.get_elements(list01, Vector2(1, 0), Vector2.right(), 3)
# print(re01)
#
# # 23               向左         3      -->22 21 20
# re02 = DoubleListHelper.get_elements(list01, Vector2(2, 3), Vector2.left(), 3)
# print(re02)
#
# # 02               向下         2      -->12 22
# re03 = DoubleListHelper.get_elements(list01, Vector2(0, 2), Vector2.down(), 2)
# print(re03)
#
# # 20               右上         2      -->11 02
# re04 = DoubleListHelper.get_elements(list01, Vector2(2, 0), Vector2.right_up(), 2)
# print(re04)
