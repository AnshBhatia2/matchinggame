import pygame
pygame.init()

WIDTH = 800
HEIGHT = 1000
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Matching Game")

white = (255,255,255)

window.fill((255,255,255))
run = True
pygame.display.update()

brawl_stars_logo = pygame.image.load("brawlstarsmatch.jfif")
fortnite_logo = pygame.image.load("fortnitematch.jfif")
minecraft_logo = pygame.image.load("minecraftmatch.jfif")
sub_surf_logo = pygame.image.load("subsurfmatch.jfif")

window.blit(brawl_stars_logo, (100, 50))
window.blit(fortnite_logo, (100, 300))
window.blit(minecraft_logo, (100, 550))
window.blit(sub_surf_logo, (100, 800))
pygame.display.update()
font = pygame.font.SysFont("Times New Roman", 40)
text1 = font.render("Minecraft", True, (0,0,0))
text2 = font.render("Brawl Stars", True, (0,0,0))
text3 = font.render("Subway Surfers", True, (0,0,0))
text4 = font.render("Fortnite", True, (0,0,0))
window.blit(text1,(450, 50))
window.blit(text2,(450, 300))
window.blit(text3,(450, 550))
window.blit(text4,(450, 800))
pygame.display.update()

while 1:

    event = pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(window, (0,0,0), (pos), 20, 0)
        pygame.display.update
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(window, (0,0,0), (pos), (pos2), 5)
        pygame.draw.circle(window, (0,0,0), (pos2), 20, 0)
        pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()