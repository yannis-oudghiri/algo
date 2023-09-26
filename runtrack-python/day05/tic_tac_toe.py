import pygame

pygame.init()

game_over = False
font = pygame.font.Font(None, 36)
winner = 0

def get_case(x,y):
    if 0 <= x <200 and 0 <= y <200:
        return [0,0]
    if 200 <= x <400 and 0 <= y <200:
        return [1,0]
    if  x >= 400 and 0 <= y <200:
        return [2,0]
    if 0 <= x <200 and 200 <= y <400:
        return [0,1]
    if 200 <= x <400 and 200 <= y <400:
        return [1,1]
    if  x >= 400 and 200 <= y <400:
        return [2,1]
    if 0 <= x <200 and 400 <= y:
        return [0,2]
    if 200 <= x <400 and 400 <= y:
        return [1,2]
    if  x >= 400 and 400 <= y:
        return [2,2]

def draw_circles(morpion):
    for i in range(3):
        for j in range(3):
            if morpion.grid[i][j] == 1:
                pygame.draw.circle(screen, blue, (100 + 200*i,100 + 200*j), 75, width=15)

def draw_cross(morpion):
    for i in range(3):
        for j in range(3):
            if morpion.grid[i][j] == 2:
                pygame.draw.line(screen, red, (30 + 200*i,170 + 200*j), (170 + 200*i,30 + 200*j), width=30)
                pygame.draw.line(screen, red, (30 + 200*i,30 + 200*j), (170 + 200*i,170 + 200*j), width=30)


class Morpion():
    def __init__(self):
        self.grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = 1

    def __str__(self):
        string = ''
        for i in range(3):
            line = ''
            for j in range(3):
                line += str(self.grid[i][j]) + ' '
            string += line + '\n'
        return string
    
    def play(self,x,y):
        if self.grid[x][y] == 0:
            self.grid[x][y] = self.player
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1

    def win(self,player):
        for i in range(3):
            if self.grid[i] == [player,player,player]:
                return 'win'
        for j in range(3):
            if self.grid[i] == [player,player,player]:
                return 'win'
        if [self.grid[0][0],self.grid[1][1],self.grid[2][2]] == [player,player,player]:
                return 'win'
        if [self.grid[2][0],self.grid[1][1],self.grid[0][2]] == [player,player,player]:
                return 'win'

    def full(self):
        n_zero = 0
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 0:
                    n_zero += 1
        if n_zero == 0:
            return 'full'
morpion = Morpion()

# Set up the drawing window

screen = pygame.display.set_mode([600, 600])
blue = pygame.Color(0, 0, 255)
grey = pygame.Color(96, 96, 96)
red = pygame.Color(255, 0, 0)


# Run until the user asks to quit

running = True

while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:
                x,y = pygame.mouse.get_pos()
                [i,j] = get_case(x,y)
                morpion.play(i,j)
                print(morpion)
                


    # Fill the background with white

    screen.fill((255, 255, 255))

    if not game_over:
        # Draw a solid blue circle in the center

        pygame.draw.line(screen, grey, (200,0), (200,600),3)
        pygame.draw.line(screen, grey, (400,0), (400,600),3)
        pygame.draw.line(screen, grey, (0,200), (600,200),3)
        pygame.draw.line(screen, grey, (0,400), (600,400),3)

        draw_circles(morpion)
        draw_cross(morpion)

        x,y = pygame.mouse.get_pos()
        text = str(get_case(x,y))
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(text, False, (0, 0, 0))
        screen.blit(text_surface, (0,0))

        if morpion.win(1) == 'win':
            game_over = True
            winner = 1
        if morpion.win(2) == 'win':
            game_over = True
            winner = 2
        if morpion.full() == 'full':
            game_over = True
        # Flip the display

        pygame.display.flip()

    if game_over:
        if winner == 0:
            text = 'It is a tie'
            my_font = pygame.font.SysFont('Calibri', 100)
            text_surface = my_font.render(text, False, (0, 0, 0))
            screen.blit(text_surface, (100,200))
            pygame.display.flip()
        else:
            text1 = f'The Player {winner}'
            text2 = 'is the winner !!!'
            my_font = pygame.font.SysFont('Calibri', 80)
            text_surface1 = my_font.render(text1, False, (0, 0, 0))
            screen.blit(text_surface1, (100,200))
            text_surface2 = my_font.render(text2, False, (0, 0, 0))
            screen.blit(text_surface2, (100,250))
            pygame.display.flip()
# Done! Time to quit.

pygame.quit()
