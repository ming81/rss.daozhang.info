#_*_ coding:utf-8 _*_

import datetime
from dateutil import tz
import base64
from Crypto.Cipher import AES
import urllib
import math

class LocalTimezone(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=8)

    def dst(self, dt):
        return datetime.timedelta(0)

def getNow():
    utc = datetime.datetime.utcnow()
    utc = utc.replace(tzinfo=tz.gettz('UTC'))
    local = utc.astimezone(LocalTimezone())
    return local

class AESCipher(object):
    # key = '8d09ae789be' + 'sogou'
    # iv = '0000000000000000'
    # 
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.bs = 16

    def encrypt(self, raw):
        raw = raw + 'hdq=' + 'sogou'
        raw = self._pad(raw)
        cipher = AES.new( self.key, AES.MODE_CBC, self.iv )
        return base64.b64encode( self.iv + cipher.encrypt( raw ) )

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _e(self, prencrypt):
        so = 'sogou'
        l = 0
        res = ''
        for at in range(len(prencrypt)):
            res += prencrypt[at]
            if at == math.pow(2, l):
                res += so[at]
                l = l + 1

    def getReq(self, raw):
        res = self.encrypt(raw)
        res = self._e(res)
        return self.quote_url(res)

    def quote_url(self, url, safe='~()*!.\''):
        """URL-encodes a string (either str (i.e. ASCII) or unicode);
        uses de-facto UTF-8 encoding to handle Unicode codepoints in given string.
        """
        return urllib.quote(unicode(url).encode('utf-8'), safe)
