import os
import sys
import random
import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
Windows_Width = 980
win = pygame.display.set_mode((980,480))
music_action = 'Mute'

pvp = True
survive_mode = False

pygame.display.set_caption("Assassination")


def TransparentColor(*args): #lists
    for pic_list in args:
        for pic in pic_list:
            transColor = pic.get_at((0,0))
            pic.set_colorkey(transColor)


# Walk Images
# 9 pic FH
base_dir = getattr(sys, '_MEIPASS', os.getcwd())
FHwalkRight = []
FHwalkLeft = []
# Stand images[right, left]
FHStanding = [pygame.image.load(os.path.join(base_dir, 'media', 'R1.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L1.png'))]


# lucas
LucaswalkRight = []
LucaswalkLeft = []
LucasLightning = []
LucasKickR = []
LucasKickL = []
for pic_num in range(1, 10):
    if pic_num <= 9:
        FHwalkRight.append(pygame.image.load(os.path.join(base_dir, 'media', f'R{pic_num}.png')))
        FHwalkLeft.append(pygame.image.load(os.path.join(base_dir, 'media', f'L{pic_num}.png')))
    if pic_num <= 4:
        LucaswalkRight.append(pygame.image.load(os.path.join(base_dir, 'media', f'LucasWalkR{pic_num}.bmp')))
        LucaswalkLeft.append(pygame.image.load(os.path.join(base_dir, 'media', f'LucasWalkL{pic_num}.bmp')))
    if pic_num <=8:
        LucasLightning.append(pygame.image.load(os.path.join(base_dir, 'media', f'LucasLightning{pic_num}.bmp')))
    if pic_num <=7:
        LucasKickR.append(pygame.image.load(os.path.join(base_dir, 'media', f'LucasKickR{pic_num}.bmp')))
        LucasKickL.append(pygame.image.load(os.path.join(base_dir, 'media', f'LucasKickL{pic_num}.bmp')))
# Stand images[right, left]
LucasStanding = [pygame.image.load(os.path.join(base_dir, 'media', 'LucasStandingR.bmp')), pygame.image.load(os.path.join(base_dir, 'media', 'LucasStandingL.bmp'))]
#LucasPhotos[face image]
LucasPhotos = [pygame.image.load(os.path.join(base_dir, 'media', 'LucasFace.jpg'))]


# 8 pic assasin
AssasinwalkRight = []
AssasinwalkLeft = []
AssasinLightningR = []
AssasinLightningL = []
AssasinDashR = []
AssasinDashL = []
AssasinKnife = []
for pic_num in range(1, 17):
    if pic_num <= 5:
        AssasinwalkRight.append(pygame.image.load(os.path.join(base_dir, 'media', f'AssasinWalkR{pic_num}.bmp')))
        AssasinwalkLeft.append(pygame.image.load(os.path.join(base_dir, 'media', f'AssasinWalkL{pic_num}.bmp')))
        AssasinLightningL.append(pygame.image.load(os.path.join(base_dir, 'media', f'AssasinLightningL{pic_num}.bmp')))
        AssasinLightningR.append(pygame.image.load(os.path.join(base_dir, 'media', f'AssasinLightningR{pic_num}.bmp')))
        AssasinDashL.append(pygame.image.load(os.path.join(base_dir, 'media', f'AssasinDashL{pic_num}.bmp')))
        AssasinDashR.append(pygame.image.load(os.path.join(base_dir, 'media', f'AssasinDashR{pic_num}.bmp')))

    if pic_num <= 16:
        AssasinKnife.append(pygame.image.load(os.path.join(base_dir, 'media', f'AssasinKnife{pic_num}.bmp')))
# Stand images[right, left]
AssasinStanding = [pygame.image.load(os.path.join(base_dir, 'media', 'AssasinStandingR.bmp')), pygame.image.load(os.path.join(base_dir, 'media', 'AssasinStandingL.bmp'))]
# Assasin adittional Photos
AssasinPhotos = [pygame.image.load(os.path.join(base_dir, 'media', 'AssasinFace.bmp'))]

