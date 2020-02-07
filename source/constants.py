# constants 不变的，永恒的

DEBUG = False
DEBUG_START_X = 110
DEBUG_START_Y = 538

SCREEN_HEIGHT = 600    # 设置游戏屏幕大小
SCREEN_WIDTH = 800
SCREEN_SIZE = (SCREEN_WIDTH,SCREEN_HEIGHT)

ORIGINAL_CAPTION = 'Super Mario Bros'  # 起始字幕

##COLORS##   颜色
#       R    G    B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)  # 深蓝色
WHITE =(255, 255, 255)
RED =(255, 0, 0)
GREEN = (0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)   # 森林绿
BLUE = (0,   0, 255)
SKY_BLUE = (39, 145, 251)   # 天空蓝
YELLOW = (255, 255,   0)
ORANGE = (255, 128,   0)
PURPLE = (255,   0, 255)    # 紫色
CYAN = (0, 255, 255)   # 蓝绿色
BLACK = (0,   0,   0)
NEAR_BLACK = (19,  15,  48)
COMBLUE = (233, 232, 255)   # 组合
GOLD = (255, 215,   0)   # 金黄色

BGCOLOR = WHITE   #背景色为白色

SIZE_MULTIPLIER = 2.5   # 尺寸乘数
BRICK_SIZE_MULTIPLIER = 2.69  # 砖块尺寸乘数
BACKGROUND_MULTIPLER = 2.679  # 背景乘数
GROUND_HEIGHT = SCREEN_HEIGHT -62  # 地面高度

GAME_TIME_OUT = 301

# STATES FOR ENTIRE GAME   整个游戏的状态
MAIN_MENU = 'main menu'   # 主菜单
LOAD_SCREEN = 'load screen'  # 加载页面
TIME_OUT = 'time out'   # 时间结束
GAME_OVER = 'game over'  # 游戏结束
LEVEL = 'level'   # 运行状态

# MAIN MENU CURSOR STATES  主菜单光标状态
PLAYER1 = '1 PLAYER GAME'  # 游戏人物1
PLAYER2 = '2 PLAYER GAME'  # 游戏人物2

# GAME INFO DICTIONARY KEYS  游戏信息字典键
COIN_TOTAL = 'coin total'  # 金币总数
SCORE = 'score'  # 分数
TOP_SCORE = 'top score'  # 总分数
LIVES = 'lives'   # 命条数
CURRENT_TIME = 'current time'   # 当前时间
LEVEL_NUM = 'level num'   # 等级数
PLAYER_NAME = 'player name'  # 游戏人物名称
PLAYER_MARIO = 'mario'   # 游戏人物马里奥
PLAYER_LUIGI = 'luigi'   # 游戏人物路易吉

# MAP COMPONENTS   地图组成
MAP_MAPS = 'maps'
SUB_MAP = 'sub_map'  # 代替地图
MAP_GROUND = 'ground'
MAP_PIPE = 'pipe'  # 地图管道
PIPE_TYPE_NONE = 0
PIPE_TYPE_IN = 1
PIPE_TYPE_HORIZONTAL = 2  # 水平管道类型为2种
MAP_STEP = 'step'  # 地图等级
MAP_BRICK = 'brick'  # 砖块
BRICK_NUM = 'brick_num'  # 砖块数量
TYPE_NONE = 0
TYPE_COIN = 1   # 金币类型为1种
TYPE_STAR = 2   # 星星类型为2种
MAP_BOX = 'box'
TYPE_MUSHROOM = 3   # 蘑菇类型为3种
TYPE_FIREFLOWER = 4   # 火花类型为4种
TYPE_FIREBALL = 5  # 火球类型为5种
TYPE_LIFEMUSHROOM = 6  # 生命蘑菇为6种
MAP_ENEMY = 'enemy'   # 敌人
ENEMY_TYPE_GOOMBA = 0    # 敌人类型高巴
ENEMY_TYPE_KOOPA = 1 # 敌人类型库帕
ENEMY_TYPE_FLY_KOOPA = 2   # 敌人类型飞库帕
ENEMY_TYPE_PIRANHA =3    # 敌人类型水虎鱼
ENEMY_TYPE_FIRESTICK = 4   # 敌人类型火棍
ENEMY_TYPE_FIRE_KOOPA = 5   # 敌人类型火库帕
ENEMY_RANGE = 'range'   # 敌人来回走动（范围）
MAP_CHECKPOINT = 'checkpoint'   # 地图检查站
ENEMY_GROUPID = 'enemy_groupid'   # 敌人组号
MAP_INDEX = 'map_index'  # 地图索引
CHECKPOINT_TYPE_ENEMY = 0
CHECKPOINT_TYPE_FLAG = 1     # 旗帜
CHECKPOINT_TYPE_CASTLE = 2   # 城堡
CHECKPOINT_TYPE_MUSHROOM = 3   # 蘑菇
CHECKPOINT_TYPE_PIPE = 4        # trigger player to go right in a pipe  触发玩家进入管道
CHECKPOINT_TYPE_PIPE_UP = 5     # trigger player to another map and go up out of a pipe 触发玩家到另一张地图，然后从管道中爬出
CHECKPOINT_TYPE_MAP = 6         # trigger player to go to another map
CHECKPOINT_TYPE_BOSS = 7        # defeat the boss  打败老板
MAP_FLAGPOLE = 'flagpole'   # 旗杆
FLAGPOLE_TYPE_FLAG = 0
FLAGPOLE_TYPE_POLE = 1   # 杆
FLAGPOLE_TYPE_TOP = 2    # 顶部
MAP_SLIDER = 'slider'   # 滑冰者
HORIZONTAL = 0  # 水平的
VERTICAL = 1    # 垂直的
VELOCITY = 'velocity'   # 速度
MAP_COIN = 'coin'

