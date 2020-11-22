#!/usr/bin/env python

PROJECT_NAME = "doidw2rss"
VERSION = '0.0.2'
URL_REDDIT_RSS = 'https://www.reddit.com/r/DasOhrIstDerWeg/.rss'
URL_CHANNEL_IMAGE = 'https://styles.redditmedia.com/t5_3a7ys/styles/communityIcon_t7esbeikey951.jpg'
RE_TITLE_FILTER = r'^Podcast'
RE_FOOTNOTE = r'\([0-9]+\)$'
TEMPLATE_STRING = """<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0">
        <channel>
            <title>{{ title|e }}</title>
            <link>{{ link }}</link>
            <description>{{ description|e }}</description>
            <image>{{ image }}</image>
            <language>{{ language|d('de-de') }}</language>
            <copyright>{{ copyright }}</copyright>
            <generator>{{ generator }} {{ version }}</generator>
            <lastBuildDate>{{ now }}</lastBuildDate>
            {% for entry in entries %}<item>
                <title>{{ entry['title']|e }}</title>
                <description>{{ entry['description']|e }}</description>
                <pubDate>{{ entry['pubDate'] }}</pubDate>
                <link>{{ entry['link'] }}</link>
                <enclosure url="{{ entry['url'] }}"/>
                <guid isPermalink="false">{{ entry['guid'] }}</guid>
            </item>{% endfor %}
        </channel>
</rss>"""