intro_pic = pygame.image.load(os.path.join(base_dir, 'media', 'intro.jpg'))
logo_pic = pygame.image.load(os.path.join(base_dir, 'media', 'logo3.png'))
survive_bg = pygame.image.load(os.path.join(base_dir, 'media', 'survive_bg.jpg'))
char = pygame.image.load(os.path.join(base_dir, 'media', 'standing.png'))
arrowKeys = pygame.image.load(os.path.join(base_dir, 'media', 'arrowKeys2.png'))
wasd_movement_keys = pygame.image.load(os.path.join(base_dir, 'media', 'wasd.png'))
TransPics = [wasd_movement_keys]

#set heroes transparent color
TransparentColor(TransPics, LucasKickR, LucasKickL, AssasinDashR, AssasinDashL, AssasinKnife, LucasLightning, AssasinwalkRight, AssasinwalkLeft, AssasinStanding, LucaswalkRight, LucaswalkLeft, LucasStanding, AssasinLightningR, AssasinLightningL)



clock = pygame.time.Clock()

# music
bulletSound = pygame.mixer.Sound(os.path.join(base_dir, 'media', 'bullet.wav'))
hitSound = pygame.mixer.Sound(os.path.join(base_dir, 'media', 'hit.wav'))
LucasLightningDSound = pygame.mixer.Sound(os.path.join(base_dir, 'media', 'LucasLightningD.wav'))
LucasLightningSound = pygame.mixer.Sound(os.path.join(base_dir, 'media', 'LucasLightning.wav'))
AssasinLightningSound = pygame.mixer.Sound(os.path.join(base_dir, 'media', 'AssasinLightning.wav'))
LucasKickSound = pygame.mixer.Sound(os.path.join(base_dir, 'media', 'kick.wav'))
AssasinKnifeSound = pygame.mixer.Sound(os.path.join(base_dir, 'media', 'throw.wav'))


music = pygame.mixer.music.load(os.path.join(base_dir, 'media', 'music.wav'))
pygame.mixer.music.play(-1)

button_press_delay = 0
def button(name, x, y, width, height, color, hoverColor, action=None):
    global button_press_delay, pvp, survive_mode
    if name == 'PVP Mode':
        pvp = True
        survive_mode = False
    elif name == 'Survive Mode':
        pvp = False
        survive_mode = True
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(win, hoverColor, (x, y, width, height))

        if click[0] == 1 and action != None and button_press_delay == 0:
            print(f'Button name {name} clicked')
            button_press_delay = 10
            action()
    else:
        pygame.draw.rect(win, color, (x, y, width, height))

    smallText = pygame.font.Font(os.path.join(base_dir, 'media', "comicsans.ttf"), 20)
    textSurf, textRect = text_objects(name, smallText)
    textRect.center = ( (x + (width/2)), (y + (height/2)) )
    win.blit(textSurf, textRect)


def quitgame():
    sys.exit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    global button_press_delay
    button_press_delay = 0
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        win.blit(intro_pic, (0, 0))
        win.blit(logo_pic, (10, 30))
        button("PVP Mode",250,50,100,50,(100, 50, 20),(200, 220, 20),Controls)
        button("Survive Mode",600,50,150,50,(50, 50, 90),(100, 200, 80),Controls)
        pygame.display.update()
        clock.tick(15)

