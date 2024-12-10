import math

import pygame


class Player:
    def __init__(self, screenDimensions: pygame.Vector2, heightMult: float, xPosMult: float, hexColor: str,
                 maxSpeed: int, controlMapping: dict):
        self.xPosMult = xPosMult
        self.size = pygame.Vector2(20, screenDimensions.y * heightMult)
        self.position = pygame.Vector2(
            screenDimensions.x * xPosMult - self.size.x // 2,
            (screenDimensions.y + self.size.y) // 2
        )
        self.velocityY = 0
        self.color = pygame.Color(hexColor)
        self.controlMapping = controlMapping
        self.maxSpeed = maxSpeed
        self.points = 0
        self.pRend: pygame.Surface = None
        self.pRend = pygame.font.SysFont("Monospace", 48).render(str(self.points), True, self.color)

    def increasePoint(self, font: pygame.font.Font, delta=1):
        self.points += delta
        self.pRend = font.render(str(self.points), True, self.color)

    def handleInput(self, keysPressed: dict, deltaTime: float, screenDimensions: pygame.Vector2):
        if keysPressed[self.controlMapping["up"]]:
            self.move(-1, deltaTime, screenDimensions)
        if keysPressed[self.controlMapping["down"]]:
            self.move(1, deltaTime, screenDimensions)

    def move(self, velocityNormalized: float, dt: float, screenDimensions: pygame.Vector2):
        self.velocityY = self.maxSpeed * velocityNormalized * dt
        newPosY = self.position.y + self.velocityY
        if newPosY < 0:
            newPosY = 0
            self.velocityY = 0
        elif newPosY > screenDimensions.y - self.size.y:
            newPosY = screenDimensions.y - self.size.y
            self.velocityY = 0
        self.position.y = int(newPosY)

    def render(self, target: pygame.Surface) -> None:
        pygame.draw.rect(target, self.color, pygame.Rect(self.position, self.size))

    def renderScore(self, target: pygame.Surface) -> None:
        target.blit(self.pRend, (
            target.get_width() * self.xPosMult - self.pRend.get_width() // 2,
            (target.get_height() - self.pRend.get_height()) // 2
        ))

    @staticmethod
    def createControlMapping(upKey, downKey):
        return {
            "up": upKey,
            "down": downKey
        }
