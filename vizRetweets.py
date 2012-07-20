# -*- coding: utf-8 -*-
#################################################################
##
## Based on the introduction__retweet_visualization.py from book
## Mining the Social Web, by Matthew A. Russell:
##  http://www.amazon.com/Mining-Social-Web-Analyzing-Facebook/dp/1449388345
##
## Improved by Beibei Yang (byang1@cs.uml.edu)
##
## Required libraries:
##  - twitter (https://github.com/sixohsix/twitter/)
##  - networkx (http://networkx.lanl.gov/)
##  - d3 (http://d3js.org/)
##
## To execute, use command-line:
##      python vizRetweets.py [keyword]
##
## For example:
##      python vizRetweets.py #bigdata
##
## This will retrieve all the users on retweets that contain 
## the #bigdata hashtag.
##
##################################################################

import sys
import os
import json
import re
import webbrowser
import codecs
import twitter
import networkx as nx

# Your query
Q = sys.argv[1]
Qname = ''.join([s for s in Q if re.match(r'\w', s)])

HTML_TEMPLATE = 'retweet_template.html'
OUT_NAME_BASE = '.'.join ( ['retweets', Qname])

OUT_DIR = 'out'

# A Json file to output the twitter data
OUT_JSON = '.'.join ( ['retweets', Qname, 'json'])
OUT = os.path.basename(HTML_TEMPLATE)



# Writes out a DOT language file that can be converted into an 
# image by Graphviz
def write_dot_output(g, out_file):

    out_file = OUT_NAME_BASE + ".dot"

    if not os.path.isdir(OUT_DIR):
        os.mkdir(OUT_DIR)

    try:
        nx.drawing.write_dot(g, os.path.join(OUT_DIR, out_file))
        print >> sys.stderr, 'Data file written to: %s' % os.path.join(os.getcwd(), OUT_DIR, out_file)
    except (ImportError, UnicodeEncodeError):

        # This block serves two purposes:
        # 1) Help for Windows users who will almost certainly not get nx.drawing.write_dot to work 
        # 2) It handles a UnicodeEncodeError that surfaces in write_dot. Appears to be a
        # bug in the source for networkx. Below, codecs.open shows one way to handle it.
        # This except block is not a general purpose method for write_dot, but is representative of
        # the same output write_dot would provide for this graph
        # if installed and easy to implement

        dot = ['"%s" -> "%s" [tweet_id=%s, avatar=%s]' % (n1, n2, g[n1][n2]['tweet_id'], g[n1][n2]['avatar'])
               for (n1, n2) in g.edges()]
        f = codecs.open(os.path.join(os.getcwd(),  OUT_DIR, out_file), 'w', encoding='utf-8')
        f.write('''strict digraph {
    %s
    }''' % (';\n'.join(dot), ))
        f.close()

        print >> sys.stderr, 'Data file written to: %s' % f.name

        return f.name

# Writes out an HTML page that can be opened in the browser
# that displays a graph 
def write_protovis_output(g, jsonfile):
    nodes = g.nodes()
    indexed_nodes = {}

    idx = 0
    for n in nodes:
        indexed_nodes.update([(n, idx,)])
        idx += 1

    links = []
    for n1, n2 in g.edges():
        links.append({'source' : indexed_nodes[n2], 
                      'target' : indexed_nodes[n1]})

    json_data = json.dumps({"nodes" : [{"nodeName" : n} for n in nodes], "links" : links}, indent=4)

    f = open(os.path.join(os.getcwd(), jsonfile), 'w')
    f.write(json_data)
    f.close()

    html = open(HTML_TEMPLATE).read() % ( Q, os.path.split(jsonfile)[1],)
    if not os.path.isdir(OUT_DIR):
        os.mkdir(OUT_DIR)
    f = open(os.path.join(os.getcwd(), OUT_DIR, OUT_NAME_BASE + ".html"), 'w')
    f.write(html)
    f.close()

    print >> sys.stderr, 'Data file written to: %s' % f.name

    return f.name

# Given a tweet, pull out any retweet origins in it and return as a list
def get_rt_origins(tweet):
    # Regex adapted from 
    # http://stackoverflow.com/questions/655903/python-regular-expression-for-retweets
    rt_patterns = re.compile(r"(RT|via)((?:\b\W*@\w+)+)", re.IGNORECASE)
    rt_origins = []

    try:
        rt_origins += [mention.strip() for mention in rt_patterns.findall(tweet)[0][1].split()]
    except IndexError, e:
        pass

    return [rto.strip("@") for rto in rt_origins]


# Get some search results for a query
twitter_search = twitter.Twitter(domain="search.twitter.com")
search_results = []
for page in range(1,6):
    #search_results.append(twitter_search.search(q="#bigdata", rpp=100, page=page))
    search_results.append(twitter_search.search(q=Q, rpp=100, page=page))

# Build up a graph data structure
g = nx.DiGraph()

all_tweets = [tweet for page in search_results for tweet in page['results']]
for tweet in all_tweets:
    rt_origins = get_rt_origins(tweet['text'])
    if not rt_origins:
        continue
    for rt_origin in rt_origins:
        g.add_node(tweet['from_user'], {'avatar': tweet['profile_image_url']} )
        g.add_edge(rt_origin, tweet['from_user'], {'tweet_id': tweet['id'], 'avatar': tweet['profile_image_url']})

# Print out some stats
print >> sys.stderr, "Number nodes:", g.number_of_nodes()
print >> sys.stderr, "Num edges:", g.number_of_edges()
print >> sys.stderr, "Num connected components:", len(nx.connected_components(g.to_undirected()))
print >> sys.stderr, "Node degrees:", sorted(nx.degree(g))

# Write Graphviz output
write_dot_output(g, OUT)

# Write Protovis output and open in browser
protovis_output = write_protovis_output(g, os.path.join(OUT_DIR, OUT_JSON) )
webbrowser.open('file://' + protovis_output)
