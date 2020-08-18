# Read lines looking for keywords. Highlight each occurrence and copy to log. Practicing, initiating in data science.

import sys
import numpy as np
from time import sleep
from termcolor import colored, cprint

print('\n')
read_lines_1 = input('File to read: ') 
print('\n')
write_log = input('File to log ocurrences: ')

lines_num = 0
kwd_1 = 'keyword'
kwd_2 = 'k3yw0rd'
kwd_3 = 'k3yword'
kwd_4 = 'keyw0rd'

print_white_on_red = lambda x: cprint(x, 'white', 'on_red')

with open(read_lines_1, 'r') as rl, \
    open(write_log, 'a+') as wl :

    lines = rl.readlines()

    for t_l in lines :
        lines_num += 1

        if (kwd_1 in t_l) or (kwd_2 in t_l) or (kwd_3 in t_l) or (kwd_4 in t_l) :
            print_white_on_red('Line {} > {}'.format(lines_num, t_l.strip()))
            sleep(0.5)
            wl = open(write_log, 'a+')
            wl.write(read_lines_1+','+t_l)
            wl.close()
            
        else :
            print('Line {} > {}'.format(lines_num, t_l.strip()))

        sleep(0.00025)

    rl.close()
    wl.close()