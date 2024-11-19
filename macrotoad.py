import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController  # On prend Key et Controller et on les utilise sous la variable KeyboardController
from pynput.mouse import Button, Controller as MouseController  # Idem pour MouseController
import tkinter as tk
import time
import threading  # Permet d'exécuter la macro dans un thread séparé
import webbrowser # Help window "skytoad GitHub"
from PIL import ImageGrab

# Fenêtre principale
window = tk.Tk()
window.title("Macros")

'''
VARIABLES 
'''
# Contrôleurs souris et clavier
keyboard_controller = KeyboardController()
mouse_controller = MouseController()

# État de la macro
macro_running = False  # True si la macro est active
macro_paused = False  # True si la macro est en pause
repetition = 0

# Thread pour exécuter la macro
macro_thread = None


# MACRO NETHER WARTH
def macro_nether_wart():
    """
    Exécute la macro "Nether Wart".
    Comprend des allers-retours automatisés et gère les pauses via une touche.
    """
    global macro_running, macro_paused, repetition

    # Actions pour la macro : Clics et appuis de touches avec durée
    actions = [
        ("key", "q", 121),  # Appuie sur 'q' pendant 121 secondes
        ("key", "d", 121),  # Appuie sur 'd' pendant 121 secondes
        ("key", "q", 121),  # Appuie sur 'q' pendant 121 secondes
        ("key", "d", 121),  # Appuie sur 'd' pendant 121 secondes
        ("key", "q", 125),  # Appuie sur 'q' pendant 121 secondes
    ]

    print("Démarrage de la macro Nether Wart.")
    macro_running = True
    was_paused = False  # Variable pour détecter les changements d'état de pause

    mouse_controller.press(Button.left)  # Démarrage du clic gauche continu

    while macro_running:
        for action_type, key, duration in actions:
            if not macro_running:  # Vérifie si la macro doit s'arrêter
                print("Macro arrêtée.")
                break

            # Vérifie la pause avant chaque action
            while macro_paused:
                if not was_paused:  # Affiche une seule fois quand on passe en pause
                    print("Macro en pause... (Appuyez sur F8 pour reprendre)")
                    was_paused = True
                time.sleep(0.1)

            if was_paused:  # Si la macro reprend après une pause
                print("Reprise de la macro.")
                was_paused = False
                mouse_controller.press(Button.left)  # Reprend le clic gauche continu après la pause

            if not macro_running:  # Double vérification pour arrêter proprement
                print("Macro arrêtée après pause.")
                break

            # Exécution des actions
            if action_type == "key":  # Appuyer sur une touche
                keyboard_controller.press(key)

                # Boucle pour maintenir la touche appuyée tout en vérifiant les pauses/arrêts
                start_time = time.time()
                elapsed_time = 0  # Variable pour suivre le temps écoulé
                time_spent_during_action = 0  # Temps déjà passé de l'action avant la pause

                while elapsed_time < duration:
                    if not macro_running:  # Arrêt immédiat si nécessaire
                        print("Macro arrêtée en cours d'exécution.")
                        break

                    if macro_paused:  # Gestion de la pause pendant l'action
                        keyboard_controller.release(key)  # Libère la touche en cas de pause
                        mouse_controller.release(Button.left)  # Libère le clic gauche en pause
                        pause_start_time = time.time()  # Moment où la pause commence

                        while macro_paused:
                            if not was_paused:
                                print("Macro en pause... (durée en cours)")
                                was_paused = True
                            time.sleep(0.1)

                        if not macro_running:  # Vérifie si la macro est arrêtée après la pause
                            print("Macro arrêtée après pause.")
                            break

                        # Calculer le temps de pause
                        pause_duration = time.time() - pause_start_time
                        time_spent_during_action += pause_duration  # Ajoute le temps de pause au temps écoulé

                        keyboard_controller.press(key)  # Reprend la pression de la touche
                        mouse_controller.press(Button.left)  # Reprend le clic gauche
                    else:
                        elapsed_time = time.time() - start_time - time_spent_during_action  # Soustraction du temps passé en pause

                    time.sleep(0.1)  # Petite attente pour éviter une charge CPU élevée

                keyboard_controller.release(key)

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    mouse_controller.release(Button.left)  # Arrêt du clic gauche continu
    macro_running = False
    print(f"Macro Nether Wart terminée. Total de répétitions : {repetition}")
    repetition = 0

