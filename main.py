import datetime
import sys
import pygame
import math
import tkinter
import threading
import time
import pygame_gui
import random
from datetime import datetime

pygame.init()

COLOR_INACTIVE = pygame.Color('white')
COLOR_ACTIVE = pygame.Color('white')
FONT = pygame.font.SysFont(None, 32)
scoreImg = pygame.image.load('score.png')
logoImg = pygame.image.load('logo.png')
winnerImg = pygame.image.load("effectforProject.png")

class User():
    def __init__(self, name, score, superPower, speed, X, Y, RED, GREEN, BLUE, size, defX, defY, supPowBeginTime):
        self.name = name
        self.score = score
        self.superPower = superPower
        self.speed = speed
        self.X = X
        self.Y = Y
        self.RED = RED
        self.GREEN = GREEN
        self.BLUE = BLUE
        self.size = size
        self.defX = defX
        self.defY = defY
        self.supPowBeginTime = supPowBeginTime

class Ball():
    X = float
    Y = float
    size = 10
    red = 255
    green = 255
    blue = 255
    default_speed = 2.9
    default_driving_speed = 1.2
    x_speed = 0
    y_speed = 0
    def_x = float
    def_y = float

class Screen:
    RED = 0
    GREEN = 128
    BLUE = 0
    root = tkinter.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

class Pitch:
    LastGoalSide = 1
    Santra = True
    GoalSize1 = float(50)
    GoalSize2 = float(50)
    name = ""
    Width = float(900)
    heigth = float(450)
    target_goal = int
    target_goal = int
    time = int

class SuperPower():
    PowerName = ""
    suppowx = int
    suppowy = int
    size = int
    usable = False

ball = Ball()
screen = Screen()
pitch = Pitch()
superPower = SuperPower()
superPower.size = 10
ekran = pygame.display.set_mode((screen.width, screen.height - 45))
User1 = User("User1", 0, "", 0.75, (screen.width - pitch.Width) / 2 + pitch.Width / 5, screen.height / 2, 255, 0, 0,
             float(20), (screen.width - pitch.Width) / 2 + pitch.Width / 5, screen.height / 2, -99)
User2 = User("User2", 0, "", 0.75, (screen.width - pitch.Width) / 2 + pitch.Width * (4 / 5), screen.height / 2, 0, 0,
             250, float(20), (screen.width - pitch.Width) / 2 + pitch.Width * (4 / 5), screen.height / 2, -99)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, (0, 0, 0))
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif len(self.text) < 15:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, False, (0, 0, 0))
        self.txt_surface = FONT.render(self.text, False, (0, 0, 0))
    def draw(self, ekran):
        # Blit the rect.
        pygame.draw.rect(ekran, self.color, self.rect)
        # Blit the text.
        ekran.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width() + 10)
        self.rect.w = width

ball.def_x = screen.width / 2
ball.def_y = screen.height / 2

class saha:
    def __init__(self, width, height, goalSize1, goalSize2):
        self.width = width
        self.height = height
        self.goalSize1 = goalSize1
        self.goalSize2 = goalSize2

    def draw(self):
        white = (255, 255, 255)
        aPos = ((screen.width - self.width) / 2, (screen.height - self.height) / 2)
        bPos = (((screen.width - self.width) / 2) + self.width, (screen.height - self.height) / 2)
        cPos = (((screen.width - self.width) / 2) + self.width, ((screen.height - self.height) / 2) + self.height)
        dPos = ((screen.width - self.width) / 2, ((screen.height - self.height) / 2) + self.height)
        aUstKalePos = (
        (screen.width - self.width) / 2, ((screen.height - self.height) / 2) + self.height / 2 - self.goalSize1 / 2)
        aaUstKalePos = (((screen.width - self.width) / 2) - 50,
                        ((screen.height - self.height) / 2) + self.height / 2 - self.goalSize1 / 2)
        aAltKalePos = (
        (screen.width - self.width) / 2, ((screen.height - self.height) / 2) + self.height / 2 + self.goalSize1 / 2)
        aaAltKalePos = (((screen.width - self.width) / 2) - 50,
                        ((screen.height - self.height) / 2) + self.height / 2 + self.goalSize1 / 2)
        bUstKalePos = (((screen.width - self.width) / 2) + self.width,
                       ((screen.height - self.height) / 2) + self.height / 2 - self.goalSize2 / 2)
        baUstKalePos = (((screen.width - self.width) / 2) + self.width + 50,
                        ((screen.height - self.height) / 2) + self.height / 2 - self.goalSize2 / 2)
        bAltKalePos = (((screen.width - self.width) / 2) + self.width,
                       ((screen.height - self.height) / 2) + self.height / 2 + self.goalSize2 / 2)
        baAltKalePos = (((screen.width - self.width) / 2) + self.width + 50,
                        ((screen.height - self.height) / 2) + self.height / 2 + self.goalSize2 / 2)
        aCenterPos = (((screen.width - self.width) / 2) + (self.width / 2), (screen.height - self.height) / 2)
        bCenterPos = (
        ((screen.width - self.width) / 2) + (self.width / 2), ((screen.height - self.height) / 2) + self.height)
        cCenterPos = (((screen.width - self.width) / 2) + (self.width / 2) + 1,
                      ((screen.height - self.height) / 2) + (self.height / 2))
        pygame.draw.line(ekran, white, aPos, bPos, 2)
        pygame.draw.line(ekran, white, bPos, cPos, 2)
        pygame.draw.line(ekran, white, cPos, dPos, 2)
        pygame.draw.line(ekran, white, dPos, aPos, 2)
        pygame.draw.line(ekran, white, aCenterPos, bCenterPos, 2)
        pygame.draw.circle(ekran, white, cCenterPos, self.height / 10, 2)
        pygame.draw.line(ekran, white, aUstKalePos, aaUstKalePos, 2)
        pygame.draw.line(ekran, white, aAltKalePos, aaAltKalePos, 2)
        pygame.draw.line(ekran, white, aaAltKalePos, aaUstKalePos, 2)

        pygame.draw.line(ekran, white, bUstKalePos, baUstKalePos, 2)
        pygame.draw.line(ekran, white, bAltKalePos, baAltKalePos, 2)
        pygame.draw.line(ekran, white, baAltKalePos, baUstKalePos, 2)

