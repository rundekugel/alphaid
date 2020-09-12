#!/usr/bin/env python
 """get a alphanumeric representative of a number"""

class Alphaid
 """
 get a alphanumeric representative of a number
 usage:
 a = Alphaid.alphaid(5) # 5=length of id 
 result = a.getAlphaIdFromNumber(345678)
 or
 result = getAlphaIdFromNumber(0xaabbccFF87)
 
 """
  alphanumeric_pool = "23456789abcdefghklmnpqrsuvwxyzABCDEFGHKLMNPQRSTUVWXYZ"
  pool_len = None
  _idlen = None
  
  def alphaid(self, idlen, pool=none):
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
    for pos in range(_idlen-1, -1, -1):
      b = number%pool_len
      print(b)
      number /= pool_len
      print(number)
      r = alphanumeric_pool[b] +r
    return r
    
  def setAlphanumericPool(self, pool):
    """
    set a string, with chars. this position of char is the value
    example for hex:
    "0123456789abcdef"
    """
    if pool:
      self.alphanumeric_pool = pool
    self.pool_len = len(alphanumeric_pool)
    
  def useOnlyUpperChars(self):
    """
    use only some upper case chars, which are easy to idenfify, 
    and not dangerous to confound
    """
    self.alphanumeric_pool = "ABCDEFGHKLMNPQRSTUVWXYZ"

  def etherMacToNumber(self, mac):
    """get number from mac-address"""
    r=0
    return 0
    
  def _posInPool(self, char):
    """get position of char in alphanumeric_pool"""
    #if not char in self.alphanumeric_pool:
    #  return -1
    for pos in range(self.pool_len):
      if char == self.alphanumeric_pool[pos]:
        return pos
    return -1
    
  def numberFromId(self, idstring):
    r=0
    for c in idstring:
        
# eof
    
