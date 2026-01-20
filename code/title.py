import pygame
from settings import *

class Title:
    def __init__(self, surface):
        self.display_surface = surface
        
        self.bg_images = []
        for i in range(1, 8):
            bg_image = pygame.transform.scale(pygame.image.load(join('graphics', 'background', f'bg_{i}.png')).convert_alpha(), (WIDTH, HEIGHT))
            self.bg_images.append(bg_image)
        
        self.bg_width = WIDTH
        self.tiles = 2
        self.scroll_values = [0] * len(self.bg_images)
        
        self.font_title = pygame.font.Font(UI_FONT, 64)
        self.font_instr = pygame.font.Font(UI_FONT, 32)
        
        self.title_text = "The Legend of Zelda"
        self.instr_text = "Press SPACE to Start"
        
        self.title_surface = self.create_outlined_text(self.title_text, self.font_title, TEXT_COLOR)
        self.instr_surface = self.create_outlined_text(self.instr_text, self.font_instr, TEXT_COLOR)
        
        self.title_rect = self.title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
        self.instr_rect = self.instr_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    
    def create_outlined_text(self, text, font, color, outline_color = OUTLINE_COLOR, outline_width = OUTLINE_WIDTH):
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
        for idx, i in enumerate(self.bg_images):
            speed = 0.5 + (0.25 * idx)
            self.scroll_values[idx] += speed
            
            for x in range(self.tiles):
                self.display_surface.blit(i, ((x * self.bg_width) - self.scroll_values[idx], 0))
                self.display_surface.blit(i, ((x * self.bg_width) - self.scroll_values[idx] + self.bg_width, 0))
            
            if self.scroll_values[idx] >= self.bg_width:
                self.scroll_values[idx] = 0
        
        self.display_surface.blit(self.title_surface, self.title_rect)
        self.display_surface.blit(self.instr_surface, self.instr_rect)