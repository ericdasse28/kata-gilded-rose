from gilded_rose.item_update_strategy import ItemUpdateStategy


class ConjuredItemUpdateStrategy(ItemUpdateStategy):
    def update_quality(self, item):
        item.quality = max(item.quality - 2, self.MIN_QUALITY)
        item.sell_in -= 1
        return item
