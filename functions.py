import random
import time
import pygame
import os
import subprocess
import json
import datetime
import constants
import gamebook as gb
import constants as cnst
# paragraphs must be imported
import paragraphs as prg
from colorama import Fore


def debug_message(msg):
    if cnst.debug_msg:
        print(f'{cnst.debug_txt_clr}DEBUG: {msg}{cnst.def_txt_clr}')


def error_message(error_name, msg):
    if cnst.dev_mode:
        if error_name == '':
            error_name = 'ERROR'
        print(f'{cnst.error_txt_clr}{error_name}{cnst.debug_txt_clr} || {msg}{cnst.def_txt_clr}')


def clear_terminal():
    subprocess.call('cls' if os.name == 'nt' else 'clear', shell=True)


def loading(duration, message=None):
    animation_signs = ['|', '/', '-', '\\']
    end_time = time.time() + duration
    sign_index = 0

    if message:
        print(message, end='')  # Display message if one is given

    print(Fore.YELLOW, end='\r')
    while time.time() < end_time:
        print('- ' + animation_signs[sign_index % len(animation_signs)] + ' -', end='\r')
        time.sleep(0.1)
        sign_index += 1
    print(cnst.def_txt_clr)


def get_music(category=None, fadeout=None, update=None):
    if update:
        pygame.mixer.music.set_volume(cnst.bckg_volume)
    else:
        if constants.get_music:
            if category == 'main' or category == 'combat' or category == 'menu':
                random_track = random.choice(cnst.music_tracks[category])

                if fadeout:
                    pygame.mixer.music.fadeout(fadeout)

                debug_message(f"Playing {category}: {random_track}")

                pygame.mixer.music.load(random_track)
                pygame.mixer.music.set_volume(cnst.bckg_volume)

                if pygame.mixer.music.get_busy() == 0:
                    pygame.mixer.music.play(-1)  # play in loop --> (-1)
            else:
                if constants.dev_mode:
                    debug_message("Playing: No music was selected")
        else:
            if constants.dev_mode:
                debug_message("if dev_mode; get_music() is disabled")


def dub_play(string_id, category=None, skippable=True, with_text=True):
    audio_file_id = None

    if category and category.lower() == 'adam':
        audio_path = f'{cnst.assets_audio_pth}/Adam'
        audio_file_id = f'{audio_path}/{cnst.translation}/audiobook_{category.lower()}_{cnst.translation}_{string_id}{cnst.audio_ext}'

    elif category and category.lower() == 'fx':
        audio_file_id = f'{cnst.assets_audio_effects_pth}/audiobook_{string_id}{cnst.audio_ext}'

    try:
        current_sound = pygame.mixer.Sound(audio_file_id)

    except FileNotFoundError:
        error_message('FileNotFoundError', f'Could not find: {audio_file_id}')
        current_sound = pygame.mixer.Sound(f'{cnst.assets_audio_effects_pth}/audiobook_click_snd.mp3')

    pygame.mixer.stop()  # stop any sound currently being played
    current_sound.set_volume(cnst.action_volume)  # ensure that volume is on default

    # find empty channel
    channel = None
    for i in range(pygame.mixer.get_num_channels()):
        if not pygame.mixer.Channel(i).get_busy():
            channel = pygame.mixer.Channel(i)
            break

    if channel is None:
        debug_message('Could not find empty channel.')
        return

    if with_text:  # display currently selected gamebook identifier as text
        try:
            if len(string_id) > 0:
                print(gb.gameboook[cnst.translation][string_id])

        except KeyError:
            channel.play(pygame.mixer.Sound(f'{cnst.assets_audio_effects_pth}/audiobook_click_snd.mp3'))
            error_message('KeyError', f'Could not find string: {string_id}')

    if skippable:
        if cnst.dubbing:
            debug_message('audio dialog skipped')
            input(f"continue {cnst.input_sign}")

        else:
            # play sound on found channel
            channel.play(current_sound)
            debug_message(f'Now playing: {audio_file_id}')


pygame.mixer.music.stop()


