import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
        pygame.display.set_caption('UN Valley')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.menu_active = True
        self.menu_bg = pygame.image.load('graphics\world\menu_bg.webp')
        self.menu_bg = pygame.transform.scale(self.menu_bg, (SCREEN_WIDHT, SCREEN_HEIGHT))
        
    def show_menu(self):
        font_title = pygame.font.Font(None, 80)
        font_option = pygame.font.Font(None, 40)
        
        title_text = font_title.render('UN Valley', True, (255, 223, 0))
        start_text = font_option.render('▶ Press ENTER to Start', True, (255, 255, 255))
        quit_text = font_option.render('✖ Press ESC to Quit', True, (255, 255, 255))
        
        title_rect = title_text.get_rect(center=(SCREEN_WIDHT // 2, 120))
        start_rect = start_text.get_rect(center=(SCREEN_WIDHT // 2, 300))
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDHT // 2, 380))
        
        while self.menu_active:
            self.screen.blit(self.menu_bg, (0, 0))
            
            # Semi-transparent overlay
            overlay = pygame.Surface((SCREEN_WIDHT, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))  # Dark translucent background
            self.screen.blit(overlay, (0, 0))
            
            self.screen.blit(title_text, title_rect)
            self.screen.blit(start_text, start_rect)
            self.screen.blit(quit_text, quit_rect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.menu_active = False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            pygame.display.update()

    def run(self):
        self.show_menu()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt = self.clock.tick()/1000
            self.level.run(dt)
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()
