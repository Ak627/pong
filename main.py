import pygame
pygame.init()

screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("The best Pong ever")

p1x = 20
p1y = 200
p1Score = 0
p2x = 650
p2y = 200
p2Score = 0

bx = 350
by = 250
bVx = 5
bVy = 5
doExit = False
clock = pygame.time.Clock()
while not doExit:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p1y -= 5
    if keys[pygame.K_s]:
        p1y+=5
    if keys[pygame.K_UP]:
        p2y -= 5
    if keys[pygame.K_DOWN]:
        p2y += 5
        
    if bx < p1x + 20 and by + 20 > p1y and by < p1y + 100:
        bVx *= -1
        
    if bx > p2x and by + 20 > p2y and by < p2y + 100:
        bVx *= -1
        
        
    if bx <= 0:
        bVx *= -1
        p2Score += 1
    if bx >= 700:
        bVx *= -1
        p1Score += 1
        
        
    bx += bVx
    by += bVy
    
    
    if by < 0 or by + 20 > 500:
        bVy *= -1   
    screen.fill((0,0,0))
    font = pygame.font.Font(None, 74)
    text = font.render(str(p1Score),1, (0, 255, 0))
    screen.blit(text, (250, 10))
    text = font.render(str(p2Score),1, (0, 255, 0))
    screen.blit(text, (420, 10))
    pygame.draw.line(screen, (128, 1, 148), [349, 0], [349, 500], 5)
    pygame.draw.rect(screen, (0, 255, 0), (p1x, p1y, 20, 100), 1)
    pygame.draw.rect(screen, (0, 255, 0), (p2x, p2y, 20, 100), 1)
    pygame.draw.circle(screen, (255, 255, 255), (bx, by), 10)
    pygame.display.flip()
pygame.quit()


