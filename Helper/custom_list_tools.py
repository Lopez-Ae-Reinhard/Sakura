"""
    针对列表的自定义工具
    配合lambda使用
"""


class ListHelper:
    @staticmethod
    def find_all(target, func_condition):
        """
            查找列表中满足条件的所有元素
        :param target: 列表
        :param func_condition: 判断条件\
               # 函数/方法类型\
               # --参数:列表内对象\
               # --返回值:是否满足条件bool类型
        :return: 返回所有元素
        """
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(target, func_condition):
        """
            查找列表中满足条件的第一个元素
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return: 返回符合要求的第一个元素
        """
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def last(target, func_condition):
        """
            查找列表中满足条件的最后一个元素
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return:返回符合要求的最后一个元素
        """
        for item in range(len(target) - 1, -1, -1):
            if func_condition(target[item]):
                return target[item]

    @staticmethod
    def select(target, func_condition):
        """
            筛选列表当中指定条件的数据
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return: 返回所有符合条件的数据
        """
        for item in target:
            yield func_condition(item)

    @staticmethod
    def exists(target, func_condition):
        """
            判断列表当中是否包含制定条件的元素
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return: 返回True或者False
        """
        for item in target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def get_max(target, func_condition):
        """
            获取列表中指定条件的最大的元素,如果相等返回第一个
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return: 最大的元素
        """
        max_num = target[0]
        for item in range(1, len(target)):
            if func_condition(max_num) < func_condition(target[item]):
                max_num = target[item]
        return max_num

    @staticmethod
    def get_min(target, func_condition):
        """
            获取列表中指定条件的最小的元素,如果相等返回第一个
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return: 最小的元素
        """
        min_num = target[0]
        for item in range(1, len(target)):
            if func_condition(min_num) < func_condition(target[item]):
                min_num = target[item]
        return min_num

    # @staticmethod
    # def get_maxs(target, func_condition):
    #     """
    #         获取列表中最大的元素,如果相等返回第一个
    #     :param target: 列表
    #     :param func_condition: func_condition:判断条件
    #             函数/方法类型
    #             --参数:列表内对象
    #     :return: 最大的元素
    #     """
    #     max_num = target[0]
    #     for item in range(1, len(target)):
    #         if func_condition(max_num) < func_condition(target[item]):
    #             max_num = target[item]
    #     return max_num

    @staticmethod
    def list_ascending(target, func_condition):
        """
            将列表中的元素根据指定条件进行升序排列
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return: 无
        """
        for r in range(len(target) - 1):
            for c in range(r + 1, len(target)):
                if func_condition(target[r]) > func_condition(target[c]):
                    target[c], target[r] = target[r], target[c]

    @staticmethod
    def __sub_sort_ascending(target, func_condition, alpha, omega):
        key = target[alpha]
        while alpha < omega:
            # 后面的数向前交换
            while alpha < omega and func_condition(target[omega]) > func_condition(key):
                omega -= 1
            target[alpha] = target[omega]
            # 前面的数向后交换
            while alpha < omega and func_condition(target[alpha]) <= func_condition(key):
                alpha += 1
            target[omega] = target[alpha]
        target[alpha] = key
        return alpha

    @staticmethod
    def __quick_ascending(target, func_condition, alpha, omega):
        """
            将列表中的元素根据指定条件进行升序排列
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :param alpha: 起始索引
        :param omega: 结束索引
        :return:
        """
        if alpha < omega:
            key = ListHelper.__sub_sort_ascending(target, func_condition, alpha, omega)
            ListHelper.__quick_ascending(target, func_condition, alpha, key - 1)
            ListHelper.__quick_ascending(target, func_condition, key + 1, omega)

    @staticmethod
    def quick_list_ascending(target, func_condition):
        """
            将列表中的元素根据指定条件进行升序排列(快速排序)
        :param target: 列表
        :param func_condition:func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return:
        """
        alpha = 0
        omega = len(target) - 1
        ListHelper.__quick_ascending(target, func_condition, alpha, omega)

    @staticmethod
    def __sub_sort_descending(target, func_condition, alpha, omega):
        key = target[alpha]
        while alpha < omega:
            # 后面的数向前交换
            while alpha < omega and func_condition(target[omega]) < func_condition(key):
                omega -= 1
            target[alpha] = target[omega]
            # 前面的数向后交换
            while alpha < omega and func_condition(target[alpha]) >= func_condition(key):
                alpha += 1
            target[omega] = target[alpha]
        target[alpha] = key
        return alpha

    @staticmethod
    def __quick_descending(target, func_condition, alpha, omega):
        """
            将列表中的元素根据指定条件进行降序排列
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :param alpha: 起始索引
        :param omega: 结束索引
        :return:
        """
        if alpha < omega:
            key = ListHelper.__sub_sort_descending(target, func_condition, alpha, omega)
            ListHelper.__quick_descending(target, func_condition, alpha, key - 1)
            ListHelper.__quick_descending(target, func_condition, key + 1, omega)

    @staticmethod
    def quick_list_descending(target, func_condition):
        """
            将列表中的元素根据指定条件进行降序排列(快速排序)
        :param target: 列表
        :param func_condition:func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return:
        """
        alpha = 0
        omega = len(target) - 1
        ListHelper.__quick_descending(target, func_condition, alpha, omega)

    @staticmethod
    def list_descending(target, func_condition):
        """
            将列表中的元素根据指定条件进行降序排列
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return: 无
        """
        for r in range(len(target) - 1):
            for c in range(r + 1, len(target)):
                if func_condition(target[r]) < func_condition(target[c]):
                    target[c], target[r] = target[r], target[c]

    @staticmethod
    def list_sort(target, func_condition, reverse=True):
        """
            将列表中的元素根据指定条件进行排列
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :param reverse: 输入判断
               # 如果是True则是升序,
               # 如果是False则是降序
               # second值默认为True
        :return: 无
        """
        if reverse == True:
            ListHelper.list_ascending(target, func_condition)
        else:
            ListHelper.list_descending(target, func_condition)

    @staticmethod
    def get_count(target, func_condition):
        """
            筛选列表当中指定条件的数据
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return: 返回符合要求的数据的个数,int
        """
        count = 0
        for item in target:
            if func_condition(item):
                count += 1
        return count

    @staticmethod
    def list_sum(target, func_condition):
        """
            计算列表中指定条件的元素的总和
        :param target: 列表
        :param func_condition: func_condition:判断条件
               # 函数/方法类型
               # --参数:列表内对象
        :return:返回符合条件元素的总和,int
        """
        sum_value = 0
        for item in target:
            sum_value += func_condition(item)
        return sum_value

    # @staticmethod
    # def list_sum(target, func_condition):
    #     sum_value = 0
    #     for i in ListHelper.select(target, func_condition):
    #         sum_value += i
    #     return sum_value
