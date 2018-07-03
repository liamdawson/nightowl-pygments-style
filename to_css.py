#!/usr/bin/env python

from style import NightOwl
from pygments.formatters.html import HtmlFormatter

if __name__ == '__main__':
    html = HtmlFormatter(style=NightOwl)
    html.style.background_color = '#011627'
    print(html.get_style_defs("pre.highlight"))
