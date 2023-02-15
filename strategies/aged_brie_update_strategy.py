from gilded_rose.item_update_strategy import ItemUpdateStategy


class AgedBrieItemUpdateStrategy(ItemUpdateStategy):
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = min(item.quality + 2, self.MAX_QUALITY)
        else:
            item.quality = min(item.quality + 1, self.MAX_QUALITY)

        item.sell_in -= 1

        return item
