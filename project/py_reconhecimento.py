from kivy.uix.screenmanager import Screen
import os

class TReconhecimento(Screen):
    def eigen(self):
        os.system('python C:/Users/larissa.siqueira/Documents/recognitionfacial/project/script/eigen.py') # Editar o caminho de acordo com o clone na máquina
