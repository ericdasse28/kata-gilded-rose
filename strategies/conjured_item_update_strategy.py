from gilded_rose.item_update_strategy import ItemUpdateStategy


class ConjuredItemUpdateStrategy(ItemUpdateStategy):
    def update_quality(self, item):
        return item