# MACRO PUMPKIN
def macro_pumpkin():
    global macro_running, macro_paused, repetition

    # Actions pour la macro : Clics et appuis de touches avec durée
    actions = [
        ("key", "q", 74),          # Appuie sur 'q' pendant 74 secondes
        ("key", "d", 74),          # Appuie sur 'd' pendant 74 secondes
        ("key", "q", 74),          # Appuie sur 'q' pendant 74 secondes
        ("key", "z", 2),           # Appuie sur 'z' pendant 2 secondes
    ]

    print("Démarrage de la macro Pumpkin.")
    macro_running = True

    mouse_controller.press(Button.left)  # Démarrage du clic gauche continu

    was_paused = False  # Variable pour détecter les changements d'état de pause

    while macro_running:
        for action_type, key, duration in actions:
            if not macro_running:  # Vérifie si la macro doit s'arrêter
                print("Macro arrêtée.")
                break

            # Vérifie la pause avant chaque action
            while macro_paused:
                if not was_paused:  # Affiche une seule fois quand on passe en pause
                    print("Macro en pause... (Appuyez sur F8 pour reprendre)")
                    mouse_controller.release(Button.left)  # Relâche le clic pendant la pause
                    was_paused = True
                time.sleep(0.1)

            if was_paused:  # Si la macro reprend après une pause
                print("Reprise de la macro.")
                mouse_controller.press(Button.left)  # Relance le clic continu
                was_paused = False

            if not macro_running:  # Double vérification pour arrêter proprement
                print("Macro arrêtée après pause.")
                break

            # Exécution des actions
            if action_type == "key":  # Appuyer sur une touche
                keyboard_controller.press(key)

                # Boucle pour maintenir la touche appuyée tout en vérifiant les pauses/arrêts
                start_time = time.time()
                elapsed_time = 0  # Variable pour suivre le temps écoulé
                time_spent_during_action = 0  # Temps déjà passé de l'action avant la pause

                while elapsed_time < duration:
                    if not macro_running:  # Arrêt immédiat si nécessaire
                        print("Macro arrêtée en cours d'exécution.")
                        break

                    if macro_paused:  # Gestion de la pause pendant l'action
                        keyboard_controller.release(key)  # Libère la touche en cas de pause
                        mouse_controller.release(Button.left)  # Libère le clic gauche en pause
                        pause_start_time = time.time()  # Moment où la pause commence

                        while macro_paused:
                            if not was_paused:
                                print("Macro en pause... (durée en cours)")
                                was_paused = True
                            time.sleep(0.1)

                        if not macro_running:  # Vérifie l'arrêt après la pause
                            print("Macro arrêtée après pause.")
                            break

                        # Calculer le temps de pause
                        pause_duration = time.time() - pause_start_time
                        time_spent_during_action += pause_duration  # Ajoute le temps de pause au temps écoulé

                        keyboard_controller.press(key)  # Reprend la pression de la touche
                        mouse_controller.press(Button.left)  # Reprend le clic gauche
                    else:
                        elapsed_time = time.time() - start_time - time_spent_during_action  # Soustraction du temps passé en pause

                    time.sleep(0.1)  # Petite attente pour éviter une charge CPU élevée

                keyboard_controller.release(key)

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    mouse_controller.release(Button.left)  # Arrêt du clic gauche continu
    macro_running = False
    print(f"Macro Pumpkin terminée. {repetition}")
    repetition = 0

