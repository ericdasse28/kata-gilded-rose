# -*- coding: utf-8 -*-
import unittest

import pytest

from gilded_rose.gilded_rose import Item, GildedRose


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

    def test_item_quality_is_never_above_50(self):
        items = [
            Item(name="Aged Brie", sell_in=12, quality=50),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=2, quality=50),
        ]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        for item in items:
            assert item.quality == 50

    def test_sulfuras_items_quality_never_drops(self):
        sulfura_items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=3, quality=5),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=3, quality=15),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=3, quality=45),
        ]
        former_qualities = [item.quality for item in sulfura_items]
        gilded_rose = GildedRose(sulfura_items)

        gilded_rose.update_quality()

        for i, item in enumerate(sulfura_items):
            former_quality = former_qualities[i]
            assert item.quality == former_quality

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

    def test_update_quality_never_decreases_sulfura_items_sell_in(self):
        sulfura_items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=3, quality=5),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=13, quality=5),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=4, quality=5),
        ]
        former_sell_ins = [item.quality for item in sulfura_items]
        gilded_rose = GildedRose(sulfura_items)

        gilded_rose.update_quality()

        for i, item in enumerate(sulfura_items):
            former_sell_in = former_sell_ins[i]
            assert item.quality == former_sell_in

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

    def test_backstage_passes_quality_increase_by_1_when_there_are_more_than_10_sell_in_days_left(
        self,
    ):
        backstage_passes_items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=13
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=11, quality=4
            ),
        ]
        former_qualities = [item.quality for item in backstage_passes_items]
        gilded_rose = GildedRose(backstage_passes_items)

        gilded_rose.update_quality()

        for i, item in enumerate(backstage_passes_items):
            former_quality = former_qualities[i]
            assert item.quality == former_quality + 1

    def test_backstage_passes_quality_increase_by_2_when_there_are_between_6_and_10_sell_in_days(
        self,
    ):
        backstage_passes_items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=13
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=4
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=4
            ),
        ]
        former_qualities = [item.quality for item in backstage_passes_items]
        gilded_rose = GildedRose(backstage_passes_items)

        gilded_rose.update_quality()

        for i, item in enumerate(backstage_passes_items):
            former_quality = former_qualities[i]
            assert item.quality == former_quality + 2

    def test_backstage_passes_increase_by_3_when_there_are_5_or_less_sell_in_days_left(
        self,
    ):
        backstage_passes_items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=13
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=4
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=4
            ),
        ]
        former_qualities = [item.quality for item in backstage_passes_items]
        gilded_rose = GildedRose(backstage_passes_items)

        gilded_rose.update_quality()

        for i, item in enumerate(backstage_passes_items):
            former_quality = former_qualities[i]
            assert item.quality == former_quality + 3

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        backstage_passes_items = [
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=13
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=4
            ),
            Item(
                name="Backstage passes to a TAFKAL80ETC concert", sell_in=-15, quality=4
            ),
        ]
        gilded_rose = GildedRose(backstage_passes_items)

        gilded_rose.update_quality()

        for i, item in enumerate(backstage_passes_items):
            assert item.quality == 0


