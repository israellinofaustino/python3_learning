import pygame


pygame.init()
pygame.display.set_mode((200, 100))
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
