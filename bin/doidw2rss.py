#!/usr/bin/env python
import feedparser
from jinja2 import Template
from datetime import datetime
import re
import html
from bs4 import BeautifulSoup

from config import *

MATCHER_TITLE = re.compile(RE_TITLE_FILTER)
MATCHER_FOOTNOTE = re.compile(RE_FOOTNOTE)


def get_footnote_text(soup, footnote):
    if not footnote:
        return ""
    tds = soup.select('table:nth-child(7) tr td')
    for fn_num, info in zip(tds[0::2], tds[1::2]):
        if fn_num.text == footnote:
            return info.text
    return ""


def translate(feed):
    entries = list()
    for entry in feed['entries']:
        if not MATCHER_TITLE.match(entry.title):
            continue
        soup = BeautifulSoup(html.unescape(entry.content)[0]['value'], features='html.parser')
        tds = soup.select('table:nth-child(3) tr td') 
        for producer, ahref in zip(tds[0::2], tds[1::2]):
            a = ahref.select('a')[0]
            text = a.text
            footnote = get_footnote_text(soup, ([""] + MATCHER_FOOTNOTE.findall(text))[-1])
            text = MATCHER_FOOTNOTE.sub("", text)
            url = a.attrs['href']
            entries.append({
                    'title': f'{producer.text} - {text}',
                    'description': f'{producer.text} - {text}.<br/>{footnote}',
                    'pubDate': entry['updated'],
                    'link': url, # TODO proper link
                    'url': url,
                    'guid': url
                    })
    return entries


def main(outpath: str) -> int:
    parsed = feedparser.parse(URL_REDDIT_RSS)
    translated = translate(parsed)
    composed = Template(TEMPLATE_STRING).render( \
            title='Das Ohr ist der Weg',
            link="https://reddit.com/r/DasOhrIstDerWeg",
            description='Gekratzt von r/DasOhrIstDerWeg',
            image=URL_CHANNEL_IMAGE,
            generator=PROJECT_NAME,
            version=VERSION,
            now=translated[0]['pubDate'],
            entries=translated \
            )

    if not outpath:
        print(composed)
        return 0

    with open(outpath, 'w') as outfile:
        outfile.write(composed)
        return 0
    return 1

if __name__ == '__main__':
    import sys
    sys.exit(main(outpath=sys.argv[1] if len(sys.argv)>1 else None))