pitch.GoalSize1 = pitch.heigth / 3
pitch.GoalSize2 = pitch.heigth / 3
pitch.time = 0
saha1 = saha(pitch.Width, pitch.heigth, pitch.GoalSize1, pitch.GoalSize2)

ball.X = screen.width / 2
ball.Y = screen.height / 2

def Distacnce(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

def ballMoves():
    keys = pygame.key.get_pressed()

    # sag taraf
    if (ball.X + ball.size > (screen.width + pitch.Width) / 2 and ball.x_speed > 0 and (
            ball.Y < ((screen.height - pitch.heigth) / 2 + pitch.heigth / 2 - pitch.GoalSize2 / 2)
            or ball.Y > ((screen.height - pitch.heigth) / 2 + pitch.heigth / 2 + pitch.GoalSize2 / 2))):
        ball.x_speed *= -1

    # sag taraf kale ici
    if (ball.X  > (screen.width + pitch.Width) / 2):
        if (ball.X + ball.size > (screen.width + pitch.Width) / 2 + 60) and ball.x_speed>0:
            ball.x_speed *= -1
        if ball.Y - ball.size < screen.height / 2 - pitch.GoalSize2 / 2 and ball.y_speed < 0:
            ball.y_speed *= -1
        if ball.Y + ball.size > screen.height / 2 + pitch.GoalSize2 / 2 and ball.y_speed > 0:
            ball.y_speed *= -1
    # sol taraf
    if (ball.X - ball.size < (screen.width - pitch.Width) / 2 and ball.x_speed < 0
            and (ball.Y < ((screen.height - pitch.heigth) / 2 + pitch.heigth / 2 - pitch.GoalSize1 / 2)
                 or ball.Y > ((screen.height - pitch.heigth) / 2 + pitch.heigth / 2 + pitch.GoalSize1 / 2))):
        ball.x_speed *= -1

    # sol taraf kale ici
    if (ball.X  < (screen.width - pitch.Width) / 2):
        if (ball.X - ball.size < (screen.width - pitch.Width) / 2 - 60) and ball.x_speed<0:
            ball.x_speed *= -1
        if ball.Y - ball.size < screen.height / 2 - pitch.GoalSize1 / 2 and ball.y_speed < 0:
            ball.y_speed *= -1
        if ball.Y + ball.size > screen.height / 2 + pitch.GoalSize1 / 2 and ball.y_speed > 0:
            ball.y_speed *= -1
    # alt taraf
    if ball.Y + ball.size > (screen.height + pitch.heigth) / 2 and ball.y_speed > 0:
        ball.y_speed *= -1
    if ball.Y - ball.size < (screen.height - pitch.heigth) / 2 and ball.y_speed < 0:
        ball.y_speed *= -1

    if Distacnce(ball.X, ball.Y, User1.X, User1.Y) < ball.size + User1.size + 4 and keys[pygame.K_SPACE]:
        pitch.Santra = False
        ball.x_speed = (ball.X - User1.X) * ball.default_speed / (User1.size + ball.size)
        ball.y_speed = (ball.Y - User1.Y) * ball.default_speed / (User1.size + ball.size)

    elif Distacnce(ball.X, ball.Y, User1.X, User1.Y) < User1.size + ball.size:
        pitch.Santra = False
        ball.x_speed = (ball.X - User1.X) * ball.default_driving_speed / (User1.size + ball.size)
        ball.y_speed = (ball.Y - User1.Y) * ball.default_driving_speed / (User1.size + ball.size)

    if Distacnce(ball.X, ball.Y, User2.X, User2.Y) < ball.size + User2.size + 4 and keys[pygame.K_KP_2]:
        pitch.Santra = False
        ball.x_speed = (ball.X - User2.X) * ball.default_speed / (User2.size + ball.size)
        ball.y_speed = (ball.Y - User2.Y) * ball.default_speed / (User2.size + ball.size)

    elif Distacnce(ball.X, ball.Y, User2.X, User2.Y) < User2.size + ball.size:
        pitch.Santra = False
        ball.x_speed = (ball.X - User2.X) * ball.default_driving_speed / (User2.size + ball.size)
        ball.y_speed = (ball.Y - User2.Y) * ball.default_driving_speed / (User2.size + ball.size)

    ball.X += ball.x_speed
    ball.Y += ball.y_speed

    pygame.draw.circle(ekran, (ball.red, ball.green, ball.blue), (ball.X, ball.Y), ball.size)
    ball.x_speed = ball.x_speed * 0.995
    ball.y_speed = ball.y_speed * 0.995

def playerMoves():
    key = pygame.key.get_pressed()

    if Distacnce(User1.X,User1.Y,User2.X,User2.Y)<User1.size+User2.size:
        speed = (User1.X - User2.X) * User1.speed / (User1.size + User2.size)
        User1.X += 2*speed

        speed = (User2.X - User1.X) * User2.speed / (User2.size + User1.size)
        User2.X += 2*speed

        speed = (User1.Y - User2.Y) * User1.speed / (User1.size + User2.size)
        User1.Y += 2 * speed

        speed = (User2.Y - User1.Y) * User2.speed / (User2.size + User1.size)
        User2.Y += 2 * speed

    if key[pygame.K_a] and User1.X - User1.size > (screen.width - pitch.Width) / 2:
        User1.X -= User1.speed
    if key[pygame.K_d] and User1.X + User1.size < (screen.width + pitch.Width) / 2 \
            and ((pitch.Santra and User1.X < (screen.width - pitch.Width) / 2 + pitch.Width / 2
             and Distacnce(ball.X, ball.Y, User1.X + User1.speed, User1.Y) > pitch.heigth / 10
             and pitch.LastGoalSide == 1) or pitch.Santra == False
            or (pitch.Santra and pitch.LastGoalSide == 2 and User1.X < (screen.width - pitch.Width) / 2 + pitch.Width / 2)):
        User1.X += User1.speed

    if key[pygame.K_s] and User1.Y + User1.size < (screen.height + pitch.heigth) / 2:
        if (pitch.Santra and Distacnce(ball.X, ball.Y, User1.X,User1.Y + User1.speed) > pitch.heigth / 10 and pitch.LastGoalSide == 1) or pitch.Santra == False \
                or (pitch.Santra and pitch.LastGoalSide == 2):
            User1.Y += User1.speed
    if key[pygame.K_w] and User1.Y - User1.size > (screen.height - pitch.heigth) / 2:
        if (pitch.Santra and Distacnce(ball.X, ball.Y, User1.X - User1.speed, User1.Y) > pitch.heigth / 10 and pitch.LastGoalSide == 1) or pitch.Santra == False \
                or (pitch.Santra and pitch.LastGoalSide == 2):
            User1.Y -= User1.speed

    pygame.draw.circle(ekran, (User1.RED, User1.GREEN, User1.BLUE), (User1.X, User1.Y), User1.size)

    if key[pygame.K_LEFT] and User2.X - User2.size > (screen.width - pitch.Width) / 2 \
                and ((pitch.Santra and User2.X > (screen.width - pitch.Width) / 2 + pitch.Width / 2
                and Distacnce(ball.X, ball.Y, User2.X - User2.speed, User2.Y) > pitch.heigth / 10
                and pitch.LastGoalSide == 2) or pitch.Santra == False or (pitch.Santra and pitch.LastGoalSide == 1
                and pitch.Santra and User2.X > (screen.width - pitch.Width) / 2 + pitch.Width / 2)):
        User2.X -= User2.speed

    if key[pygame.K_RIGHT] and User2.X + User2.size < (screen.width + pitch.Width) / 2:
        User2.X += User2.speed

    if key[pygame.K_DOWN] and User2.Y + User2.size < (screen.height + pitch.heigth) / 2 and ((pitch.Santra and Distacnce(ball.X, ball.Y,User2.X,User2.Y + User2.speed) > pitch.heigth / 10 and pitch.LastGoalSide == 2) or pitch.Santra == False or (pitch.Santra and pitch.LastGoalSide == 1)):
        User2.Y += User2.speed
    if key[pygame.K_UP] and User2.Y - User2.size > (screen.height - pitch.heigth) / 2 and ((pitch.Santra and Distacnce(ball.X, ball.Y, User2.X, User2.Y - User2.speed) > pitch.heigth / 10 and pitch.LastGoalSide == 2) or pitch.Santra == False or (pitch.Santra and pitch.LastGoalSide == 1)):
        User2.Y -= User2.speed

    pygame.draw.circle(ekran, (User2.RED, User2.GREEN, User2.BLUE), (User2.X, User2.Y), User2.size)

def restart():
    User1.Y = User1.defY
    User1.X = User1.defX
    User2.Y = User2.defY
    User2.X = User2.defX

    ball.X = ball.def_x
    ball.Y = ball.def_y
    ball.x_speed = 0
    ball.y_speed = 0

def endofthegame():
    User1.Y = User1.defY
    User1.X = User1.defX
    User1.score = 0
    User1.superPower = ""

    User2.Y = User2.defY
    User2.X = User2.defX
    User2.score = 0
    User2.superPower = ""

    ball.X = ball.def_x
    ball.Y = ball.def_y
    ball.x_speed = 0
    ball.y_speed = 0
    pitch.time = 0

booltime = True

def time():
    global dt, t, booltime,emptytime
    if pitch.Santra:
        emptytime = pitch.time
        t = datetime.now()
    else:
        dt = datetime.now()
        pitch.time = emptytime + (dt-t).seconds


    """global dt, t, booltime
    if booltime:
        t = datetime.now()
        booltime = False
    if booltime == False:
        dt = datetime.now()
        pitch.time = (dt - t).seconds"""

    FONT = pygame.font.SysFont(None, 48)
    second = FONT.render(" {}".format(pitch.time % 60), 1, (255, 255, 255))
    minute = FONT.render("{} :".format(pitch.time // 60), 1, (255, 255, 255))
    ekran.blit(minute, ((screen.width / 2 - minute.get_width() + 5, 36)))
    ekran.blit(second, ((screen.width / 2 + second.get_width() / 4, 36)))

timeA = True
timeC = False

def goal():
    global timeA, c, timeC
    b = datetime.now()
    if (ball.X+ball.size < (screen.width - pitch.Width) / 2 or ball.X-ball.size  > (screen.width + pitch.Width) / 2) and \
            ((ball.Y > screen.height / 2 - pitch.GoalSize1/2 and ball.Y < screen.height / 2 + pitch.GoalSize1 / 2)
             or (ball.Y > screen.height / 2 - pitch.GoalSize2/2 and ball.Y < screen.height / 2 + pitch.GoalSize2 / 2) ):
        pitch.Santra = True
        if timeA:
            a = datetime.now()
            c = a
            timeC = True
            timeA = False
    if timeC and (b - c).seconds > 0.1:

        if ball.X + ball.size < screen.width / 2:
            User2.score += 1
            pitch.LastGoalSide = 2

        elif ball.X - ball.size > screen.width / 2:
            User1.score += 1
            pitch.LastGoalSide = 1
        timeC = False
        timeA = True
        restart()
    if User1.score == pitch.target_goal:

        winner(User1.name)
    if User2.score == pitch.target_goal:
        winner(User2.name)
    FONT = pygame.font.SysFont(None, 40)
    score1 = "{}   {}  ".format(User1.name, User1.score)
    score2 = "{}   {}".format(User2.score, User2.name)
    usr1Score = FONT.render(score1, 1, (0, 0, 0))
    usr2Score = FONT.render(score2, 1, (0, 0, 0))
    ekran.blit(usr1Score, (screen.width / 2 - usr1Score.get_width() + 5, 73))
    ekran.blit(usr2Score, (screen.width / 2 + 10, 73))

def superPowerSelection():
    powers=['fireball','iceball','smallergoal','biggergoal','biggerball','smallerball','unstoppebleball','biggerplayer','smallerplayer']
    #powers = ['smallergoal']
    if pitch.time % 30 == 1 and superPower.usable == False and pitch.Santra==False:
        superPower.usable = True
        superPower.PowerName = random.choice(powers)
        superPower.suppowx = random.randint((screen.width - pitch.Width) / 2 + int(pitch.Width / 3),(screen.width + pitch.Width) / 2 - int(pitch.Width / 3))
        superPower.suppowy = random.randint((screen.height - pitch.heigth) / 2, (screen.height + pitch.heigth) / 2)
    elif superPower.usable:
        pygame.draw.circle(ekran, (0, 0, 0), (superPower.suppowx, superPower.suppowy), superPower.size)

def drawTimeBar(x,y,suppowbegintime,time):
    pygame.draw.rect(ekran,(0,255,0),(x,y,200,20))
    pygame.draw.rect(ekran, (255,0,0), (x, y, ((pitch.time-suppowbegintime)/time)*200, 20))

def runSuperPower():
    if superPower.usable and Distacnce(superPower.suppowx, superPower.suppowy, User1.X,User1.Y) < superPower.size + User1.size and superPower.usable:
        User1.supPowBeginTime = pitch.time
        User1.superPower = superPower.PowerName
        superPower.usable = False
    if superPower.usable and Distacnce(superPower.suppowx, superPower.suppowy, User2.X,User2.Y) < superPower.size + User2.size and superPower.usable:
        User2.supPowBeginTime = pitch.time
        User2.superPower = superPower.PowerName
        superPower.usable = False

    if (User1.superPower == "biggerball" or User2.superPower == "biggerball"):
        if pitch.time - User1.supPowBeginTime == 20 or pitch.time - User2.supPowBeginTime == 20:
            ball.size = 10
            if pitch.time - User1.supPowBeginTime == 20:
                User1.superPower = ""
            if pitch.time - User2.supPowBeginTime == 20:
                User2.superPower = ""
        else:
            ball.size = 15
        if User1.superPower == "biggerball":
            drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50,User1.supPowBeginTime, 20)
        if User2.superPower == "biggerball":
            drawTimeBar((screen.width + pitch.Width) / 2-200, (screen.height + pitch.heigth) / 2 + 50, User2.supPowBeginTime, 20)
    elif (User1.superPower != "smallerball" and User2.superPower != "smallerball"):
        ball.size = 10

    if (User1.superPower == "smallerball" or User2.superPower == "smallerball"):
        if pitch.time - User1.supPowBeginTime == 20 or pitch.time - User2.supPowBeginTime == 20:
            ball.size = 10
            if pitch.time - User1.supPowBeginTime == 20:
                User1.superPower = ""
            if pitch.time - User2.supPowBeginTime == 20:
                User2.superPower = ""
        else:
            ball.size = 5
        if User1.superPower == "smallerball":
            drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50,User1.supPowBeginTime, 20)
        if User2.superPower == "smallerball":
            drawTimeBar((screen.width + pitch.Width) / 2-200, (screen.height + pitch.heigth) / 2 + 50, User2.supPowBeginTime, 20)
    elif (User1.superPower != "biggerball" and User2.superPower != "biggerball"):
        ball.size = 10

    if (User1.superPower == "fireball" or User2.superPower == "fireball"):
        if pitch.time - User1.supPowBeginTime == 10 or pitch.time - User2.supPowBeginTime == 10:
            ball.default_speed = 2.9
            ball.default_driving_speed = 1.2
            ball.red = 255
            ball.green = 255
            ball.blue = 255
            if pitch.time - User1.supPowBeginTime == 10:
                User1.superPower = ""
            if pitch.time - User2.supPowBeginTime == 10:
                User2.superPower = ""
        else:
            if Distacnce(ball.X, ball.Y, User1.X, User1.Y) < ball.size + User1.size + 5 and User1.superPower == "fireball":
                ball.default_speed = 4
                ball.default_driving_speed = 1.2
                ball.red = 255
                ball.green = 100
                ball.blue = 100
            elif (Distacnce(ball.X, ball.Y, User2.X,User2.Y) < ball.size + User2.size + 5 and User2.superPower != "fireball"):
                ball.default_speed = 2.7
                ball.default_driving_speed = 1.2
                ball.red = 255
                ball.green = 255
                ball.blue = 255
            if Distacnce(ball.X, ball.Y, User2.X, User2.Y) < ball.size + User2.size + 5 and User2.superPower == "fireball":
                ball.default_speed = 4
                ball.default_driving_speed = 1.2
                ball.red = 255
                ball.green = 100
                ball.blue = 100
            elif (Distacnce(ball.X, ball.Y, User1.X, User1.Y) < ball.size + User1.size + 5 and User1.superPower != "fireball"):
                ball.default_speed = 2.7
                ball.default_driving_speed = 1.2
                ball.red = 255
                ball.green = 255
                ball.blue = 255
        if User1.superPower == "fireball":
            drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50,User1.supPowBeginTime, 10)
        if User2.superPower == "fireball":
            drawTimeBar((screen.width + pitch.Width) / 2-200, (screen.height + pitch.heigth) / 2 + 50, User2.supPowBeginTime, 10)
    elif (User1.superPower != "iceball" and User2.superPower != "iceball"):
        ball.default_speed = 2.9
        ball.default_driving_speed = 1.2
        ball.red = 255
        ball.green = 255
        ball.blue = 255

    if (User1.superPower == "iceball" or User2.superPower == "iceball"):
        if pitch.time - User1.supPowBeginTime == 7 or pitch.time - User2.supPowBeginTime == 7:
        #if pitch.time - User1.supPowBeginTime == 700 or pitch.time - User2.supPowBeginTime == 700:
            ball.default_speed = 2.9
            ball.default_driving_speed = 1.2
            ball.red = 255
            ball.green = 255
            ball.blue = 255
            if pitch.time - User1.supPowBeginTime == 7:
            #if pitch.time - User1.supPowBeginTime == 700:
                User1.superPower = ""
            if pitch.time - User2.supPowBeginTime == 7:
                User2.superPower = ""
        else:
            if Distacnce(ball.X, ball.Y, User1.X, User1.Y) < ball.size + User1.size + 5 and User1.superPower == "iceball":
                ball.default_speed = 2.9
                ball.default_driving_speed = 1.2
                ball.red = 255
                ball.green = 255
                ball.blue = 255
            elif (Distacnce(ball.X, ball.Y, User2.X,User2.Y) < ball.size + User2.size + 6 and User2.superPower != "iceball"):
                ball.default_speed = 1
                ball.x_speed = 0
                ball.y_speed = 0
                ball.red = 100
                ball.green = 100
                ball.blue = 255
            if Distacnce(ball.X, ball.Y, User2.X, User2.Y) < ball.size + User2.size + 5 and User2.superPower == "iceball":
                ball.default_speed = 2.9
                ball.default_driving_speed = 1.2
                ball.red = 255
                ball.green = 255
                ball.blue = 255
            elif (Distacnce(ball.X, ball.Y, User1.X, User1.Y) < ball.size + User1.size + 6 and User1.superPower != "iceball"):
                ball.default_speed = 1
                ball.x_speed = 0
                ball.y_speed = 0
                ball.red = 100
                ball.green = 100
                ball.blue = 255
        if User1.superPower == "iceball":
            drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50,User1.supPowBeginTime, 7)
        if User2.superPower == "iceball":
            drawTimeBar((screen.width + pitch.Width) / 2-200, (screen.height + pitch.heigth) / 2 + 50, User2.supPowBeginTime, 7)
    elif (User1.superPower != "fireball" and User2.superPower != "fireball"):
        ball.default_speed = 2.9
        ball.default_driving_speed = 1.2
        ball.red = 255
        ball.green = 255
        ball.blue = 255

    if (User1.superPower == "biggerplayer" or User2.superPower == "biggerplayer"):
        if pitch.time - User1.supPowBeginTime == 15 or pitch.time - User2.supPowBeginTime == 15:
            if pitch.time - User1.supPowBeginTime == 15:
                User1.superPower = ""
                User1.size = 20
            if pitch.time - User2.supPowBeginTime == 15:
                User2.superPower = ""
                User2.size = 20
        else:
            if User1.superPower == "biggerplayer":
                User1.size = 28
            if User2.superPower == "biggerplayer":
                User2.size = 28
        if User1.superPower == "biggerplayer":
            drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50, User1.supPowBeginTime, 15)
        if User2.superPower == "biggerplayer":
            drawTimeBar((screen.width + pitch.Width) / 2 - 200, (screen.height + pitch.heigth) / 2 + 50,
                        User2.supPowBeginTime, 15)
    elif (User1.superPower != "smallerplayer" and User2.superPower != "smallerplayer"):
        User1.size = 20
        User2.size = 20

    if (User1.superPower == "smallerplayer" or User2.superPower == "smallerplayer"):
        if pitch.time - User1.supPowBeginTime == 15 or pitch.time - User2.supPowBeginTime == 15:
            if pitch.time - User1.supPowBeginTime == 15:
                User1.superPower = ""
                User2.size = 20
            if pitch.time - User2.supPowBeginTime == 15:
                User2.superPower = ""
                User1.size = 20
        else:
            if User1.superPower == "smallerplayer":
                User2.size = 12
            if User2.superPower == "smallerplayer":
                User1.size = 12
        if User1.superPower == "smallerplayer":
            drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50, User1.supPowBeginTime, 15)
        if User2.superPower == "smallerplayer":
            drawTimeBar((screen.width + pitch.Width) / 2 - 200, (screen.height + pitch.heigth) / 2 + 50, User2.supPowBeginTime, 15)
    elif (User1.superPower != "biggerplayer" and User2.superPower != "biggerplayer"):
        User1.size = 20
        User2.size = 20

    if (User1.superPower == "unstoppebleball" or User2.superPower == "unstoppebleball"):
        if pitch.time - User1.supPowBeginTime == 15 or pitch.time - User2.supPowBeginTime == 15:
            ball.default_driving_speed = 1.2
            if pitch.time - User1.supPowBeginTime == 15:
                User1.superPower = ""
            if pitch.time - User2.supPowBeginTime == 15:
                User2.superPower = ""
        else:
            if User1.superPower== "unstoppebleball":
                drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50,User1.supPowBeginTime, 15)
            if User2.superPower == "unstoppebleball":
                drawTimeBar((screen.width + pitch.Width) / 2-200, (screen.height + pitch.heigth) / 2 + 50, User2.supPowBeginTime, 15)
            ball.default_driving_speed = 2.5
    elif User1.superPower != "fireball" and User2.superPower != "fireball" and User1.superPower != "iceball" and User2.superPower != "iceball":
        ball.default_driving_speed = 1.2

    if(User1.superPower == "smallergoal" or User2.superPower == "smallergoal"):
        if pitch.time - User1.supPowBeginTime == 20 or pitch.time - User2.supPowBeginTime == 20:
            if pitch.time - User1.supPowBeginTime == 20:
                User1.superPower = ""
                pitch.GoalSize1 = pitch.heigth / 3
                saha1.goalSize1 = pitch.heigth / 3
            if pitch.time - User2.supPowBeginTime == 20:
                User2.superPower = ""
                pitch.GoalSize2 = pitch.heigth / 3
                saha1.goalSize2 = pitch.heigth / 3

        else:
            if User1.superPower == "smallergoal":
                pitch.GoalSize1 = pitch.heigth / 5
                saha1.goalSize1 = pitch.heigth / 5
            if User2.superPower == "smallergoal":
                pitch.GoalSize2 = pitch.heigth / 5
                saha1.goalSize2 = pitch.heigth / 5
        if User1.superPower == "smallergoal":
            drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50,
                        User1.supPowBeginTime, 20)

        if User2.superPower == "smallergoal":
            drawTimeBar((screen.width + pitch.Width) / 2 - 200, (screen.height + pitch.heigth) / 2 + 50,
                        User2.supPowBeginTime, 15)

    elif (User1.superPower != "biggergoal" and User2.superPower != "biggergoal"):
        pitch.GoalSize1 = pitch.heigth / 3
        saha1.goalSize1 = pitch.heigth / 3
        pitch.GoalSize2 = pitch.heigth / 3
        saha1.goalSize2 = pitch.heigth / 3

    if (User1.superPower == "biggergoal" or User2.superPower == "biggergoal"):
        if pitch.time - User1.supPowBeginTime == 20 or pitch.time - User2.supPowBeginTime == 20:
            if pitch.time - User1.supPowBeginTime == 20:
                User1.superPower = ""
                pitch.GoalSize2 = pitch.heigth / 3
                saha1.goalSize2 = pitch.heigth / 3
            if pitch.time - User2.supPowBeginTime == 20:
                User2.superPower = ""
                pitch.GoalSize1 = pitch.heigth / 3
                saha1.goalSize1 = pitch.heigth / 3

        else:
            if User1.superPower == "biggergoal":
                pitch.GoalSize2 = pitch.heigth / 2
                saha1.goalSize2 = pitch.heigth / 2
            if User2.superPower == "biggergoal":
                pitch.GoalSize1 = pitch.heigth / 2
                saha1.goalSize1 = pitch.heigth / 2
        if User1.superPower == "biggergoal":
            drawTimeBar((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 50,
                        User1.supPowBeginTime, 20)
        if User2.superPower == "biggergoal":
            drawTimeBar((screen.width + pitch.Width) / 2 - 200, (screen.height + pitch.heigth) / 2 + 50,
                        User2.supPowBeginTime, 20)

    elif (User1.superPower != "smallergoal" and User2.superPower != "smallergoal"):
        pitch.GoalSize1 = pitch.heigth / 3
        saha1.goalSize1 = pitch.heigth / 3
        pitch.GoalSize2 = pitch.heigth / 3
        saha1.goalSize2 = pitch.heigth / 3

    FONT = pygame.font.SysFont(None, 32)
    if User1.superPower == "":
        User1WritePower = FONT.render(("{} has nothing".format(User1.name)), 1, (255, 255, 255))
        ekran.blit(User1WritePower, ((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 10))
    else:
        User1WritePower = FONT.render("{} has {}".format(User1.name, User1.superPower), 1, (255, 255, 255))
        ekran.blit(User1WritePower, ((screen.width - pitch.Width) / 2, (screen.height + pitch.heigth) / 2 + 10))
    if User2.superPower == "":
        User2WritePower = FONT.render(("{} has nothing".format(User2.name)), 1, (255, 255, 255))
        ekran.blit(User2WritePower, ((screen.width+pitch.Width) / 2 - User2WritePower.get_width(), (screen.height + pitch.heigth) / 2 + 10))
    else:
        User2WritePower = FONT.render("{} has {}".format(User2.name, User2.superPower), 1, (255, 255, 255))
        ekran.blit(User2WritePower, ((screen.width+pitch.Width) / 2 - User2WritePower.get_width(), (screen.height + pitch.heigth) / 2 + 10))

def winner(name):
    ekran.fill((0, 109, 0))
    FONT = pygame.font.SysFont(None, 40)
    ekran.blit(winnerImg, ((screen.width - 900) / 2, (screen.height - 493) / 2 - 50))
    nickname = FONT.render("Winner " + name, True, (227, 204, 23))
    ekran.blit(nickname, (screen.width / 2 - nickname.get_width() / 2, screen.height / 2 + 65))
    manager = pygame_gui.UIManager((screen.width, screen.height))
    buttonRst = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen.width / 2 - 110, screen.height / 2 + 100), (100, 50)), text='Restart',manager=manager)
    buttonExt = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen.width / 2 + 10, screen.height / 2 + 100), (100, 50)), text='Exit ',manager=manager)

    clock = pygame.time.Clock()
    time_delta = clock.tick(60) / 1000.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == buttonExt:
                        sys.exit()
                    if event.ui_element == buttonRst:
                        endofthegame()
                        game()
            manager.process_events(event)
        manager.update(time_delta)
        manager.draw_ui(ekran)
        pygame.display.update()

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ekran.fill((screen.RED, screen.GREEN, screen.BLUE))
        ekran.blit(scoreImg, (screen.width / 2 - 172, 0))
        threading.Thread(target=saha1.draw()).start()
        threading.Thread(target=playerMoves()).start()
        threading.Thread(target=ballMoves()).start()
        threading.Thread(target=goal()).start()
        threading.Thread(target=time()).start()
        threading.Thread(target=superPowerSelection()).start()
        threading.Thread(target=runSuperPower()).start()

        pygame.display.update()

