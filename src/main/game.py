# 主文件
# 系统模块
import pygame
from pygame.locals import *
from sys import exit
# 自定义模块
from common.manager import *
from common.res import *
import utils.opUtil

# 初始化
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption(SCREEN_TITLE)
background_image = pygame.image.load(background_image_filename).convert()
chessboard_image = pygame.image.load(chessboard_image_filename).convert()
black_chess_image = pygame.image.load(black_chess_image_filename).convert_alpha()
white_chess_image = pygame.image.load(white_chess_image_filename).convert_alpha()

screen.blit(background_image, (0, 0))
screen.blit(chessboard_image, (200, 100))



def start_game():
    # 定义落子顺序
    turn_image = white_chess_image
    turn = WHITE_CHESS
    game_over=False
    while True:
        # 事件
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and game_over!=True:
                print("点击位置=", event.pos)
                result = utils.opUtil.chess_on_board(event, screen, turn_image, turn)
                # 换令牌
                if result == True:
                    if turn_image == white_chess_image:
                        # 算杀
                        success = utils.opUtil.is_success(WHITE_CHESS)
                        if success:
                            game_over = True
                            utils.opUtil.game_over(screen,white_chess_image)
                        # 切换
                        turn_image = black_chess_image
                        turn = BLACK_CHESS
                    else:
                        success = utils.opUtil.is_success(BLACK_CHESS)
                        if success:
                            game_over = True
                            utils.opUtil.game_over(screen,black_chess_image)
                        turn_image = white_chess_image
                        turn = WHITE_CHESS
        # 刷新画面
        pygame.display.update()


start_game()
