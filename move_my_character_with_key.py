from pico2d import *

TUK_WIDTH, TUK_HEIGHT=1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
sprite_col=0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)


    character.clip_draw(frame * 146, sprite_col * 148, 146, 148, x, y)
    update_canvas()

    frame = (frame + 1) % 12
    delay(0.05)


close_canvas()
