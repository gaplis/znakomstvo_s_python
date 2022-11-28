import sys
import pygame
import check

def run():
    pygame.init()
    size_block = 100
    margin = 15
    width = heigth = size_block*3 + margin*4

    size_window = (width, heigth)
    screen = pygame.display.set_mode(size_window)
    pygame.display.set_caption("Крестики-нолики")

    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    white = (255, 255, 255)
    array = [[0]*3 for i in range(3)]
    count = 0
    game_over = False
    current_player = 'x'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                col = x_mouse // (size_block+margin)
                row = y_mouse // (size_block+margin)
                if array[row][col] == 0:
                    if current_player == 'x':
                        array[row][col] = 'x'
                        current_player = 'o'
                    else:
                        array[row][col] = 'o'
                        current_player = 'x'
                    count+=1
            elif event.type == pygame.MOUSEBUTTONDOWN and game_over:
                game_over = False
                array = [[0]*3 for i in range(3)]
                count = 0
                screen.fill(black)
        
        if not game_over:
            for row in range(3):
                for col in range(3):
                    if array[row][col] == 'x':
                        color = red
                    elif array[row][col] == 'o':
                        color = green
                    else:
                        color = white
                    x = col*size_block + (col+1)*margin
                    y = row*size_block + (row+1)*margin
                    pygame.draw.rect(screen, color, (x,y,size_block,size_block))
                    
                    if color == red:
                        pygame.draw.line(screen, white, (x+5, y+5), (x+size_block-5, y+size_block-5), 8)
                        pygame.draw.line(screen, white, (x+size_block-5, y+5), (x+5, y+size_block-5), 8)
                    elif color == green:
                        pygame.draw.circle(screen, white, (x+size_block//2, y+size_block//2), size_block//2-3, 7)

        if current_player == 'o':
            game_over = check.check_win(array, 'x', count)
        else:
            game_over = check.check_win(array, 'o', count)

        if game_over:
            screen.fill(black)
            font = pygame.font.SysFont('stxingkai', 80)
            text1 = font.render(game_over, True, white)
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])

        pygame.display.update()