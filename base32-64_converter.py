#!/usr/bin/env python2

import sys

def text2bits( t ):
    bits = str();
    for i in t:
        bits += bin( ord( i ) )[2:];
    return bits;

def base32_to_bits( t ):
    bit = str();
    for i in range(len(t)):
        bit += '{0:05b}'.format(dec_32[t[i].upper()]);
    return bit;

def get_pad_count( t ):
    pad = int();
    for i in list(reversed(range(0,len( t )))):
        if( t[i] == '=' ):
            pad += 1;
        else:
            break;
    return pad;

alpha32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567';
dec_32 = dict(zip(alpha32,range(32)));
alpha64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
enc_64 = dict(zip(range(64),alpha64));

text = list( sys.argv[1] );
print(text);
#bit_strip = text2bits( text );
fullbit = base32_to_bits( text );
print(fullbit);
print( len(fullbit));
chars_bit = list()
for i in range(0,len(fullbit),6):
#    print("i={0}, {1}".format(i,fullbit[i:i+6]));
#    print("{0} - {1}".format(
#                            int(fullbit[i:i+6], base=2), 
#                            enc_64[int(fullbit[i:i+6], base=2)] ));
    chars_bit.append(fullbit[i:i+6]);
print chars_bit;
padding = get_pad_count( text );


