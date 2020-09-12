#!/usr/bin/env python

"""
Get a alphanumeric representative of a number.
Licence: MIT
"""

__author__  = "rundekugel@github.com"
__version__ = "0.0.1"
__date__    = "2020-10-12"


class Alphaid:
  """
  get a alphanumeric representative of a number
  usage:
  a = Alphaid.alphaid(5) # 5=length of id 
  result = a.getAlphaIdFromNumber(345678)
  or
  result = getAlphaIdFromNumber(0xaabbccFF87)

  """
  alphanumeric_pool = "23456789abcdefghklmnpqrsuvwxyzABCDEFGHKLMNPQRSTUVWXYZ"
  _pool_len = None
  _idlen = None
  
  def __init__(self, idlen, pool=None):
    """
    initiate this class with the length of the desired id-result
    and optionally a new pool of alphanumeric chars, to use for
    encoding.
    """
    self._idlen = idlen
    self.setAlphanumericPool(pool)
    
  def getAlphaIdFromNumber(self, number):
    """get a alphanumeric representative of a number"""
    r= "" # alphanumeric_pool[0]*_idlen;
    if not self._pool_len:
      return None
    for pos in range(self._idlen-1, -1, -1):
      b = number%self._pool_len
      print(b)
      number /= self._pool_len
      print(number)
      r = self.alphanumeric_pool[b] +r
    return r
    
  def setAlphanumericPool(self, pool):
    """
    set a string, with chars. this position of char is the value
    example for hex:
    "0123456789abcdef"
    """
    if pool:
      self.alphanumeric_pool = pool
    self._pool_len = len(self.alphanumeric_pool)
    
  def setAlphanumericPoolHex(self):
    """
    sets the pool to hex.
    """
    self.setAlphanumericPool("0123456789abcdef")
    
  def useOnlyUpperChars(self):
    """
    use only some upper case chars, which are easy to idenfify, 
    and not dangerous to confound
    """
    self.alphanumeric_pool = "ABCDEFGHKLMNPQRSTUVWXYZ"

  def etherMacToNumber(self, mac):
    """get number from mac-address AA-BB-CC-DD-EE-FF or AA:BB:CC:DD:EE:FF"""
    hexchars = "0123456789abcdef"
    r=0

    for h in mac:
      if h in hexchars:
        r *= 0x10
        r += int(h,0x10)
    return r
    
  def _posInPool(self, char):
    """get position of char in alphanumeric_pool"""
    #if not char in self.alphanumeric_pool:
    #  return -1
    for pos in range(self._pool_len):
      if char == self.alphanumeric_pool[pos]:
        return pos
    return -1
    
  def numberFromId(self, idstring):
    r=0
    f=0
    for c in idstring:
      p = self._posInPool(c)
      if p>-1:
       r += p * self._pool_len^f
       f+=1
    return p
    
# eof
