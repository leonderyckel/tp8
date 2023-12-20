#tp8 Gui
#EXERCICE 1
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
import random

class Calculatrice1(App):
    def build(self):
        self.title='Calculatrice1'
        box = BoxLayout(orientation='vertical',spacing=15,padding=15)

        self.nombre1 = TextInput(hint_text='Entrez le premier nombre', multiline=False)
        self.nombre2 = TextInput(hint_text='Entrez le deuxième nombre', multiline=False)
        box.add_widget(self.nombre1)
        box.add_widget(self.nombre2)
        box.add_widget(Button(text='Calculer', on_press=self.Somme))
        self.resultat = Label(text='Résulat')
        box.add_widget(self.resultat)
        return box


    def Somme(self,other):
        try:
            num1 = float(self.nombre1.text)
            num2 = float(self.nombre2.text)
            resultat = num1+num2
            self.resultat.text = f'Résultat de {num1} + {num2}: {resultat}'
        except ValueError :
            self.resultat.text = 'Veuillez entrer deux nombres (int)'



if __name__ == '__main__':
    Calculatrice1().run()

#Exercice2


class Calculatrice2(App):
    def build (self):

        self.title = 'Calculatrice2'
        box = BoxLayout(orientation='vertical')


        self.num1 = TextInput(hint_text='Entrez le premier nombre', multiline=False)
        box.add_widget(self.num1)
        self.num2 = TextInput(hint_text='Entrez le deuxieme nombre', multiline=False)
        box.add_widget(self.num2)

        #Checkboxes
        operations = BoxLayout(orientation='horizontal')

        # Addition
        add = BoxLayout(orientation='vertical')
        self.addition= CheckBox(group='operation', active=True)
        add.add_widget(self.addition)
        add.add_widget(Label(text='Addition'))
        operations.add_widget(add)

        # Soustraction
        sub = BoxLayout(orientation='vertical')
        self.soustraction = CheckBox(group='operation')
        sub.add_widget(self.soustraction)
        sub.add_widget(Label(text='Soustraction'))
        operations.add_widget(sub)

        # Multiplication
        mul = BoxLayout(orientation='vertical')
        self.multiplication = CheckBox(group='operation')
        mul.add_widget(self.multiplication)
        mul.add_widget(Label(text='Multiplication'))
        operations.add_widget(mul)

        # Division
        div = BoxLayout(orientation='vertical')
        self.division = CheckBox(group='operation')
        div.add_widget(self.division)
        div.add_widget(Label(text='Division'))
        operations.add_widget(div)

        box.add_widget(operations)

        # Boutton
        self.calcul_button = Button(text='Calculer', on_press=self.calculer)
        box.add_widget(self.calcul_button)

        # Afficher le résultat
        self.resultlabel = Label()
        box.add_widget(self.resultlabel)

        return box

    def calculer(self, other):
        try:
            num1 = float(self.num1.text)
            num2 = float(self.num2.text)

            if self.addition.active:
                result = num1 + num2
            elif self.soustraction.active:
                result = num1 - num2
            elif self.multiplication.active:
                result = num1 * num2
            elif self.division.active:
                result = num1 / num2

            self.resultlabel.text = f"Résultat : {result}"
        except ValueError:
            self.resultlabel.text = "Veuillez entrer deux nombres (int)"
        except ZeroDivisionError :
            self.resultlabel.text = "Division par 0 :("



if __name__ == '__main__':
    Calculatrice2().run()

#Exercice3
class Couleur(App):

    def build(self):

        self.title='Couleur'
        fenetre = GridLayout(rows=5,cols=5)
        for i in range (25):
            boutton = Button( background_normal='', background_color=(1,1,1,1))
            boutton.bind(on_press=self.Couleur)
            fenetre.add_widget(boutton)
        return fenetre
    def Couleur(self,button):

        couleurs = [[1, 2, 0, 1], [1, 2, 2, 0], [0, 2, 2, 1]]
        button.background_color = random.choice(couleurs)




if __name__ =='__main__':
    Couleur().run()