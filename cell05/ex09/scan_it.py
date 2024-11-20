#!/usr/bin/env python3

import sys 
if len(sys.argv) != 3:
    print("none")
else:
    key = sys.argv[1]
    search = sys.argv[2]
    count_search = search.count(key)
    if count_search == 0:
        print("none")
    else:
        print(count_search)
