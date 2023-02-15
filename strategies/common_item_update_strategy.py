from gilded_rose.item_update_strategy import ItemUpdateStategy


class CommonItemUpdateStrategy(ItemUpdateStategy):
    def update_quality(self, item):
        if item.sell_in <= 0:
            item.quality = max(item.quality - 2, self.MIN_QUALITY)
        else:
            item.quality = max(item.quality - 1, self.MIN_QUALITY)

        item.sell_in -= 1

        return item
