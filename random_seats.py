# coding:utf-8
import random

people = {1: '陈俊宇', 2: '陈铭隽', 3: '陈奕纶', 4: '邓历新', 5: '何启荣', 6: '黄炜钊', 7: '黄烨锋', 8: '黄钊华', 9: '李  可', 10: '李铭轩', 11: '李志翔', 12: '李宗轩', 13: '练浩诚', 14: '梁俊文', 15: '梁宇轩', 16: '林子尧', 18: '韦睿行', 19: '冼飘虹', 20: '许  航', 21: '叶孝轩', 22: '张  乐', 23: '郑  超', 24: '钟梓洋', 25: '朱信华', 26: '邹佳洵', 27: '陈楚原', 28: '陈隽欣', 29: '陈沛怡', 30: '陈易沛', 31: '陈钰甄', 32: '范海瑶', 33: '冯琬乔', 34: '何恩希', 35: '何文静', 36: '何宗阳', 37: '黄逸帆', 38: '黎晋旭', 39: '李烨彤', 40: '梁楚清', 41: '梁子怡', 42: '林雨涵', 43: '罗思薇', 44: '马麒越', 45: '邱  童', 46: '石粤礽', 47: '汪雨桐', 48: '谢砚琪', 49: '许艺馨', 50: '杨梓馨', 51: '詹  岚', 52: '张嘉宁', 53: '周熙临', 54: '朱怡晨', 55: '左芷溪'}

def get_random_seats():
    BOYS = list(range(1, 27))
    BOYS.remove(17)
    GIRLS = list(range(27, 56))
    random.shuffle(BOYS)
    random.shuffle(GIRLS)



    result = []
    seat_sex = [0]*(len(BOYS)//2) + [1]*(len(GIRLS)//2)
    if len(seat_sex) != len(BOYS+GIRLS):
        seat_sex.append(0.5)
    random.shuffle(seat_sex)

    for num in range(1, len(BOYS+GIRLS)//2+1):
        sex = seat_sex.pop(0)
        if sex == 0:
            result.append([BOYS.pop(0), BOYS.pop(0)])
        elif sex == 1:
            result.append([GIRLS.pop(0), GIRLS.pop(0)])
        else:

            opposite = [BOYS.pop(0), GIRLS.pop(0)]
            print(people[opposite[0]], people[opposite[1]], 'opposite')
            random.shuffle(opposite)
            result.append(opposite)

    return result

def print_seats(seats):

    for y in range(7):
        print(y+1, ' ', end='')
        for x in range(4):
            if not (x==3 and y==6):

                pair = seats[y*4+x]

                print('|'+people[pair[0]]+' '+people[pair[1]], end='')
        print('|')

print_seats(get_random_seats())