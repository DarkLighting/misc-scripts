#!/usr/bin/env python2

import sys;

try:
    if( len(sys.argv) != 3 ):
        throw;
    b = list();
    for line in open(sys.argv[1]):
        c = line.rstrip().split();
        if(isinstance(c,list)):
            while(1):
                try:
                    b.append(c.pop());
                except:
                    break;
    with open(sys.argv[2], 'a') as dictionary:
        for word in sorted(b):
            dictionary.write("%s\n" % word) 
except:
    print('\nCould not open the specified files');
    print('\nSYNTAX: '+sys.argv[0]+' <file to open> <dictionary output>\n');

