
import pygame
import sys
from pygame import color
import random 

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 32)

# Textbox properties
textbox_width = 400
textbox_height = 40
textbox_rect = pygame.Rect((WIDTH - textbox_width) // 2, (HEIGHT - textbox_height) // 2, textbox_width, textbox_height)
textbox_color = WHITE
text_color = WHITE
text = ''
cursor_visible = True
cursor_timer = 0

tentativas =  6 
mensagem = f'Tentativas: {tentativas}'
text_font = pygame.font.SysFont('Arial', 24, True, True)
text_format = text_font.render(mensagem, True, (0,255,0))
text_rect = text_format.get_rect()
random_word = random.choice(words)
quantidade_caracteres = len(random_word)
mensagem1 = f'Quantidade letras: {quantidade_caracteres}'
text_font1 = pygame.font.SysFont('Arial', 24, True, True)
text_format1 = text_font1.render(mensagem1, True, (255,0,0))
text_rect1 = text_format1.get_rect()
print(random_word)

hangman_index = 0


# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_RETURN:
                palavra_digitada = text
                text = ''
                if palavra_digitada == random_word:
                    
                    mensagem_vitoria = "Você ganhou!"
                    text_format_vitoria = text_font.render(mensagem_vitoria, True, (0,255,0))
                    text_rect_vitoria = text_format_vitoria.get_rect()
                    print(f"{mensagem_vitoria}")
                    
                    
                else : 
                    print("Voce perdeu uma tentativa")  
                    tentativas = tentativas - 1
                    hangman_index += 1 
                    print(f"{tentativas}") 
                    
                      
            else:
                text += event.unicode
    if(tentativas == 6):
     pic_lines = HANGMANPICS[0].split('\n')
     for i, line in enumerate(pic_lines):
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (320, 50 + i * 20)) 
    
    elif(tentativas < 6):
         pic_lines = HANGMANPICS[hangman_index].split('\n')
         for i, line in enumerate(pic_lines):
          hangman_surface = font.render(line, True, WHITE)
          screen.blit(hangman_surface, (320, 50 + i * 20))
    else:
        print(f"jogo terminado")     
      
    # Draw textbox
    pygame.draw.rect(screen, textbox_color, textbox_rect, 2)
    rendered_text = font.render(text, True, text_color)
    screen.blit(rendered_text, (textbox_rect.x + 5, textbox_rect.y + 5))

    # Draw cursor
    if cursor_visible:
        cursor_rect = pygame.Rect(textbox_rect.x + 5 + rendered_text.get_width(), textbox_rect.y + 5, 2, rendered_text.get_height())
        pygame.draw.rect(screen, BLACK, cursor_rect)

    # Update the display
    # Control cursor visibility
    if pygame.time.get_ticks() - cursor_timer > 500:
        cursor_visible = not cursor_visible
        cursor_timer = pygame.time.get_ticks()
    
     
    text_format = text_font.render(f'Tentativas: {tentativas}', True, (0, 255, 0))
    screen.blit(text_format, (10, 10))
    showLetters = text_font.render(f'Quantidade de letras: {quantidade_caracteres}', True, (0, 255, 0))
    screen.blit(text_format1, (550, 10))
   
        
     

    if(tentativas == 0):
      pygame.quit()
         
    
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()