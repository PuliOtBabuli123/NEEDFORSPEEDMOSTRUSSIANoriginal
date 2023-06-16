import pygame
from time import sleep
window = display.set_mode((700,500))
display.set_caption("NEED FOR SPEED MOST RUSIIAN")
background = transform.scale(image.load(".png"), (700,500))
game = True
reload_time = False
mixer.init()
mixer.music.load('.mp3')
mixer.music.play()
kick = mixer.Sound('.mp3')
font.init()
proigrish = font.render('Wasted!', True, (250, 0, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image,player_x,player_y,size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x>5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x<635:
            self.rect.x += self.speed 
class NPS(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 490:
            self.rect.y = 0
            self.rect.x = randint(10,690)
            lost +=1
def printit():
    kilometr = 1
    while True:
        popal_nadp = font.render('Ты проехал:'+str(kilometr)'km',True,(250,0,0))
        sleep(1)
        kilometr+=1
player = Player('.png', 5, 400,200,200, 7)
enemy = NPS('.png', randint(10,690), 10,150,150 , randint(1,2))
enemy2 = NPS('.png', randint(10,690), 10,150,150, randint(1,2))
enemy3 = NPS('.png', randint(10,690), 10,150,150, randint(1,2))
enemy4 = NPS('.png', randint(10,690), 10,150,150, randint(1,2))
enemys = sprite.Group()
for i in range(4):
    enemy = NPS('.png', randint(10,690), 10,150,150 , randint(1,4))
    enemys.add(enemy)
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
    if finish != True:
        window.blit(background,(0, 0))
        if sprite.spritecollide(player, enemys, False):
            finish = True
            window.blit(proigrish, (250,200))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        enemys.draw(window)
        enemys.update()
        popal_nadp = font.render('Ты проехал:'+str(kilometr)'km',True,(250,0,0))
        window.blit(popal_nadp, (10, 10))

    display.update()
    clock.tick(FPS)

