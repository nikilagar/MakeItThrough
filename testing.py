import pygame

class Circle(pygame.sprite.Sprite):
    def __init__(self):
        WHITE=(255, 255, 255)
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,50))
        self.image.fill(WHITE)
        self.rect=pygame.draw.circle(self.image,(100,0,100),(20,20),10,0)
        self.image.set_colorkey(WHITE)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.move((0,0))


screen=pygame.display.set_mode((200,200))

done=False
clock=pygame.time.Clock()
cir1=Circle()
cir2=Circle()
cir1.rect.left=10
cir2.rect.left=29
cir2.rect.top=10
print(pygame.sprite.collide_mask(cir1,cir2))
sprites=pygame.sprite.RenderPlain((cir1,cir2))
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(10)