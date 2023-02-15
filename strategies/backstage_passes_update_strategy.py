from gilded_rose.item_update_strategy import ItemUpdateStategy


class BackstagePassesItemUpdateStrategy(ItemUpdateStategy):
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = 0
        elif item.sell_in <= 5:
            item.quality = min(item.quality + 3, self.MAX_QUALITY)
        elif item.sell_in <= 10:
            item.quality = min(item.quality + 2, self.MAX_QUALITY)
        else:
            item.quality = min(item.quality + 1, self.MAX_QUALITY)

        item.sell_in -= 1

        return item
