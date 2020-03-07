#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("/PATH/TO/craigapts/craigapts")

from search import CLSearch

nj_ns8 = CLSearch(geo="newjersey", query="'no section 8'")
nj_ns8_df = nj_ns8.data
