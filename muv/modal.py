"""

"""
import urwid
import markdown
import webbrowser
from mdx_gfm import GithubFlavoredMarkdownExtension
from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString
from .util import make_padding



class ContentParser:

    def __init__(self):
        self.tag2method = {
            'code': self.simple_tag2markup,
            'em': self.simple_tag2markup,
            'strong': self.simple_tag2markup,
            'li': self.simple_tag2markup,
            }
        self.highlight_set = ['kd', 'nx', 'nf', 'ne', 's1', 's2', 'k']

    def markdown2markup(self, file_name):
        html = self.markdown2html(file_name)
        return self.html2markup(html)

    def markdown2html(self, file_name):
        source = open(file_name).read()
        html = markdown.markdown(source, extensions=[GithubFlavoredMarkdownExtension()])
        return html

    def html2markup(self, html):
        listbox_content = []
        soup = BeautifulSoup(html, 'html.parser')
        for e in soup.body or soup:
            if isinstance(e, NavigableString):
                continue
            name = e.name
            method = self.tag2method.get(name, getattr(self, '_'+name, self.tag2text))
            markup = method(e)
            if not isinstance(markup, urwid.Widget):
                txt = urwid.Text(markup)
                markup = urwid.Padding(txt, align='left', width=('relative', 100), min_width=None, left=5, right=2)
            listbox_content.append(markup)
        return listbox_content

    def tag2text(self, element):
        content = []
        for child in element.children:
            if isinstance(child, Tag):
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                inner_content = method(child)
                content.append(inner_content)
            else:
                content.append(child)
        return ''.join(content)
    
    def simple_tag2markup(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        return (element.name,markups)
    
    @make_padding(7, 2)
    def _blockquote(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        quote = urwid.Text((element.name,markups))
        void_divider = urwid.Divider(" ")
        #block = urwid.AttrMap(quote, 'header')
        return urwid.Pile([void_divider, quote, void_divider])

    def _p(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        return (element.name,markups)

    
    def _img(self, element):
        #<img alt="GitHub Logo" src="/images/logo.png" />
        url = element.attrs.get('src', 'No link')
        alt = element.attrs.get('alt', 'Here is a image from '+url) 

        markup =  ('img', [('alt', alt),  ' (', ('url', url), ')'])
        return markup

    def _a(self, element):
        #<a href="http://github.com">GitHub</a></p>
        url = element.attrs.get('href', 'No link')
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        markups.append(('url', [' (', url, ')']))
        return (element.name,markups)
        
    @make_padding(0, 2)
    def _h1(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        h = urwid.Text(('h1' ,markups))
        void_divider = urwid.Divider(" ", 0, 0)
        block = urwid.AttrMap(h, 'header')
        divider = urwid.Divider("=", 0, 2)
        return urwid.Pile([void_divider, block, divider])
    
    @make_padding(1, 2)
    def _h2(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        h = urwid.Text(('h2' ,markups))
        void_divider = urwid.Divider(" ", 0, 0)
        block = urwid.AttrMap(h, 'header')
        divider = urwid.Divider("=", 0, 1)
        return urwid.Pile([void_divider, block, divider])
        #return urwid.Padding(h, align='left', width=('relative', 100), min_width=None, left=1, right=2)

    @make_padding(2, 2)
    def _h3(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        h = urwid.Text(('h3' ,markups))
        void_divider = urwid.Divider(" ", 0, 0)
        block = urwid.AttrMap(h, 'header')
        divider = urwid.Divider("=", 0, 1)
        return urwid.Pile([void_divider, block, divider])


    @make_padding(3, 2)
    def _h4(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        h = urwid.Text(('h4' ,markups))
        void_divider = urwid.Divider(" ", 0, 0)
        block = urwid.AttrMap(h, 'header')
        divider = urwid.Divider("-", 0, 1)
        return urwid.Pile([void_divider, block, divider])
        return h

    @make_padding(4, 2)
    def _h5(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        h = urwid.Text(('h5' ,markups))
        void_divider = urwid.Divider(" ", 0, 0)
        block = urwid.AttrMap(h, 'header')
        divider = urwid.Divider("-")
        return urwid.Pile([void_divider, block, divider])

    @make_padding(5, 2)
    def _h6(self, element):
        markups = []
        for child in element.children:
            if child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        h = urwid.Text(('h6' ,markups))
        void_divider = urwid.Divider(" ", 0, 0)
        block = urwid.AttrMap(h, 'header')
        divider = urwid.Divider(" ")
        return urwid.Pile([void_divider, block, divider])


    @make_padding(5, 2)
    def _div(self, element):
        if 'class' not in element.attrs or 'highlight' not in element.attrs['class']:
            return self.simple_tag2markup(element)
            
        markups = []
        for child in element.children:
            if child.name == 'pre':
                markup = self._hightlight(child)
                markups.append(markup)
            elif child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append(markup)
            else:
                markups.append(child)
        txt = urwid.Text(('highlight', markups))
        innePadder = urwid.Padding(txt, align='left', width=('relative', 100), min_width=None, left=2, right=2)
        block = urwid.AttrMap(innePadder, 'code_block')
        void_divider = urwid.Divider(" ")
        piles = urwid.Pile([void_divider, block, void_divider])
        return piles

    @make_padding(5, 2)
    def _pre(self, element):
        
        markup = self._hightlight(element)
        txt = urwid.Text(('pre', markup))
        innePadder = urwid.Padding(txt, align='left', width=('relative', 100), min_width=None, left=2, right=2)
        block = urwid.AttrMap(innePadder, 'code_block')
        void_divider = urwid.Divider(" ")
        piles = urwid.Pile([void_divider, block, void_divider])
        return piles

    def _hightlight(self, element):
        markups = []
        for child in element.children:
            if child.name == 'span' and 'class' in child.attrs:
                clss = child.attrs['class']
                # Only get first class if there're classes available
                c = clss[0] if len(clss)>0 else 'class_code_space'
                c = 'class_' + c if c in self.highlight_set else 'class_code_space'
                markups.append((c, child.contents))
            elif child.name:
                method = self.tag2method.get(child.name, getattr(self, '_'+child.name, self.tag2text))
                markup = method(child)
                markups.append((child.name, markup))
            else:
                markups.append(('class_code_space', child))
        return markups

    @make_padding(6, 0)
    def _ol(self, element):
        widgets = [urwid.Divider(" ")]
        i = 1
        for li in element.find_all('li'):
            method = self.tag2method.get('li', getattr(self, '_li', self.tag2text))
            markup = method(li)
            txt = urwid.Text(('li',[str(i), '. ', markup]))
            widgets.append(txt)
            i+=1
        widgets.append(urwid.Divider(" "))
        ol = urwid.Pile(widgets)
        return ol

    @make_padding(6, 0)
    def _ul(self, element):
        widgets = [urwid.Divider(" ")]
        for li in element.find_all('li'):
            method = self.tag2method.get('li', getattr(self, '_li', self.tag2text))
            markup = method(li)
            txt = urwid.Text(('li',['* ', markup]))
            widgets.append(txt)
        widgets.append(urwid.Divider(" "))
        ol = urwid.Pile(widgets)
        return ol

    @make_padding(6, 6)
    def _table(self, table):
        divider = urwid.Divider(" ")
        widgets = []
        ths = []
        for th in table.thead.tr:
            if not isinstance(th, Tag):
                continue
            method = self.tag2method.get('th', getattr(self, '_th', self.tag2text))
            markup = method(th)
            txt = urwid.LineBox(urwid.Text(markup))
            ths.append(txt)
        widgets.append(urwid.Columns(ths, dividechars=2))
        widgets.append(urwid.Divider("="))
        for tr in table.tbody:
            if not isinstance(tr, Tag):
                    continue
            tds = []
            for td in tr:
                if not isinstance(td, Tag):
                    continue
                method = self.tag2method.get('td', getattr(self, '_td', self.tag2text))
                markup = method(td)
                txt = urwid.Text(markup)
                tds.append(txt)
            widgets.append(urwid.Columns(tds, dividechars=2))
            widgets.append(urwid.Divider("-"))
        widgets.pop()
        widgets.append(urwid.Divider(" "))
        return urwid.Pile(widgets)


class PageListBox(urwid.ListBox):
    """
    Simple listbox with basic navigation.
    """

    def mouse_event(self, size, event, button, col, row, focus):

        if event == 'mouse press':
            if button == 4:
                for _ in range(5):
                    self.keypress(size, 'up')
                return True
            if button == 5:
                for _ in range(3):
                    self.keypress(size, 'down')
                return True
            return super().mouse_event(size, event, button, col, row, focus)

    def keypress(self, size, key):
        cols, rows = size
        commands = {
                    'j': (1, 'down'),
                    'k': (1, 'up'),
                    'd': (rows//2, 'down'),
                    'e': (rows//2, 'up'),
                    'f': (1, 'page down'),
                    'b': (1, 'page up')
                }
        command_map = commands.get(key)
        if command_map:
            number, command = command_map
            for _ in range(0, number):
                self.keypress(size, command)
            return True
        if key == 'q':
            raise urwid.ExitMainLoop()
        return super().keypress(size, key)       
    


