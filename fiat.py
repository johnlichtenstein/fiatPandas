#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:47:33 2020

@author: jcl
"""

import pandas as pd
from pandas import DataFrame # import DataFrame separately to act on 

# we can define a method anyplace
def xTab(self, vert, hor):
    """
    Parameters
    ----------
    vert : string
        column name for vertical.
    hor : string
        column name for horizontal.

    Returns
    -------
    None.
    """
    try:
        return pd.crosstab(self[vert], self[hor])
    except:
        return None

DataFrame.xTab = xTab # give the xTab method to DataFrame

if __name__ == "__main__":
    exampleD = {"sv": "a a a a a b b b b b".split() \
                , "x": [1, 2, 3, 2, 3, 4, 4, 5, 6, 1]}
    exampleR = DataFrame(exampleD) 
    # print(exampleR)
    # print ()
    
    # classic crosstab calls are messy
    print (pd.crosstab(exampleR.query("x < 6").x \
                           , exampleR.query("x < 6").sv))
    print ()
    # xTab calls are neater
    print (exampleR.query("x < 6").xTab("x", "sv"))