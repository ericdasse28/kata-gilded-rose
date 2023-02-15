from abc import ABCMeta, abstractmethod


class ItemUpdateStategy(metaclass=ABCMeta):
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    @abstractmethod
    def update_quality(item):
        pass
