# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, ConjuredItem, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_update_quality_method_decreases_sell_in_and_quality(self):
        items = [Item("foo", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_quality_degrades_twice_as_fast_after_sell_by(self):
        items = [Item("foo", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_quality_never_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(0, items[0].quality)

    def test_aged_brie_quality_increases(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreater(items[0].quality, 0)

    def test_item_quality_never_greater_than_50(self):
        items = [Item("Aged Brie", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_update_quality_doest_affect_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    def test_backstage_pass_quality_changes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 10),
                 Item("Backstage passes to a TAFKAL80ETC concert", 5, 10),
                 Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)
        self.assertEqual(13, items[1].quality)
        self.assertEqual(0, items[2].quality)

    """def test_conjured_items_degrade_twice_as_fast(self):
        items = [ConjuredItem("foo", 10, 10),
                 ConjuredItem("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)
        self.assertEqual(6, items[1].quality)"""


if __name__ == '__main__':
    unittest.main()
