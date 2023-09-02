# 18班座位安排 \﻿ (•◡•) /

[![Author_page](https://img.shields.io/badge/Author%20page-on%20bilibili-green)](https://space.bilibili.com/290472819)

基于python、js的座位安排程序
> 偷偷说一声18班牛啤 (>▽<)

## BUG fix
### 在前三个版本的random_seats中，使用了array内置的sort()函数，传入随机数进行打乱。
  `array.sort(() => {return Math.round(Math.random()) - 0.5});`


### 这种打乱方式有问题，即打乱并不完全随机。
 > 以下是对 打乱前array的首字符 在打乱后出现的位置 的频数统计：
 
 > [1078, 712, 523, 416, 420, 439, 527, 580, 607]
 
 > 总计5302次打乱中，原位置不动(还是在首位置)出现了1078次，频率为20.3%
 
### 对此，在第四个版本中重写了打乱函数。
    function randArr(arr) {
        for (var i = 0; i < arr.length; i++) {
            var iRand = parseInt(arr.length * Math.random());
            var temp = arr[i];
            arr[i] = arr[iRand];
            arr[iRand] = temp;
        }
        return arr;
    }
 > 总计9319次打乱，以下是频数统计
 
 > [1007, 1005, 1017, 1014, 1122, 1043, 992, 1025, 1094]
 
 > 频率统计： 

 > 10.8% 10.8% 10.9% 10.9% 12.0% 11.2% 10.6% 11.0% 11.7%
 
 > 理想情况为 100%/9=11.1%
 
### 修改后打乱更为随机
 > 用 数组排序函数sort 反向实现 数组打乱，会出现 部分乱了部分不变的情况。



## 功能
  - 格式化输出座位表
  - 支持座位表Excel下载
  - ~~18班还没有学习小组，所以又随机了~~
  > 避免男女同桌
  
## 运行
  - 在python3环境下，运行./python_code/random_seats.py
  - 无需外部库
  - 打开 https://baoqi.js.org/random_seats 可使用在线版


---

##更新日志

    version 1.0  -2020.8.31
    实现了基本功能
    
    version 1.1  -2020.9.15
    更新排版与结束input
    
    version 2.0  -2020.10.3
    添加了网页版，移动了代码
    
    version 3.0  -2020.11.29
    改成学习小组模式，增加座位安排规范
    
    version 4.0  -2021.2.14
    重写打乱函数，添加致歉声明
    
    version 5.0  -2021.2.14
    18班牛啤! 更新了名单
    
    version 5.1  -2021.2.14
    男女同桌调整
    
    version 5.2  -2021.3.28
    女生座位调整.女生将不会抽到靠后的位置


## 关于代码使用的相关声明
  1. 代码仅供大家交流学习使用，欢迎大家进行修改和补充<br>
  2. 未经许可禁止未经允许将本项目的代码用作商业行为<br>
  
  
最后，祝大家好运\\(≧▽≦)/
---
