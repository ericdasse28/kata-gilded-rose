from gilded_rose import Item
from item_update_strategy import ItemUpdateStategy


class ItemUpdater:
    def __init__(self, item_update_strategy: ItemUpdateStategy):
        self.item_update_strategy = item_update_strategy

    def update_quality(self, item: Item) -> Item:
        return self.item_update_strategy.update_quality(item)
