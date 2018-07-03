from style import NightOwl
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.lexers import CLexer, MarkdownLexer

if __name__ == "__main__":
    samples = {
        "samples/sample.c": CLexer(),
        "samples/sample.md": MarkdownLexer()
    }

    formatter = HtmlFormatter(style=NightOwl)
    formatter.style.background_color = '#011627'

    with open('test.html', 'w') as out_file:
        out_file.truncate()
        out_file.write("<html><head><link rel='stylesheet' href='base.css'><style>{}</style></head><body>".format(
            formatter.get_style_defs('div.highlight pre')))

        files = samples.keys()
        files.sort()

        for key in files:
            with open(key, 'r') as sample_file:
                out_file.write(
                    highlight(sample_file.read(), samples[key], formatter))
        out_file.write("</body></html>")
