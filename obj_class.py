# / OBJECTS
import functions as func


# // entity builder
class Entity:
    def __init__(self, name, entity_z_init, entity_z_count, entity_w_init, entity_w_count, state, esc_possible):
        self.name = name
        self.entity_z_init = entity_z_init
        self.entity_z_count = entity_z_count
        self.entity_w_init = entity_w_init
        self.entity_w_count = entity_w_count
        self.state = state
        self.esc_possible = esc_possible

    # /// die action
    def die(self):
        print(f"{self.name} został zabity!")
        """func.dub_play()
        # find empty channel
        channel = None
        for i in range(pygame.mixer.get_num_channels()):
            if not pygame.mixer.Channel(i).get_busy():
                channel = pygame.mixer.Channel(i)
                break
        if channel is None:
            print("DEBUG: Nie znaleziono wolnego kanału.")
            return

        play sound on found channel
        channel.play(f'{cnst.assets_audio_effects_pth}/{self.name}_kill_sound.mp3')"""

        # For some weird reason, this code is not functioning correctly.
        # It appears that the issue may be connected to its placement within a class instance.
        # However, in an ideal scenario, it should work seamlessly, just as it does in other modules (ex. functions.py).

        self.state = False


# // room builder
class Room:
    def __init__(self, room_num, room_state=False, max_visit_count=999, visit_count=0):
        self.room_num = room_num
        self.room_state = room_state
        self.max_visit_count = max_visit_count
        self.visit_count = visit_count
