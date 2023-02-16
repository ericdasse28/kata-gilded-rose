# -*- coding: utf-8 -*-


from gilded_rose.item_updater import ItemUpdater
from strategies.aged_brie_update_strategy import AgedBrieItemUpdateStrategy
from strategies.backstage_passes_update_strategy import (
    BackstagePassesItemUpdateStrategy,
)
from strategies.common_item_update_strategy import CommonItemUpdateStrategy
from strategies.conjured_item_update_strategy import ConjuredItemUpdateStrategy
from strategies.legendary_item_update_strategy import LegendaryItemUpdateStrategy


class GildedRose(object):
    def __init__(self, items):
        self.items = items
        self._strategies = {
            "Aged Brie": AgedBrieItemUpdateStrategy(),
            "Backstage passes": BackstagePassesItemUpdateStrategy(),
            "Legendary": LegendaryItemUpdateStrategy(),
            "Conjured": ConjuredItemUpdateStrategy(),
            "Common": CommonItemUpdateStrategy(),
        }
        self._item_updater = ItemUpdater(
            item_update_strategy=self._strategies["Common"]
        )

    def update_quality(self):
        strategy_book = {
            "Aged Brie": self._strategies["Aged Brie"],
            "Backstage passes to a TAFKAL80ETC concert": self._strategies[
                "Backstage passes"
            ],
            "Sulfuras, Hand of Ragnaros": self._strategies["Legendary"],
            "Conjured Mana Cake": self._strategies["Conjured"],
        }

        for item in self.items:
            self._item_updater.item_update_strategy = strategy_book.get(
                item.name, self._strategies["Common"]
            )

            item = self._item_updater.update_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
