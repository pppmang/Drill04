from pico2d import *

TUK_WIDTH, TUK_HEIGHT=1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite.png')

def handle_events():
    global running, dx, dy, sprite_col
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                dx -= 1
            elif event.key == SDLK_UP:
                dy += 1
            elif event.key == SDLK_DOWN:
                dy -= 1
            elif event.key == SDLK_RIGHT:
                dx += 1

            if dx == -1 and dy == 1:
                sprite_col = 0
            elif dx == -1 and dy == -1:
                sprite_col = 2
            elif dx == 1 and dy == 1:
                sprite_col = 6
            elif dx == 1 and dy == -1:
                sprite_col = 4
            elif dx == -1:
                sprite_col = 1
            elif dx == 1:
                sprite_col = 5
            elif dy == 1:
                sprite_col = 7
            elif dy == -1:
                sprite_col = 3
                
            elif event.key == SDLK_ESCAPE:
                running = False
                
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dx -= 1
            elif event.key == SDLK_LEFT:
                dx += 1
            elif event.key == SDLK_UP:
                dy -= 1
            elif event.key == SDLK_DOWN:
                dy += 1


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
dx, dy = 0, 0
sprite_col=0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)


    character.clip_draw(frame * 146, sprite_col * 148, 146, 148, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 12
    x += dx * 7
    y += dy * 7
    delay(0.05)


close_canvas()
