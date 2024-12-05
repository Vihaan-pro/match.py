import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

screen.fill("white")

pygame.display.update()

s = pygame.image.load("s.png")
t = pygame.image.load("t.png")
c = pygame.image.load("c.jpg")
l = pygame.image.load("l.png")

screen.blit(s,(150,100))
screen.blit(t,(150,300))
screen.blit(c,(150,200))
screen.blit(l,(150,400))

font=pygame.font.SysFont("Arial",36)
t1 = font.render("subway surfer",True,(0,0,0))
t2 = font.render("temple run",True,(0,0,0))
t3 = font.render("candy crush",True,(0,0,0))
t4 = font.render("ludo",True,(0,0,0))

screen.blit(t1,(350,100))
screen.blit(t2,(350,200))
screen.blit(t3,(350,300))
screen.blit(t4,(350,400))
pygame.display.update()

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()      
                pygame.draw.circle(screen, (0,0,0) ,(pos), 20, 0)
                pygame. display.update()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos2 = pygame.mouse.get_pos()
                pygame.draw.line(screen,(0,0,0), (pos), (pos2),5)
                pygame.draw.circle(screen, (0,0,0) ,(pos2), 20, 0)
                pygame.display.update()
        