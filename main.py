# This is a sample Python script.

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from pygments.styles import arduino

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.button import Label

# Importing Libraries
#import serial
import time


# Inherit Kivy's App class which represents the window
# for our widgets
# HelloKivy inherits all the fields and methods
# from Kivy
#def add_widget(checkBox):
#    pass


class HelloKivy(App):
    #arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
    # This returns the content we want in the window
    print(arduino)

    def build(self):
        b = BoxLayout(orientation='vertical')

        # Adding the text input
        t = TextInput(font_size=18,
                      size_hint_y=None,
                      height=35)

        #checkBox = CheckBox(active = True)


        f = FloatLayout()

        # By this you are able to move the
        # Text on the screen to anywhere you want
        s = Scatter()

        l = Label(text="Oh Hi, Hello There!",
                  font_size=50)

        b.add_widget(s)
        b.add_widget(l)

        #b.add_widget(t)
        #b.add_widget(checkBox)
        #b.add_widget(f)

        # Binding it with the label
        t.bind(text=l.setter('text'))

        return b


'''
    def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        time.sleep(0.05)
        data = arduino.readline()
        Label(text=data)

    while True:
        num = input("Enter a number: ") # Taking input from user
        write_read(num)
        #print(value) # printing the value
'''

# Run the App
#if __name__ == "__main__":
HelloKivy().run()
# or just use the code below
# helloKivy = HelloKivy()
# helloKivy.run()
