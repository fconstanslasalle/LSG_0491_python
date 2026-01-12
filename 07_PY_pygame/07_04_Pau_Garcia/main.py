import pygame

pygame.init()

# Font
font = pygame.font.Font('freesansbold.ttf', 20)
fontTimer = pygame.font.Font('freesansbold.ttf', 50)

# Screen parameters
WIDTH = 1280
HEIGHT = 760
HALF_HEIGHT = HEIGHT / 2 - 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (70, 167, 203)
GREEN = (70, 203, 100)

#Tick of the game
clock = pygame.time.Clock()    
FPS = 60

# Striker parameters
STRIKER_HEIGHT = 100
STRIKER_WIDTH = 10 
STRIKER_SPEED = 10 

# player factors
player1YFac = 0
player2YFac = 0


# Add userevent for timer
pygame.time.set_timer(pygame.USEREVENT, 1000)



# Striker class 
class Striker:
        # Constructor of the Striker class
    def __init__(self, posX, posY, width, height, speed, color):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        # Generate rect
        self.strikerRect = pygame.Rect(posX, posY, width, height)
    
     # Draw the object on the screen
    def display(self):
        self.striker = pygame.draw.rect(screen, self.color, self.strikerRect)

    #Update the player
    def update(self, yFac):
        self.posY = self.posY + self.speed*yFac
 
        # Don't allow the player to leave from the top of the screen
        if self.posY <= 0:
            self.posY = 0
        # Don't allow the player to leave from the bottom of the screen
        elif self.posY + self.height >= HEIGHT:
            self.posY = HEIGHT-self.height
 
        # Generate rect with new values
        self.strikerRect = (self.posX, self.posY, self.width, self.height)

    def getStriker(self):
        return self.strikerRect

    def displayScore(self, text, score, x, y, color):
        text = font.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)

    # reset position to half screen
    def reset(self):
        self.posY = HALF_HEIGHT
 

# Ball class
class Ball:
    # Constructor of the Ball
    def __init__(self, posX, posY, radius, speed, color):
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.scored = 1
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posX, self.posY), self.radius)
 
    # Display the object on the screen
    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.posX, self.posY), self.radius)
 
    def update(self):
        self.posX += self.speed*self.xFac
        self.posY += self.speed*self.yFac
 
        # If the ball hits the top or bottom surfaces, 
        # then the sign of yFac is changed and 
        # it results in a reflection
        if self.posY <= 0 or self.posY >= HEIGHT:
            self.yFac *= -1

         # The ball has scored or not
        if self.posX <= 0 and self.scored:
            self.scored = 0
            return 1
        elif self.posX >= WIDTH and self.scored:
            self.scored = 0
            return -1
        else:
            return 0
 
    # The ball goes to the center of the screen
    def reset(self):
        self.posX = WIDTH//2
        self.posY = HEIGHT//2
        self.xFac *= -1
        self.scored = 1
 
    # Used to reflect the ball along the X-axis
    def hit(self):
        self.xFac *= -1
 
    def getBall(self):
        return self.ball


# Game Manager
def main():
    running = True
 
    # Defining the objects
    player1 = Striker(20, HALF_HEIGHT, STRIKER_WIDTH, STRIKER_HEIGHT, STRIKER_SPEED, BLUE)
    player2 = Striker(WIDTH-30, HALF_HEIGHT, STRIKER_WIDTH, STRIKER_HEIGHT, STRIKER_SPEED, GREEN)
    ball = Ball(WIDTH//2, HEIGHT//2, 7, 7, WHITE)
    listOfPlayers = [player1, player2]
 
    # Initial parameters of the players
    # Scores
    player1Score = 0
    player2Score = 0
    # Speed
    player1YFac = 0
    player2YFac = 0

    #timer
    timerSec = 3
    timerText = fontTimer.render(str(timerSec), True, WHITE)

    # reset player positions
    player1.reset()
    player2.reset()

 
    while running:
        screen.fill(BLACK)
 
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2YFac = -1
                if event.key == pygame.K_DOWN:
                    player2YFac = 1
                if event.key == pygame.K_w:
                    player1YFac = -1
                if event.key == pygame.K_s:
                    player1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1YFac = 0
            if event.type == pygame.USEREVENT:
                if timerSec > 0:
                    timerSec -= 1
                    timerText = fontTimer.render(str(timerSec), True, WHITE)

        if timerSec > 0:
            if timerSec <= 3:
                screen.blit(timerText, (WIDTH / 2 - 10, HALF_HEIGHT))
        else:
             # Collision detection
            for player in listOfPlayers:
                if pygame.Rect.colliderect(ball.getBall(), player.getStriker()):
                    ball.hit()
    
            # Updating the objects
            player1.update(player1YFac)
            player2.update(player2YFac)
            point = ball.update()
    
            # -1 -> player 1 has scored
            # 1 -> player 2 has scored
            if point == -1:
                player1Score += 1
            elif point == 1:
                player2Score += 1
 
            # Someone has scored
            # a point and the ball is out of bounds.
            # So, we reset it's position
            if point:   
                timerSec = 4
                ball.reset()
                player1.reset()
                player2.reset()
    
        # Displaying the objects on the screen
        player1.display()
        player2.display()
        ball.display()
        

        # Displaying the scores of the players
        player1.displayScore("Player 1: ", player1Score, 100, 20, BLUE)
        player2.displayScore("Player 2: ", player2Score, WIDTH-100, 20, GREEN)
      
 
        pygame.display.update()
        clock.tick(FPS)    

if __name__ == '__main__':
    main()
    pygame.quit()