def Controls():
    global button_press_delay, pvp, survive_mode
    button_press_delay = 0
    Controls = True

    while Controls:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        win.blit(survive_bg, (0, 0))
        button("Ok",420,380,100,50,(0, 150, 60),(78, 100, 130),game_loop)
        font3 = pygame.font.Font(os.path.join(base_dir, 'media', "comicsans.ttf"), 30)
        if pvp:
            text = font3.render(f'Lucas Controls:', 1, (100, 29, 200))
            win.blit(text, (20, 30))
            text = font3.render(f'movement:', 1, (7, 29, 251))
            win.blit(text, (20, 80))
            win.blit(arrowKeys, (180, 80))
            text = font3.render(f'Lightning Ball: ', 1, (7, 29, 251))
            win.blit(text, (20, 130))
            text = font3.render(f'Space', 1, (10, 150, 100))
            win.blit(text, (20 + 210, 130))
            text = font3.render(f'Lightning Transform: ', 1, (7, 29, 251))
            win.blit(text, (20, 180))
            text = font3.render(f'Down + (Right or Left) + Space', 1, (10, 150, 100))
            win.blit(text, (20, 230))
            text = font3.render(f'Lucas Kicks: ', 1, (7, 29, 251))
            win.blit(text, (20, 280))
            text = font3.render(f'Down + Space', 1, (10, 150, 100))
            win.blit(text, (20 + 170, 280))

            text = font3.render(f'Assassin Controls:', 1, (100, 29, 200))
            win.blit(text, (510, 30))
            text = font3.render(f'movement:', 1, (7, 29, 251))
            win.blit(text, (510, 80))
            win.blit(wasd_movement_keys, (670, 80))
            text = font3.render(f'Knife Throw:', 1, (7, 29, 251))
            win.blit(text, (510, 130))
            text = font3.render(f'Shift', 1, (10, 150, 100))
            win.blit(text, (510 + 200, 130))
            text = font3.render(f'Slice: ', 1, (7, 29, 251))
            win.blit(text, (510, 180))
            text = font3.render(f'S + (D or A) + Shift', 1, (10, 150, 100))
            win.blit(text, (510, 230))
            text = font3.render(f'Mega Punch: ', 1, (7, 29, 251))
            win.blit(text, (510, 280))
            text = font3.render(f'S + Shift', 1, (10, 150, 100))
            win.blit(text, (510 + 170, 280))


        if survive_mode:
            text = font3.render(f'Lucas Controls:', 1, (100, 29, 200))
            win.blit(text, (250, 30))
            text = font3.render(f'movement:', 1, (7, 29, 251))
            win.blit(text, (250, 80))
            win.blit(arrowKeys, (410, 80))
            text = font3.render(f'Lightning Ball: ', 1, (7, 29, 251))
            win.blit(text, (250, 130))
            text = font3.render(f'Space', 1, (10, 150, 100))
            win.blit(text, (250 + 210, 130))
            text = font3.render(f'Lightning Transform: ', 1, (7, 29, 251))
            win.blit(text, (250, 180))
            text = font3.render(f'Down + (Right or Left) + Space', 1, (10, 150, 100))
            win.blit(text, (250, 230))
            text = font3.render(f'Lucas Kicks: ', 1, (7, 29, 251))
            win.blit(text, (250, 280))
            text = font3.render(f'Down + Space', 1, (10, 150, 100))
            win.blit(text, (250 + 170, 280))

        pygame.display.update()
        clock.tick(15)


