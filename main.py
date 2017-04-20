import pygame,random,math
SCREEN_SIZE=(450, 500)
WHITE=(255,255,255)
BLACK=(0,0,0)
left_bars=[]
right_bars=[]
left_balls=[]
right_balls=[]
MOVING_SPEED=2
ANGLE_SPEED=1.5
HI_SCORE=0
CURRENT_SCORE=0
FPS=60

class Bar(pygame.sprite.Sprite):
    RIGHT=0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.reset_y= -SCREEN_SIZE[1] / 2;
        self.image=pygame.Surface((SCREEN_SIZE[0], SCREEN_SIZE[1]/ 15))
        self.image.fill(WHITE)
        self.rect=self.image.get_rect()
        self.image.set_colorkey(BLACK)
        self.mask=pygame.mask.from_surface(self.image)
    def update(self):
        self.rect.move_ip((0,MOVING_SPEED))

    def setLocation(self,which_position,ypos,xpos):
        self.rect.top=ypos
        if which_position==self.RIGHT:
            self.rect.right=xpos
        else:
            self.rect.left=xpos


class Ball(pygame.sprite.Sprite):
    BALL_RADIUS=15
    RADIUS=80
    MAX_ANGLE=20
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40,40))
        self.rect = pygame.draw.circle(self.image,WHITE, (20, 20), self.BALL_RADIUS, 0)
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle=random.random()*self.MAX_ANGLE
        self.angle_speed=ANGLE_SPEED
        self.center_x=0
        self.center_y=0

    def set_location(self,center_y,center_x):
        self.rect.centery=center_y
        self.center_x,self.center_y=center_x,center_y
        self.angle=random.random()*self.MAX_ANGLE+(270-self.MAX_ANGLE)

    def update(self):
        self.center_y+=MOVING_SPEED
        self.angle+=self.angle_speed
        if self.angle>(270+self.MAX_ANGLE) or self.angle<(270-self.MAX_ANGLE):
            self.angle_speed=-self.angle_speed
        current_angle=self.angle*math.pi/180
        self.rect.centerx=self.center_x+self.RADIUS*math.cos(current_angle)
        self.rect.centery = self.center_y - self.RADIUS * math.sin(current_angle)


class Player(pygame.sprite.Sprite):
    BALL_RADIUS=10
    SPEED_INCREMENTER=-0.3
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.rect = pygame.draw.circle(self.image, (255,0,0), (20, 20), self.BALL_RADIUS, 0)
        self.image.set_colorkey(BLACK)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx=SCREEN_SIZE[0]/2
        self.rect.centery=(SCREEN_SIZE[1]-SCREEN_SIZE[1]/5)
        self.xvelocity=2

    def update(self):
        global CURRENT_SCORE,HI_SCORE
        if self.rect.centerx <= 0 or self.rect.centerx >= SCREEN_SIZE[0] or collided():
            reset_game()
        for i in range (0,3):
            if(left_bars[i].rect.top==self.rect.bottom):
                CURRENT_SCORE+=1
                HI_SCORE=max(HI_SCORE,CURRENT_SCORE)
        self.xvelocity+=self.SPEED_INCREMENTER
        self.rect.move_ip((self.xvelocity,0))

def collided():
    collided=False
    for i in range(0,3):
        if pygame.sprite.collide_mask(player,left_balls[i])!=None:
            collided=True
        if pygame.sprite.collide_mask(player,right_balls[i])!=None:
            collided=True
        if pygame.sprite.collide_mask(player,right_bars[i])!=None:
            collided=True
        if pygame.sprite.collide_mask(player,left_bars[i])!=None:
            collided=True
    return collided

def reset(index,ypos):
    global SCREEN_SIZE,left_bars,right_bars,left_balls,right_balls
    offset=SCREEN_SIZE[0]/10
    blank_space=SCREEN_SIZE[0]/2.5
    x1=offset+(SCREEN_SIZE[0]-2*offset-blank_space)*random.random()
    x2=x1+blank_space
    left_bars[index].setLocation(0,ypos,x1)
    right_bars[index].setLocation(1,ypos,x2)
    left_balls[index].set_location(ypos,x1)
    right_balls[index].set_location(ypos, x2)



def reset_game():
    global player,can_update,CURRENT_SCORE
    can_update=False
    player.rect.centerx=SCREEN_SIZE[0]/2
    for i in range(0,3):
        reset(i, -(i + 1) * width_between_bars)
    CURRENT_SCORE=0



pygame.init()
screen=pygame.display.set_mode(SCREEN_SIZE)
background=pygame.Surface(screen.get_size())
background.fill(BLACK)
done = False
can_update= False
clock=pygame.time.Clock()

player=Player()
width_between_bars=SCREEN_SIZE[1]/2
for i in range(0,3):
    left_bars.append(Bar())
    right_bars.append(Bar())
    left_balls.append(Ball())
    right_balls.append(Ball())
    reset(i,-(i+1)*width_between_bars)
sprites=pygame.sprite.RenderPlain((left_bars,right_bars,left_balls,right_balls,player))
font = pygame.font.SysFont("comicsansms", 12)


while not done :
    pygame.draw.rect(screen,(0,0,255),pygame.Rect(10,10,20,20))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
        elif event.type==pygame.MOUSEBUTTONDOWN or event.type==pygame.KEYDOWN:
            can_update=True
            player.SPEED_INCREMENTER=-player.SPEED_INCREMENTER
            if player.xvelocity <0:
                player.xvelocity=-5
            else :
                player.xvelocity=5
    for i in range(0,3):
        if(left_bars[i].rect.top>=SCREEN_SIZE[1]):
            reset(i,-width_between_bars)

    screen.blit(background,(0,0))
    high_score = font.render("HIGH SCORE:"+str(HI_SCORE), True, (0, 128, 0))
    current_score = font.render("CURRENT SCORE:"+str(CURRENT_SCORE), True, (0, 128, 0))
    screen.blit(high_score,(2,SCREEN_SIZE[1]-high_score.get_height()-2))
    screen.blit(current_score, (SCREEN_SIZE[0]-current_score.get_width()-2, SCREEN_SIZE[1] - current_score.get_height() - 2))
    if can_update :
        sprites.update()
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
