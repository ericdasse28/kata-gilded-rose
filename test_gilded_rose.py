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
        gilded_rose = GildedRose(
            [
                Item(
                    name="Backstage passes to a TAFKAL80ETC concert",
                    sell_in=7,
                    quality=50,
                )
            ]
        )

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
