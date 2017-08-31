import urwid

def make_padding(left, right):
    def _padding(func): 
        def wrapper(*args, **kwargs):
            markups = func(*args, **kwargs)
            if not isinstance(markups, urwid.Widget):
                markups = urwid.Text(urwid)
            return urwid.Padding(markups, align='left', width=('relative', 100), min_width=None, left=left, right=right)
        return wrapper
    return _padding