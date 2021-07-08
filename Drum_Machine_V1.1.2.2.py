"""						   DillaDrummer
		Designed by Evan Scallan - 2021. All Rights Reserved.
	Drum Sample Credit: STLNDRM X Soul Surplus // One for Dilla (Sample Pack)
"""
#module imports
from tkinter import *
import pygame
from pygame.locals import *

#creates GUI
root = Tk()
root.title('Drum Machine V1.0')
root.geometry('400x125')

#initialize pygame, mixer
pygame.init()
pygame.mixer.init()

#channel setup for multiple sounds at same time
pygame.mixer.set_num_channels(6)

"""
---------------INSTRUMENTS/SAMPLES---------------
"""

#SNARES
def snare1():
	pygame.mixer.Channel(0).play(pygame.mixer.Sound(
		"DILLA_SNARE_1.wav"
		))

snare1_button = Button(root, text="Snare 1", font=("Futura", 32),command=snare1)
snare1_button.grid(row=1, column=0)


def snare2():
	pygame.mixer.Channel(1).play(pygame.mixer.Sound(
		"DILLA_SNARE_2.wav"
		))

snare2_button = Button(root, text="Snare 2", font=("Futura", 32),command=snare2)
snare2_button.grid(row=2, column=0)

#KICKS
def kick1():
	pygame.mixer.Channel(2).play(pygame.mixer.Sound(
		"DILLA_KICK_1.wav"
		))

kick1_button = Button(root, text="Kick 1", font=("Futura", 32), command=kick1)
kick1_button.grid(row=1, column=1)

def kick2():
	pygame.mixer.Channel(3).play(pygame.mixer.Sound(
		"DILLA_KICK_2.wav"
		))

kick2_button = Button(root, text="Kick 2", font=("Futura", 32),command=kick2)
kick2_button.grid(row=2, column=1)


#HIHATS
def hat1():
	pygame.mixer.Channel(4).play(pygame.mixer.Sound(
		"DILLA_HAT_1.wav"
		))

hat1_button = Button(root, text="Hat 1", font=("Futura", 32),command=hat1)
hat1_button.grid(row=1, column=2)


def hat2():
	pygame.mixer.Channel(5).play(pygame.mixer.Sound(
		"DILLA_HAT_2.wav"
		))

hat2_button = Button(root, text="Hat 2", font=("Futura", 32),command=hat2)
hat2_button.grid(row=2, column=2)

#MAC OS KEYBOARD MAPPINGS
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit();
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_1:
				kick1()
			if event.key == pygame.K_2:
				kick2()
			if event.key == pygame.K_3:
				snare1()
			if event.key == pygame.K_4:
				snare2()
			if event.key == pygame.K_5:
				hat1()
			if event.key == pygame.K_6:
				hat2()
		
#executes GUI for DillaDrummer
mainloop()
