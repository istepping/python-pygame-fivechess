# 主文件
# 系统模块
from sys import exit

import pygame
from pygame.locals import *

import algorithm.get_score
import algorithm.robot
import algorithm.test
import utils.opUtil
# 自定义模块
from common.manager import *
from common.res import *

# 初始化
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption(SCREEN_TITLE)
background_image = pygame.image.load(background_image_filename).convert()
chessboard_image = pygame.image.load(chessboard_image_filename).convert()
black_chess_image = pygame.image.load(black_chess_image_filename).convert_alpha()
white_chess_image = pygame.image.load(white_chess_image_filename).convert_alpha()
flag_image = pygame.image.load(flag_image_filename).convert_alpha()

screen.blit(background_image, (0, 0))
screen.blit(chessboard_image, (200, 100))


def robot_and_robot():
    # 定义落子顺序
    turn = WHITE_CHESS
    turn_image = white_chess_image
    robot_chess = WHITE_CHESS
    human_chess = BLACK_CHESS
    game_over = False
    while True:
        location = (-1, -1)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        if turn == WHITE_CHESS and game_over != True:
            location = algorithm.robot.chess2(WHITE_CHESS)
        if turn == BLACK_CHESS and game_over != True:
            location = algorithm.robot.chess1(BLACK_CHESS)
        if location[0] != -1 and game_over != True:
            result = utils.opUtil.chess(location, screen, turn_image, turn)
            # 换令牌
            if result:
                # 落子测试
                # algorithm.test.is_empty()
                # 算杀
                success = utils.opUtil.is_success(turn, screen)
                if success:
                    game_over = True
                    utils.opUtil.game_over(screen, success)
                # 切换
                elif turn == WHITE_CHESS:
                    turn_image = black_chess_image
                    turn = BLACK_CHESS
                else:
                    turn_image = white_chess_image
                    turn = WHITE_CHESS

        # 刷新画面
        pygame.display.update()


def start_game_robot():
    # 定义落子顺序
    turn_image = white_chess_image
    turn = WHITE_CHESS
    robot_chess = WHITE_CHESS
    human_chess = BLACK_CHESS
    game_over = False
    while True:
        location = (-1, -1)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and game_over != True:
                if turn == human_chess:
                    location = event.pos
        if turn == robot_chess and game_over != True:
            location = algorithm.robot.chess2(robot_chess)
        if location[0] != -1 and game_over != True:
            if turn == robot_chess:
                # print("robot chess")
                result = utils.opUtil.chess(location, screen, turn_image, turn)
            else:
                result = utils.opUtil.chess_on_board(location, screen, turn_image, turn)
            # 换令牌
            if result:
                # 算杀
                success = utils.opUtil.is_success(turn, screen)
                if success:
                    game_over = True
                    utils.opUtil.game_over(screen, success)
                # 切换
                elif turn == WHITE_CHESS:
                    turn_image = black_chess_image
                    turn = BLACK_CHESS
                else:
                    turn_image = white_chess_image
                    turn = WHITE_CHESS

        # 刷新画面
        pygame.display.update()


def start_game():
    # 定义落子顺序
    turn_image = white_chess_image
    turn = WHITE_CHESS
    game_over = False
    while True:
        # 事件
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN and game_over != True:
                result = utils.opUtil.chess_on_board(event.pos, screen, turn_image, turn)
                # 换令牌
                if result:
                    # 测试
                    if turn_image == white_chess_image:
                        # 算杀
                        success = utils.opUtil.is_success(WHITE_CHESS, screen)
                        if success:
                            game_over = True
                            utils.opUtil.game_over(screen, success)
                        # 切换
                        turn_image = black_chess_image
                        turn = BLACK_CHESS
                    else:
                        success = utils.opUtil.is_success(BLACK_CHESS, screen)
                        if success:
                            game_over = True
                            utils.opUtil.game_over(screen, turn)
                        turn_image = white_chess_image
                        turn = WHITE_CHESS
        # 刷新画面
        pygame.display.update()


robot_and_robot()
