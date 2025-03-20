import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController  # on prend Key et Controller et on les utilise sous la variable KeyboardController
from pynput.mouse import Button, Controller as MouseController  # // pour MouseController
import tkinter as tk
import time
import threading  
import webbrowser # Help window "skytoad GitHub"
from PIL import ImageGrab

# main windiow
window = tk.Tk()
window.title("Macros")

'''
VARIABLES 
'''

keyboard_controller = KeyboardController()
mouse_controller = MouseController()

macro_running = False
macro_paused = False  
repetition = 0

macro_thread = None


# MACRO NETHER WARTH
def macro_nether_wart():
    global macro_running, macro_paused, repetition

    actions = [
        ("key", "q", 121),
        ("key", "d", 121), 
        ("key", "q", 121),  
        ("key", "d", 121),  
        ("key", "q", 125),  
    ]

    print("Démarrage de la macro Nether Wart.")
    macro_running = True
    was_paused = False  

    mouse_controller.press(Button.left)  

    while macro_running:
        for action_type, key, duration in actions:
            if not macro_running:  
                print("Macro arrêtée.")
                break

            while macro_paused:
                if not was_paused: 
                    print("Macro en pause... (Appuyez sur F8 pour reprendre)")
                    was_paused = True
                time.sleep(0.1)

            if was_paused: 
                print("Reprise de la macro.")
                was_paused = False
                mouse_controller.press(Button.left) 

            if not macro_running:  
                print("Macro arrêtée après pause.")
                break

            # exécution des actions
            if action_type == "key": 
                keyboard_controller.press(key)

                start_time = time.time()
                elapsed_time = 0  
                time_spent_during_action = 0 

                while elapsed_time < duration:
                    if not macro_running:  
                        print("Macro arrêtée en cours d'exécution.")
                        break

                    if macro_paused:  
                        keyboard_controller.release(key)  
                        mouse_controller.release(Button.left) 
                        pause_start_time = time.time()

                        while macro_paused:
                            if not was_paused:
                                print("Macro en pause... (durée en cours)")
                                was_paused = True
                            time.sleep(0.1)

                        if not macro_running:  
                            print("Macro arrêtée après pause.")
                            break

                        # calculer le temps de pause
                        pause_duration = time.time() - pause_start_time
                        time_spent_during_action += pause_duration  

                        keyboard_controller.press(key) 
                        mouse_controller.press(Button.left)
                    else:
                        elapsed_time = time.time() - start_time - time_spent_during_action  # soustraction du temps passé en pause

                    time.sleep(0.1) 

                keyboard_controller.release(key)

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    mouse_controller.release(Button.left)  
    macro_running = False
    print(f"Macro Nether Wart terminée. Total de répétitions : {repetition}")
    repetition = 0

# MACRO PUMPKIN
def macro_pumpkin(): # UTILISE 
    global macro_running, macro_paused, repetition

    actions = [
        ("key", "q", 74),          
        ("key", "d", 74),          
        ("key", "q", 74),          
        ("key", "z", 2),          
    ]

    print("Démarrage de la macro Pumpkin.")
    macro_running = True

    mouse_controller.press(Button.left)  

    was_paused = False

    while macro_running:
        for action_type, key, duration in actions:
            if not macro_running:  
                print("Macro arrêtée.")
                break

            while macro_paused:
                if not was_paused:  
                    print("Macro en pause... (Appuyez sur F8 pour reprendre)")
                    mouse_controller.release(Button.left)  
                    was_paused = True
                time.sleep(0.1)

            if was_paused:  
                print("Reprise de la macro.")
                mouse_controller.press(Button.left)  
                was_paused = False

            if not macro_running: 
                print("Macro arrêtée après pause.")
                break

            # exécution des actions
            if action_type == "key": 
                keyboard_controller.press(key)

                start_time = time.time()
                elapsed_time = 0
                time_spent_during_action = 0 
                while elapsed_time < duration:
                    if not macro_running: 
                        print("Macro arrêtée en cours d'exécution.")
                        break

                    if macro_paused: 
                        keyboard_controller.release(key) 
                        mouse_controller.release(Button.left)  
                        pause_start_time = time.time()

                        while macro_paused:
                            if not was_paused:
                                print("Macro en pause... (durée en cours)")
                                was_paused = True
                            time.sleep(0.1)

                        if not macro_running: 
                            print("Macro arrêtée après pause.")
                            break

                        pause_duration = time.time() - pause_start_time
                        time_spent_during_action += pause_duration 

                        keyboard_controller.press(key) 
                        mouse_controller.press(Button.left)  
                    else:
                        elapsed_time = time.time() - start_time - time_spent_during_action  

                    time.sleep(0.1)  

                keyboard_controller.release(key)

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    mouse_controller.release(Button.left) 
    macro_running = False
    print(f"Macro Pumpkin terminée. {repetition}")
    repetition = 0

