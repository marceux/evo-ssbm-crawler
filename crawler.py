#!/usr/bin/env python

"""
EVO SSBM Bracket Crawler

by Marceux (@Marceux)

Based on the Web Crawler by James Mills (James dot Mills st dotred dot com dot au)
"""

import re
import sys
import urllib2
from bs4 import BeautifulSoup

## Player Handle
searchHandle = 'Type Your Player Handle Here'

## EVO Waves
waves = [
    'a101',
    'a102',
    'a103',
    'a104',
    'a105',
    'a106',
    'a107',
    'a108',
    'a109',
    'a110',
    'a111',
    'a112',
    'a113',
    'a114',
    'a115',
    'a116',
    'a117',
    'a118',
    'a119',
    'a120',
    'a121',
    'a122',
    'b101',
    'b102',
    'b103',
    'b104',
    'b105',
    'b106',
    'b107',
    'b108',
    'b109',
    'b110',
    'b111',
    'b112',
    'b113',
    'b114',
    'b115',
    'b116',
    'b117',
    'b118',
    'b119',
    'b120',
    'b121',
    'b122',
    'c101',
    'c102',
    'c103',
    'c104',
    'c105',
    'c106',
    'c107',
    'c108',
    'c109',
    'c110',
    'c111',
    'c112',
    'c113',
    'c114',
    'c115',
    'c116',
    'c117',
    'c118',
    'c119',
    'c120',
    'c121',
    'c122',
    'd101',
    'd102',
    'd103',
    'd104',
    'd105',
    'd106',
    'd107',
    'd108',
    'd109',
    'd110',
    'd111',
    'd112',
    'd113',
    'd114',
    'd115',
    'd116',
    'd117',
    'd118',
    'd119',
    'd120',
    'd121',
    'd122',
    'e101',
    'e102',
    'e103',
    'e104',
    'e105',
    'e106',
    'e107',
    'e108',
    'e109',
    'e110',
    'e111',
    'e112',
    'e113',
    'e114',
    'e115',
    'e116',
    'e117',
    'e118',
    'e119',
    'e120',
    'e121',
    'e122',
    'f101',
    'f102',
    'f103',
    'f104',
    'f105',
    'f106',
    'f107',
    'f108',
    'f109',
    'f110',
    'f111',
    'f112',
    'f113',
    'f114',
    'f115',
    'f116',
    'f117'
]

__version__ = "0.1"
AGENT = "%s/%s" % (__name__, __version__)

class Fetcher(object):

    def __init__(self, wave):
        self.url = "http://evo2015.s3.amazonaws.com/brackets/ssbm_" + wave + ".html"
        self.urls = []
        self.wave = wave

    def __getitem__(self, x):
        return self.urls[x]

    def _addHeaders(self, request):
        request.add_header("User-Agent", AGENT)

    def open(self):
        url = self.url
        try:
            request = urllib2.Request(url)
            handle = urllib2.build_opener()
        except IOError:
            return None
        return (request, handle)

    def fetch(self):
        request, handle = self.open()
        self._addHeaders(request)
        if handle:
            try:
                content = unicode(handle.open(request).read(), "utf-8",
                        errors="replace")
                soup = BeautifulSoup(content)
                divs = soup.find_all('div', {"class" : "player-handle"})
            except urllib2.HTTPError, error:
                if error.code == 404:
                    print >> sys.stderr, "ERROR: %s -> %s" % (error, error.url)
                else:
                    print >> sys.stderr, "ERROR: %s" % error
                tags = []
            except urllib2.URLError, error:
                print >> sys.stderr, "ERROR: %s" % error
                tags = []

            players = []
            
            for div in divs:
                playerHandle = div.string.strip()
                
                if playerHandle and playerHandle == searchHandle:
                    print "Wave: %s" % self.wave
                    print playerHandle

def main():
    for wave in waves:
        page = Fetcher(wave)
        page.fetch()

if __name__ == "__main__":
    main()