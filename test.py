from style import NightOwl
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.lexers import CLexer

if __name__ == "__main__":
  samples = {
    "samples/sample.c": CLexer()
  }

  formatter = HtmlFormatter(style=NightOwl)
  formatter.style.background_color = '#011627'

  with open('test.html', 'w') as out_file:
    out_file.truncate()
    out_file.write("<html><head><link rel='stylesheet' href='base.css'><style>{}</style></head><body>".format(formatter.get_style_defs('div.highlight pre')))
    for (key, val) in samples.iteritems():
      with open(key, 'r') as sample_file:
        out_file.write(highlight(sample_file.read(), val, formatter))
    out_file.write("</body></html>")
