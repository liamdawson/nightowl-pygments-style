# Night Owl Pygments

An early, partially tested adaptation of
[Sarah Drasner's Night Owl](https://github.com/sdras/night-owl-vscode-theme)
[Visual Studio Code](https://code.visualstudio.com)
theme to [pygments](http://pygments.org/).

Unfortunately, due to differences between lexers, it seems impossible to
perfectly replicate the style achieved in the reference theme.

## Rationale

[Hugo, the static site generator](https://gohugo.io) uses a Pygments
compatible code formatter, which supports using compatible CSS stylesheets for
syntax highlighting colours. Using `to_css.py` in this repository will generate
one of these stylesheets based on the current implementation of the theme.

## Development

Run `test.py` to generate `test.html` based on the output of highlighting all
of the defined samples. Compare against `vscode.html` for how it is rendered
with the official theme.

## Contributing

1. Add a sample case to the `samples` folder.
2. Add the sample case (copied from the appropriately highlighted file in VS
   Code, using the `Copy With Syntax Highlighting` command pallette option)
   to the `vscode.html` file (Note that samples are alphabetically sorted by
   sample filename).
3. Modify the `samples` array in `test.py` to add the sample with the correct
   lexer.
4. Open a PR once `style.py` is to your liking (being careful to check for
   regressions for other samples).
