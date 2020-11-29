# coding:utf-8
import random


people = {1: '陈俊宇', 2: '陈铭隽', 3: '陈奕纶', 4: '邓历新', 5: '何启荣', 6: '黄炜钊', 7: '黄烨锋', 8: '黄钊华', 9: '李  可', 10: '李铭轩', 11: '李志翔', 12: '李宗轩', 13: '练浩诚', 14: '梁俊文', 15: '梁宇轩', 16: '林子尧', 18: '韦睿行', 19: '冼飘虹', 20: '许  航', 21: '叶孝轩', 22: '张  乐', 23: '郑  超', 24: '钟梓洋', 25: '朱信华', 26: '邹佳洵', 27: '陈楚原', 28: '陈隽欣', 29: '陈沛怡', 30: '陈易沛', 31: '陈钰甄', 32: '范海瑶', 33: '冯琬乔', 34: '何恩希', 35: '何文静', 36: '何宗阳', 37: '黄逸帆', 38: '黎晋旭', 39: '李烨彤', 40: '梁楚清', 41: '梁子怡', 42: '林雨涵', 43: '罗思薇', 44: '马麒越', 45: '邱  童', 46: '石粤礽', 47: '汪雨桐', 48: '谢砚琪', 49: '许艺馨', 50: '杨梓馨', 51: '詹  岚', 52: '张嘉宁', 53: '周熙临', 54: '朱怡晨', 55: '左芷溪'}

team_seats = {0: '0 1 2 3 4 5'.split(),
              1: '8 9 16 17 24 25'.split(),
              2: '10 11 18 19 26 27'.split(),
              3: '12 13 20 21 28 29'.split(),
              4: '32 33 40 41 48 49'.split(),
              5: '34 35 42 43 50 51'.split(),
              6: '36 37 44 45 52 53'.split(),
              7: '6 7 14 15 22 23'.split(),
              8: '30 31 38 39 46 47'.split()}

team_member = {0: '24 23 40 52 11 12'.split(),
              1: '45 29 4 8 26 25'.split(),
              2: '51 31 50 42 30 48'.split(),
              3: '46 36 38 34 28 33'.split(),
              4: '43 39 44 3 9 6'.split(),
              5: '10 18 21 32 55 35'.split(),
              6: '1 15 41 54 2 53'.split(),
              7: '16 49 14 5 7 19'.split(),
              8: '47 37 13 27 22 20'.split()}

def get_random_seats():
    global team_member

    def random_group():
        global group
        group = list(range(0, 9))
        random.shuffle(group)
        return group

    groups = random_group()
    result = [-1]*54
    for group in range(len(groups)):
        random.shuffle(team_member[group])


        for i in range(6):
            result[int(team_seats[group][i])] = int(team_member[groups[group]][i])
    return result




def print_seats(seats):
    """格式化输出座位表
    """
    print(seats)
    for y in range(7):
        for x in range(8):
            if not (x == 6 and y == 6 or x == 7 and y == 6):
                p = y*8+x-1
                if p >=17:
                    p += 1
                print('|'+str(people[seats[p]]), end='')
        print('|')


print_seats(get_random_seats())
input()
