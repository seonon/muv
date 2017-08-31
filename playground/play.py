import sys
import urwid
import urwid.raw_display
import urwid.web_display


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
        rows = size[1]
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


def main():

    palette = [
        ('code', 'black,underline', 'light gray', 'standout,underline',
            'black,underline', '#88a'),
        ('em', 'light gray', 'dark blue', '',
            '#ffd', '#00a'),
        ('italic', 'light gray', 'dark cyan', 'bold',
            '#ff8', '#806'),
        ]
    screen = urwid.raw_display.Screen()
    screen.register_palette(palette)
    listbox_content = []
    txt = urwid.Text(('code', [u"nesting example "]))
    listbox_content.append(txt)

    listbox = PageListBox(urwid.SimpleListWalker(listbox_content))

    urwid.MainLoop(listbox, screen=screen).run()


if __name__=='__main__':
    main()
