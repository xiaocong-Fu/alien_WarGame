class Settings():
    '''储存游戏中所有设置的类'''
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船设置
        # self.ship_speed_factor = 2
        self.ship_limit = 3

        # 子弹设置
        # self.bullet_speed_factor = 3
        self.bullet_width = 150
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        # 外星人设置
        # self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # self.fleet_direction = 1

        # 设置动态属性，加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        # 1表示向右，-1表示向左
        self.fleet_direction = 1

    def increase_speed(self):
        '''提高速度设置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