# COMPONENT COLOR  组成颜色
COLOR = 'color'
COLOR_TYPE_ORANGE = 0
COLOR_TYPE_GREEN = 1
COLOR_TYPE_RED = 2

# BRICK STATES  砖块状态
RESTING = 'resting'   # 静止的
BUMPED = 'bumped'     # 凸起的
OPENED = 'opened'

# MUSHROOM STATES  蘑菇的状态
REVEAL = 'reveal'   # 露出
SLIDE = 'slide'     # 滑动

# Player FRAMES   游戏人物画面
PLAYER_FRAMES = 'image_frames'
RIGHT_SMALL_NORMAL = 'right_small_normal'
RIGHT_BIG_NORMAL = 'right_big_normal'
RIGHT_BIG_FIRE = 'right_big_fire'

# PLAYER States  游戏人物状态
STAND = 'standing'  # 站立
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'  # 跌落
FLY = 'fly'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'   # 旗杆
WALK_AUTO = 'walk auto'     # not handle key input in this state  在这个状态下不处理按钮输入
END_OF_LEVEL_FALL = 'end of level fall'  # 水平下降结束
IN_CASTLE = 'in castle'
DOWN_TO_PIPE = 'down to pipe'
UP_OUT_PIPE = 'up out of pipe'

# PLAYER FORCES  游戏人物的力量
PLAYER_SPEED = 'speed'
WALK_ACCEL = 'walk_accel'   # 加速走
RUN_ACCEL = 'run_accel'
JUMP_VEL = 'jump_velocity'   # 迅速跳
MAX_Y_VEL = 'max_y_velocity'
MAX_RUN_SPEED = 'max_run_speed'
MAX_WALK_SPEED = 'max_walk_speed'
SMALL_TURNAROUND = .35
JUMP_GRAVITY = .31
GRAVITY = 1.01     # 万有引力

# LIST of ENEMIES  敌人列表
GOOMBA = 'goomba'
KOOPA = 'koopa'
FLY_KOOPA = 'fly koopa'
FIRE_KOOPA = 'fire koopa'
FIRE = 'fire'
PIRANHA = 'piranha'
FIRESTICK = 'firestick'

# GOOMBA Stuff
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

# KOOPA STUFF
SHELL_SLIDE = 'shell slide'

# FLAG STATE
TOP_OF_POLE = 'top of pole'  # 杆顶部
SLIDE_DOWN = 'slide down'  # 下滑
BOTTOM_OF_POLE = 'bottom of pole'   # 杆底部

# FIREBALL STATE  火棍状态
FLYING = 'flying'
BOUNCING = 'bouncing'    # 强壮的
EXPLODING = 'exploding'    # 爆炸

# IMAGE SHEET  图像表
ENEMY_SHEET = 'smb_enemies_sheet'
ITEM_SHEET = 'item_objects'   # 项目目标