# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        quality_change = -1
        multiplier = 1

        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue
            if item.name == "Aged Brie":
                quality_change = 1
            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.sell_in <= 10:
                    quality_change = 2
                if item.sell_in <= 5:
                    quality_change = 3
                if item.sell_in <= 0:
                    multiplier = -1 * item.quality

            item.sell_in -= 1
            if item.sell_in < 0 and item.name != "Backstage passes to a TAFKAL80ETC concert":
                multiplier = 2

            item.quality += quality_change * multiplier

            if item.quality < 0:
                item.quality = 0
            if item.quality > 50:
                item.quality = 50


class Item:
    """Do not alter the Item class"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ConjuredItem(Item):
    pass

