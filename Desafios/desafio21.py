#Adicionar uma música
from pygame import mixer 
mixer.init()
mixer.music.load('C:\\Users\\paulo\\OneDrive\\Área de Trabalho\\Estudos\\Python\\Desafios\\mdesafio.mp3')
mixer.music.play()