# MACRO MELON
# MACRO MELON
def macro_melon():
    global macro_running, macro_paused, repetition

    actions = [
        ("key", "d", 73),
        ("key", "q", 73),
        ("key", "d", 73),
        ("key", "q", 73),
        ("key", "d", 73),
    ]

    print("Démarrage de la macro Melon.")
    macro_running = True

    mouse_controller.press(Button.left)

    was_paused = False

    while macro_running:
        for action_type, key, duration in actions:
            if not macro_running:
                print("Macro arrêtée.")
                break

            while macro_paused:
                if not was_paused:
                    print("Macro en pause... (Appuyez sur F8 pour reprendre)")
                    mouse_controller.release(Button.left)
                    was_paused = True
                time.sleep(0.1)

            if was_paused:
                print("Reprise de la macro.")
                mouse_controller.press(Button.left)
                was_paused = False

            if not macro_running:
                print("Macro arrêtée après pause.")
                break

            if action_type == "key":
                keyboard_controller.press(key)

                start_time = time.time()
                elapsed_time = 0
                time_spent_during_action = 0

                while elapsed_time < duration:
                    if not macro_running:
                        print("Macro arrêtée en cours d'exécution.")
                        break

                    if macro_paused:
                        keyboard_controller.release(key)
                        mouse_controller.release(Button.left)
                        pause_start_time = time.time()

                        while macro_paused:
                            if not was_paused:
                                print("Macro en pause... (durée en cours)")
                                was_paused = True
                            time.sleep(0.1)

                        if not macro_running:
                            print("Macro arrêtée après pause.")
                            break

                        pause_duration = time.time() - pause_start_time
                        time_spent_during_action += pause_duration

                        keyboard_controller.press(key)
                        mouse_controller.press(Button.left)
                    else:
                        elapsed_time = time.time() - start_time - time_spent_during_action

                    time.sleep(0.1)

                keyboard_controller.release(key)

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    mouse_controller.release(Button.left)
    macro_running = False
    print(f"Macro Melon terminée. {repetition}")
    repetition = 0

# MACRO ACACIA
def macro_acacia():
    global macro_running, macro_paused, repetition

    was_paused = False
    current_inventory_slot = 0
    inventory_list = [("é", '"'), ("'", "("), ("-", "è")]

    print("Démarrage de la macro Acacia.")
    macro_running = True

    while macro_running:
        element1, element2 = inventory_list[current_inventory_slot]
        print(f"Utilisation des éléments : {element1} et {element2}")
        current_inventory_slot = (current_inventory_slot + 1) % len(inventory_list)

        actions = [
            ("press", element1, 0.15),
            ("mouse", "right", 0.75),
            ("press", element2, 0.15),
            ("mouse", "right", 0.75),
            ("key", "&", 0.15),
            ("mouse", "left", 0.3),
            (None, None, 0.2),
        ]

        for action in actions:
            if not macro_running:
                print("Macro arrêtée.")
                break

            while macro_paused:
                if not was_paused:
                    print("Macro en pause... (durée en cours)")
                    was_paused = True
                time.sleep(0.1)

                if not macro_running:
                    print("Macro arrêtée après pause.")
                    return

            if was_paused:
                print("Reprise de la macro.")
                was_paused = False

            if action[0] == "press":
                keyboard_controller.press(action[1])
                time.sleep(action[2])
                keyboard_controller.release(action[1])

            elif action[0] == "key":
                keyboard_controller.press(action[1])
                time.sleep(action[2])
                keyboard_controller.release(action[1])

            elif action[0] == "mouse":
                if action[1] == "left":
                    mouse_controller.press(Button.left)
                    time.sleep(action[2])
                    mouse_controller.release(Button.left)
                elif action[1] == "right":
                    mouse_controller.press(Button.right)
                    time.sleep(action[2])
                    mouse_controller.release(Button.right)

            elif action[0] is None:
                time.sleep(action[2])

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    macro_running = False
    print(f"Macro Acacia terminée. Total de répétitions : {repetition}")
    repetition = 0

