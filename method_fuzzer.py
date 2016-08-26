#!/usr/bin/python

import os;
import sys;
import requests;
import argparse;


parser = argparse.ArgumentParser( description='HTTP method Scanner' );
parser.add_argument( '--unsafe', action='store_true', help='Enable unsafe methods ("PUT/DELETE")');
url_group = parser.add_mutually_exclusive_group();
url_group.add_argument( '-u', metavar='<URL>', help='URL to be tested');
url_group.add_argument( '-f', metavar='<URLs list file>', help='File containing list of URLs to be tested');
parser.add_argument( '--custom', metavar='<Method>', help='Defines a custom method like \'BLAH\' to test against servers');
parser.add_argument( '--timeout', metavar='<Seconds>', help='Prints each response received', type=int);
parser.add_argument( '--redirect', action='store_true', help='Requests should accept redirection');
parser.add_argument( '-v', action='store_true', help='Prints each response received');
args = parser.parse_args();


safe_methods = ['OPTIONS', 'GET', 'HEAD', 'POST', 'TRACE', 'CONNECT']
unsafe_methods = ['PUT', 'DELETE']


def get_urls_from_file( url_file ):
    try:
        if (os.path.exists( url_file )):
            lines = list();
            with open( url_file, 'r') as fp_url:
                for url in fp_url:
                    lines.append(url)
            return lines;
        else:
            end( "File not found: %s\n" %( url_file ) );
    except:
        print sys.exc_info();



def scan(url):
    try:
        url = url.rstrip();
        print "\n[+] - "+url
        test_methods = safe_methods;
        if(not (args.custom is None)):
            test_methods = [ args.custom ];
        for i in range(0,len(test_methods)):
            try:
                r = requests.request(test_methods[i], url, allow_redirects=args.redirect, timeout=args.timeout, verify=False);
                if(len(r.history) > 0):
                    print "\tRedirections:"
                    for i in range(0,len(r.history)):
                        print "\t\t"+r.history[i].raw.get_redirect_location();
                    print '';
            except requests.exceptions.ReadTimeout:
                print "[-]"+test_methods[i]+' - Timed out';
                continue
            except requests.exceptions.ConnectionError:
                print "Connection error: "+str(sys.exc_info()[1]);
                continue
            print "[+]"+ test_methods[i]+' - '+str(r.status_code);
            if(args.v):
                print "\n"+r.content;
            if((test_methods[i] == 'OPTIONS') and (r.status_code == int(200))):
                if('Allow' in r.headers): 
                    print "\tURL accepts "+r.headers['Allow']+" methods";
                else:
                    print "\tResponse lacks \'Allow\' header";
            if((test_methods[i] == 'CONNECT') and (r.status_code == int(200))):
                print "Endpoint may accept Proxy requests. Validate!";
    except:
        print sys.exc_info();

def url_check(url):
    if(not url.startswith('http://') and (not url.startswith('https://'))):
        return 'http://'+url;
    else:
        return url;

def main():
    try:
        if(args.timeout is None):
            args.timeout = 5;
        if(args.u):
            url = args.u;
            scan( url_check(url) );
        elif(args.f):
            urls = get_urls_from_file(args.f);
            for url in urls:
                scan( url_check(url) );
        if((args.u is None)and (args.f is None)):
            print("\n[!] You need to specify one of them: [-h | -u | -f]");
    except:
        print sys.exc_info();

if ( __name__ == '__main__' ):
    main();