def name_randomizer():
    first_parts = ['Bogdan', 'Dobrosław', 'Jarosław', 'Grzesiu', 'Mścisław', 'Radosław', 'Sławomir',
                   'Zbyszko z Bogdańca', 'Władysław', 'Zbigniew', 'Stanisław']
    last_parts = ['z Levygradu', 'Mądry', 'Odważny', 'z Małomorza', 'Prawy', 'Sprawiedliwy', 'Słomka', 'Wielki',
                  'Zacny', 'Zuchwały', 'Pyzdra']

    first_name = random.choice(first_parts)
    last_name = None

    # 'zbyszko z bogdańca' easteregg mechanic
    if first_name == 'Zbyszko z Bogdańca':  # meme for ya (probably only poles could understand, sorry)
        dub_play("zbych", "fx", True, False)
        time.sleep(2.7)
        clear_terminal()
        print(cnst.and_his_name_is)
        time.sleep(5.6)
    else:
        last_name = random.choice(last_parts)
    player_name = f'{Fore.LIGHTYELLOW_EX}{first_name} {last_name}{cnst.def_txt_clr}'
    print(player_name)
    time.sleep(1)
    cnst.player_name = player_name
    return cnst.player_name


def update_variable(variable, change):
    if isinstance(variable, bool):
        new_variable = change
    elif isinstance(variable, int) or isinstance(variable, float):
        new_variable = variable + change
    else:
        # Handling other variable types
        new_variable = variable

    return new_variable


def get_player_par():
    cnst.z_init = cnst.z_count = random.randint(1, 6) + 6
    cnst.w_init = cnst.w_count = random.randint(2, 12) + 12
    cnst.s_init = cnst.s_count = random.randint(1, 6) + 6
    return cnst.z_init, cnst.z_count, cnst.w_init, cnst.w_count, cnst.s_init, cnst.s_count


def update_setup_file(manual=False, backup=False):
    if manual:
        print("Leave empty for no changes:")
        setup_data = {}
        fields = [
            ("active_gameplay", "(path)"),
            ("translation", ", ".join(list(gb.gameboook.keys()))),
            ("dev_mode", "(True/False)"),
            ("use_dummy", "(True/False)"),
            ("show_start_sequence", "(True/False)"),
            ("manual_battle", "(True/False)"),
            ("dubbing", "(True/False)"),
            ("get_music", "(True/False)"),
            ("ver_num", "int, float, or string"),
            ("difficulty", "(1, 1.3, 1.6)"),
            ("action_volume", "int from 0.1 to 1.0"),
            ("sfx_volume", "int from 0.1 to 1.0"),
            ("bckg_volume", "int from 0.1 to 1.0")
        ]

        for field, prompt in fields:
            print()
            print(prompt)
            value = input(f"{field}: ").strip()

            if value:
                if field == "ver_num":
                    try:
                        value = eval(value)
                    except:
                        value = str(value)
                elif field == "difficulty":
                    try:
                        value = float(value)
                    except:
                        value = cnst.__dict__[field]
                elif field in ["action_volume", "sfx_volume", "bckg_volume"]:
                    try:
                        value = float(value)
                        if not 0.1 <= value <= 1.0:
                            value = cnst.__dict__[field]
                    except:
                        value = cnst.__dict__[field]
                elif field in ["dev_mode", "use_dummy", "show_start_sequence", "manual_battle", "dubbing", "get_music"]:
                    value = value.lower() == "true"

                setup_data[field] = value
            else:
                setup_data[field] = cnst.__dict__[field]


    elif backup:
        setup_data = {
            "active_gameplay": "dreszcz_dummy.json",
            "translation": "en",
            "dev_mode": True,
            "debug_msg": True,
            "use_dummy": True,
            "show_start_sequence": False,
            "manual_battle": False,
            "dubbing": False,
            "get_music": False,
            "ver_num": None,
            "difficulty": 1,
            "action_volume": 1,
            "sfx_volume": 0.8,
            "bckg_volume": 0.8
        }
        debug_message('backup data loaded')

    else:
        setup_data = {
            "active_gameplay": cnst.active_gameplay,
            "translation": cnst.translation,
            "dev_mode": cnst.dev_mode,
            "debug_msg": cnst.debug_msg,
            "use_dummy": cnst.use_dummy,
            "show_start_sequence": cnst.show_start_sequence,
            "manual_battle": cnst.manual_battle,
            "dubbing": cnst.dubbing,
            "get_music": cnst.get_music,
            "ver_num": cnst.ver_num,
            "action_volume": cnst.action_volume,
            "sfx_volume": cnst.sfx_volume,
            "bckg_volume": cnst.bckg_volume
        }

    with open(cnst.setup_name, 'w') as json_file:  # Save the setup data to a JSON file
        json.dump(setup_data, json_file)
    debug_message("setup.json has been updated")

    if manual:
        input(f"{cnst.special_txt_clr}Some changes needs restarting the game to take effect.\
        \n{cnst.input_sign}{cnst.def_txt_clr}")


