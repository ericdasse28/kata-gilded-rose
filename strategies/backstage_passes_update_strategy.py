from gilded_rose.item_update_strategy import ItemUpdateStategy


class BackstagePassesItemUpdateStrategy(ItemUpdateStategy):
    def update_quality(self, item):
        return item