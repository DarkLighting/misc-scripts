#!/usr/bin/python2

import time
import sys
import dns.resolver

def print_help():
    print("\nSyntax: "+sys.argv[0]+" <domain> [record type]")
    print("\n\tThis tool checks for dns servers that allow zone transfers\n")
    exit()

def domain_val(_domain):
    if(domain is not None):
        if(domain.count('.') < 1):
            print("\n\tInvalid domain.")
            print_help()

def print_soa(rec):
    for entry in rec:
        print("\t"+str(entry.mname)[:-1])

def get_records(records):
    for rec in records:
        print("\t"+rec)

if(len(sys.argv) == 1 or len(sys.argv) > 3):
    print_help()

domain = sys.argv[1]
domain_val(domain)
nameservers = list()

try:
    resolver = dns.resolver.Resolver();
    resolver.timeout = 10;
    resolver.lifetime = 10;
    soa = resolver.query(domain, 'SOA')
    print("\nStart of Authority - "+domain)
    print_soa(soa)
    for ns in resolver.query(domain, 'NS'):
        nameservers.append(ns.to_text()[:-1])
    print("\nList of nameservers - "+domain)
    nameservers.sort()
    get_records(nameservers)
    print("\nTrying to make zone transfers from nameservers...")
    for ns_server in nameservers:
        xfr = dns.query.xfr(ns_server, domain)
        try:
            answer = next(xfr)
            if(answer is not None):
                print 'none'
                print("*** Server "+ns_server+" allows zone transfers! ***")
        except dns.resolver.Timeout:
            print("\tRequest timed out contacting server "+ns_server)
        except:
            print("\tNameserver "+ns_server+" doesn\'t allow zone transfers")
    print("\n")    

except:
    print("\n")
    print(sys.exc_info())
