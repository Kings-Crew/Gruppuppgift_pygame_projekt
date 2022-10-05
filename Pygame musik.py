# musik for pygame

#bakground musik
from pygame import mixer_music

pygame.mixer.music.load('Sounds/hk.mp3')  # Sounds/hk.mp3 är ett exempel med här ska man tala om i vilken mapp samt vilken ljudfil. Path med andra ord
pygame.mixer.music.play('Loops=-1') # Denna rad gör att låter hela tiden spelar i oandlighet, det är -1 som bidrar att det spelar om och om igen men här skulle man även kunna välja ett bestämst antal gånger som låten ska spelas, tex max 2 eller 3 gånger. 
pygame.mixer.music.set_volume(0.5) # Man kan skriva in ett värde mellan 0-1, detta styr volymen som ljudet ska spelas och innebär inte att använderar kan välja ljudnivå. 

#sound buttons
namn_på_knapp1 = pygame.mixer.sound('kanpp1.mp3') #fyll i rätt path
namn_på_knapp2 = pygame.mixer.sound('knapp2.mp3') #ljud för nästa knapp med rätt path osv. 

# I nästa steg ska dessa rader lägga in i while true kodblock

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if namn_på_knapp1.checkForInput(pygame.mouse.get_pos())
                namn_på_knapp1.play()
            if namn_på_knapp2.checkForInput(pygame.mouse.get_pos())
                namn_på_knapp2.play()

# ljud för att skjuta
skott_ljud = pygame.mixer.sound('ljud.mp3')
skott_ljud.play()


# ljud för skott som träffar mål
träff_ljud = pygame.mixer.sound('ljud.mp3')
träff_ljud.play()

#bakgrundsbild
BG = pygame.image.load("") 



# Sound effects - https://freesound.org/
# Background music - https://incompetech.filmmusic.io/
# Sound effect and music - https://opengameart.org/

