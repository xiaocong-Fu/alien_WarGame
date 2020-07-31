import pygame.font                                                                                  # pygame.font可将文本渲染到屏幕

class Button():
    def __init__(self,ai_settings,screen,msg):
        '''初始化按钮的属性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # 设置按钮其他属性和尺寸
        self.width,self.height = 200,50
        self.button_color = (0,128,255)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        # 创建按钮的rect对象
        self.rect = pygame.Rect(0,0,self.width,self.height)                                         # 创建一个表示按钮的rect对象（见❹），并将其center属性设置为屏幕的center属性。
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self,msg):
        '''将msg渲染为图像，并使其在按钮上居中'''
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)                   # font.render()将存储在msg中的文本转换为图像，然后将该图像存储在msg_image中。
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''绘制一个用颜色填充的按钮，在绘制文本'''
        self.screen.fill(self.button_color,self.rect)                                                   # fill():来绘制标识按钮的矩形。
        self.screen.blit(self.msg_image,self.msg_image_rect)                                            # blit():向矩形传递一幅图像。