# MACRO MELON
def macro_melon():
    global macro_running, macro_paused, repetition

    # Actions pour la macro : Clics et appuis de touches avec durée
    actions = [
        ("key", "d", 73),          # Appuie sur 'd' pendant 73 secondes
        ("key", "q", 73),          # Appuie sur 'q' pendant 73 secondes
        ("key", "d", 73),          # Appuie sur 'd' pendant 73 secondes
        ("key", "q", 73),          # Appuie sur 'q' pendant 73 secondes
        ("key", "d", 73),          # Appuie sur 'd' pendant 73 secondes
    ]

    print("Démarrage de la macro Melon.")
    macro_running = True

    mouse_controller.press(Button.left)  # Démarrage du clic gauche continu

    was_paused = False  # Variable pour détecter les changements d'état de pause

    while macro_running:
        for action_type, key, duration in actions:
            if not macro_running:  # Vérifie si la macro doit s'arrêter
                print("Macro arrêtée.")
                break

            # Vérifie la pause avant chaque action
            while macro_paused:
                if not was_paused:  # Affiche une seule fois quand on passe en pause
                    print("Macro en pause... (Appuyez sur F8 pour reprendre)")
                    mouse_controller.release(Button.left)  # Relâche le clic pendant la pause
                    was_paused = True
                time.sleep(0.1)

            if was_paused:  # Si la macro reprend après une pause
                print("Reprise de la macro.")
                mouse_controller.press(Button.left)  # Relance le clic continu
                was_paused = False

            if not macro_running:  # Double vérification pour arrêter proprement
                print("Macro arrêtée après pause.")
                break

            # Exécution des actions
            if action_type == "key":  # Appuyer sur une touche
                keyboard_controller.press(key)

                # Boucle pour maintenir la touche appuyée tout en vérifiant les pauses/arrêts
                start_time = time.time()
                elapsed_time = 0  # Variable pour suivre le temps écoulé
                time_spent_during_action = 0  # Temps déjà passé de l'action avant la pause

                while elapsed_time < duration:
                    if not macro_running:  # Arrêt immédiat si nécessaire
                        print("Macro arrêtée en cours d'exécution.")
                        break

                    if macro_paused:  # Gestion de la pause pendant l'action
                        keyboard_controller.release(key)  # Libère la touche en cas de pause
                        mouse_controller.release(Button.left)  # Libère le clic gauche en pause
                        pause_start_time = time.time()  # Moment où la pause commence

                        while macro_paused:
                            if not was_paused:
                                print("Macro en pause... (durée en cours)")
                                was_paused = True
                            time.sleep(0.1)

                        if not macro_running:  # Vérifie l'arrêt après la pause
                            print("Macro arrêtée après pause.")
                            break

                        # Calculer le temps de pause
                        pause_duration = time.time() - pause_start_time
                        time_spent_during_action += pause_duration  # Ajoute le temps de pause au temps écoulé

                        keyboard_controller.press(key)  # Reprend la pression de la touche
                        mouse_controller.press(Button.left)  # Reprend le clic gauche
                    else:
                        elapsed_time = time.time() - start_time - time_spent_during_action  # Soustraction du temps passé en pause

                    time.sleep(0.1)  # Petite attente pour éviter une charge CPU élevée

                keyboard_controller.release(key)

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    mouse_controller.release(Button.left)  # Arrêt du clic gauche continu
    macro_running = False
    print(f"Macro Melon terminée. {repetition}")
    repetition = 0

# MACRO ACACIA
def macro_acacia():
    global macro_running, macro_paused, repetition

    # Initialisation
    was_paused = False
    current_inventory_slot = 0  # Index de l'inventaire
    inventory_list = [("é", '"'), ("'", "("), ("-", "è")]  # Paires d'éléments à utiliser

    print("Démarrage de la macro Acacia.")
    macro_running = True

    while macro_running:
        # Sélectionne la paire courante dans l'inventaire
        element1, element2 = inventory_list[current_inventory_slot]
        print(f"Utilisation des éléments : {element1} et {element2}")
        current_inventory_slot = (current_inventory_slot + 1) % len(inventory_list)

        # Actions pour la paire actuelle
        actions = [
            ("press", element1, 0.15),  # Appuie sur le premier élément de la paire
            ("mouse", "right", 0.75),  # Clic droit
            ("press", element2, 0.15),  # Appuie sur le second élément de la paire
            ("mouse", "right", 0.75),  # Clic droit
            ("key", "&", 0.15),  # Appuie sur '&'
            ("mouse", "left", 0.3),  # Clic gauche
            (None, None, 0.2),  # Pause sans action
        ]

        for action in actions:
            if not macro_running:  # Vérifie si la macro doit s'arrêter
                print("Macro arrêtée.")
                break

            # Pause
            while macro_paused:
                if not was_paused:
                    print("Macro en pause... (durée en cours)")
                    was_paused = True
                time.sleep(0.1)

                if not macro_running:  # Arrêt après une pause
                    print("Macro arrêtée après pause.")
                    return

            if was_paused:  # Reprise après pause
                print("Reprise de la macro.")
                was_paused = False

            # Exécution des actions
            if action[0] == "press":  # Appuie sur un élément de l'inventaire
                keyboard_controller.press(action[1])
                time.sleep(action[2])
                keyboard_controller.release(action[1])

            elif action[0] == "key":  # Appuie sur une touche spécifique
                keyboard_controller.press(action[1])
                time.sleep(action[2])
                keyboard_controller.release(action[1])

            elif action[0] == "mouse":  # Clic de souris (gauche/droit)
                if action[1] == "left":
                    mouse_controller.press(Button.left)
                    time.sleep(action[2])
                    mouse_controller.release(Button.left)
                elif action[1] == "right":
                    mouse_controller.press(Button.right)
                    time.sleep(action[2])
                    mouse_controller.release(Button.right)

            elif action[0] is None:  # Pause sans action
                time.sleep(action[2])

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    macro_running = False
    print(f"Macro Acacia terminée. Total de répétitions : {repetition}")
    repetition = 0

