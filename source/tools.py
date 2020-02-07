import os
import pygame as pg
from abc import ABC, abstractmethod

keybinding = {  # 键盘绑定
    'action':pg.K_s,
    'jump':pg.K_SPACE,
    'left':pg.K_LEFT,
    'right':pg.K_RIGHT,
    'down':pg.K_DOWN
}

class State():     # 状态类
    def __init__(self):
        self.start_time = 0.0
        self.current_time = 0.0
        self.done = False    # 状态结束为否
        self.next = None     # 下一个状态为空
        self.persist = {}    # 传递数据为空字典

    @abstractmethod
    def startup(self, current_time, persist):  # 状态开始
        '''abstract method'''

    def cleanup(self):    # 状态结束清空
        self.done = False
        return self.persist

    @abstractmethod
    def update(self, surface, keys, current_time):   # 状态运行过程中的数据更新:界面，键，当前时间
        '''abstract method'''

class Control():   # 控制类
    def __init__(self):
        self.screen = pg.display.get_surface()   # 获取当前显示的 Surface 对象
        self.done = False
        self.clock = pg.time.Clock()   # python时间性能测量：time.Clock()：测量程序运行的cpu时间
        self.fps = 60    # 帧为60
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()  # pygame.key.get_pressed()  —  获取键盘上所有按键的状态
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.name = None
        self.clock = 0.0
        self.current_time = 0.0

