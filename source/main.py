import pygame as pg
from . import setup, tools
from . import constants as c
from .states import main_menu, load_screen, level

def main():
    game = tools.Control()    # tools.py页面中的Control类
    state_dict = {c.MAIN_MENU: main_menu.Menu(),   # 状态字典
                  c.LOAD_SCREEN: load_screen.LoadScreen(),
                  c.LEVEL: level.Level(),
                  c.GAME_OVER: load_screen.GameOver(),
                  c.TIME_OUT: load_screen.TimeOut()}
    game.setup_states(state_dict, c.MAIN_MENU)    # 设置状态
    game.main()