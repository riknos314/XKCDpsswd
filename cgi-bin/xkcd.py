#!/usr/bin/python
import os


stringofnames = os.environ['QUERY_STRING']
namepairs = stringofnames.split('=')
