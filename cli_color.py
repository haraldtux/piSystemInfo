#!/usr/bin/python
#
# ^H> HucDuino 11-11-2018
#
## test
#
## https://stackoverflow.com/questions/287871/print-in-terminal-with-colors/293633#293633   (307)
#

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()