def get_game_state(action, last_paragraph='prg.00', new_game=None):
    if cnst.use_dummy:
        # use game states saved in project location
        folder_path = os.path.dirname(os.path.abspath(__file__))
    else:
        # use local 'documents' folder path for saving json file
        folder_path = os.path.join(os.path.expanduser("~/Documents"), cnst.game_state_dir_name)

    json_files = []  # list of json files in folder_path

    if os.path.exists(folder_path):
        json_files = [file for file in os.listdir(folder_path) if file.endswith(".json") and file != "setup.json"]

        for file_name in json_files:
            if not file_name.startswith("dreszcz_") or not file_name.endswith(".json"):
                debug_message(f"{file_name} is not a valid game state file")
    else:
        if not cnst.use_dummy:
            os.makedirs(folder_path)
            debug_message(f'Directory {folder_path} created')

    if action == 's':
        if new_game:
            # Create new file path and update active gameplay file_path
            cnst.active_gameplay = os.path.join(folder_path,
                                                f"dreszcz_{datetime.datetime.now().strftime('%y-%m-%d_%S')}.json")

        # Save game state to variable
        game_state = {
            "last_paragraph": last_paragraph,
            "player_name": cnst.player_name,
            "difficulty": cnst.difficulty,
            "s_count": cnst.s_count,
            "w_count": cnst.w_count,
            "z_count": cnst.z_count,
            "s_init": cnst.s_init,
            "w_init": cnst.w_init,
            "z_init": cnst.z_init,
            "equipment": cnst.main_eq,
            "potion": cnst.potion,
            "potion_count": cnst.potion_count,
            "eatables_count": cnst.eatables_count,
            "gold_amount": cnst.gold_amount
        }

        # Saving game state as json file
        with open(cnst.active_gameplay, "w") as f:
            json.dump(game_state, f)
        debug_message(f'Game saved to: {cnst.active_gameplay}')


    elif action == 'l':

        if len(json_files) > 0:
            print("Saved game states:")  # List of JSON files
            for i, file in enumerate(json_files, start=1):
                print(f"{i}. {file}")

            while True:
                file_number = input(f"\nChoose game state to load (leave empty to return to main menu)\
                \n{cnst.input_sign}")

                if file_number == '':
                    break

                try:
                    file_number = int(file_number)

                    if 1 <= file_number <= len(json_files):
                        selected_file = json_files[file_number - 1]
                        cnst.active_gameplay = os.path.join(folder_path, selected_file)
                        with open(cnst.active_gameplay, "r") as f:
                            game_state = json.load(f)
                        debug_message(f'Game state loaded from: {selected_file}')
                        break
                    else:
                        debug_message("Incorrect file number provided.")

                except ValueError:
                    debug_message("Incorrect file number provided.")

            # Assigning the loaded data back to variables.
            input(last_paragraph)
            last_paragraph = game_state.get("last_paragraph")
            cnst.player_name = game_state.get("player_name")
            cnst.difficulty = game_state.get("difficulty")
            cnst.s_count = game_state.get("s_count")
            cnst.s_count = game_state.get("s_count")
            cnst.w_count = game_state.get("w_count")
            cnst.z_count = game_state.get("z_count")
            cnst.s_count = game_state.get("s_init")
            cnst.w_count = game_state.get("w_init")
            cnst.z_count = game_state.get("z_init")
            cnst.main_eq = game_state.get("equipment")
            cnst.potion = game_state.get("potion")
            cnst.potion_count = game_state.get("potion_count")
            cnst.eatables_count = game_state.get("eatables_count")
            cnst.gold_amount = game_state.get("gold_amount")

        else:
            debug_message("No saved game states found.")

        update_setup_file()  # dump all setup to json file


    elif action == 'c':  # continue
        with open(cnst.active_gameplay, "r") as f:
            game_state = json.load(f)

            debug_message(f'Game state loaded from: {cnst.active_gameplay}')

            # Assigning the loaded data back to variables.
            last_paragraph = game_state.get("last_paragraph")
            cnst.player_name = game_state.get("player_name")
            cnst.difficulty = game_state.get("difficulty")
            cnst.s_count = game_state.get("s_count")
            cnst.w_count = game_state.get("w_count")
            cnst.z_count = game_state.get("z_count")
            cnst.s_count = game_state.get("s_init")
            cnst.w_count = game_state.get("w_init")
            cnst.z_count = game_state.get("z_init")
            cnst.main_eq = game_state.get("equipment")
            cnst.potion = game_state.get("potion")
            cnst.potion_count = game_state.get("potion_count")
            cnst.eatables_count = game_state.get("eatables_count")
            cnst.gold_amount = game_state.get("gold_amount")

            update_setup_file()  # dump all setup to json file

    elif action == 'init':
        if len(json_files) > 0:
            cnst.game_state_exists = True

        else:
            if cnst.use_dummy and cnst.active_gameplay is None:
                cnst.active_gameplay = "dreszcz_dummy.json"
                game_state = {
                    "last_paragraph": "prg._25()",
                    "player_name": "dummy_player",
                    "difficulty": 1,
                    "s_count": 20,
                    "w_count": 20,
                    "z_count": 20,
                    "s_init": 20,
                    "w_init": 20,
                    "z_init": 20,
                    "equipment": {
                        "plecak na Prowiant": "",
                        "prowiant": 8,
                        "tarcza": "",
                        "miecz": ""
                    },
                    "potion": "w",
                    "potion_count": 2,
                    "eatables_count": 8,
                    "gold_amount": 0
                }
                with open(cnst.active_gameplay, "w") as f:
                    json.dump(game_state, f)
                debug_message(f"Restored dummy game_state to: {cnst.active_gameplay}")
                cnst.game_state_exists = True
            else:
                cnst.game_state_exists = False

    return last_paragraph


