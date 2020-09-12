#!/usr/bin/env python

"""
Test class Alphaid.
Licence: MIT
"""

__author__  = "rundekugel@github.com"
__version__ = "0.0.1"
__date__    = "2020-10-12"


import alphaid

mac = "00:23-45AABB-cd"
a = alphaid.Alphaid(6*2)
a.setAlphanumericPoolHex()
e = a.etherMacToNumber(mac)
r = a.getAlphaIdFromNumber(e)

mac = mac.replace(':','').replace('-','').upper()
print("assume %s == %s"%(mac,r))
if r==mac:
  print("Result ok!")
else:
  print("Result wrong")
  
a = alphaid.Alphaid(5)
e = a.etherMacToNumber(mac[7:])
a.useOnlyUpperChars()
r = a.getAlphaIdFromNumber(e)

soll="CNVUF"
print("assume %s == %s"%(r,soll))
if r==soll:
  print("Result ok!")
else:
  print("Result wrong")

# eof
