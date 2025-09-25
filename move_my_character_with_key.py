from pico2d import *

open_canvas()
TUK_WIDTH, TUK_HEIGHT = 1280,1024
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
dir_x =0
dir_y =0
animations =0

def draw_character(animation):
    clear_canvas()
    tuk_ground.draw(400,30)
    character.clip_draw(animation*100,100,100,100,x,90)
    update_canvas()
    delay(0.05)


def handle_events():
    global running
    global dir_x,dir_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x = 2
            elif event.key == SDLK_LEFT:
                dir_x = -2
            elif event.key == SDLK_UP:
                dir_y = 1
            elif event.key == SDLK_DOWN:
                dir_y = -1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

while running:
    draw_character(animations)

    handle_events()

close_canvas()