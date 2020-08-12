# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.
from pygame import mixer
mixer.init()
mixer.music.load('music 1.mp3')
mixer.music.play()
input('\033[7mAgora você escuta ?\033[m ')
