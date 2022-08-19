# -*- coding=utf-8 -*-
import random
import pygame
from pygame.locals import KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN
pygame.init()
screencaption = pygame.display.set_caption('贪吃蛇')
screen = pygame.display.set_mode((1000,1000)) #设置400*400窗口

snake_x = random.randint(0,9)*40+20
snake_y = random.randint(0,9)*40+20
score = 0
dire = 0

game_state = 1 # 游戏状态1.表示正常 2.表示失败
def get_bean_pos():
    return random.randint(0,9)*40+20,random.randint(0,9)*40+20

def AI_game():
    if snake_x == bean_x and snake_y > bean_y:
        dire = 2
    if snake_x == bean_x and snake_y < bean_y:
        dire = 3
    if snake_y == bean_y and snake_x > bean_x:
        dire = 0
    if snake_y == bean_y and snake_x < bean_x:
        dire = 1
    #print ('(' + str(snake_x) + ',' + str(snake_y) + ')(' + str(bean_x) + ',' + str(bean_y))

    


yellow = 255,255,0
orange = 255,128,0
white = 255,255,255
red = 255,0,0
bean_x,bean_y = get_bean_pos()

diff_ticks = 200
 # 移动一次蛇头的事件，单位毫秒
ticks = pygame.time.get_ticks()
ticks += diff_ticks

dire = random.randint(0,3) # 假设0、1、2、3分别代表方向左、右、上、下
if snake_x < 200:
    dire = 1 # 往右移动
else: 
    dire = 0 # 往左移动 

body_y = snake_y
if dire == 0: # 向左移动
    if snake_x + 40 < 400: 
        body_x = snake_x + 40
    else: # 身体不能放右侧了，只能往上下方向放
        if snake_y > 200:
            body_x = snake_x
            body_y -= 40
        else:
            body_x = snake_x
            body_y += 40
else: # 向右移动
    if snake_x - 40 > 0:
        body_x = snake_x - 40
    else: # 身体不能放左侧了，只能往上下方向放
        if snake_y > 200:
            body_x = snake_x
            body_y -= 40
        else:
            body_x = snake_x
            body_y += 40
body_arr = [(body_x,body_y)]

def set_snake_next_pos(snake_x, snake_y):
    if dire == 0:
        if snake_x - 40 > 0:
            snake_x -= 40
        elif snake_x - 20 == 0:
            snake_x = 980
    if dire == 1:
        if snake_x + 40 < 1000:
            snake_x += 40
        elif snake_x + 20 == 1000:
            snake_x = 20
    if dire == 2:
        if snake_y - 40 > 0:
            snake_y -= 40
        elif snake_y - 20 == 0:
            snake_y = 980
    if dire == 3:
        if snake_y + 40 < 1000:
            snake_y += 40
        elif snake_y + 20 == 1000:
            snake_y = 20
    return snake_x,snake_y
def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if dire!=0 and dire!=1 and snake_x - 40 > 0: # 和当前方向不是同方向或反方向并且可以左移
                    dire = 0
            if event.key == K_RIGHT:
                if dire!=0 and dire!=1 and snake_x + 40 < 1000: # 和当前方向不是同方向或反方向并且可以右移
                    dire = 1
            if event.key == K_UP:
                if dire!=2 and dire!=3 and snake_y - 40 > 0: # 和当前方向不是同方向或反方向并且可以上移
                    dire = 2
            if event.key == K_DOWN:
                if dire!=2 and dire!=3 and snake_y + 40 < 1000: # 和当前方向不是同方向或反方向并且可以下移
                    dire = 3
        
        
        

    screen.fill((0,0,255)) # 将界面设置为蓝色

    #for x in range(0,400,40):
    #    pygame.draw.line(screen,(255,255,255),(x,0),(x,400),1)
    #for y in range(0,400,40):
    #    pygame.draw.line(screen,(255,255,255),(0,y),(400,y),1)

    pygame.draw.circle(screen,yellow,[snake_x,snake_y],20,2)
    for body_x,body_y in body_arr:
        pygame.draw.rect(screen,orange,[body_x-20,body_y-20,40,40],5)  
 
    pygame.draw.circle(screen,yellow,[bean_x,bean_y],10,10)
   
    if game_state == 2:
        myfont = pygame.font.Font(None,30)
        
        textImage = myfont.render("Game over", True, white)
        screen.blit(textImage, (160,190))
        screen.blit(myfont.render("Your Score:" + str(score), True, red), (200,230))



   
    pygame.display.update() # 必须调用update才能看到绘图显示

    if game_state == 1 and pygame.time.get_ticks() >= ticks:
        last_body_x,last_body_y = body_arr[-1]
        body_arr = [(snake_x,snake_y)]+body_arr[:-1]
        snake_x,snake_y = set_snake_next_pos(snake_x,snake_y)
        ticks += diff_ticks
        #if snake_x == bean_x and snake_y == bean_y:
        #    bean_x,bean_y = get_bean_pos()
        #    body_arr.append((last_body_x,last_body_y))
        for body_x,body_y in body_arr:
            if snake_x == body_x and snake_y == body_y: # 判断下蛇头和身体是否有重合
                game_state = 2
                break
        for i in range(len(body_arr)-1):
            for j in range(i+1,len(body_arr)):
                if body_arr[i][0] == body_arr[j][0] and body_arr[i][1] == body_arr[j][1]: # 判断下身体每节是否有重合
                    game_state = 2
                    break
    
    if snake_x == bean_x and snake_y == bean_y:
        bean_x,bean_y = get_bean_pos()
        body_arr.append((last_body_x,last_body_y))
        score += 1

game()