import pygame
import pygame as pg
import random
import os
import sys
import time


fps = 90
pg.init()
pygame.display.set_caption('Repeat after me')
sound1 = pg.mixer.Sound('data/zvuk-notyi-do.mp3')
sound2 = pg.mixer.Sound('data/zvuk-notyi-fa.mp3')
sound3 = pg.mixer.Sound('data/zvuk-notyi-lya.mp3')
sound4 = pg.mixer.Sound('data/zvuk-notyi-si.mp3')
colors_list = ['red', 'black', 'blue', 'white']
score = 1
record = 0
check = []
user_check = []


def game():
    global score, check, user_check, record
    if user_check == check:
        score += 1
    else:
        if score > record:
            record = score
            record -= 1
        score = 1
        check = []

    check.append(get_random_color())
    animation_and_sound(check)
    user_check = []
    print(check)


def animation_and_sound(colors):
    time.sleep(0.4)
    for color in colors:
        if color == 'red':
            if pygame.mixer.Channel(0).get_busy():
                time.sleep(0.5)
            update(color)
            pygame.mixer.Sound.play(sound1)
        if color == 'white':
            if pygame.mixer.Channel(0).get_busy():
                time.sleep(0.5)
            update(color)
            pygame.mixer.Sound.play(sound3)
        if color == 'black':
            if pygame.mixer.Channel(0).get_busy():
                time.sleep(0.5)
            update(color)
            pygame.mixer.Sound.play(sound2)
        if color == 'blue':
            if pygame.mixer.Channel(0).get_busy():
                time.sleep(0.5)
            update(color)
            pygame.mixer.Sound.play(sound4)


def update(color):
    if color == 'red':
        pass
    if color == 'white':
        pass
    if color == 'black':
        pass
    if color == 'blue':
        pass


def get_random_color():
    global colors_list
    random_color = random.choice(colors_list)
    return random_color


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def start_screen(screen):
    fon = pygame.transform.scale(load_image('менюшка.png'), (300, 300))
    screen.blit(fon, (0, 0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


def draw(screen):
    global score
    screen.fill((235, 198, 240))
    screen.fill(pygame.Color('red'), pygame.Rect(125, 50, 50, 50))
    screen.fill(pygame.Color('black'), pygame.Rect(50, 125, 50, 50))
    screen.fill(pygame.Color('white'), pygame.Rect(200, 125, 50, 50))
    screen.fill(pygame.Color('blue'), pygame.Rect(125, 200, 50, 50))
    font = pygame.font.Font(None, 30)
    text = font.render(f'score: {score - 1}', True, (0, 0, 0))
    text2 = font.render(f'record: {record}', True, (0, 0, 0))
    screen.blit(text, (200, 20))
    screen.blit(text2, (200, 40))


def click(pos):
    global user_check
    x, y = pos
    if 124 < x < 175 and 50 < y < 100:
        user_check.append('red')
        pygame.mixer.Sound.play(sound1)
    elif 50 < x < 100 and 125 < y < 175:
        user_check.append('black')
        pygame.mixer.Sound.play(sound2)
    elif 200 < x < 250 and 125 < y < 175:
        user_check.append('white')
        pygame.mixer.Sound.play(sound3)
    elif 125 < x < 175 and 200 < y < 250:
        user_check.append('blue')
        pygame.mixer.Sound.play(sound4)
    else:
        print('not rect')
    if len(user_check) == score:
        game()

    else:
        for i in range(len(user_check)):
            if user_check[i] != check[i]:
                game()


if __name__ == '__main__':
    pygame.init()
    all_sprites = pygame.sprite.Group()
    sprite, sprite2, sprite3, sprite4 = pygame.sprite.Sprite(), pygame.sprite.Sprite(),\
        pygame.sprite.Sprite(), pygame.sprite.Sprite()
    sprite.image = load_image("bomb.png")
    im, im2, im3 = load_image('star.png'), load_image('car.png'), load_image('creature.png')
    im3 = pygame.transform.scale(im3, (60, 60))
    sprite2.image = im3
    sprite2.image.set_colorkey('white')
    im = pygame.transform.scale(im, (50, 50))
    sprite3.image = im
    im2 = pygame.transform.scale(im2, (80, 60))
    sprite4.image = im2
    sprite.rect = sprite.image.get_rect()
    sprite2.rect = sprite2.image.get_rect()
    sprite3.rect = sprite2.image.get_rect()
    sprite4.rect = sprite2.image.get_rect()
    all_sprites.add(sprite)
    all_sprites.add(sprite2)
    all_sprites.add(sprite3)
    all_sprites.add(sprite4)
    sprite.rect.x, sprite.rect.y = 52, 123
    sprite2.rect.x, sprite2.rect.y = 117, 40
    sprite3.rect.x, sprite3.rect.y = 125, 200
    sprite4.rect.x, sprite4.rect.y = 200, 123
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    start_screen(screen)
    running = True
    clock = pygame.time.Clock()
    check.append(get_random_color())
    game()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                click(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()
        draw(screen)
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()