#!/usr/bin/env python

import zlib;
import os;
import sys;


def error():
    print("\nUsage:\n\t%s <file with deflate data>\n" %(sys.argv[0]));
    exit();

if (len(sys.argv) == 2 and os.path.isfile( sys.argv[1] )):
    fh = open( sys.argv[1], 'r');
else:
    error();

body = fh.read();
decompressed_data = zlib.decompress(body);
print decompressed_data;


