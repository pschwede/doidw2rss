# r/DasOhrIstDerWeg to RSS

[![subscribe rss feed](https://img.shields.io/badge/%F0%9F%94%8A%20RSS-subscribe-orange)](https://github.com/pschwede/doidw2rss/raw/master/feed.rss) ![build](https://github.com/pschwede/doidw2rss/workflows/build/badge.svg) ![issues](https://img.shields.io/github/issues/pschwede/doidw2rss) [![antennapod](https://img.shields.io/badge/Subscribe%20with-Antennapod-blue)](https://github.com/AntennaPod/AntennaPod) [![tweet](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fpschwede%2Fdoidw2rss)](https://twitter.com/intent/tweet?text=r%2FDas%20Ohr%20ist%20der%20Weg%20als%20Podcast%0Ahttps%3A%2F%2Fgithub.com%2Fpschwede%2Fdoidw2rss%2Fraw%2Fmaster%2Ffeed.rss)

[r/DasOhrIstDerWeg](https://www.reddit.com/r/DasOhrIstDerWeg) ist eine Sammlung von hörenswerten Podcastfolgen, die von [u/DieHermetischeGarage](u/DieHemetischeGarage) täglich gepflegt wird.
Dies ist ein Reddit-Scraper, der diese Folgen in einen Podcast (RSS-feed) umwandelt.

## Abonnieren

Klicke auf [den Feed](https://raw.githubusercontent.com/pschwede/doidw2rss/master/feed.rss) um ihn mit der Standardapp zu öffnen oder füge seine URL in deine Podcastapp ein:

```https://raw.githubusercontent.com/pschwede/doidw2rss/master/feed.rss```

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
