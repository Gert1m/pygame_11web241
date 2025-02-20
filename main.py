from sys import flags

import pygame
import asyncio

pygame.init()

x, y = (640, 360)  # лучшее соотношение сторон для 2д графики
pygame.display.set_caption("Game name here we go")
screen = pygame.display.set_mode((x * 2, y * 2), flags=32)  # flags=32 убрать рамки экрана(fullscreen)


def start_game(*, isPlaying: bool, fps: int) -> None:
    """
    Функция с которой программа берёт своё начало и отлавливает все действия от пользователя.
    :param isPlaying: Запущена программа или нет.
    :param fps: С какой частотой обрабатывать информацию (кадр/с).
    :return: Окно игры
    """
    while isPlaying:
        screen.fill((0, 0, 0))
        pygame.display.update()

        # обработка нажатий
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            screen.fill((255, 255, 255))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isPlaying = False
                pygame.quit()

        pygame.time.delay(1000 // fps)


if __name__ == "__main__":
    start_game(isPlaying=True, fps=240)
