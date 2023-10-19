from pico2d import *

import game_world
from grass import Grass
from boy import Boy


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def create_world():
    global running
    global grass
    global team
    global boy

    running = True

    boy = Boy()
    boy.y -= 20
    game_world.add_object(boy, 1)

    grass = Grass()
    grass.y = 50
    game_world.add_object(grass, 0)

    grass = Grass()
    game_world.add_object(grass, 2)



def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
create_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
