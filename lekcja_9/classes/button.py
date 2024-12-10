import pygame


class Button:
    START_GAME_VSAI = 101
    START_GAME_VSPLAYER = 202

    def __init__(self, screenDimensions: pygame.Vector2, hexColor: str, rect: pygame.Rect, text: str, font: pygame.font.Font, btnType: int):
        self.screenDimensions = screenDimensions
        self.color = pygame.color.Color(hexColor)
        self.rect = rect
        self.text = text
        self.btnType = btnType
        self.renderedText = font.render(self.text, True, "#FFFFFF")

    def render(self, target: pygame.Surface):
        pygame.draw.rect(target, self.color, self.rect)
        target.blit(self.renderedText, (
            self.rect.x + (self.rect.width - self.renderedText.get_width()) // 2,
            self.rect.y + (self.rect.height - self.renderedText.get_height()) // 2
        ))

    def isPressed(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and any(mouse_pressed)
