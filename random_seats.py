# coding:utf-8
import random

people = {1: '陈俊宇', 2: '陈铭隽', 3: '陈奕纶', 4: '邓历新', 5: '何启荣', 6: '黄炜钊', 7: '黄烨锋', 8: '黄钊华', 9: '李  可', 10: '李铭轩', 11: '李志翔', 12: '李宗轩', 13: '练浩诚', 14: '梁俊文', 15: '梁宇轩', 16: '林子尧', 18: '韦睿行', 19: '冼飘虹', 20: '许  航', 21: '叶孝轩', 22: '张  乐', 23: '郑  超', 24: '钟梓洋', 25: '朱信华', 26: '邹佳洵', 27: '陈楚原', 28: '陈隽欣', 29: '陈沛怡', 30: '陈易沛', 31: '陈钰甄', 32: '范海瑶', 33: '冯琬乔', 34: '何恩希', 35: '何文静', 36: '何宗阳', 37: '黄逸帆', 38: '黎晋旭', 39: '李烨彤', 40: '梁楚清', 41: '梁子怡', 42: '林雨涵', 43: '罗思薇', 44: '马麒越', 45: '邱  童', 46: '石粤礽', 47: '汪雨桐', 48: '谢砚琪', 49: '许艺馨', 50: '杨梓馨', 51: '詹  岚', 52: '张嘉宁', 53: '周熙临', 54: '朱怡晨', 55: '左芷溪'}


def get_random_seats():
    """获取随机座位数据
    input: None
    OUTPUT: List
    输出格式: [[同桌对1]， [同桌对2]， ...]
        E.g. [[2, 5], [7, 12], ...]
        其中，数字为学号
    """

    # 生成打乱后的男女学号
    boys = list(range(1, 27))
    boys.remove(17)
    girls = list(range(27, 56))
    random.shuffle(boys)
    random.shuffle(girls)

    # 确定每对同桌性别
    result = []
    seat_sex = [0]*(len(boys)//2) + [1]*(len(girls)//2)
    if len(seat_sex) != len(boys+girls):
        seat_sex.append(0.5)  # 此处0.5为男女同桌
    random.shuffle(seat_sex)

    # 将男生女生学号随机填入座位
    for num in range(1, len(boys+girls)//2+1):
        sex = seat_sex.pop(0)
        if sex == 0:
            result.append([boys.pop(0), boys.pop(0)])
        elif sex == 1:
            result.append([girls.pop(0), girls.pop(0)])
        else:

            opposite = [boys.pop(0), girls.pop(0)]
            print(people[opposite[0]], people[opposite[1]], 'opposite')  # 男女同桌公开处刑
            random.shuffle(opposite)
            result.append(opposite)

    return result


def print_seats(seats):
    """格式化输出座位表
    """

    for y in range(7):
        print(y+1, ' ', end='')
        for x in range(4):
            if not (x == 3 and y == 6):
                pair = seats[y*4+x]

                print('|'+people[pair[0]]+' '+people[pair[1]], end='')
        print('|')


print_seats(get_random_seats())
