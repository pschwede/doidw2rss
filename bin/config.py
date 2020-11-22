#!/usr/bin/env python

PROJECT_NAME = "doidw2rss"
VERSION = '0.0.1'
URL_REDDIT_RSS = 'https://www.reddit.com/r/DasOhrIstDerWeg/.rss'
URL_CHANNEL_IMAGE = 'https://styles.redditmedia.com/t5_3a7ys/styles/communityIcon_t7esbeikey951.jpg'
RE_TITLE_FILTER = r'^Podcast'
RE_FOOTNOTE = r'\([0-9]+\)$'
TEMPLATE_STRING = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
        <channel>
            <title>{{ title|d('Das Ohr ist der Weg')|e }}</title>
            <link>{{ link|d(URL_REDDIT_RSS) }}</link>
            <description>{{ description|d('Gekratzt von r/DasOhrIstDerWeg')|e }}</description>
            <image>{{ image|d(URL_CHANNEL_IMAGE) }}</image>
            <language>{{ language|d('de-de') }}</language>
            <copyright>{{ copyright|d('u/DieHermetischeGarage') }}</copyright>
            <generator>{{ generator|d(PROJECT_NAME) }} {{ version|d(VERSION) }}</generator>
            <lastBuildDate>{{ now }}</lastBuildDate>
            {% for entry in feed['entries'] %}<item>
                <title>{{ entry['title']|e }}</title>
                <description>{{ entry['description']|e }}</description>
                <pubDate>{{ entry['pub_date'] }}</pubDate>
                <link>{{ entry['link'] }}</link>
                <enclosure url="{{ entry['url'] }}"/>
                <guid isPermalink="false">{{ entry['guid'] }}</guid>
            </item>{% endfor %}
        </channel>
</rss>"""
