from typing import List

import pygame

from classes.aiPlayer import AIPlayer
from classes.ball import Ball
from classes.button import Button
from classes.player import Player


class PingPongGame:
    MAINMENU = 101
    GAMEPLAY = 202
    GAMEFINISH = 303

    def __init__(self):
        self._shouldclose: bool = None
        self.framesPerSecond: int = None

        self.screenDimensions: pygame.Vector2 = None
        self.display: pygame.Surface = None
        self.renderedWinText: pygame.Surface = None
        self.clock: pygame.time.Clock = None

        self.players: List[Player] = []
        self.balls: List[Ball] = []
        self.buttons: List[Button] = []

        self.font: pygame.font.Font = None
        self.gameState: int = None

        self.pointsToWin: int = None

    def run(self) -> None:
        self.startgame()
        while not self.shouldclose():
            self.mainloop()
        self.closegame()

    def startgame(self) -> None:
        pygame.init()

        self.pointsToWin = 3
        self.gameState = self.MAINMENU
        self.font = pygame.font.SysFont("Monospace", 48)
        self._shouldclose = False
        self.framesPerSecond = 75
        displayInfo = pygame.display.Info()
        self.screenDimensions = pygame.Vector2(
            int(displayInfo.current_w * 0.9),
            int(displayInfo.current_h * 0.9)
        )
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(self.screenDimensions)

        ballRadius = 10
        ballStartPos = pygame.Vector2(
            self.screenDimensions.x // 2 - ballRadius,
            self.screenDimensions.y // 2 - ballRadius
        )
        playerSpeed = displayInfo.current_h * 2 ** (-10)
        self.balls = [
            Ball(ballStartPos, None, ballRadius, "white", playerSpeed, 1.0125),
        ]

        self.buttons = [
            Button(self.screenDimensions, "blue",
                   pygame.Rect(self.screenDimensions.x // 3 - 200, self.screenDimensions.y // 2 - 75, 400, 150),
                   "One Player", self.font, Button.START_GAME_VSAI),
            Button(self.screenDimensions, "darkgreen",
                   pygame.Rect(2 * self.screenDimensions.x // 3 - 200, self.screenDimensions.y // 2 - 75, 400, 150),
                   "Two Players", self.font, Button.START_GAME_VSPLAYER)
        ]

    def mainloop(self) -> None:
        self.clock.tick(self.framesPerSecond)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._shouldclose = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.gameState = self.MAINMENU
                for b in self.balls:
                    b.resetBall(self.screenDimensions)
        frameDT = self.clock.get_time()
        if self.gameState == self.GAMEPLAY:
            self.mainloopUpdateGameplay(frameDT)
            self.mainloopRenderGameplay(frameDT)
        elif self.gameState == self.MAINMENU:
            self.mainloopUpdateMainMenu(frameDT)
            self.mainloopRenderMainMenu(frameDT)
        elif self.gameState == self.GAMEFINISH:
            self.mainloopUpdateGameFinish(frameDT)
            self.mainloopRenderGameFinish(frameDT)

    # gameplay ------------------------------------------------------------------------------------------------------- #
    def mainloopUpdateGameplay(self, frameDT: float) -> None:
        keysPressed = pygame.key.get_pressed()

        def updatePlayer(player):
            if isinstance(player, AIPlayer):
                player.handleAI(self.balls[0].position, frameDT, self.screenDimensions)
            elif isinstance(player, Player):
                player.handleInput(keysPressed, frameDT, self.screenDimensions)

        for i, player in enumerate(self.players):
            updatePlayer(player)
            if player.points >= self.pointsToWin:
                self.renderedWinText = self.font.render(f"Player {i+1} wins (ESC to return to main menu)", True,
                                                        player.color)
                self.gameState = self.GAMEFINISH

        def updateBall(ball: Ball):
            ball.handleCollision(frameDT, self.players)
            return ball.updateMovement(frameDT, self.screenDimensions)

        for ball in self.balls:
            result = updateBall(ball)
            if result == "leftWon":
                self.players[0].increasePoint(self.font)
            elif result == "rightWon":
                self.players[1].increasePoint(self.font)

    def mainloopRenderGameplay(self, frameDT: float) -> None:
        self.display.fill((0, 0, 0))
        for player in self.players:
            player.render(self.display)
            player.renderScore(self.display)
        for ball in self.balls:
            ball.render(self.display)
        pygame.display.update()

    # mainmenu ------------------------------------------------------------------------------------------------------- #
    def mainloopUpdateMainMenu(self, frameDT: float) -> None:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        for btn in self.buttons:
            if btn.isPressed(mouse_pos, mouse_pressed):
                displayInfo = pygame.display.Info()
                playerSpeed = displayInfo.current_h * 2 ** (-10)
                if btn.btnType == btn.START_GAME_VSAI:
                    self.gameState = self.GAMEPLAY
                    self.players = [
                        Player(
                            self.screenDimensions, 0.15, 0.05, "red", playerSpeed,
                            Player.createControlMapping(pygame.K_w, pygame.K_s)
                        ),
                        AIPlayer(
                            self.screenDimensions, 0.15, 0.95, "cyan", playerSpeed
                        )
                    ]
                elif btn.btnType == btn.START_GAME_VSPLAYER:
                    self.gameState = self.GAMEPLAY
                    self.players = [
                        Player(
                            self.screenDimensions, 0.15, 0.05, "red", playerSpeed,
                            Player.createControlMapping(pygame.K_w, pygame.K_s)
                        ),
                        Player(
                            self.screenDimensions, 0.15, 0.95, "green", playerSpeed,
                            Player.createControlMapping(pygame.K_UP, pygame.K_DOWN)
                        ),
                    ]

    def mainloopRenderMainMenu(self, frameDT: float) -> None:
        self.display.fill((0, 0, 0))
        for btn in self.buttons:
            btn.render(self.display)
        pygame.display.update()

    # gamefinish ----------------------------------------------------------------------------------------------------- #
    def mainloopUpdateGameFinish(self, frameDT: float) -> None:
        pass  # tu w sumie nic nie musimy robić, gracz klika ESC aby wyjść do menu

    def mainloopRenderGameFinish(self, frameDT: float) -> None:
        self.display.fill((0, 0, 0))
        self.display.blit(self.renderedWinText, (
            (self.screenDimensions.x - self.renderedWinText.get_width()) // 2,
            (self.screenDimensions.y - self.renderedWinText.get_height()) // 2
        ))
        pygame.display.update()

    def shouldclose(self) -> bool:
        return self._shouldclose

    def closegame(self) -> None:
        pygame.quit()


if __name__ == '__main__':
    PingPongGame().run()
