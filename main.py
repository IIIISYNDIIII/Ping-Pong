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
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 4)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)



 
 
 
game = True
finish = False
clock = time.Clock()
FPS = 60
 
font.init()
font = font.Font(None, 70)
win = font.render('Ты натурал!', True, (255, 215, 0))
lose = font.render('Ты', True, (180, 0, 0))
 
#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
 
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       window.blit(background,(0, 0))
       player.update()
       monster.update()
      
       player.reset()
       monster.reset()

   if sprite.collide_rect(player, monster):
        finish = True
        window.blit(lose, (200, 200))

   if sprite.collide_rect(player, final):
        finish = True
        window.blit(win, (200, 200))
        money.play()

 
   display.update()
   clock.tick(FPS)