def pth_selector(path_strings=None, actions=None, visit_check=False, room_id=None):
    if room_id:  # add visit count if room number was given
        room_id.visit_count = update_variable(room_id.visit_count, 1)
        debug_message(f'added visit: visit count of room number {room_id.room_num} = {room_id.visit_count}')

    if visit_check:
        if room_id.room_state:  # if open
            print(
                f"{gb.gameboook[cnst.translation]['door']} {cnst.special_txt_clr}{room_id.room_num}{cnst.def_txt_clr} {gb.gameboook[cnst.translation]['are']} {cnst.special_txt_clr}{gb.gameboook[cnst.translation]['opened']}{cnst.def_txt_clr}.")
            dub_play('opened', 'adam', False)

            # Player is visiting the room more times than the allowed number.
            if not room_id.visit_count - 1 >= room_id.max_visit_count:
                if room_id.visit_count == 1:  # Player first time in room
                    debug_message(f'eval: {actions[1]}')
                    get_game_state('s', actions[1])
                    eval(actions[1])

                # Player has already visited the room before, but did not exceed the allowed number of visits.
                elif room_id.visit_count >= 2:
                    debug_message(f'eval: {actions[0]}')
                    get_game_state('s', actions[0])
                    eval(actions[0])

            else:
                print("Nothing to find here")

        else:  # if closed
            try:
                print(
                    f"{gb.gameboook[cnst.translation]['door']} {cnst.special_txt_clr}{room_id.room_num}{cnst.def_txt_clr} {gb.gameboook[cnst.translation]['are']} {cnst.special_txt_clr}{gb.gameboook[cnst.translation]['closed']}{cnst.def_txt_clr}.")
            except KeyError:
                debug_message(f"this line does not exist in gamebook[{cnst.translation}]")
            dub_play('closed', 'adam', False)
            debug_message(f'eval: {actions[1]}')
            eval(actions[1])

    else:
        debug_message(f'pth_selector(): evaluating action: {actions}')

        if len(actions) != 1:  # if there is more than one path, display choice menu
            for i, path in enumerate(path_strings):
                print(f'{i + 1} · {path}')
                time.sleep(cnst.delay)

            while True:
                odp = input(f'{cnst.input_sign}')

                try:
                    odp = int(odp)

                    if 0 < odp <= len(path_strings):
                        break

                except ValueError:
                    print(f'/!/ {cnst.special_txt_clr}Choose number from list{cnst.def_txt_clr}')

            clear_terminal()
            pygame.mixer.stop()  # abort any dubbing currently playing
            get_game_state('s', actions[odp - 1])
            eval(actions[odp - 1])

        else:  # if there is only one path, continue automatically
            clear_terminal()
            get_game_state('s', actions[0])
            eval(actions[0])


