"""
Preview markdown file
"""
import argparse
import json
import logging
import os

import pkg_resources
import urwid
import urwid.raw_display

from .modal import ContentParser, PageListBox
from .util import check_if_italic
from .version import __version__

CONF_DIR = pkg_resources.resource_filename('muv', 'conf')
CONF_FALLBACK_PATH = [os.curdir, os.path.expanduser("~/.muv"), 
                      "/etc/muv", os.environ.get("MUV_CONF"), CONF_DIR]
PALETTE_FILE_NAME = 'palette.json' if check_if_italic() else 'palette_without_italics.json'

def load_palette(palette_file):
    """Load palette from json file"""
    palette = []
    if not palette_file:
        for loc in CONF_FALLBACK_PATH:
            try:
                palette_file = os.path.join(loc, PALETTE_FILE_NAME)
                if os.path.exists(palette_file):
                    break
            except Exception:
                pass
        else:
            logging.error("No palette file found, colors and other settings unavailable")
            return palette
    
    with open(palette_file) as infile:
        attrs = json.load(infile)
        for attr in attrs["palette"]:
            attr = (attr['name'], attr['fg'], attr['bg'], attr['mono'], attr['fgh'], attr['bgh'])
            palette.append(attr)
    return palette

def load_config(config_file):
    """Load configuration from json file"""
    if not config_file:
        for loc in CONF_FALLBACK_PATH:
            try:
                config_file = os.path.join(loc, 'muv.conf')
                if os.path.exists(config_file):
                    break
            except Exception:
                pass
        else:
            logging.info("No config file found")
            return {}
    with open(config_file) as f:
        return json.load(f)

def preview(file_name, log=None, palette=None, config_file=None):
    """
    Preview markdown file.

    Positional argument:
    file_name -- the file to view
    log -- specify log level, valid options include DEBUG, INFO, WARNING, ERROR, CRITICAL
    Keyword arguments:
    palette -- palette file location
    config_file -- json configuration file
    """
    numeric_level = getattr(logging, log, None)
    logging.basicConfig(level=numeric_level, format='%(asctime)s %(levelname)s: %(message)s')

    palette = load_palette(palette)
    config = load_config(config_file)
    screen = urwid.raw_display.Screen()
    screen.register_palette(palette)

    parser = ContentParser(config=config)
    listbox_content = parser.markdown2markup(file_name)
    listbox = PageListBox(urwid.SimpleListWalker(listbox_content))
    urwid.MainLoop(listbox, screen=screen).run()

def main():
    """Preview markup file"""
    argparser = argparse.ArgumentParser(
        description='preview markdown file',
        epilog='Markup file viewer',
        prog='muv')

    argparser.add_argument('file_name', metavar='markdown file to view', help='the file to preview')
    argparser.add_argument('-p', '--palette', metavar='palette file location', 
        help='palettes file show how tags or classes being rendered')
    argparser.add_argument('-c', '--config', metavar='config file location', 
        help='possible configurations supported')
    argparser.add_argument('--version', action='version', version='%(prog)s '+__version__, 
        help='look up the version')
    argparser.add_argument('--log', metavar='enable logging', default='CRITICAL', 
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Enable logging and set loggin level, available options include DEBUG, INFO, WARNING, ERROR, CRITICAL')

    args = argparser.parse_args()

    preview(args.file_name, args.log, args.palette, args.config)
