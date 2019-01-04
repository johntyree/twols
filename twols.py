#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

from functools import wraps
from timeit import default_timer


with open('/usr/share/dict/american-english') as fin:
    valid_words = frozenset(
        s[:-1].lower()
        for s in fin.readlines()
        if len(s) > 2
        if "'" not in s)


def trace(f):
    @wraps(f)
    def inner(*args, **kwargs):
        indent = ' ' * trace.level
        print(indent, "{}(*{}, **{})".format(f.__name__, args, kwargs))
        trace.level += 1
        output = f(*args, **kwargs)
        trace.level -= 1
        print(indent, f.__name__, ":", repr(output))
        return output
    return inner
trace.level = 0


class _Time(object):

    def __init__(self):
        self.elapsed = {}

    def __call__(self, f):
        @wraps(f)
        def inner(*a, **k):
            start = default_timer()
            try:
                return f(*a, **k)
            finally:
                elapsed = default_timer() - start
                time.elapsed.setdefault(f.__name__, []).append(elapsed)
        return inner

    def stats(self, factor=1):
        s = {}
        for func, times in sorted(time.elapsed.items(), key=lambda x: x[0]):
            times = [t * factor for t in times]
            low = min(times)
            high = max(times)
            mean = sum(times) / len(times)
            if len(times) == 1:
                std = 0
            else:
                std = sum((t-mean)**2 for t in times) / (len(times)-1)
            s[func] = (low, high, mean, std)
        return s

    def show(self, factor=1):
        s = self.stats(factor=factor)
        for func in sorted(s.keys()):
            low, high, mean, std = s[func]
            fmt = "{:>20}: {:.2f} {:.2f}({:.2f}) {:.2f}"
            print(fmt.format(func, low, mean, std, high))

time = _Time()
