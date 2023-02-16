[![CI](https://github.com/ericdasse28/kata-gilded-rose/actions/workflows/python-app.yml/badge.svg)](https://github.com/ericdasse28/kata-gilded-rose/actions/workflows/python-app.yml)
[![Coverage Status](https://coveralls.io/repos/github/ericdasse28/kata-gilded-rose/badge.svg?branch=master)](https://coveralls.io/github/ericdasse28/kata-gilded-rose?branch=master)

# Kata Gilded Rose
Implementation of the Gilded Rose refactoring kata

Find the kata specifications [here](https://kata-log.rocks/gilded-rose-kata)

## Glossary
`SellIn`: number of days we have to sell the item

`Quality`: value that denotes how valuable the item is

## Rules
- At the end of each day, our system lowers both values for every item
- Quality is never negative or above 50
- When sell-by has passed, Quality decreases twice as fast
- "Aged Brie" actually increases in Quality as it gets older
- "Sulfuras" is a legendary item, never has to be sold and never decreases in Quality
- "Backstage passes" increase in Quality as its SellIn value approaches
    - +2 when there are 10 days or less left, +3 when there are 5 days or less left
    - Drops to 0 after concert
