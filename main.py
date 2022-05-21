from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       # каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (55, 55))
       self.speed = player_speed
       # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 80:
           self.rect.y += self.speed
 
#класс-наследник для спрайта-врага (перемещается сам)
class Enemy(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

 
#Игровая сцена:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Пинг-понг")
background = transform.scale(image.load("Без названия.jpeg"), (win_width, win_height))
 
#Персонажи игры:
player = Player('1.png', 5, win_height - 80, 4)
monster = Enemy('2.png', win_width - 80, 280, 4)
ball = GameSprite(('ball.png'), win_width/2, win_height/2, 0)
  
game = True
finish = False
clock = time.Clock()
FPS = 60
 
font.init()
font = font.Font(None, 70)
#win = font.render('Ты натурал!', True, (255, 215, 0))
lose1 = font.render('проиграл 1', True, (180, 0, 0))
lose2 = font.render('проиграл 2', True, (180, 0, 0))
 
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

speed_x = 1
speed_y = 1
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
  
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monster.update()

        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(player, ball) or sprite.collide_rect(monster, ball):
            speed_x *= -1

        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_y *= -1    

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        player.reset()
        monster.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)