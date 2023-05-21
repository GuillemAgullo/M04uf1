#!/usr/bin/python3

import xmltodict
from enemy_classe import Enemy
import json

class Enemies:
	def __init__(self):
		xml_file = open("enemies.xml", "r")
		enemies_tmp = xmltodict.parse(xml_file.read())
		xml_file.close()
		self.enemy_list = enemies_tmp['enemies']['enemy']
		
		self.enemies = []
		for e in self.enemy_list:
			self.enemies.append(Enemy(e["name"], e["health"], e["damage"], e["description"]))

	def json_enemies(self):
		with open("enemies_json.json", "r") as f:
			data = json.load(f)
		
		self.enemies = []

		for e in data:

			self.enemies.append(Enemy(e["name"],e["health"], e["damage"], e["description"]))
		
			
			

if __name__ == "__main__":
	enemies = Enemies()
	enemies.jsonenemies()