# MACRO DARK OAK 
def macro_dark_oak():
    global macro_running, macro_paused, repetition

    # Initialisation
    was_paused = False
    current_inventory_slot = 0  # Index de l'inventaire
    inventory_list = ['"', "'", "(", "-"]  # Éléments de l'inventaire

    # Actions pour la macro
    actions = [
        ("press", None, 0.15),  # Appuie sur un élément de l'inventaire
        ("mouse", "right", 0.75),  # Clic droit
        ("key", "d", 0.4),  # Appuie sur 'd'
        ("press", None, 0.15),  # Appuie sur un autre élément de l'inventaire
        ("mouse", "right", 0.75),  # Clic droit
        ("key", "q", 0.5),  # Appuie sur 'q'
        ("key", "è", 0.2),  # Appuie sur 'è'
        ("mouse", "right", 0.75),  # Clic droit
        ("key", "é", 0.15),  # Appuie sur 'é'
        ("mouse", "left", 0.3),  # Clic gauche
        (None, None, 0.2),  # Pause sans action
    ]

    print("Démarrage de la macro Dark Oak.")
    macro_running = True

    while macro_running:
        # Change l'élément sélectionné dans l'inventaire
        element = inventory_list[current_inventory_slot]
        print(f"Changement d'élément dans l'inventaire : {element}")
        current_inventory_slot = (current_inventory_slot + 1) % len(inventory_list)

        for action in actions:
            if not macro_running:  # Vérifie si la macro doit s'arrêter
                print("Macro arrêtée.")
                break

            # Pause
            while macro_paused:
                if not was_paused:
                    print("Macro en pause... (durée en cours)")
                    was_paused = True
                time.sleep(0.1)

                if not macro_running:  # Arrêt après une pause
                    print("Macro arrêtée après pause.")
                    return

            if was_paused:  # Reprise après pause
                print("Reprise de la macro.")
                was_paused = False

            # Exécution des actions
            if action[0] == "press" and element is not None:  # Appuie sur un élément de l'inventaire
                keyboard_controller.press(element)
                time.sleep(action[2])
                keyboard_controller.release(element)

            elif action[0] == "key":  # Appuie sur une touche spécifique
                keyboard_controller.press(action[1])
                time.sleep(action[2])
                keyboard_controller.release(action[1])

            elif action[0] == "mouse":  # Clic de souris (gauche/droit)
                if action[1] == "left":
                    mouse_controller.press(Button.left)
                    time.sleep(action[2])
                    mouse_controller.release(Button.left)
                elif action[1] == "right":
                    mouse_controller.press(Button.right)
                    time.sleep(action[2])
                    mouse_controller.release(Button.right)

            elif action[0] is None:  # Pause sans action
                time.sleep(action[2])

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    macro_running = False
    print(f"Macro Dark Oak terminée. Total de répétitions : {repetition}")
    repetition = 0


'''
FISHING 
'''

# Zone de surveillance pour la couleur verte
zone_surveillance = (760, 340, 400, 400)  # Une zone de 400x400 pixels autour du centre de l'écran

# Fonction pour détecter un pixel avec une tolérance sur les couleurs
def detecter_pixel_vert(zone, tolerance=10):
    screenshot = pyautogui.screenshot(region=zone)  # Capture de la zone spécifiée
    couleur_cible = (86, 255, 86)  # La couleur verte cible

    for x in range(screenshot.width):
        for y in range(screenshot.height):
            pixel = screenshot.getpixel((x, y))

            # Comparaison avec la tolérance
            if all(abs(pixel[i] - couleur_cible[i]) <= tolerance for i in range(3)):
                return True

    return False

