from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.graphics import Color
from kivy.animation import Animation
from kivy.uix.button import Button

from random import randint

class Character(Widget):
	dieCount = NumericProperty(None)
	health = NumericProperty(None)

	def create(self, createHealth):
		self.health = createHealth
	
	def take_damage(self, damage):
		self.health -= damage

class HealthDisplay(Widget):
	curHealth = NumericProperty(100)
	maxHealth = NumericProperty(100)

	def animate(self, instance):
		#self.curHealth += 10
		#anim = Animation(self.size(self.curHealth,50))
		anim = Animation(size(self.curHealth,50))
		anim.start(instance)


class CombatGame(Widget):
	#2 players
	player1 = ObjectProperty(None)
	player2 = ObjectProperty(None)
	player1HealthBar = ObjectProperty(None)
	player2HealthBar = ObjectProperty(None)
	
	def initialize(self):
		self.player1.health=200
		self.player2.health=200
		button = Button(size_hint=(None, None), text='plop', on_press=self.update())
		return button
		
	#def update(self, dt):
	def update(self):
		self.player1HealthBar.animate
		self.player2HealthBar.animate
		self.player1.take_damage(10)
		self.player2.take_damage(3)
		self.player1HealthBar.curHealth=self.player1.health
		self.player2HealthBar.curHealth=self.player2.health


class CombatApp(App):
	def build(self):
		game = CombatGame()
		game.initialize()
		#Clock.schedule_interval(game.update, 1.0/60.0)
		return game

if __name__ == '__main__':
	CombatApp().run()