def kill():
    print("Przegrałeś!!!")
    pygame.mixer.music.fadeout(2000)
    exit()


def win():
    print("Wygrałeś!!!")
    pygame.mixer.music.fadeout(2000)
    exit()


def check_for_luck():
    print(f'{cnst.special_txt_clr}Sprawdzam czy masz szczęście:')
    loading(2)
    cfl_val = random.randint(2, 12)

    if cfl_val <= cnst.s_count:
        print('\rUff, masz szczęscie.\
        \n')
        cnst.p_luck = True
    elif cfl_val > cnst.s_count:
        print('\rNie masz szczęścia!\
        \n')
        cnst.p_luck = False

    cnst.s_count -= 1
    time.sleep(1)

    return cnst.p_luck, cnst.s_count


def check_for_gold_amount(req_amount):
    if cnst.gold_amount >= req_amount:
        return True
    else:
        print("You don't have enough gold.")
        return False


def eatables():
    if cnst.eatables_count != 0:
        while True:
            if cnst.w_count != cnst.w_init:
                dub_play("eatables", "adam", False)
                print(f"/// Wytrzymałość: {cnst.w_count}/{cnst.w_init}")
                print(f"/// Prowiant: {cnst.eatables_count}/{cnst.init_eatables_count}")
                odp = input(f"{cnst.input_sign}")
                loading(1)
                if odp.lower() in {'tak', 't', 'y', 'yes'}:
                    if cnst.w_count < cnst.w_init:
                        cnst.eatables_count -= 1
                        wzrost_wytrzymalosci = min(cnst.eatable_W_load, cnst.w_init - cnst.w_count)
                        cnst.w_count += wzrost_wytrzymalosci
                        print(f"Wytrzymałość + {wzrost_wytrzymalosci}")
                        print(f"/// Wytrzymałość: {cnst.w_count}/{cnst.w_init}")
                        print(f"/// Prowiant: {cnst.eatables_count}/{cnst.init_eatables_count}{cnst.def_txt_clr}")
                        print(f"{cnst.def_txt_clr}")
                        break

                elif odp.lower() in {'nie', 'n', 'no'}:
                    print("Zostawiasz prowiant na później")
                    print(f"{cnst.def_txt_clr}")
                    break

                else:
                    print("Wpisz tak/nie")

                return cnst.w_count, cnst.eatables_count


def show_equipment_list():
    for i in cnst.main_eq:
        print(f'- {i}')
    input(f"{cnst.input_sign} ")


def eq_change(new_item_name):
    input(f"/// {cnst.special_txt_clr}Zdobyto nowy przedmiot: {new_item_name}{cnst.def_txt_clr}\
    \n{cnst.input_sign}")


def show_player_stats():
    print(f'{cnst.def_txt_clr}\
    \nWytrzymałość: {cnst.w_count}/{cnst.w_init} \
    \nZręczność: {cnst.z_count}/{cnst.z_init} \
    \nSzczęście: {cnst.s_count}/{cnst.s_init}')


def show_entity_stats(entity):
    print(f'{cnst.def_txt_clr}\
    \nStatystyki {entity.name}:\
    \nWytrzymałość: {entity.entity_w_count}/{entity.entity_w_init}\
    \nZręczność: {entity.entity_z_count}/{entity.entity_z_init}')


def stats_change(attribute_name, parameter, amount, limit=None):
    inter = '+' if amount >= 0 else ''

    if limit:  # for attributes that can't be increased above limit
        updated_parameter = min(parameter + amount, limit)

    else:  # for attributes that can be increased above limit
        updated_parameter = parameter + amount

    if parameter != limit:
        print(f'{cnst.special_txt_clr}/// {attribute_name}({parameter}) {inter} {amount} {constants.input_sign}{updated_parameter}{cnst.def_txt_clr}')

    return updated_parameter


