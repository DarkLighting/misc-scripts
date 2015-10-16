#!/usr/bin/env python
#
# query-summary.py
# Search Shodan and print summary information for the query.
#
# Author: achillean
 
import shodan
import sys
 
# Configuration
API_KEY = sys.argv[1]; 
#API_KEY = 'Ocxy16a5xMTcbXcXr76PPOohnXqZhiwI'; 
 
# The list of properties we want summary information on
FACETS = [
    ('domain',50),
    ('port',50),
    ('product',50),
]
 
FACET_TITLES = {
    'domain': 'Top 50 Domains',
    'port': 'Top 50 Ports',
    'product': 'Top 50 Services',
}
# Input validation
if len(sys.argv) == 2:
    print 'Usage: %s <API key> <search query>' % sys.argv[0]
    sys.exit(1)
 
try:
    # Setup the api
    api = shodan.Shodan(API_KEY)
    # Generate a query string out of the command-line arguments
    query = ' '.join(sys.argv[2:])
    # Use the count() method because it doesn't return results and doesn't require a paid API plan
    # And it also runs faster than doing a search().
    result = api.count(query, facets=FACETS)
 
    print 'Shodan Summary Information'
    print 'Query: %s' % query
    print 'Total Results: %s\n' % result['total']
 
    # Print the summary info from the facets
    for facet in result['facets']:
        print FACET_TITLES[facet]
        for term in result['facets'][facet]:
            print '%s: %s' % (term['value'], term['count'])
 
        # Print an empty line between summary info
        print ''
 
except Exception, e:
    print 'Error: %s' % e
    sys.exit(1)
