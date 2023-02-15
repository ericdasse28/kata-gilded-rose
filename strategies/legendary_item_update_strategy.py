from gilded_rose.item_update_strategy import ItemUpdateStategy


class LegendaryItemUpdateStrategy(ItemUpdateStategy):
    def update_quality(self, item):
        return item
