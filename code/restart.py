import pygame
from settings import *

class Restart:
    def __init__(self, surface):
        self.display_surface = surface
        
        self.font_title = pygame.font.Font(UI_FONT, 80)
        self.font_instr = pygame.font.Font(UI_FONT, 40)
        
        self.title_text = "GAME OVER"
        self.instr_text = "Press SPACE to Restart"
        
        self.title_surface = self.create_outlined_text(self.title_text, self.font_title, (255, 0, 0))
        self.instr_surface = self.create_outlined_text(self.instr_text, self.font_instr, TEXT_COLOR)
        
        self.title_rect = self.title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 80))
        self.instr_rect = self.instr_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80))
    
    def create_outlined_text(self, text, font, color, outline_color=(0, 0, 0), outline_width=3):
        outline_surface = pygame.Surface((font.size(text)[0] + outline_width * 2, 
                                         font.size(text)[1] + outline_width * 2), pygame.SRCALPHA)
        
        outline_text = font.render(text, True, outline_color)
        
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    outline_surface.blit(outline_text, (outline_width + dx, outline_width + dy))
        
        main_text = font.render(text, True, color)
        
        outline_surface.blit(main_text, (outline_width, outline_width))
        
        return outline_surface
    
    def display(self):
        self.display_surface.blit(self.title_surface, self.title_rect)
        self.display_surface.blit(self.instr_surface, self.instr_rect)
