from style import NightOwl
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.lexers import CLexer

if __name__ == "__main__":
  samples = {
    "samples/sample.c": CLexer()
  }

  formatter = HtmlFormatter(style=NightOwl)

  with open('test.html', 'w') as out_file:
    out_file.truncate()
    for (key, val) in samples.iteritems():
      with open(key, 'r') as sample_file:
        out_file.write(highlight(sample_file.read(), val, formatter))




