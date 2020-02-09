import os
import pygame as pg
from . import constants as c
from . import tools  # .表示当前目录

pg.init()  # 初始化所有导入的pygame模块
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])    # 控制哪些事件允许进入队列：键盘被按下，键盘被放开，用户按下关闭按钮
pg.event.set_caption(c.ORIGINAL_CAPTION)   # 设置字幕事件
SCREEN = pg.display.set_mode(c.SCREEN_SIZE)   # 初始化一个准备显示的屏幕
SCREEN_RECT = SCREEN.get_rect()      # 处理屏幕矩阵图像

GFX = tools.load_all_gfx(os.path.join("resource", "graphics"))   # 从tools.py文件中获取图像