# Fonction pour démarrer la macro de la pêche (sans pause interne)
def macro_trophy_fishing():
    global macro_running, macro_paused

    actions = [
        # Action 1: lancer la ligne (clic droit)
        {"action": "clic_droit", "delay": 0.12},
        # Action 2: attendre le message en vert
        {"action": "attendre_message_vert", "delay": 0.14},  # Attendre le message sans délai max
        # Action 3: récupérer la canne à pêche (clic droit)
        {"action": "clic_droit", "delay": 0.14},
    ]

    print("Démarrage de la macro de pêche.")
    macro_running = True

    while macro_running:
        for action in actions:
            if action["action"] == "clic_droit":
                pyautogui.mouseDown(button='right')  # press
                pyautogui.mouseUp(button='right')    # release
                time.sleep(action["delay"]) 
            elif action["action"] == "attendre_message_vert":
                pixel_detected = False  # Booléen pour savoir si le pixel vert est détecté
                start_time = time.time()

                while not pixel_detected:  # Tant que le pixel n'est pas détecté
                    if detecter_pixel_vert(zone_surveillance):  # Vérification du pixel vert
                        print("Message détecté, reprise de la canne à pêche.")
                        pixel_detected = True  # Pixel trouvé, on arrête la recherche
                    if macro_paused:  
                        print("Macro en pause. Appuyez sur F8 pour reprendre.")
                        while macro_paused:
                            time.sleep(0.2)  # Attente active pendant la pause
                    time.sleep(0.1)  # Petite attente pour éviter une charge CPU excessive

                # On sort de la boucle dès que le pixel est détecté
                # Pas de délai max ici, la boucle attendra indéfiniment jusqu'à détection
                print(f"Message vert détecté après {time.time() - start_time:.2f} secondes.")
                # La macro continue avec l'action suivante

            # La macro continue sans relancer un clic droit non désiré
            if not macro_running:
                break

    macro_running = False
    print("Macro de Trophy Fishing terminée.")

# Fonction pour démarrer une macro dans un thread séparé 
def start_macro_thread():
    global macro_thread, macro_running

    if macro_running:
        print("Une macro est déjà en cours d'exécution.")
        return

    # Sélectionne la macro à exécuter ( si on coche une case False devient True )
    if btn_farm_var.get():
        macro_thread = threading.Thread(target=macro_nether_wart)
    elif btn_dark_oak_var.get():
        macro_thread = threading.Thread(target=macro_dark_oak)
    elif btn_farm2_var.get():
        macro_thread = threading.Thread(target=macro_pumpkin)
    elif btn_farm3_var.get():
        macro_thread = threading.Thread(target=macro_melon)
    elif btn_acacia_var.get():
        macro_thread = threading.Thread(target=macro_acacia)
    elif btn_tr_fishing_var.get():
        macro_thread = threading.Thread(target=macro_trophy_fishing)
    else:
        print("Aucune macro sélectionnée.")
        return

    # Démarre le thread
    macro_thread.start()

# Gestion des touches pour pause/reprise et arrêt
'''
Fonction pour gérer les touches de pause, reprise, et arrêt
'''
def on_press(key):
    global macro_running, macro_paused, macro_thread

    try:
        if key == Key.f5:  # Démarre ou reprend la macro
            if not macro_running:  # Si la macro n'est pas déjà en cours d'exécution
                print("F5 pressée : démarrage de la macro.")
                start_macro_thread()  # Démarre la macro sélectionnée
            else:
                print("F5 pressée : reprise de la macro.")
                macro_paused = False  # Reprend la macro si elle est en pause

        elif key == Key.f8:  # Met en pause ou reprend la macro
            if macro_running:  # Si la macro est en cours
                macro_paused = not macro_paused  # Change l'état de la pause
                print("Macro en pause." if macro_paused else "Macro reprise.")
            else:
                print("Aucune macro en cours pour mettre en pause/reprendre.")

        elif key == Key.f3:  # Arrête complètement la macro
            if macro_running:  # Si une macro est en cours
                print("F3 pressée : arrêt complet de la macro.")
                macro_running = False  # Arrête la macro
                if macro_thread is not None:  # Si le thread existe, on l'arrête proprement
                    macro_thread.join()  # Attendre que le thread termine avant de continuer
                print("Macro arrêtée.")
            else:
                print("Aucune macro en cours à arrêter.")

    except Exception as e:
        print(f"Erreur : {e}")


# Écouteur pour gérer les touches globales ( après la fonction on_press sinon c po cool )
listener = keyboard.Listener(on_press=on_press)
listener.start()
'''
CUSTOMISATION + BUTTONS 
Farming 
'''
# Définir une police et une taille
font_large = ("Arial", 16)  # Police Arial, taille 16
font_title = ("Helvetica", 20, "bold")  # Police Helvetica, taille 20, en gras
font_category = ("New Romance", 13)

