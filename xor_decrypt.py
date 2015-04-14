#!/usr/bin/env python2
import sys;

def xor(key, cipher):
    lista = list();
    for i,j in zip(key, cipher):
        lista.append( chr(ord(i)^j) );
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

#a = raw_input();
a = sys.argv[1]
#b = raw_input();
b = sys.argv[2]
c = list();
for i in range(0, len(b), 2):
    c.append( int(str(b[i])+str(b[i+1]), base=16));
rep_key = repeated_key( a, len(b)/2 );
final =  xor(rep_key, c);
print( ''.join(final));