manager = pygame_gui.UIManager((screen.width, screen.height))
button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen.width / 2 -50, screen.height / 2 + 160), (100, 50)), text='Play',manager=manager)
clock = pygame.time.Clock()

def entry():
    key = pygame.key.get_pressed()
    ekran.fill((screen.RED, screen.GREEN, screen.BLUE))
    FONT = pygame.font.SysFont(None, 24)
    nickname1 = FONT.render("Player 1 Nickname", 1, (255, 255, 255))
    ekran.blit(nickname1, (screen.width / 2 - 220, screen.height / 2 + 45))
    input_box1 = InputBox(screen.width / 2 - 220, screen.height / 2 + 72, 200, 32)
    nickname2 = FONT.render("Player 2 Nickname", 1, (255, 255, 255))
    ekran.blit(nickname2, (screen.width / 2 + 20, screen.height / 2 + 45))
    input_box2 = InputBox(screen.width / 2 + 20, screen.height / 2 + 72, 200, 32)
    nickname3 = FONT.render("Score Limit", 1, (255, 255, 255))
    ekran.blit(nickname3, (screen.width / 2 - nickname3.get_width()/2, screen.height / 2-nickname3.get_height()-50))
    input_box3 = InputBox(screen.width / 2 - 70, screen.height / 2 -50, 140, 32)
    input_boxes = [input_box1, input_box2, input_box3]

    time_delta = clock.tick(60) / 1000.0
    run = True
    while run:
        ekran.blit(logoImg, (screen.width / 2 - 150, 75))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            for box in input_boxes:
                box.handle_event(event)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button:
                        if len(input_box1.text) != 0:
                            User1.name = input_box1.text
                        else:
                            User1.name = "User1"
                        if len(input_box2.text) != 0:
                            User2.name = input_box2.text
                        else:
                            User2.name = "User2"
                        try:
                            if input_box3.text == "":
                                pitch.target_goal = 5
                                run = False
                                game()
                            else:
                                if int(input_box3.text)>0:
                                    pitch.target_goal = int(input_box3.text)
                                    run = False
                                    game()
                                else:
                                    input_box3.text = "Hata"
                        except:
                            input_box3.text = "Hata"
            manager.process_events(event)

        for box in input_boxes:
            box.draw(ekran)
        for box in input_boxes:
            box.update()
        manager.update(time_delta)
        manager.draw_ui(ekran)
        pygame.display.update()

entry()
