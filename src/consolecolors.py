# Functions for applying console ANSI text effect and color codes.
# Copyright (C) 2011 Dario Giovannetti <dev@dariogiovannetti.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Functions for applying console ANSI text effect and color codes.

@author: Dario Giovannetti
@copyright: Copyright (C) 2011 Dario Giovannetti <dev@dariogiovannetti.com>
@license: GPLv3
@version: 1.0
@date: 2011-11-27
"""

import sys

colors = {
    # SGR (Select Graphic Rendition) parameters
    't': {
            'R': '0',  # Normal / Regular
            'B': '1',  # Bright (increased intensity) or Bold
            'F': '2',  # Faint (decreased intensity)
            'I': '3',  # Italic
            'U': '4',  # Underline
            'S': '5',  # Blink (slow)
            'K': '6',  # Blink (rapid)
            #'N': '7',  # Negative (swap foreground and background)
            #'C': '8',  # Conceal
            'L': '9'  # Line-through
        },
    
    # Foreground colors
    'f': {
            'K': '30',  # Black
            'R': '31',  # Red
            'G': '32',  # Green
            'Y': '33',  # Yellow
            'B': '34',  # Blue
            'P': '35',  # Purple
            'C': '36',  # Cyan
            'W': '37'  # White
        },
    
    # Background colors
    'b': {
            'K': '40',  # Black
            'R': '41',  # Red
            'G': '42',  # Green
            'Y': '43',  # Yellow
            'B': '44',  # Blue
            'P': '45',  # Purple
            'C': '46',  # Cyan
            'W': '47'  # White
        }
}

# Reset colors to default
reset = '\033[0m'

# Negative (swap foreground and background)
swap = '\033[7m'


def code(string):
    """Return the escape code corresponding to a string
    
    Example: code('tBfG')
    """
    code = []
    for k, g in enumerate(string[0:len(string) - 1:2]):
        code.append(colors[g][string[1:len(string):2][k]])
    return(''.join(('\033[', ';'.join(code), 'm')))


def table(x=True):
    """Display an effects and colors table
    
    x: if False continue script execution (default: True, print the table and
    exit the script)
    """
    print('The following list of parameter combinations is {}not{} '
                                     'exhaustive.'.format(code('tBfR'), reset))
    print('To reset the effects, use {}[instance].reset{}.'
                                                ''.format(code('tBfC'), reset))
    print('To swap foreground and background colors, use '
                            '{}[instance].swap{}.'.format(code('tBfC'), reset))
    print('{}Remember{} that the various codes are displayed differently '
                        'depending on the terminal used, and some may even '
                        'not be supported at all.'.format(code('tBfR'), reset))
    print()
    print('{}One-parameter examples:{}'.format(code('tU'), reset))
    print()
    for g in colors:
        for e in colors[g]:
            string = ''.join((g, e))
            print(code(string), string, reset, end='')
        print()
    print()
    print('{}One-parameter, swapped-color examples:'.format(code('tU'), reset))
    print()
    for g in colors:
        for e in colors[g]:
            string = ''.join((g, e))
            print(code(string) + swap, string, reset, end='')
        print()
    print()
    print('{}Two-parameter examples:'.format(code('tU'), reset))
    print()
    for t in ('R', 'B', 'F'):
        for f in colors['f']:
            string = ''.join(('t', t, 'f', f))
            print(code(string), string, reset, end='')
        print()
    for t in ('R', 'B', 'F'):
        for b in colors['b']:
            string = ''.join(('t', t, 'b', b))
            print(code(string), string, reset, end='')
        print()
    for f in colors['f']:
        for b in colors['b']:
            string = ''.join(('f', f, 'b', b))
            print(code(string), string, reset, end='')
        print()
    print()
    print('{}Two-parameter, swapped-color examples:'.format(code('tU'), reset))
    print()
    for t in ('R', 'B', 'F'):
        for b in colors['b']:
            string = ''.join(('t', t, 'b', b))
            print(code(string) + swap, string, reset, end='')
        print()
    for t in ('R', 'B', 'F'):
        for f in colors['f']:
            string = ''.join(('t', t, 'f', f))
            print(code(string) + swap, string, reset, end='')
        print()
    for b in colors['b']:
        for f in colors['f']:
            string = ''.join(('f', f, 'b', b))
            print(code(string) + swap, string, reset, end='')
        print()
    print()
    print('{}Three-parameter examples:'.format(code('tU'), reset))
    print()
    for f in colors['f']:
        for t in ('R', 'B', 'F'):
            for b in colors['b']:
                string = ''.join(('t', t, 'f', f, 'b', b))
                print(code(string), string, reset, end='')
            print()
    print()
    print('{}Three-parameter, swapped-color examples:'.format(code('tU'),
                                                                        reset))
    print()
    for b in colors['b']:
        for t in ('R', 'B', 'F'):
            for f in colors['f']:
                string = ''.join(('t', t, 'f', f, 'b', b))
                print(code(string) + swap, string, reset, end='')
            print()
    # By default, terminate the script
    if x:
        sys.exit()
