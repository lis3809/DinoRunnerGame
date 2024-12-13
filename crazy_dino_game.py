import pygame as pg

import game_config
import game_config as config
from game_objects.brick import Brick
from game_objects.dino import Dino
from game_objects.kaktus import Kaktus


def load_img(name):
    img = pg.image.load(name)
    # img = img.convert()
    # colorkey = img.get_at((0, 0))
    # img.set_colorkey(colorkey)
    img = pg.transform.scale(img, config.WINDOW_SIZE)
    return img

class CrazyDinoRunnerGame():
    """Базовый класс для запуска игры"""
    def __init__(self):
        # Фон игры
        self.background = load_img("picture/desert.jpg")
        # Скорость обновления кадров
        self.__FPS = config.FPS
        self.__clock = pg.time.Clock()

        # Текущее значение очков игрока
        self.__current_player_score = 0

        # Вызываем метод инициализациии остальных параметров
        self.__init_game()

    def __init_game(self):
        # Создаем объект основного окна
        self.screen = pg.display.set_mode(game_config.WINDOW_SIZE)
        pg.display.set_caption("Космическая гонка")

        # Список всех спрайтов (графических объектов)
        self.all_sprites = pg.sprite.Group()

        # Объект игрока
        self.dino = Dino(self.screen)
        self.all_sprites.add(self.dino)

        # Будет всего три кактуса
        count_kaktus = 3
        for i in range(count_kaktus):
            # Объект астероида
            kaktus = Kaktus(self.screen)
            self.all_sprites.add(kaktus)

        # В начале игры будет всего 1 ящик
        self.count_brick = 1
        for i in range(self.count_brick):
            # Объект астероида
            brick = Brick(self.screen)
            self.all_sprites.add(brick)

    def __draw_scene(self):
        # отрисовка
        self.screen.blit(self.background, (0, 0))

        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

        # Обновляем экран
        pg.display.update()
        pg.display.flip()
        self.__clock.tick(self.__FPS)

    def run_game(self, game_is_run):
        # Основной цикл игры
        while game_is_run:
            # Обрабатываем событие закрытия окна
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

            # Отрисовываем всё
            self.__draw_scene()