def use_potion():
    updated_state = None
    if cnst.potion_count > 0:
        potion_attributes = {
            'w': (cnst.w_count, cnst.w_init),
            'z': (cnst.z_count, cnst.z_init),
            's': (cnst.s_count, cnst.s_init + 1)
        }
        if cnst.potion in potion_attributes:
            attr_name, attr_value = potion_attributes[cnst.potion]
            setattr(cnst, attr_name, attr_value)
        updated_state = cnst.potion_count - 1

    return updated_state


# - - - - - - - - -
# /// COMBAT
# - - - - - - - - -

def combat_main(entity, state, esc_possible, escape_id, stay_id, win_path):
    pygame.mixer.music.fadeout(1500)

    # loading background music
    get_music('combat')

    # setting up the combat
    cnst.round_count = 0
    p_w_count = cnst.w_count
    e_w_count = entity.entity_w_count

    show_player_stats()
    show_entity_stats(entity)

    input(f"\n{cnst.combat_txt_clr}{gb.gameboook[cnst.translation]['combat_init']} {cnst.input_sign}")

    while True:

        if state:  # if enemy is alive begin new round

            # preparing next round
            clear_terminal()
            cnst.round_count += 1

            print(f"\n{cnst.combat_txt_clr}Round: {cnst.round_count}{cnst.combat_txt_clr}")  # display round ID

            if cnst.manual_battle:
                a = input(f"Enter the value of 'a' by rolling two dice{cnst.input_sign}")
                b = input(f"Enter the value of 'b' by rolling two dice{cnst.input_sign}")

            else:
                a = random.randint(2, 12) + entity.entity_z_count * cnst.entity_hit_mult  # value of enemy power
                b = random.randint(2, 12) + cnst.z_count  # value of player power

            if a > b:  # if the enemy is stronger
                if cnst.w_count > 0:
                    cnst.w_count += cnst.e_hit_val_
                    dub_play('round_false', 'adam', False, False)
                    cnst.w_count = max(cnst.w_count, 0)
                    print(f"{Fore.LIGHTRED_EX}{entity.name}{cnst.combat_txt_clr} landed a hit!")

            elif a < b:  # if the player is stronger
                if entity.entity_w_count > 0:
                    entity.entity_w_count += cnst.p_hit_val_
                    dub_play('round_true', 'adam', False, False)
                    entity.entity_w_count = max(entity.entity_w_count, 0)
                    print(f"{Fore.LIGHTYELLOW_EX}{cnst.player_name}{cnst.combat_txt_clr} landed a hit!")

            else:  # if it's a draw
                print(f'{cnst.special_txt_clr}Draw!\
                \nNobody got hurt!')
                dub_play('round_none', 'adam', False, False)

            print(
                f"\
                \n{Fore.LIGHTYELLOW_EX}{cnst.player_name}{cnst.special_txt_clr}: {cnst.w_count}/{cnst.w_init}\
                \n{Fore.LIGHTRED_EX}{entity.name}{cnst.special_txt_clr}: {entity.entity_w_count}/{entity.entity_w_init}")

            debug_message(f"enemy:{entity.entity_w_count}, player: {cnst.w_count}")

            loading(1)

            if entity.entity_w_count <= 0:  # if the enemy is dead
                break

            elif cnst.w_count <= 0:  # if the player is dead
                print(
                    f"\n{gb.gameboook[cnst.translation]['combat_dead_info']} {Fore.LIGHTRED_EX}{entity.name}{cnst.combat_txt_clr}!")
                dub_play('combat_false', 'adam', False, False)
                kill()

    pygame.mixer.music.fadeout(1500)
    get_music('main')

    print(
        f"\n{cnst.combat_txt_clr}{gb.gameboook[cnst.translation]['combat_win_info']} {Fore.LIGHTRED_EX}{entity.name}{cnst.combat_txt_clr}!")
    dub_play('combat_true', 'adam', False)
    show_player_stats()
    if esc_possible:
        escape_opt = f"{escape_id})"
        stay_opt = f"{stay_id})"
        print(gb.gameboook[cnst.translation]['esc_choice'])
        odp = input(cnst.input_sign)
        if len(odp) == 0:
            print(
                f"{cnst.special_txt_clr}Wytrzymałość: {cnst.w_count} {cnst.input_sign} {cnst.w_count - 2}{cnst.def_txt_clr}")
            cnst.w_count -= 2
            eval(escape_opt)
        elif len(odp) > 0:
            eval(stay_opt)
    else:
        eval(win_path)
