from pygments.style import Style
from pygments.token import Token

class NightOwl(Style):
  background_color = '#011627'
  default_style = ''
  styles = {
    Token: '#d6deeb',
    Token.Keyword: 'italic #c792ea',
    Token.Keyword.Constant: 'noitalic #82aaff',
    Token.Keyword.Declaration: '',
    Token.Keyword.Namespace: '',
    Token.Keyword.Psuedo: '',
    Token.Keyword.Reserved: '',
    Token.Keyword.Type: 'noitalic #82aaff',
    Token.Name: '#d6deeb',
    Token.Name.Function: '#82aaff',
    Token.String.Quote: '#d9f5dd',
    Token.String: '#ecc48d',
    Token.Number: '#f78c6c',
    Token.Operator: '#7fdbca',
    Token.Comment: 'italic #637777',
    Token.Comment.Preproc: 'noitalic #7fdbca'
  }