# MACRO DARK OAK
def macro_dark_oak():
    global macro_running, macro_paused, repetition

    was_paused = False
    current_inventory_slot = 0
    inventory_list = ['"', "'", "(", "-"]

    actions = [
        ("press", None, 0.15),
        ("mouse", "right", 0.75),
        ("key", "d", 0.4),
        ("press", None, 0.15),
        ("mouse", "right", 0.75),
        ("key", "q", 0.5),
        ("key", "è", 0.2),
        ("mouse", "right", 0.75),
        ("key", "é", 0.15),
        ("mouse", "left", 0.3),
        (None, None, 0.2),
    ]

    print("Démarrage de la macro Dark Oak.")
    macro_running = True

    while macro_running:
        element = inventory_list[current_inventory_slot]
        print(f"Changement d'élément dans l'inventaire : {element}")
        current_inventory_slot = (current_inventory_slot + 1) % len(inventory_list)

        for action in actions:
            if not macro_running:
                print("Macro arrêtée.")
                break

            while macro_paused:
                if not was_paused:
                    print("Macro en pause... (durée en cours)")
                    was_paused = True
                time.sleep(0.1)

                if not macro_running:
                    print("Macro arrêtée après pause.")
                    return

            if was_paused:
                print("Reprise de la macro.")
                was_paused = False

            if action[0] == "press" and element is not None:
                keyboard_controller.press(element)
                time.sleep(action[2])
                keyboard_controller.release(element)

            elif action[0] == "key":
                keyboard_controller.press(action[1])
                time.sleep(action[2])
                keyboard_controller.release(action[1])

            elif action[0] == "mouse":
                if action[1] == "left":
                    mouse_controller.press(Button.left)
                    time.sleep(action[2])
                    mouse_controller.release(Button.left)
                elif action[1] == "right":
                    mouse_controller.press(Button.right)
                    time.sleep(action[2])
                    mouse_controller.release(Button.right)

            elif action[0] is None:
                time.sleep(action[2])

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    macro_running = False
    print(f"Macro Dark Oak terminée. Total de répétitions : {repetition}")
    repetition = 0

    # MACRO TROPHY FISHING
def macro_trophy_fishing():
    global macro_running, macro_paused, repetition

    actions = [
        ("key", "w", 120),
        ("key", "a", 120),
        ("key", "s", 130),
        ("key", "d", 100),
    ]

    print("Démarrage de la macro Trophy Fishing.")
    macro_running = True
    was_paused = False

    while macro_running:
        for action_type, key, duration in actions:
            if not macro_running:
                print("Macro arrêtée.")
                break

            while macro_paused:
                if not was_paused:
                    print("Macro en pause... (Appuyez sur F8 pour reprendre)")
                    was_paused = True
                time.sleep(0.1)

            if was_paused:
                print("Reprise de la macro.")
                was_paused = False

            if not macro_running:
                print("Macro arrêtée après pause.")
                break

            # exécution des actions
            if action_type == "key":
                keyboard_controller.press(key)

                start_time = time.time()
                elapsed_time = 0
                time_spent_during_action = 0

                while elapsed_time < duration:
                    if not macro_running:
                        print("Macro arrêtée en cours d'exécution.")
                        break

                    if macro_paused:
                        keyboard_controller.release(key)
                        pause_start_time = time.time()

                        while macro_paused:
                            if not was_paused:
                                print("Macro en pause... (durée en cours)")
                                was_paused = True
                            time.sleep(0.1)

                        if not macro_running:
                            print("Macro arrêtée après pause.")
                            break

                        pause_duration = time.time() - pause_start_time
                        time_spent_during_action += pause_duration

                        keyboard_controller.press(key)
                    else:
                        elapsed_time = time.time() - start_time - time_spent_during_action

                    time.sleep(0.1)

                keyboard_controller.release(key)

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    macro_running = False
    print(f"Macro Trophy Fishing terminée. Total de répétitions : {repetition}")
    repetition = 0


# MACRO CLICK FARM
def macro_click_farm():
    global macro_running, macro_paused, repetition

    print("Démarrage de la macro Click Farm.")
    macro_running = True
    was_paused = False

    while macro_running:
        # Effectuer un clic toutes les 0.2 secondes (simulateur de farm)
        mouse_controller.click(Button.left)
        time.sleep(0.2)

        while macro_paused:
            if not was_paused:
                print("Macro en pause... (Appuyez sur F8 pour reprendre)")
                was_paused = True
            time.sleep(0.1)

        if was_paused:
            print("Reprise de la macro.")
            was_paused = False

        print(f"Une répétition de la macro est terminée. Répétition {repetition} en cours.")
        repetition += 1

    macro_running = False
    print(f"Macro Click Farm terminée. Total de répétitions : {repetition}")
    repetition = 0


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

