#!/usr/bin/env python3

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class Spaceship(Widget):
     def on_touch_move(self,touch):
        if touch.y > 50: # Touch is above the scoreboard
            self.center_x = touch.x + self.width/4.0

class SpaceInvGame(Widget):
    ship = ObjectProperty(None)

    def update(self, dt):
        pass
    
    def fire_button_pressed(self):
        print("Fire!")

class SpaceInvApp(App):
    def build(self):
        game = SpaceInvGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    SpaceInvApp().run()