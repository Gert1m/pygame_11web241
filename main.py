import pygame
import asyncio

from handlers.key_handlers import KeyBoard

pygame.init()
pygame.display.set_caption("Game name here we go")


class GameView:
    """
    Класс обработки игрового пространства.
    """

    def __init__(self, x, y):
        self.screen = pygame.display.set_mode((x, y), flags=0)  # flags=32 убрать рамки экрана(fullscreen)

        # словарь изображений
        self.img_dict = {
            "bg": pygame.image.load("res/img/bg.png").convert_alpha()
        }

        # изменение размеров изображений
        self.img_dict["bg"] = pygame.transform.scale(self.img_dict["bg"], (x, y))

        self.keyboard = KeyBoard(img=self.img_dict, screen=self.screen)

    def start_game(self, *, isPlaying: bool, fps: int) -> None:
        """
        Функция с которой программа берёт своё начало и отлавливает все действия от пользователя.
        :param isPlaying: Запущена программа или нет.
        :param fps: С какой частотой обрабатывать информацию (кадр/с).
        :return: Окно игры
        """
        while isPlaying:
            # обработка нажатий
            keys = pygame.key.get_pressed()
            if keys[pygame.K_f]:  # клавиша F
                asyncio.run(self.keyboard.f())

            else:
                self.screen.blit(self.img_dict["bg"], (0, 0))

            pygame.display.update()  # обновление экрана
            pygame.time.Clock().tick(fps)  # кадры в секунду

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # выход из программы
                    isPlaying = False
                    pygame.quit()


if __name__ == "__main__":
    screenRatio = 3

    GameView(640 * screenRatio, 360 * screenRatio).start_game(isPlaying=True,
                                                              fps=60)  # лучшее соотношение сторон для 2д графики