# touches pour pause/reprise et arrêt

def on_press(key):
    global macro_running, macro_paused, macro_thread

    try:
        if key == Key.f5:  # start 
            if not macro_running:  # si c'est pas alr start
                print("F5 pressée : démarrage de la macro.")
                start_macro_thread()  # Démarre la macro sélectionnée
            else:
                print("F5 pressée : reprise de la macro.")
                macro_paused = False  # if paused : start back
        
        elif hasattr(key, 'char') and key.char == 'x':  # macro click maths
            if not macro_running: 
                print("'x' pressée : démarrage de la macro de clic.")
                macro_running = True
                macro_thread = threading.Thread(target=macro_click_farm)
                macro_thread.start()
            else:  # stop if running
                print("'x' pressée : arrêt de la macro de clic.")
                macro_running = False
                if macro_thread is not None:
                    macro_thread.join() 
                print("Macro de clic arrêtée.")
                
        elif key == Key.f8:  # pause / start back
            if macro_running: 
                macro_paused = not macro_paused 
                print("Macro en pause." if macro_paused else "Macro reprise.")
            else:
                print("Aucune macro en cours pour mettre en pause/reprendre.")

        elif key == Key.f3:  # STOP
            if macro_running:  
                print("F3 pressée : arrêt complet de la macro.")
                macro_running = False  
                if macro_thread is not None:  
                    macro_thread.join()
                print("Macro arrêtée.")
            else:
                print("Aucune macro en cours à arrêter.")

    except Exception as e:
        print(f"Erreur : {e}")


# on listen les touches ( après la fonction on_press sinon c po cool )
listener = keyboard.Listener(on_press=on_press)
listener.start()
'''
CUSTOMISATION + BUTTONS 
Farming 
'''
font_large = ("Arial", 16) 
font_title = ("Helvetica", 20, "bold") 
font_category = ("New Romance", 13)

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

btn_farm3_var = tk.BooleanVar() 
btn_farm3 = tk.Checkbutton(window, text="Melon Macro / opti farm", variable=btn_farm3_var, font=font_large)
btn_farm3.pack()

btn_click_var = tk.BooleanVar()
btn_click = tk.Checkbutton(window, text="CLICK MACRO", variable=macro_click_farm, font=font_large)
btn_click.pack()

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
def open_guide_window():

    window_guide = tk.Toplevel(window)
    window_guide.title("Guide")
    window_guide.minsize(500, 400)
    
    label = tk.Label(window_guide, text="Bienvenue dans le guide !", font=("Arial", 22))
    label.pack(pady=20)

    title_category = tk.Label(window_guide, text="------------------------------------------------------COMMANDES------------------------------------------------------", font=("Arial", 14))
    title_category.pack()

    help_label = tk.Label(window_guide, text="Afin d'utiliser correctement MacroToad, voici quelques indications :", font=("Arial", 22))
    help_label.pack(pady=20) 

    commands_text = """\
Cochez premièrement la case correspondant à la macro souhaitée.
F5 vous permettra de démarrer la macro sélectionnée.
F8 vous permettra d'arrêter temporairement une macro en cours puis de la reprendre.
F3 vous permettra d'arrêter la macro en cours / en pause."""
    
    command_category = tk.Label(window_guide, text=commands_text, font=("Arial", 18), justify="center")
    command_category.pack(pady=10)

    more_help_category = tk.Label(window_guide, text="---------------------------------------------------INFORMATIONS---------------------------------------------------", font=("Arial", 14))
    more_help_category.pack()
    information_category =  tk.Label(window_guide, text="Pour plus d'informations sur MacroToad, sur le skyblock,\n ou sur l'utilisation en jeu des macros :", font=("Arial", 18), justify="center")
    information_category.pack()

    def open_link():
        webbrowser.open("https://github.com/1KuMo/Skytoad")
    link_label = tk.Label(
        window_guide,
        text="GitHub KuMo",
        font=("Arial", 16),
        fg="blue",
        cursor="hand2"  #  curseur > main
    )
    link_label.pack(pady=20)

    # click = lien 
    link_label.bind("<Button-1>", lambda e: open_link())
    
guide_button = tk.Button(window, text="Guide", font=("Arial", 14), command=open_guide_window)
guide_button.pack(pady=10) 

window.mainloop()
window.minsize(400, 300)
