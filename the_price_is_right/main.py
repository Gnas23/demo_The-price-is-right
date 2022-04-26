import pygame
import inputBox
import button
import time

pygame.init()
white = (255, 255, 255)

X = 900
Y = 600
screen = pygame.display.set_mode((X, Y ))
pygame.display.set_caption("THE PRICE IS RIGHT")


background = pygame.image.load(r'assets\background.jpg').convert()
ask = pygame.image.load(r'assets\ask.png').convert()
product_1 = pygame.image.load(r'assets\product1.PNG').convert()
product_2 = pygame.image.load(r'assets\product2.PNG').convert()
right_img = pygame.image.load(r'assets\right.png').convert_alpha()
left_img = pygame.image.load(r'assets\left.png').convert_alpha()

right_button = button.Button(380, 50, right_img, 0.07)
left_button = button.Button(40, 50, left_img, 0.07)
screen.blit(pygame.transform.scale(product_1, (250, 120)), (120, 30))
screen.blit(pygame.transform.scale(background, (900, 600)), (0, 0))
input_box1 = inputBox.InputBox(600, 400, 140, 32)
input_boxes = [input_box1]

mainloop = True
while mainloop:

    screen.blit(pygame.transform.scale(ask, (300, 150)), (550, 310))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        for box in input_boxes:
            box.handle_event(event)
    for box in input_boxes:
        box.update()
    for box in input_boxes:
        box.draw(screen)

    if right_button.draw(screen):
        screen.blit(pygame.transform.scale(product_1, (250, 120)), (120, 30))
        pygame.display.update()

    elif left_button.draw(screen):
        screen.blit(pygame.transform.scale(product_2, (250, 120)), (120, 30))
        pygame.display.update()

    pygame.display.update()


