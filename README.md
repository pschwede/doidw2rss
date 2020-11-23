# r/DasOhrIstDerWeg to RSS

![build](https://github.com/pschwede/doidw2rss/workflows/build/badge.svg)

[r/DasOhrIstDerWeg](https://www.reddit.com/r/DasOhrIstDerWeg) ist eine Sammlung von hörenswerten Podcastfolgen, die von [u/DieHermetischeGarage](u/DieHemetischeGarage) täglich gepflegt wird.
Dies ist ein Reddit-Scraper, der diese Folgen in einen Podcast (RSS-feed) umwandelt.

[![RSS](https://raw.githubusercontent.com/barredo/podcasts_badges/master/badges/feed_subscribe_white_en.png)](https://github.com/pschwede/doidw2rss/raw/master/feed.rss)

## Installation

```
git clone https://github.com/pschwede/doidw2rss.git doidw2rss
cd doidw2rss
python3 -mvenv env
pip install -r requirements.txt
```

## Neusten Feed aggregieren
```
./cron.sh feed.rss
```
