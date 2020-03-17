#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.append("/PATH/TO/craigapts")

import pandas as pd
import craigapts as cg

nnj_ns8 = cg.CLSearch(geo="newjersey", query='"no section 8"')
df = nnj_ns8.data
any(df.duplicated("post_id"))
