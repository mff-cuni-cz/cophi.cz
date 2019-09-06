#!/usr/bin/env python3

import fileinput
import string

s = None
with open('tally.tex.template') as template:
    s = string.Template(template.read())

year = 2019
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

i = 2
for line in fileinput.input():
    if i == 13:
        year += 1
        i = 1
    month = months[i-1]
    quote_text, quote_author = line.strip().split('\t')
    fn = 'tally.{0}.{1:02d}.tex'.format(year, i)
    with open(fn, 'w') as outf:
        tex = s.substitute({
            'month': month,
            'quote_author': quote_author,
            'quote_text': quote_text,
            'year': year,
        })
        outf.write(tex)
    print(fn)
    i += 1
