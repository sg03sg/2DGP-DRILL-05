from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280,1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


running = True
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
dir_x =1
dir_y =0
animations =0
frame =0

def draw_character(animation,frame):
    global x,y
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    character.clip_draw(frame*100,animation,100,100,x,y)
    update_canvas()
    delay(0.05)


def handle_events():
    global running
    global dir_x,dir_y
    global x,y

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
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
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
    if x<30:
        x=30
    if x>TUK_WIDTH-30:
        x=TUK_WIDTH-30
    if y<50:
        y=50
    if y>TUK_HEIGHT-50:
        y=TUK_HEIGHT-50

while running:

    if dir_x ==2:
        animations = 100
    elif dir_x == -2:
        animations = 0
    elif dir_x == 1:
        animations = 300
    elif dir_x == -1:
        animations = 200

    frame = (frame + 1) % 8

    draw_character(animations,frame)

    handle_events()

    if not(dir_x==1 or dir_x==-1):
        x += dir_x *5
    y += dir_y *10

close_canvas()