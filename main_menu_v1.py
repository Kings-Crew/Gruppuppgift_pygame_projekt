import pygame
import sys
from button_v1 import Button
from main import Main
pygame.init()

#// RECT eller rect = rectangle \\#
#// POS eller pos = position \\#
#// options,play och quit rect är bara en transparent bild \\#

# Längst upp i vänstra hörnet i spelfönstret kommer det stå: Menu
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("DashLack Breakout")

#Variabel för bakgrund
BG = pygame.image.load("assets/Background.png")


def get_font(size):  # Returnerar tryck-på-start sekvensen i önskad storlek
    return pygame.font.Font("assets/font.ttf", size)

#--------------------------------------------------------------------------
#Denna funktion är enbart en placholder för när man trycker på knappen play
def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        #När du anropar play() så kommer du se denna text
        PLAY_TEXT = get_font(45).render(
            "This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        #När du anropar play() så kommer du till denna knapp
        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
#--------------------------------------------------------------------------

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()  #Hämtar position för musen om den är på options

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render(
            "This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))         #rectangeln som är runt texten för options
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)                         #Lägger upp texten och rectangeln för Options

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        #Ändrar färg på options om muspekaren svävar över knappen
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)
        #Går tillbacka till huvudmenyn om back har blivit klickad eller avslutar spelet om exit knappen blivit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        #// Dessa knappar kommer att dyka upp på skärmen
        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        #\\ 

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        #Lägger in knapparna i en loop så att förändring av färgerna på knapparna så att de på ett dynamiskt sätt förändras
        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        #Knapparna läggs in i en event loop på så vis 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()                                          #Anropa denna funktion för att komma till spelsekvensen: Main.main()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
        main_menu()
