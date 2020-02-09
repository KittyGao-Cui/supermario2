import os
import pygame as pg
from abc import ABC, abstractmethod

keybinding = {  # 键盘绑定
    'action': pg.K_s,   # 行动键
    'jump': pg.K_SPACE,  # 跳跃
    'left': pg.K_LEFT,   # 左跑
    'right': pg.K_RIGHT,  # 右跑
    'down': pg.K_DOWN    # 下蹲
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
        self.fps = 60    # 帧频率为60
        self.current_time = 0.0
        self.keys = pg.key.get_pressed()  # 获取键盘上所有按键的状态
        self.state_dict = {}   # 状态字典
        self.state_name = None
        self.state = None

    def setup_states(self, state_dict, start_state):   # 设置状态
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def update(self):   # 更新状态时间
        self.current_time = pg.time.get_ticks()   # 获取以毫秒为时间间隔的时间
        if self.state.done:   # 如果状态结束为真
            self.flip_state()    # 跳状态
        self.state.update(self.screen, self.keys, self.current_time)   # 更新状态数据

    def flip_state(self):   # 跳状态
        previous, self.state_name = self.state_name, self.state.next  # 之前的状态名，下一个状态名
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)

    def event_loop(self):   # 事件循环
        for event in pg.event.get():  # 在游戏循环中监听事件
            if event.type == pg.QUIT:   # 如果事件类型为用户按下关闭按钮
                self.done = True   # 状态结束为真
            elif event.type == pg.KEYDOWN:     # 键盘被按下
                self.keys = pg.key.get_pressed()   # 获取键盘上所有的按键状态
            elif event.type == pg.KEYUP:    # 键盘被放开
                self.keys = pg.key.get_pressed()

    def main(self):    # 主函数
        while not self.done:   # 状态结束不为真时
            self.event_loop()   # 循环监听事件
            self.update()     # 更新状态时间
            pg.display.update()   # 更新部分界面显示信息
            self.clock.tick(self.fps)   # 设置游戏的帧频， 帧率可以理解为游戏在一秒钟内进行多少次画面刷新。

def get_image(sheet, x, y, width, height, colorkey, scale):   # 获取图像
        image = pg.Surface([width, height])    # 设置pygame的界面大小
        rect = image.get_rect()   # 处理矩形图像的方法

        image.blit(sheet, (0, 0), (x, y, width, height))  # 将一个图像（Surface 对象）绘制到另一个图像上方
        image.set_colorkey(colorkey)
        image = pg.transform.scale(image,     # 图像大小的缩放
                                   (int(rect.width*scale),
                                    int(rect.height*scale)))
        return image

def load_all_gfx(directory, colorkey=(255,0,255), accept=('.png', '.jpg', '.bmp', '.gif')):   # 加载文件夹中的图片
    graphics = {}   # 图标字典
    for pic in os.listdir(directory):   # os.listdir():返回文件夹中的文件
        name, ext = os.path.splitext(pic)   # 分离文件名与扩展名
        if ext.lower() in accept:   # Python判断一个文件夹内哪些文件是accept扩展名中的图片实例
            img = pg.image.load(os.path.join(directory, pic))  # os.path.join()函数：连接两个或更多的路径名组件   pygame.image.load()从文件加载新图片。
            if img.get_alpha():    # 如果获取到了图像的透明度
                img = img.convert_alpha()    # 保留图像的透明部分
            else:
                img = img.convert()   # 将图像转化为surface对象
                img.set_colorkey(colorkey)  # 设置透明颜色键，与colorkey颜色相同的任何像素都是透明的
            graphics[name] = img  # 图像列表
    return graphics
