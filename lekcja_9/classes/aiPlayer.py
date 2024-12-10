import random

import pygame
from classes.player import Player


class AIPlayer(Player):
    def __init__(self, screenDimensions: pygame.Vector2, heightMult: float, xPosMult: float, hexColor: str,
                 maxSpeed: int):
        super().__init__(screenDimensions, heightMult, xPosMult, hexColor, maxSpeed, {})
        self.errorMargin = 50
        self.reflexDelay = 1.5
        self.timeSinceLastUpdate = 0

    def trackBall(self, ballPosition: pygame.Vector2, deltaTime: float, screenDimensions: pygame.Vector2):
        self.timeSinceLastUpdate += deltaTime
        if self.timeSinceLastUpdate < self.reflexDelay:
            return
        self.timeSinceLastUpdate = 0

        targetY = ballPosition.y + random.uniform(-self.errorMargin, self.errorMargin)

        if targetY < self.position.y:
            self.move(-1, deltaTime, screenDimensions)
        elif targetY > self.position.y + self.size.y:
            self.move(1, deltaTime, screenDimensions)

    def handleAI(self, ballPosition: pygame.Vector2, deltaTime: float, screenDimensions: pygame.Vector2):
        self.trackBall(ballPosition, deltaTime, screenDimensions)
