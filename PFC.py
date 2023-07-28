# import keyboard

# pointsJ1 = 0
# pointsJ2 = 0
# turn = True
# newGame = True

# print("Jeux du Pierre Feuille Ciseaux")
# while newGame:
#     print("Le joueur 1 commence")

#     while pointsJ1 < 2 and pointsJ2 < 2:
#         if turn:
#             print("1 > Pierre, 2 > Feuille, 3 > Ciseaux")
#             print("Choix du joueur 1:")
#             # Attendre jusqu'à ce qu'une touche soit enfoncée
#             event = keyboard.read_event(suppress=True)
#             while event.event_type != keyboard.KEY_DOWN:
#                 event = keyboard.read_event(suppress=True)

#             choiceJ1 = event.name
#         else:
#             print("Choix du joueur 2:")
#             # Attendre jusqu'à ce qu'une touche soit enfoncée
#             event = keyboard.read_event(suppress=True)
#             while event.event_type != keyboard.KEY_DOWN:
#                 event = keyboard.read_event(suppress=True)

#             choiceJ2 = event.name
#             if choiceJ1 == "1" and choiceJ2 == "2":
#                 print("Joueur 1 à choisi Pierre")
#                 print("Joueur 2 à choisi Feuille")
#                 print("Joueur 2 remporte cette manche")
#                 pointsJ2 += 1

#             elif choiceJ1 == "1" and choiceJ2 == "3":
#                 print("Joueur 1 à choisi Pierre")
#                 print("Joueur 2 à choisi Ciseaux")
#                 print("Joueur 1 remporte cette manche")

#                 pointsJ1 += 1
#             elif choiceJ1 == "2" and choiceJ2 == "1":
#                 print("Joueur 1 à choisi Feuille")
#                 print("Joueur 2 à choisi Pierre")
#                 print("Joueur 1 remporte cette manche")

#                 pointsJ1 += 1
#             elif choiceJ1 == "2" and choiceJ2 == "3":
#                 print("Joueur 1 à choisi Feuille")
#                 print("Joueur 2 à choisi Ciseaux")
#                 print("Joueur 2 remporte cette manche")

#                 pointsJ2 += 1
#             elif choiceJ1 == "3" and choiceJ2 == "1":
#                 print("Joueur 1 à choisi Ciseaux")
#                 print("Joueur 2 à choisi Pierre")
#                 print("Joueur 2 remporte cette manche")

#                 pointsJ2 += 1
#             elif choiceJ1 == "3" and choiceJ2 == "2":
#                 print("Joueur 1 à choisi Ciseaux")
#                 print("Joueur 2 à choisi Feuille")
#                 print("Joueur 1 remporte cette manche")

#                 pointsJ1 += 1

#             print("J1: " + str(pointsJ1) + " J2: " + str(pointsJ2))
#         turn = not turn

#     if pointsJ1 == 2:
#         print("Le joueur 1 a gagné !")
#     else:
#         print("Le joueur 2 a gagné !")
    
#     playAgain = input("Voulez-vous refaire une partie? y/n")
#     if playAgain == "y":
#         pointsJ1 = 0
#         pointsJ2 = 0
#         newGame = True
#     else:
#         newGame = False

import tkinter as tk
from tkinter import messagebox
import keyboard

def play_game():
    global pointsJ1, pointsJ2, turn

    if pointsJ1 < 2 and pointsJ2 < 2:
        if turn:
            player_label.config(text="Joueur 1, c'est à toi !")
            keyboard.on_press_key("1", lambda _: handle_choice("1"))
            keyboard.on_press_key("2", lambda _: handle_choice("2"))
            keyboard.on_press_key("3", lambda _: handle_choice("3"))
        else:
            player_label.config(text="Joueur 2, c'est à toi !")
            keyboard.on_press_key("1", lambda _: handle_choice("1"))
            keyboard.on_press_key("2", lambda _: handle_choice("2"))
            keyboard.on_press_key("3", lambda _: handle_choice("3"))

def handle_choice(choice):
    global pointsJ1, pointsJ2, turn, choiceJ1, choiceJ2

    if turn:
        choiceJ1 = choice
    else:
        choiceJ2 = choice
        if choiceJ1 == "1" and choiceJ2 == "2":
            print("Joueur 1 à choisi Pierre")
            print("Joueur 2 à choisi Feuille")
            print("Joueur 2 remporte cette manche")
            pointsJ2 += 1
        elif choiceJ1 == "1" and choiceJ2 == "3":
            print("Joueur 1 à choisi Pierre")
            print("Joueur 2 à choisi Ciseaux")
            print("Joueur 1 remporte cette manche")
            pointsJ1 += 1
        elif choiceJ1 == "2" and choiceJ2 == "1":
            print("Joueur 1 à choisi Feuille")
            print("Joueur 2 à choisi Pierre")
            print("Joueur 1 remporte cette manche")
            pointsJ1 += 1
        elif choiceJ1 == "2" and choiceJ2 == "3":
            print("Joueur 1 à choisi Feuille")
            print("Joueur 2 à choisi Ciseaux")
            print("Joueur 2 remporte cette manche")
            pointsJ2 += 1
        elif choiceJ1 == "3" and choiceJ2 == "1":
            print("Joueur 1 à choisi Ciseaux")
            print("Joueur 2 à choisi Pierre")
            print("Joueur 2 remporte cette manche")
            pointsJ2 += 1
        elif choiceJ1 == "3" and choiceJ2 == "2":
            print("Joueur 1 à choisi Ciseaux")
            print("Joueur 2 à choisi Feuille")
            print("Joueur 1 remporte cette manche")
            pointsJ1 += 1
        print("J1: " + str(pointsJ1) + " J2: " + str(pointsJ2))

    turn = not turn
    play_game()

def check_winner():
    global pointsJ1, pointsJ2

    if pointsJ1 == 2:
        messagebox.showinfo("Résultat", "Le joueur 1 a gagné !")
    elif pointsJ2 == 2:
        messagebox.showinfo("Résultat", "Le joueur 2 a gagné !")
    else:
        if messagebox.askyesno("Nouvelle partie", "Voulez-vous refaire une partie?"):
            pointsJ1 = 0
            pointsJ2 = 0
            turn = True
            play_game()
        else:
            root.destroy()

# Initialisation des variables
pointsJ1 = 0
pointsJ2 = 0
turn = True

# Création de la fenêtre principale
root = tk.Tk()
root.minsize(1000, 800)
root.title("Jeux du Pierre Feuille Ciseaux")

# Étiquette pour afficher le joueur actuel
player_label = tk.Label(root, text="Le joueur 1 commence", font=("Arial", 14))
player_label.pack(pady=10)

# Bouton pour commencer la partie
start_button = tk.Button(root, text="Commencer la partie", command=play_game)
start_button.pack()

# Appel périodique de check_winner toutes les 100 millisecondes
# root.after(100, check_winner)

root.mainloop()

