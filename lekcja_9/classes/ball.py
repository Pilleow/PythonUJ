import random
from typing import List

import pygame
from classes.player import Player


class Ball:
    def __init__(self, startPos: pygame.Vector2, startVelocity: pygame.Vector2, radius: int, hexColor: str,
                 maxSpeed: int, maxSpeedMult: float):
        self.radius = radius
        self.position = startPos
        self.velocity = startVelocity
        self.color = pygame.Color(hexColor)
        self.originalMaxSpeed = maxSpeed
        self.maxSpeed = 0
        self.maxSpeedMultiplier = maxSpeedMult

        if self.velocity is None:
            self.velocity = pygame.Vector2(random.choice([-1, 1]), random.uniform(-1, 1))
        self.velocity = self.velocity.normalize()

    def handleCollision(self, deltaTime: float, players: List[Player]):
        plBall = pygame.Rect(self.position.x - self.radius, self.position.y - self.radius, self.radius * 2,
                             self.radius * 2)
        for pl in players:
            plRect = pygame.Rect(pl.position.x, pl.position.y, pl.size.x, pl.size.y)
            if plRect.colliderect(plBall):
                self.velocity.x = 1 if self.velocity.x < 0 else -1
                self.velocity.y = random.uniform(-1, 1)
                self.move(self.velocity, deltaTime, pygame.Vector2(2 ** 16, 2 ** 16))
                self.maxSpeed *= self.maxSpeedMultiplier
                self.velocity = self.velocity.normalize()
                break

    def updateMovement(self, deltaTime: float, screenDimensions: pygame.Vector2):
        if self.maxSpeed < self.originalMaxSpeed:
            self.maxSpeed += 0.01
            if self.maxSpeed > self.originalMaxSpeed:
                self.maxSpeed = self.originalMaxSpeed
        return self.move(self.velocity, deltaTime, screenDimensions)

    def move(self, velocityNormalized: pygame.Vector2, dt: float, screenDimensions: pygame.Vector2):
        newPosY = self.position.y + self.maxSpeed * velocityNormalized.y * dt
        if newPosY < self.radius or newPosY > screenDimensions.y - self.radius:
            self.velocity.y *= -1
        else:
            self.position.y = int(newPosY)
        newPosX = self.position.x + self.maxSpeed * velocityNormalized.x * dt
        self.position.x = int(newPosX)

        if newPosX < -self.radius * 2:
            self.resetBall(screenDimensions)
            return "rightWon"
        elif newPosX > screenDimensions.x:
            self.resetBall(screenDimensions)
            return "leftWon"
        return None

    def resetBall(self, screenDimensions: pygame.Vector2):
        self.velocity = pygame.Vector2(random.choice([-1, 1]), random.uniform(-0.6, 0.6))
        self.position.x = screenDimensions.x // 2 - self.radius
        self.position.y = screenDimensions.y // 2 - self.radius
        self.maxSpeed = 0

    def render(self, target: pygame.Surface) -> None:
        pygame.draw.circle(target, self.color, self.position, self.radius)
