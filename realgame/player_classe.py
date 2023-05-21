#!/usr/bin/python3
import xmltodict
import random
import json

class Player:
	def __init__ (self, name="", health=100, strength=10, level=1, xp=0):
			self.name = name
			self.health = health
			self.strength = strength
			self.level = level
			self.xp = xp

	def input_info(self):
		self.name=input("Dime tu nombre: ")
		self.health=input("Dime tu vida: ")
		self.strength=input("Dime fuerza: ")
		self.level=input("Dime tu nivel: ")
		self.xp=input("Dime tu cantidad de experiencia: ")
		
		return{
		"name": self.name,
		"health": self.health,
		"strength": self.strength,
		"level": self.level,
		"xp": self.xp
		}
	def save_json(self,datos,nombre_archivo):
		with open(nombre_archivo, "w") as archivo:
			json.dump(datos, archivo)
	
	def write_info(self, export):
		player_xml = xmltodict.unparse(export, pretty=True)
		print(player_xml)
		f = open("player_xml", "w")
		f.write(player_xml)

		f.close()

	def read_info (self):
		xml_file=open("player_xml", "r")
		player_tmp=xmltodict.parse(xml_file.read())
		info=player_tmp["player_save"]["player"]
		self.name = info["name"]
		self.health = info["health"]
		self.strength = info["strength"]
		self.level = info["level"]
		self.xp = info["xp"]
	
	def read_info_json(self):
		json_file=open("player_json.json", "r")
		data =json.load(json_file)
		json_file.close()
		self.name = data["name"]
		self.health = data["health"]
		self.strength = data["strength"]
		self.level = data["level"]
		self.xp = data["xp"]
		
	def show_info (self):
		print("Name: "+str(self.name))
		print("Health: "+str(self.health))
		print("Strength: "+str(self.strength))
		print("Level: "+str(self.level))
		print("XP: "+str(self.xp))

	def attack (self, strength):
		return random.randint(0,int(self.strength))
	
	def hurt (self, damage):
		print("El enemigo te ataca con "+ str(damage) + " de daño!!")
		print("")
		isdead = int(self.health) - int(damage) 
		int(self.health) - int(damage)
		if isdead < 1:
			print("Te mataron papu. :(")
			return True
		else:
			return False

