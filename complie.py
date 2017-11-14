import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang=None):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                   mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter()
        return highlight(code, lexer, formatter)


renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)
file = open("/Users/yuanxiansen/Desktop/test1.txt", "rb")
string_result = file.read().decode("utf-8")
print(markdown(string_result))
