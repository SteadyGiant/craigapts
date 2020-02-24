#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from search import CLSearch
import sys

sys.path.append(r"/home/evroot/Dropbox/Projects/badslist2/craigapts/craigapts")

GEO = "newjersey"
QUERY = "'no section 8'"

_all = CLSearch(GEO)
n_all = _all.data.shape[0]

_ns8 = CLSearch(GEO, QUERY)
n_ns8 = _ns8.data.shape[0]

pct_ns8 = round((n_ns8/n_all)*100, 1)
print(f"{n_ns8:,} ({pct_ns8}%) of all {n_all:,} Craigslist ads in {GEO} contain {QUERY}.")
