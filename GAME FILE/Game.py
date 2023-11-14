import pygame

pygame.init()

WIDTH,HEIGHT = 800,600
FPS = 60

player_width = 50
player_height = 50
player_x = 50
player_y = HEIGHT - player_height - 50
player_speed = 5
jump = False
jump_count = 10
facing_left = False

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('GAME')

player_img = pygame.image.load('assets/knight.png')
player_img = pygame.transform.scale(player_img, (player_width, player_height))
player_img_flipped = pygame.transform.flip(player_img, True, False)

clock = pygame.time.Clock()

run = True
while run:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
        facing_left = True
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
        facing_left = False
    if not jump:
        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if jump_count >= -10:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
            jump = False
            jump_count = 10
    
    if facing_left:
        screen.blit(player_img_flipped, (player_x, player_y))
    else:
        screen.blit(player_img, (player_x, player_y))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()