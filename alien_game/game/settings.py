class Settings:
    # 存储变量
    def __init__(self):
        # 初始化游戏
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (254, 254, 254)

        # 飞船速度
        self.ship_speed_factor = 1.5

        # 设置子弹属性
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_speed_factor = 1
        self.bullet_color = 60, 60, 60
        # 子弹数量
        self.bullet_allowed = 3
