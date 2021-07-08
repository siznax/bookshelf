#!/usr/bin/env python3

'''
imdex - media indexer

    /books
        The Histories (430 BCE) Herodotus.gif
        War and Peace (1869) Lev Tolstoy.jpg
        Harry Potter and the Sorcerer's Stone (1998) J.K. Rowling.png

    $ imdex.py books > index.html
    imdexed (3) images in books

    $ head index.html
    <a href="https://google.com/search?q=The Histories">
      <img alt="The Histories (430 BCE) Herodotus"
           title="The Histories (430 BCE) Herodotus"
           src="books/The Histories (430 BCE) Herodotus.jpg"></a>

    $ imdex.py books --json > index.json
    imdexed (3) images in books
'''

import argparse
import json
import os
import sys

__author__ = "Steve @siznax"
__author_email__ = "steve@siznax.net"
__version__ = "0.1"


def emit(path, emit_json=False):
    '''
    emit index to standard out as HTML or JSON
    '''
    data = dict()
    index = imdex(path)

    for count,image in enumerate(index):
        if not emit_json:
            print(html(image[5], image[3], os.path.join(path,image[4])))
        else:
            data[src] = {
                '_': image,
                'year': image[0],
                'note': image[1],
                'title': image[2],
                'alt': image[3],
                'fname': image[4],
                'href': image[5],
            }

    if emit_json:
        print(json.dumps(data, indent=4, sort_keys=True))

    print('imdexed {} images in {}'.format(count, path), file=sys.stderr)


def html(href, alt, src):
    '''
    returns <a href><img height alt title src></a> HTML fragment
    '''
    return '''<a href="{}">
    <img decoding="sync" loading="lazy"
     alt="{}"
     title="{}"
     src="{}"></a>'''.format(href, alt, alt, src)


def imdex(pname='./'):
    '''
    returns list of image metadata tuples from image filenames
    non-conforming file(names) are ignored

    INPUT
        <title (year) note.ext>, ...

    OUTPUT
        [(year, note, title, fname, alt), ...]

    EXAMPLE

    Wabi-Sabi (1994) Leonard Koren.png

        ("1994",
         "Leonard Koren",
         "Wabi-Sabi",
         "Wabi-Sabi (1994) Leonard Koren",
         "Wabi-Sabi (1994) Leonard Koren.png")
    '''
    images = list()

    for fname in os.listdir(pname):
        if fname.startswith('.'):
            continue

        if '(' not in fname or ')' not in fname:
            continue

        alt, ext = os.path.splitext(fname)
        parts = fname.split('(')
        title = parts[0].strip()

        if "tinyurl_" in alt:
            alt = alt.split("tinyurl_")[0].strip()

        note = None
        year = None

        if parts and ')' in parts[1]:
            year, note = parts[1].split(')')

            if note:
                note = note.strip().replace(ext, '')

            href = "https://google.com/search?q={} {}".format(
                title, note)

            if "tinyurl_" in note:
                href="https://tinyurl.com/{}".format(
                    note.replace('tinyurl_', ''))

            images.append((year, note, title, alt, fname, href))

    return reversed(sorted(images))


def main():
    '''
    main program
    '''
    argp = argparse.ArgumentParser(
        description='create HTML image index from filenames')
    argp.add_argument('path', help="path to image folder")
    argp.add_argument('-j', '--json', action='store_true',
                      help="emit JSON")
    args = argp.parse_args()

    emit(args.path, args.json)
    

if __name__ == '__main__':
    '''
    command-line interface
    '''
    main()
