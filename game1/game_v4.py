import pygame

#Игра с добавлением СОБЫТИЙ

window  =  pygame.display.set_mode((700, 700))
pygame.display.set_caption('My first game')
screen = pygame.Surface((700, 700))

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Intersect(x1, x2, y1, y2, db1, db2):
    if(x1>x2-db1)and(x1<x2+db2)and(y1>y2-db1)and(y1<y2+db2):
        return 1
    else:
        return 0

hero = Sprite(200, 400, 'lion.ico')
goal = Sprite(10, 10, 'android.png')
goal.right = False
goal.step = 1

love = Sprite(-128, 400, 'love_cloud.png')
love.push  = False

done = True

#Чтобы работало с зажатой клавишей, дублирует действие, пока держим клавишу нажатой
#Принимает 2 параметра. 1-задержка перед первым дублированием, 2-задержка между остальными дублированиями
pygame.key.set_repeat(1, 1)

while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
           done = False

           #Событие - нажатие клавишь
        if e.type == pygame.KEYDOWN:
            #Перемещение героя
            if e.key  == pygame.K_LEFT:
                if hero.x > 10:
                    hero.x -= 1
            if e.key == pygame.K_RIGHT:
                if hero.x < 444:
                    hero.x += 1
            if e.key  == pygame.K_UP:
                if hero.y > 10:
                    hero.y -= 1
            if e.key == pygame.K_DOWN:
                if hero.y < 444:
                    hero.y += 1
                    
           #Запуск стрелы
            if e.key == pygame.K_SPACE:
                if love.push == False:
                    love.x = hero.x+64
                    love.y = hero.y+64
                    love.push = True

    screen.fill((205, 145, 158))

    if goal.right == True:
        goal.x -= goal.step
        if goal.x < 0:
            goal.right = False
    else:
        goal.x += goal.step
        if goal.x > 400:
            goal.right = True

    #Перемещение стрелы
    if love.y <  0:
        love.push  = False

    if love.push == False:
        love.y = 400
        love.x = -128
    else:
        love.y -= 1

    #Столкновение стрелы и цели
    if Intersect(love.x, goal.x, love.y, goal.y, 128, 300) == True:
        love.push = False
        #Увеличение сложности путём увеличения скорости после каждого попадания
        goal.step += 0.2

    love.render()
    hero.render()
    goal.render()
    window.blit(screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5)
pygame.quit()
