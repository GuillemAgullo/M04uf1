#!/usr/bin/python3

import random

class Enemy:
	def __init__ (self, name, health, strength, description = ""):
		self.name = name
		self.health = int(health)
		self.strength = int(strength)
		self.description = description
		

	def show_info (self):
		print("Name: "+(self.name))
		print("TotalHealth: "+str(self.health))
		print("Strength: "+str(self.strength))
		if self.description != "":
			print("Description: "+(self.description))

	def hurt (self, damage):
		isdead = int(self.health) - int(damage)
		int(self.health) - int(damage)
		if isdead < 1:
			print("¡Lo has matado!")
			return True
		print(self.name + " se ha quedado a "+ str(isdead) +" de vida.")
		return False
	
	def attack (self, strength):
		return random.randint(0,int(self.strength))
	
	def get_health(self):
		return self.health
