#!/usr/bin/env python2

import sys

def xor( key_bin, cipher_text_bin ):
    result = list();
    i = gen_key( key_bin );
    j = gen_key( cipher_text_bin );
    while(1):
        try:
            result.append( int(i.next()) ^ int(j.next()) );
        except:
            return result; 

def xor(key, cipher):
    lista = list();
    for i,j in zip(key, cipher):
        lista.append( ord(i)^ord(j) );
    return lista;

def gen_key( c ):
    for i in c:
        yield i;

def repeated_key( key, length ):
    while( len( key ) < length ):
        try:
            key += char.next();
        except:
            char = gen_key( list( key ) );
    return key;

rep_key = repeated_key( sys.argv[1], len(sys.argv[2]) );
print("rep_key: %s" %(rep_key) );
final =  xor(rep_key, sys.argv[2]);
print( ''.join('%02x'%i for i in final));

