from abc import ABCMeta, abstractmethod

from gilded_rose.gilded_rose import Item


class ItemUpdateStategy(metaclass=ABCMeta):
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    @abstractmethod
    def update_quality(item: Item) -> Item:
        pass
