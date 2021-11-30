import pygame
from colors import *
from menu import Menu
from objects import *
from main import Main

# Game loop and render
if __name__ == "__main__":

    all_sprites = pygame.sprite.Group()
    size = width, height = 1920, 1080

    window = Main(size)
    menu = Menu("Fonts/Roboto-Medium.ttf", window.screen)
    ball = Ball(window.screen.get_width()/2, window.screen.get_height()/2+100, 50, 50, window.screen.get_width(), window.screen.get_height())
    platform = Platform((window.screen.get_width()//2), (window.screen.get_height()-90), 300, 150, 30)

    bricks_list = []
    brick_x = 10
    brick_y = 10
    bricks_cols = (window.screen.get_width() - (10+(10*window.screen.get_width()//100)))//100
    brick_rows = int((window.screen.get_height()/2)//70)
    for i in range(brick_rows):
        if i <= 2:
            brick_color = 'Assets/red_brick.png'
        elif 2 < i <=4:
            brick_color = 'Assets/orange_brick.png'
        else:
            brick_color = 'Assets/yellow_brick.png'
        for j in range(bricks_cols):
            bricks_list.append(Brick(brick_color, brick_x, brick_y))
            brick_x = brick_x + bricks_list[j].rect.width + 10

        brick_y = brick_y + bricks_list[i].rect.height + 10
        brick_x = 10

    for i in range(len(bricks_list)):
        all_sprites.add(bricks_list[i])

    all_sprites.add(ball)
    all_sprites.add(platform)

    while not window.process_stopped:
        for event in pygame.event.get():
            if menu.opened:
                menu.controls(event)
            platform.controls(event)
            window.quit(event)

        window.screen.fill(DARK_GRAY)

        if menu.opened:
            started_ago = pygame.time.get_ticks()
            if started_ago <= 1500:
                window.screen.blit(menu.load_scr, [0, 0])

            elif ball.is_alive:
                window.screen.blit(menu.line_scr, [0, 0])
                menu.text_render(menu.play_button, (window.screen.get_width() // 2, window.screen.get_height() // 2))

            else:
                window.screen.blit(menu.line_scr, [0, 0])
                menu.text_render(menu.game_over, (menu.game_over_rect.x, menu.game_over_rect.y))

                score_text = menu.create_text_field(("Your Final Score is: " + str(window.score)))
                menu.text_render(score_text, (window.screen.get_width()/3, window.screen.get_height()/1.5))
                ball.is_alive = menu.restart
                menu.restart = False

        else:
            if ball.is_alive:
                score_text = menu.create_text_field(("Score: " + str(window.score)))
                menu.text_render(score_text, (window.screen.get_width() - 150, window.screen.get_height() - 150))
                lives_text = menu.create_text_field("Lives: " + str(ball.lives))
                menu.text_render(lives_text, (window.screen.get_width() - 150, window.screen.get_height() - 100))
                ball.update(platform)
                platform.update()
                for i in range(len(bricks_list)):
                    if bricks_list[i].is_alive:
                        bricks_list[i].update(ball)
                    else:
                        if not bricks_list[i].is_scored:
                            window.score += 1
                            bricks_list[i].is_scored = True
                all_sprites.draw(window.screen)
            else:
                ball.lives = 3
                menu.opened = True

        window.clock.tick(90)
        pygame.display.flip()