def game_loop():
    class player(object):
        def __init__(self, name, x, y, width, height, leftK, rightK, upK, downK, shootK, shieldK, WalkLeftPic, WalkRightPic, Standing, Photos, spAttack1PicR, spAttack1PicL, spAttack1Vel, spAttack1dmg, spAttack2PicR, spAttack2PicL, spAttack2Vel, spAttack2dmg):
            self.name = name
            self.hitDelay = 0
            self.health = 20
            self.x = x
            self.y = y
            self.xStart = x
            self.yStart = y
            self.width = width
            self.height = height
            self.vel = 10
            self.isJump = False
            self.left = True
            self.right = False
            self.walkCount = 0
            self.jumpCount = 10
            self.standing = True
            self.shootLoop = 0
            self.hitbox = (self.x + 17, self.y + 11, 29, 52)
            self.leftK = leftK
            self.rightK = rightK
            self.upK = upK
            self.downK = downK
            self.shootK = shootK
            self.shieldK = shieldK
            self.WalkLeftPic = WalkLeftPic
            self.WalkRightPic = WalkRightPic
            self.Standing = Standing
            self.Photos = Photos
            self.spAttack1PicR = spAttack1PicR
            self.spAttack1PicL = spAttack1PicL
            self.spAttack1Vel = spAttack1Vel
            self.spAttack1dmg = spAttack1dmg
            self.spAttack2PicR = spAttack2PicR
            self.spAttack2PicL = spAttack2PicL
            self.spAttack2Vel = spAttack2Vel
            self.spAttack2dmg = spAttack2dmg
            self.currentAttack = None #[Rpics, Lpics, vel, dmg]
            self.AttackCount = 0
            self.spAttackLoop = 0

        def draw(self, win):
            if self.hitDelay > 0:
                self.hitDelay -= 1
            if self.walkCount + 1 >= len(self.WalkLeftPic)*3:
                self.walkCount = 0

            if self.AttackCount:
                self.AttackCount += 1
                if self.right:
                    win.blit(self.currentAttack[0][self.AttackCount//3], (self.x,self.y))
                    if self.x < Windows_Width - self.width - self.vel:
                        self.x += (self.currentAttack[2])*1.4
                else:
                    win.blit(self.currentAttack[1][self.AttackCount//3], (self.x,self.y))
                    if self.x > self.vel:
                        self.x -= (self.currentAttack[2])*1.4

                if self.AttackCount + 1 >= len(self.currentAttack[0])*3:
                    self.AttackCount = 0

            elif not(self.standing):
                if self.left:
                    win.blit(self.WalkLeftPic[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(self.WalkRightPic[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
            else:
                if self.right:
                    win.blit(self.Standing[0], (self.x, self.y))
                else:
                    win.blit(self.Standing[1], (self.x, self.y))
            self.hitbox = (self.x + 17, self.y + 11, self.width - 35, self.height - 12)

            # draw hero pic and Life Points
            StartXtoDraw = 130
            win.blit(self.Photos[0], (StartXtoDraw + 250*heroes.index(self), 18))
            pygame.draw.rect(win, (255,0,0), (StartXtoDraw+140 + 250*heroes.index(self), 18, 80, 20))
            if self.health != 0:
                pygame.draw.rect(win, (0,128,0), (StartXtoDraw+140 + 250*heroes.index(self), 18, 80 - (4 * (20 - self.health)), 20))

            # optional draw Life Points near the head
            # pygame.draw.rect(win, (255,0,0), (self.x + 2, self.y - 5, 60, 10))
            # if self.health != 0:
            #     pygame.draw.rect(win, (0,128,0), (self.x + 2, self.y - 5, 60 - (3 * (20 - self.health)), 10))

            # optional draw hitbox
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)


        def hit(self, damage, sound=None):
            nonlocal Score
            if self.health > 0 and self.hitDelay == 0:
                if sound != None:
                    sound.play()
                print(f'the hit delay is: {self.hitDelay}')
                self.health -= damage
                print(f'{self.name} got a hit, and now have {self.health} life points')
                # Getting Hitted Delay
                if pvp:
                    self.hitDelay = 10
                if survive_mode:
                    self.hitDelay = 40
            if self.health <= 0:
                self.health = 0
                self.draw(win)
                pygame.display.update()
                print(f'{self.name} defeated')
                font1 = pygame.font.Font(os.path.join(base_dir, 'media', "comicsans.ttf"), 100)
                font2 = pygame.font.Font(os.path.join(base_dir, 'media', "comicsans.ttf"), 25)
                if pvp:
                    Loser_index = heroes.index(self)
                    heroes.pop(Loser_index)
                    text = font1.render(f'{heroes[0].name} won!', 1, (0, 44, 226))
                if survive_mode:
                    text1 = font1.render('Game Over', 1, (77, 2, 0))
                    text2 = font2.render(f'Your score is: {Score}', 1, (7, 141, 251))
                while True:
                    clock.tick(27)
                    if survive_mode:
                        win.blit(text1, ((Windows_Width//2) - (text1.get_width()/2) - 30, 120))
                        win.blit(text2, ((Windows_Width//2) - (text2.get_width()/2) - 40, 270))
                    if pvp:
                        win.blit(text, ((Windows_Width//2) - (text.get_width()/2) - 30, 150))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            quitgame()

                    button('Go back',850,10,100,50,(200, 0, 0),(200, 220, 20),game_intro)
                    button('Fight again',400,330,115,50,(160, 50, 100),(40, 10, 230),game_loop)


    class AttackParts(object):
        def __init__(self, x, y, radius, facing, user, vel, damage, length_living, FramesForPic, attackBornEndPicNum, attackLivingEndPicNum, PicsR, PicsL=None):
            self.user = user
            self.x = x
            self.original_x = x
            self.y = y
            self.radius = radius
            self.facing = facing
            self.vel = vel * facing
            self.damage = damage
            self.PicsR = PicsR
            self.PicsL = PicsL
            self.length_living = length_living
            self.AttackCount = 0
            self.attackBornEndPicNum = attackBornEndPicNum
            self.attackLivingEndPicNum = attackLivingEndPicNum
            self.isOver = False
            self.FramesForPic = FramesForPic
            self.hitbox = (self.x + 17, self.y + 11, self.radius*2 - 35, self.radius*2 - 12)

        def draw(self, win):
            # if there is diff between right and left
            if self.PicsL != None and self.facing < 0:
                win.blit(self.PicsL[self.AttackCount//self.FramesForPic], (self.x,self.y))
            else:
                win.blit(self.PicsR[self.AttackCount//self.FramesForPic], (self.x,self.y))

            self.AttackCount += 1

            if self.AttackCount >= self.attackLivingEndPicNum*self.FramesForPic and not(self.isOver):
                self.AttackCount = (self.attackBornEndPicNum)*self.FramesForPic
            #when its done show exit animation- pop the attack
            if self.AttackCount//self.FramesForPic >= len(self.PicsR) and self.isOver:
                attacks.pop(attacks.index(self))

            self.hitbox = (self.x + 17, self.y + 11, self.radius*2 - 35, self.radius*2 - 12)

            # optional draw hitbox
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    class AttackLoop(object):
        def __init__(self, x, y, radius, facing, user, vel, damage, length_living, FramesForPic, PicsR, PicsL=None):
            self.user = user
            self.x = x
            self.original_x = x
            self.y = y
            self.radius = radius
            self.facing = facing
            self.vel = vel * facing
            self.damage = damage
            self.PicsR = PicsR
            self.PicsL = PicsL
            self.length_living = length_living
            self.AttackCount = 0
            self.isOver = False
            self.FramesForPic = FramesForPic
            self.hitbox = (self.x + 17, self.y + 11, self.radius*2 - 35, self.radius*2 - 12)

        def draw(self, win):
            # if there is diff between right and left
            if self.PicsL != None and self.facing < 0:
                win.blit(self.PicsL[self.AttackCount//self.FramesForPic], (self.x,self.y))
            else:
                win.blit(self.PicsR[self.AttackCount//self.FramesForPic], (self.x,self.y))

            self.AttackCount += 1

            if self.AttackCount >= len(self.PicsR)*self.FramesForPic and not(self.isOver):
                self.AttackCount = 1
            #when its done show exit animation- pop the attack
            if self.isOver:
                attacks.pop(attacks.index(self))

            self.hitbox = (self.x + 17, self.y + 11, self.radius*2 - 35, self.radius*2 - 12)

            # optional draw hitbox
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)




    class enemy(object):
        FHwalkRight = [pygame.image.load(os.path.join(base_dir, 'media', 'R1E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R2E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R3E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R4E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R5E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R6E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R7E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R8E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R9E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R10E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'R11E.png'))]
        FHwalkLeft = [pygame.image.load(os.path.join(base_dir, 'media', 'L1E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L2E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L3E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L4E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L5E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L6E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L7E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L8E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L9E.png')), pygame.image.load(os.path.join(base_dir,'media', 'L10E.png')), pygame.image.load(os.path.join(base_dir, 'media', 'L11E.png'))]

        def __init__(self, name, x, y, width, height, end):
            self.name = name
            self.x = x
            self.y = y
            self.xStart = x
            self.yStart = y
            self.width = width
            self.height = height
            self.end = end
            self.path = [self.x, self.end]
            self.walkCount = 0
            self.vel = 3
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            self.health = 10
            self.visible = True
            self.respawn = 0
            self.hitDelay = 0

        def __str__(self):
            return (f'{self.name}')


        def draw(self, win, Player_1_x):
            if self.hitDelay > 0:
                self.hitDelay -= 1
            self.move(Player_1_x)
            if self.respawn > 0:
                self.respawn -= 1
            if self.respawn == 1:
                self.visible = True
                print(f'{self.name} have respawned')
                self.health = 10
                self.respawn == 0
                self.x = random.choice(range(1, 980))
                self.y = self.yStart
                goblins.append(enemy('goblin', random.choice(range(1, 980)), 350, 64, 64, 460))
            if self.visible:
                if self.walkCount + 1 >= 33:
                    self.walkCount = 0

                if self.vel > 0:
                    win.blit(self.FHwalkRight[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.FHwalkLeft[self.walkCount //3], (self.x, self.y))
                    self.walkCount += 1

                self.hitbox = (self.x + 17, self.y + 2, 31, 57)
                pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 40, 10))
                pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 40 - (4 * (10 - self.health)), 10))

                # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

        def move(self, Player_x_To_Chase):
            # chasing after Player
            if self.vel > 0:
                if self.x < Player_x_To_Chase:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0
            else:
                if self.x > Player_x_To_Chase:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkCount = 0

        def hit(self, dmg):
            nonlocal Score
            if self.health > 0 and self.hitDelay==0:
                hitSound.play()
                self.health -= dmg
                print(f'{self} got a hit')
            if self.health <= 0:
                self.health = 0
                print(f'{self} defeated')
                self.visible = False
                self.respawn = 100
                Score += 1

        def __str__(self):
            return self.name

    def Mute():
        global music_action
        print('Muted')
        pygame.mixer.music.pause()
        music_action = 'Play music'
        print(f'now in Mute: ma is {music_action}')

    def Play():
        global music_action
        print('Playing music')
        pygame.mixer.music.unpause()
        pygame.mixer.music.rewind()
        music_action = 'Mute'


    heroes = []
    attacks = []

    if pvp:
        print('pvp mode')
        Player_1 = player('Lucas', 900, 335, 64, 64, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP,  pygame.K_DOWN, pygame.K_SPACE, pygame.K_n, LucaswalkLeft, LucaswalkRight, LucasStanding, LucasPhotos, LucasLightning, LucasLightning, 13, 2, LucasKickR, LucasKickL, 17, 1.5)
        heroes.append(Player_1)
        Player_2 = player('Assassin', 30, 335, 80, 80, pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, pygame.K_LSHIFT, pygame.K_q, AssasinwalkLeft, AssasinwalkRight, AssasinStanding, AssasinPhotos, AssasinLightningR, AssasinLightningL, 15, 3, AssasinDashR, AssasinDashL, 10, 4)
        Player_2.right = True
        Player_2.left = False
        heroes.append(Player_2)

    if survive_mode:
        Score = 0
        print('survive_mode')
        Player_1 = player('Lucas', 440, 335, 64, 64, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_SPACE, pygame.K_n, LucaswalkLeft, LucaswalkRight, LucasStanding, LucasPhotos, LucasLightning, LucasLightning, 13, 2, LucasKickR, LucasKickL, 17, 1)
        heroes.append(Player_1)
        goblin1 = enemy('goblin1', 0, 350, 64, 64, 450)
        goblin2 = enemy('goblin2', Windows_Width, 350, 64, 64, 460)
        goblins = [goblin1, goblin2]



    run = True

    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quitgame()

            pos = pygame.mouse.get_pos()

        #goblin interactions
        if survive_mode:
            # goblins hits Player_1
            for goblin in goblins:
                if goblin.visible == True:
                    if Player_1.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and Player_1.hitbox[1] + Player_1.hitbox[3] > goblin.hitbox[1]:
                        if Player_1.hitbox[0] + Player_1.hitbox[2] > goblin.hitbox[0] and Player_1.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                            if Player_1.AttackCount:
                                if goblin.hitDelay == 0:
                                    goblin.hit(Player_1.currentAttack[3])
                                    goblin.hitDelay = 3
                            else:
                                Player_1.hit(2)


                if goblin.visible:
                    for attack in attacks:
                        if attack.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and attack.hitbox[1] + attack.hitbox[3] > goblin.hitbox[1]:
                            if attack.hitbox[0] + attack.hitbox[2] > goblin.hitbox[0] and attack.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                                if not(attack.isOver):
                                    goblin.hit(attack.damage)
                                    attack.isOver = True
                                    if type(attack) == AttackParts:
                                        attack.AttackCount = attack.attackLivingEndPicNum*attack.FramesForPic

        # player hits player
        if pvp:
            for hero in heroes:
                for attack in attacks: #out attack
                    if attack.user != hero.name:
                        if not(attack.isOver):
                            if attack.hitbox[1] < hero.hitbox[1] + hero.hitbox[3] and attack.hitbox[1] + attack.hitbox[3] > hero.hitbox[1]:
                                if attack.hitbox[0] + attack.hitbox[2] > hero.hitbox[0] and attack.hitbox[0] < hero.hitbox[0] + hero.hitbox[2]:
                                    print(f'{attack.user} hit {hero.name}')
                                    hero.hit(attack.damage, sound=hitSound)
                                    attack.isOver = True
                                    if type(attack) == AttackParts:
                                        attack.AttackCount = attack.attackLivingEndPicNum*attack.FramesForPic

                if hero.AttackCount: #bodyAttack
                    for hero2 in heroes:
                        if hero != hero2:
                            if hero.hitbox[1] < hero2.hitbox[1] + hero2.hitbox[3] and hero.hitbox[1] + hero.hitbox[3] > hero2.hitbox[1]:
                                if hero.hitbox[0] + hero.hitbox[2] > hero2.hitbox[0] and hero.hitbox[0] < hero2.hitbox[0] + hero2.hitbox[2]:
                                    hero2.hit(hero.currentAttack[3], sound=hitSound)



        for attack in attacks:
            if not(attack.isOver):
                if attack.x < Windows_Width - attack.radius*2 and attack.x > 0 and abs(attack.original_x - attack.x) < attack.length_living:
                    attack.x += attack.vel
                else:
                    attack.isOver = True
                    if type(attack) == AttackParts:
                        attack.AttackCount = attack.attackLivingEndPicNum*attack.FramesForPic

        # Attacks delay
        for hero in heroes:
            if hero.spAttackLoop > 0:
                hero.spAttackLoop += 1
            if hero.spAttackLoop > 30:
                hero.spAttackLoop = 0
                hero.shootLoop = 1

            #regular attack delay
            if hero.shootLoop > 0:
                hero.shootLoop += 1
            if hero.shootLoop > 17:
                hero.shootLoop = 0

        keys = pygame.key.get_pressed()

        # Players movement and shooting
        for hero in heroes:
            if keys[hero.shootK]:
                if keys[hero.downK]:
                    if keys[hero.rightK] or keys[hero.leftK]:
                        if hero.spAttackLoop == 0 and hero.shootLoop == 0:
                            hero.AttackCount = 1
                            hero.spAttackLoop = 1
                            if hero.name == 'Lucas':
                                LucasLightningDSound.play()
                            if hero.name == 'Assassin':
                                AssasinLightningSound.play()
                            hero.currentAttack = [hero.spAttack1PicR, hero.spAttack1PicL, hero.spAttack1Vel, hero.spAttack1dmg]
                    else:
                        if hero.spAttackLoop == 0 and hero.shootLoop == 0:
                            hero.AttackCount = 1
                            hero.spAttackLoop = 1
                            if hero.name == 'Lucas':
                                LucasKickSound.play()
                                LucasKickSound.play()
                                LucasKickSound.play()
                            if hero.name == 'Assassin':
                                LucasKickSound.play()
                            hero.currentAttack = [hero.spAttack2PicR, hero.spAttack2PicL, hero.spAttack2Vel, hero.spAttack2dmg]

                if hero.left:
                    facing = -1
                else:
                    facing = 1
                if hero.shootLoop == 0 and hero.AttackCount == 0:
                    if hero.name == 'Lucas':
                        LucasLightningSound.play()
                        attacks.append(AttackParts(round(hero.x + hero.width//2)-50+10*facing, round(hero.y + hero.height//2)-40, 50, facing, hero.name, 15, 2, 700, 5, 3, 6, LucasLightning))
                        hero.shootLoop = 1

                    if hero.name == 'Assassin':
                        AssasinKnifeSound.play()
                        attacks.append(AttackLoop(round(hero.x + hero.width//2)-50+10*facing, round(hero.y + hero.height//2)-30, 24, facing, hero.name, 25, 1, 800, 2, AssasinKnife))
                        hero.shootLoop = 1


            if keys[hero.leftK] and hero.x > hero.vel:
                hero.x -= hero.vel
                hero.left = True
                hero.right = False
                hero.standing = False

            elif keys[hero.rightK] and hero.x < Windows_Width - hero.width - hero.vel:
                hero.x += hero.vel
                hero.right = True
                hero.left = False
                hero.standing = False
            else:
                hero.standing = True
                hero.walkCount = 0

            if not(hero.isJump):
                if keys[hero.upK]:
                    hero.isJump = True
                    hero.walkCount = 0
            else:
                if hero.jumpCount >= -10:
                    neg = 1
                    if hero.jumpCount < 0:
                        neg = -1
                    hero.y -= (hero.jumpCount ** 2) * 0.5 * neg
                    hero.jumpCount -= 1
                else:
                    hero.isJump = False
                    hero.jumpCount = 10


        def redrawGameWindow():
            global button_press_delay
            win.blit(survive_bg, (0,0))
            for hero in heroes:
                hero.draw(win)

            if survive_mode:
                for goblin in goblins:
                    goblin.draw(win, Player_1.x)
                font2 = pygame.font.Font(os.path.join(base_dir, 'media', "comicsans.ttf"), 30)
                text = font2.render(f'Score: {Score}', 1, (7, 29, 251))
                win.blit(text, (700, 15))

            for attack in attacks:
                attack.draw(win)

            if button_press_delay > 0:
                button_press_delay -= 1
            if music_action == "Mute":
                button(music_action,10,10,100,50,(250, 250, 100),(70, 5, 150),Mute)
            else:
                button(music_action,10,10,100,50,(200, 0, 0),(200, 220, 20),Play)
            button('Go back',850,10,100,50,(200, 0, 0),(200, 220, 20),game_intro)

            pygame.display.update()
        redrawGameWindow()

game_intro()
quitgame()
