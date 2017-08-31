"""
Preview markup document
"""
import argparse
import json
import os
import pkg_resources

import urwid
import urwid.raw_display

from .modal import ContentParser, PageListBox

CONF_DIR = pkg_resources.resource_filename('muv', 'conf')
CONF_FALLBACK_PATH = [os.curdir, os.path.expanduser("~/.muv"), "/etc/muv", os.environ.get("MUV_CONF"), CONF_DIR]

def load_palette(palette_file):
    if not palette_file:
        for loc in CONF_FALLBACK_PATH:
            try:
                palette_file = os.path.join(loc,"palette.json")
                if os.path.exists(palette_file):
                    break
            except Exception:
                pass
        else:
            raise FileNotFoundError("no palette file found!")
    palette = []
    
    with open(palette_file) as f:
        attrs = json.load(f)
        for attr in attrs["palette"]:
            attr = (attr['name'], attr['fg'], attr['bg'], attr['mono'], attr['fgh'], attr['bgh'])
            palette.append(attr)
    return palette

def load_config(config_file):
    if not config_file:
        for loc in CONF_FALLBACK_PATH:
            try:
                config_file = os.path.join(loc, 'muv.conf')
                if os.path.exists(config_file):
                    break
            except Exception:
                pass
    with open(config_file) as f:
        return json.load(f)

def preview(file_name, palette=None, config_file=None):
    
    palette = load_palette(palette)
    config = load_config(config_file)
    screen = urwid.raw_display.Screen()
    screen.register_palette(palette)

    parser = ContentParser()
    listbox_content = parser.markdown2markup(file_name)
    listbox = PageListBox(urwid.SimpleListWalker(listbox_content))
    #return
    urwid.MainLoop(listbox, screen=screen).run()




def main():
    """Preview markup file"""
    argparser = argparse.ArgumentParser(
        description='preview markdown file',
        epilog='Markup file previewer by sean',
        prog='')

    argparser.add_argument('file_name', metavar='markdown file to view', help='the file to preview')
    argparser.add_argument('-p', '--palette', metavar='palette file location', 
        help='palettes file show how tags or class being rendered')
    argparser.add_argument('-c', '--config', metavar='config file location', 
        help='possible configurations supported')
    argparser.add_argument('--version', action='version', version='%(prog)s 0.0.0', 
                        help='look up the version')

    args = argparser.parse_args()
    preview(args.file_name, args.palette)
