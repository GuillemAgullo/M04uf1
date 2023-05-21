#!/usr/bin/python3
from player_classe import Player
from enemies_classe import Enemies


player = Player("serdo","23","34","3","45")
enemies = Enemies()


from player_classe import Player
from enemies_classe import Enemies

player = Player("serdo", 23, 34, 3, 45)
enemies = Enemies()

def game():
    salir = False
    index = 0
    enemy = enemies.enemies[index]
    while not salir:
        print("Te ataca un enemigo")
        enemies.enemies[index].show_info()
        print("")
        print("Que quieres hacer?")
        print("a -> atacar")
        print("n -> nada")
        print("g -> guardar juego y salir")

        election = input(">>>").lower()

        if election == "a":
            damagedone = player.attack(player.strength)
            print("Has hecho " + str(damagedone) + " de daño al enemigo!!!")
            enemydead = enemy.hurt(damagedone)
            
            if enemydead == False:
                enemydmg = enemy.attack(enemy.strength)
                isplayerdead = player.hurt(enemydmg)
                
                if isplayerdead == True:
                    print("FIN DEL JUEGO SAD ENDING.")
                    salir = True
            
            elif enemydead == True and index != len(enemies.enemies) - 1: 
                index = index + 1
            
            elif enemydead == True and index >= len(enemies.enemies) - 1:
                index = 4
                print("GANASTE el juego!!! GOOD ENDING: VIVA VIM!!!")
                break
        
        elif election == "n":
            enemydmg = enemy.attack(enemy.strength)
            isplayerdead = player.hurt(enemydmg)
            
            if isplayerdead:
                print("FIN DEL JUEGO SAD ENDING.")
                salir = True
        
        elif election == "g":
            return

        
    salir = False
    index = 0 
    enemies.json_enemies()
    enemy = enemies.enemies[index] 
    while not salir:
        enemies.enemies[index].show_info()
        print("")
        print("Has derrotado todos los enemigos guardados en archivos xml. Ahora te toca los de json.")
        print("")
       
        print("Que quieres hacer?")
        print("a -> atacar")
        print("n -> nada")
        print("g -> guardar juego y salir")
        
        election = input(">>>").lower()


        if election == "a":

            damagedone = player.attack(player.strength)
            print("Has hecho "+ str(damagedone) +" de daño al enemigo!!!")
            enemydead = enemy.hurt(damagedone)
            if enemydead == False:
                enemydmg = enemy.attack(enemy.strength)
                isplayerdead = player.hurt(enemydmg)
                if isplayerdead == True:
                    print("FIN DEL JUEGO SAD ENDING.")
                    salir = True
            elif enemydead == True and index != len(enemies.enemies) -1: 
                index = index + 1
            elif enemydead == True and index >= len(enemies.enemies) -1:
                index = 4
                print("GANASTE el juego!!! GOOD ENDING: VIVA VIM!!!")
                break        
        elif election == "n":
            enemydmg = enemy.attack(enemy.strength)
            isplayerdead = player.hurt(enemydmg)
            if isplayerdead:
                print("FIN DEL JUEGO SAD ENDING.")
                salir = True
        elif election == "g":
            return



if __name__ == "__main__":
    title="""                               
  _ __   __ _ _ __   ___  _   _ ___  ___ _ __ ___   ___  __ _ 
 | '_ \ / _` | '_ \ / _ \| | | / __|/ _ \ '__/ __| / __|/ _` |
 | | | | (_| | | | | (_) | |_| \__ \  __/ |  \__ \_\__ \ (_| |
 |_| |_|\__,_|_| |_|\___/ \__,_|___/\___|_|  |___(_)___/\__,_|""".strip()
    print(title)

    opc = ""
    while opc!="s":
        print("1.- Juego nuevo")
        print("2.- Cargar juego (xml)")
        print("3.- Cargar juego (json)")
        print("S.- Salir")

        opc = input("Introduce una opción: ").lower()

        if opc == "1":
            player_info = player.input_info()
            player_export = {
                "player_save": {
					"player": player_info
				}
            }
            player.write_info(player_export)
            player.save_json(player_info, "player_json.json")
            
            game()

        if opc == "2":
            print("Personatge que tenies guardat:")
            player.read_info()
            player.show_info()
            game()
        
        if opc == "3":
            print("personatge que teníes guardat: ")
            player.read_info_json()
            player.show_info()
            game()