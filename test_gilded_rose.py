# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        assert items[0].name == "foo"

    def test_update_quality_should_decrease_quality_when_it_is_a_normal_item(
        self,
    ):
        normal_items = [
            Item(name="foo", sell_in=12, quality=13),
            Item(name="bar", sell_in=14, quality=4),
            Item(name="foobar", sell_in=2, quality=45),
        ]
        gilded_rose = GildedRose(normal_items)
        initial_qualities = [item.quality for item in normal_items]

        gilded_rose.update_quality()

        for i, item in enumerate(normal_items):
            former_quality = initial_qualities[i]
            assert item.quality == former_quality - 1

    def test_item_quality_never_becomes_negative(self):
        items = [
            Item(name="foo", sell_in=3, quality=0),
            Item(name="bar", sell_in=-14, quality=0),
        ]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        for item in items:
            assert item.quality == 0

    def test_update_quality_should_increase_item_quality_when_it_is_aged_brie(self):
        items = [
            Item(name="Aged Brie", sell_in=12, quality=13),
            Item(name="foo", sell_in=14, quality=4),
            Item(name="Aged Brie", sell_in=2, quality=45),
        ]
        aged_bries = [item for item in items if item.name == "Aged Brie"]
        initial_aged_bries_qualities = [aged_brie.quality for aged_brie in aged_bries]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        for i, aged_brie in enumerate(aged_bries):
            former_quality = initial_aged_bries_qualities[i]
            assert aged_brie.quality == former_quality + 1

    def test_update_quality_decrease_sell_in_for_items_other_than_sulfuras(self):
        items = [
            Item(name="foo", sell_in=12, quality=13),
            Item(name="bar", sell_in=14, quality=4),
            Item(name="foobar", sell_in=2, quality=45),
            Item(name="Aged Brie", sell_in=1, quality=1),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=3, quality=5),
        ]
        gilded_rose = GildedRose(items)
        former_sell_ins = [item.sell_in for item in items]

        gilded_rose.update_quality()

        for i, item in enumerate(items):
            if item.name != "Sulfuras, Hand of Ragnaros":
                former_sell_in = former_sell_ins[i]
                assert item.sell_in == former_sell_in - 1

    def test_update_quality_should_decrease_normal_item_quality_twice_as_fast_when_sell_by_has_passed(
        self,
    ):
        normal_items = [
            Item(name="foo", sell_in=0, quality=13),
            Item(name="bar", sell_in=-14, quality=4),
            Item(name="foobar", sell_in=-2, quality=45),
        ]
        gilded_rose = GildedRose(normal_items)
        initial_qualities = [item.quality for item in normal_items]

        gilded_rose.update_quality()

        for i, item in enumerate(normal_items):
            former_quality = initial_qualities[i]
            assert item.quality == former_quality - 2


if __name__ == "__main__":
    unittest.main()
