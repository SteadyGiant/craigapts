#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import craigapts as cg

GEO = "newjersey"
QUERY = "'no section 8'"

_all = cg.CLSearch(GEO)
n_all = _all.data.shape[0]

_ns8 = cg.CLSearch(GEO, QUERY)
n_ns8 = _ns8.data.shape[0]

pct_ns8 = round((n_ns8/n_all)*100, 1)
print(f"{n_ns8:,} ({pct_ns8}%) of all {n_all:,} Craigslist ads in {GEO} contain {QUERY}.")


craigslists = cg.craigslists()
print(craigslists)
