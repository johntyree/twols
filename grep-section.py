#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""<+Module Description.+>"""

from __future__ import division, print_function

import sys
import os
import itertools as it
from subprocess import run, PIPE


def read_section(fin):
    seen_content = False
    for line in fin:
        yield line
        if line == '\n' and seen_content:
            break
        else:
            seen_content = True


def main():
    """Run main."""
    with open(os.path.join(os.curdir, __file__), 'r', encoding='utf-8') as f:
        s = True
        while s:
            section = ''.join(read_section(f))
            grep = run(['grep', '--', '=='], stderr=PIPE, stdout=PIPE,
                        input=section.encode('utf-8'))
            if grep.returncode == 0:
                sys.stdout.write(section)
            elif grep.returncode == 2:
                sys.stderr.write(grep.stderr.decode('utf-8'))


    return 0

if __name__ == '__main__':
    main()
