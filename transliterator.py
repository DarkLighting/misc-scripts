#!/usr/bin/env python

import argparse;



def transliterate( string, key ):
    index = 0;
    decoded_text = '';
    print('string = ' + string);
    print('key = ' + key);
    for x in range( 0, len(string) ):
        index = string[x];
        y = key.index(index);
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz.";
        decoded_text += alphabet[y];
    return decoded_text;


def main():
    parser = argparse.ArgumentParser( description='Transliteration decoder' );
    parser.add_argument( '-k', metavar='<Key>',  help='String that defines the corresponding character' );
    parser.add_argument( '-s', metavar='<String>', help='String to be decoded' );
    args = parser.parse_args();
    if( args.k is None ):
        print('\nThe decoding key is missing!');
        exit();
    if( args.s is None ):
        print('\nThe string to be decoded is missing!');
        exit();
    print args;
    result = transliterate( args.s, args.k );
    print result;
    exit();


if __name__ == '__main__':
    main();
