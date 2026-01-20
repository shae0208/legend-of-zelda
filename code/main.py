import pygame, sys
from settings import *
from level import Level
from title import Title
from restart import Restart

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("The Legend of Zelda")
        icon = pygame.image.load(join('graphics', 'icon', 'icon.png'))
        pygame.display.set_icon(icon)
        
        self.clock = pygame.time.Clock()
        self.title = Title(self.screen)
        self.restart = Restart(self.screen)
        self.level = None
        self.game_started = False
        self.game_over = False
        
        main_sound = pygame.mixer.Sound(join('audio', 'main.ogg'))
        main_sound.set_volume(0.5)
        main_sound.play(-1)
    
    def run(self):
        while True:            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not self.game_started:
                        self.game_started = True
                        self.game_over = False
                        self.level = Level()
                    
                    if event.key == pygame.K_SPACE and self.game_over:
                        self.game_started = True
                        self.game_over = False
                        self.level = Level()
                    
                    if self.game_started and not self.game_over and event.key == pygame.K_c:
                        self.level.toggle_menu()
            
            if not self.game_started:
                self.title.display()
            elif self.game_over:
                self.restart.display()
            else:
                self.screen.fill(WATER_COLOR)
                self.level.run()
                
                if self.level.player.health <= 0:
                    self.game_over = True
            
            pygame.display.update()
            
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    
    game.run()