class TestCommonItems:
    @pytest.mark.parametrize("initial_sell_in", [6, 7, 8, 0, -2])
    def test_sell_in_should_decrease_after_update(self, initial_sell_in):
        gilded_rose = GildedRose([Item(name="foo", sell_in=initial_sell_in, quality=2)])

        gilded_rose.update_quality()

        actual_sell_in = gilded_rose.items[0].sell_in
        assert actual_sell_in == initial_sell_in - 1

    @pytest.mark.parametrize("initial_quality", [8, 7, 6, 9, 1, 49])
    def test_quality_should_decrease_after_update(self, initial_quality):
        gilded_rose = GildedRose([Item(name="bar", sell_in=7, quality=initial_quality)])

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == initial_quality - 1

    @pytest.mark.parametrize("initial_quality", [8, 7, 6, 9, 2, 49])
    def test_quality_should_decrease_twice_as_fast_after_sell_by(self, initial_quality):
        gilded_rose = GildedRose(
            [Item(name="foobar", sell_in=0, quality=initial_quality)]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == initial_quality - 2

    def test_quality_never_becomes_negative(self):
        gilded_rose = GildedRose([Item(name="foobar", sell_in=3, quality=0)])

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == 0


class TestAgedBrieItems:
    @pytest.mark.parametrize("initial_sell_in", [6, 7, 8, 0, -2])
    def test_sell_in_should_decrease(self, initial_sell_in):
        gilded_rose = GildedRose(
            [Item(name="Aged Brie", sell_in=initial_sell_in, quality=2)]
        )

        gilded_rose.update_quality()

        actual_sell_in = gilded_rose.items[0].sell_in
        assert actual_sell_in == initial_sell_in - 1

    @pytest.mark.parametrize("initial_quality", [8, 7, 6, 9, 2, 49])
    def test_quality_should_increase_after_update(self, initial_quality):
        gilded_rose = GildedRose(
            [Item(name="Aged Brie", sell_in=7, quality=initial_quality)]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == initial_quality + 1

    def test_quality_is_never_above_50(self):
        gilded_rose = GildedRose([Item(name="Aged Brie", sell_in=7, quality=50)])

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == 50


class TestSulfuraItems:
    @pytest.mark.parametrize("initial_sell_in", [6, 7, 8, 0, -2])
    def test_sell_in_never_changes(self, initial_sell_in):
        gilded_rose = GildedRose(
            [
                Item(
                    name="Sulfuras, Hand of Ragnaros",
                    sell_in=initial_sell_in,
                    quality=2,
                )
            ]
        )

        gilded_rose.update_quality()

        actual_sell_in = gilded_rose.items[0].sell_in
        assert actual_sell_in == initial_sell_in

    @pytest.mark.parametrize("initial_quality", [8, 7, 6, 9, 2, 49])
    def test_quality_never_changes(self, initial_quality):
        gilded_rose = GildedRose(
            [
                Item(
                    name="Sulfuras, Hand of Ragnaros",
                    sell_in=7,
                    quality=initial_quality,
                )
            ]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == initial_quality


class TestBackstagePasses:
    @pytest.mark.parametrize("initial_sell_in", [6, 7, 8, 0, -2])
    def test_sell_in_should_decrease(self, initial_sell_in):
        gilded_rose = GildedRose(
            [Item(name="Conjured Mana Cake", sell_in=initial_sell_in, quality=2)]
        )

        gilded_rose.update_quality()

        actual_sell_in = gilded_rose.items[0].sell_in
        assert actual_sell_in == initial_sell_in - 1

    @pytest.mark.parametrize(
        "sell_in, initial_quality",
        [(11, 8), (15, 7), (13, 6), (17, 9), (25, 2), (14, 49)],
    )
    def test_quality_should_increase_by_1_after_update_when_sell_in_is_above_10(
        self, sell_in, initial_quality
    ):
        gilded_rose = GildedRose(
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=sell_in,
                    quality=initial_quality,
                )
            ]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == initial_quality + 1

    @pytest.mark.parametrize(
        "sell_in, initial_quality",
        [(10, 8), (6, 7), (7, 6), (8, 9), (9, 2), (7, 48)],
    )
    def test_quality_should_increase_by_2_after_update_when_sell_in_is_between_6_and_10(
        self, sell_in, initial_quality
    ):
        gilded_rose = GildedRose(
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=sell_in,
                    quality=initial_quality,
                )
            ]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == initial_quality + 2

    @pytest.mark.parametrize(
        "sell_in, initial_quality",
        [(5, 8), (4, 7), (3, 6), (2, 9), (1, 2), (3, 47)],
    )
    def test_quality_should_increase_by_3_after_update_when_sell_in_less_than_5(
        self, sell_in, initial_quality
    ):
        gilded_rose = GildedRose(
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=sell_in,
                    quality=initial_quality,
                )
            ]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == initial_quality + 3

    @pytest.mark.parametrize(
        "sell_in, initial_quality",
        [(0, 8), (-1, 7), (-3, 6), (-2, 9), (-11, 2), (-15, 47)],
    )
    def test_quality_drops_to_0_after_concert(self, sell_in, initial_quality):
        gilded_rose = GildedRose(
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=sell_in,
                    quality=initial_quality,
                )
            ]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == 0

    def test_quality_is_never_above_50(self):
        gilded_rose = GildedRose([Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=7, quality=50)])

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == 50


class TestConjuredItems:
    @pytest.mark.parametrize("initial_sell_in", [6, 7, 8, 0, -2])
    def test_sell_in_should_decrease(self, initial_sell_in):
        gilded_rose = GildedRose(
            [Item(name="Conjured Mana Cake", sell_in=initial_sell_in, quality=2)]
        )

        gilded_rose.update_quality()

        actual_sell_in = gilded_rose.items[0].sell_in
        assert actual_sell_in == initial_sell_in - 1

    @pytest.mark.parametrize("initial_quality", [8, 7, 6, 9, 2, 49])
    def test_quality_should_decrease_after_update(self, initial_quality):
        gilded_rose = GildedRose(
            [Item(name="Conjured Mana Cake", sell_in=7, quality=initial_quality)]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == initial_quality - 2

    def test_quality_should_never_become_negative(self):
        gilded_rose = GildedRose(
            [Item(name="Conjured Mana Cake", sell_in=3, quality=0)]
        )

        gilded_rose.update_quality()

        actual_quality = gilded_rose.items[0].quality
        assert actual_quality == 0


if __name__ == "__main__":
    unittest.main()
