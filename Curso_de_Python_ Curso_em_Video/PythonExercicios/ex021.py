#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.initi()
pygame.mixer.music.load()
pygame.mixer.music.play()
pygame.event.wait()