# Texte principal avec une police grande 
title_label = tk.Label(window, text="Bienvenue dans l'interface", font=font_title) 
title_label.pack(pady=10)

''' le label et Label ne sont pas les memes : un pour le nom de la variable qui contient le titre l'autre pour le texte '''

title_category = tk.Label(window, text="---------------------------Farming---------------------------", font=font_category) 
title_category.pack()

# Checkbuttons avec texte agrandi
btn_farm_var = tk.BooleanVar()
btn_farm = tk.Checkbutton(window, text="Nether Wart Macro", variable=btn_farm_var, font=font_large)
btn_farm.pack()


btn_farm2_var = tk.BooleanVar()
btn_farm2 = tk.Checkbutton(window, text="Pumpkin Macro", variable=btn_farm2_var, font=font_large)
btn_farm2.pack()

btn_farm3_var = tk.BooleanVar()  # Variable associée à la case "Melon Macro"
btn_farm3 = tk.Checkbutton(window, text="Melon Macro / opti farm", variable=btn_farm3_var, font=font_large)
btn_farm3.pack()

'''
Foraging 
'''

title_category = tk.Label(window, text="---------------------------Foraging---------------------------", font=font_category) 
title_category.pack()

btn_dark_oak_var = tk.BooleanVar()
btn_dark_oak = tk.Checkbutton(window, text="Dark Oak Macro", variable=btn_dark_oak_var, font=font_large)
btn_dark_oak.pack()

btn_acacia_var = tk.BooleanVar()
btn_acacia = tk.Checkbutton(window, text="Acacia Macro", variable=btn_acacia_var, font=font_large)
btn_acacia.pack()

'''
Mining
'''
title_category = tk.Label(window, text="---------------------------Fishing---------------------------", font=font_category) 
title_category.pack()

btn_tr_fishing_var = tk.BooleanVar()
btn_tr_fishing = tk.Checkbutton(window, text="Trophy Fishing Macro", variable=btn_tr_fishing_var, font=font_large)
btn_tr_fishing.pack()

'''
ENCHANTING
'''
title_category = tk.Label(window, text="---------------------------Enchanting---------------------------", font=font_category) 
title_category.pack()

'''
GUIDE 
''' 
# Fonction pour ouvrir la fenêtre "Guide"
def open_guide_window():
    # Créer une nouvelle fenêtre
    window_guide = tk.Toplevel(window)
    window_guide.title("Guide")
    window_guide.minsize(500, 400)
    
    # Contenu de la fenêtre Guide
    label = tk.Label(window_guide, text="Bienvenue dans le guide !", font=("Arial", 22))
    label.pack(pady=20)

    title_category = tk.Label(window_guide, text="------------------------------------------------------COMMANDES------------------------------------------------------", font=("Arial", 14))
    title_category.pack()

    help_label = tk.Label(window_guide, text="Afin d'utiliser correctement MacroToad, voici quelques indications :", font=("Arial", 22))
    help_label.pack(pady=20) 

    # Affichage des commandes
    commands_text = """\
Cochez premièrement la case correspondant à la macro souhaitée.
F5 vous permettra de démarrer la macro sélectionnée.
F8 vous permettra d'arrêter temporairement une macro en cours puis de la reprendre.
F3 vous permettra d'arrêter la macro en cours / en pause."""
    
    command_category = tk.Label(window_guide, text=commands_text, font=("Arial", 18), justify="center")
    command_category.pack(pady=10)

    # Informations supplémentaires
    more_help_category = tk.Label(window_guide, text="---------------------------------------------------INFORMATIONS---------------------------------------------------", font=("Arial", 14))
    more_help_category.pack()
    information_category =  tk.Label(window_guide, text="Pour plus d'informations sur MacroToad, sur le skyblock,\n ou sur l'utilisation en jeu des macros :", font=("Arial", 18), justify="center")
    information_category.pack()

    def open_link():
        webbrowser.open("https://github.com/1KuMo/Skytoad")
    # Texte du lien
    link_label = tk.Label(
        window_guide,
        text="GitHub KuMo",
        font=("Arial", 16),
        fg="blue",
        cursor="hand2"  # Change le curseur en main
    )
    link_label.pack(pady=20)

    # Associer le clic au lien
    link_label.bind("<Button-1>", lambda e: open_link())
    
# Créer le bouton pour ouvrir le guide
guide_button = tk.Button(window, text="Guide", font=("Arial", 14), command=open_guide_window)
guide_button.pack(pady=10) 

# Boucle principale
window.mainloop()
window.minsize(400, 300)