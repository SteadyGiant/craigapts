#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("/PATH/TO/craigapts/craigapts")

import pandas as pd
from search import CLSearch

nnj_ns8 = CLSearch(geo="newjersey", query='"no section 8"')
df = nnj_ns8.data
any(df.duplicated("post_id"))
