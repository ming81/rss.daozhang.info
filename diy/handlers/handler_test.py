# coding: utf-8

from public import AESCipher

key = '8d09ae789besogou'
iv = '0000000000000000'

openid = 'oIWsFt21qSSM8vUrjrXBk4GGOrRk'
res = 'JFsFoDagFY8ro03H%2BQ5cduRbVoEcle8dbeDpcU3K9xjHIgInVZ5mx0LUBJfpKArGYIlCY'

aes = AESCipher(key, iv)
encryptedtext = aes.getReq(openid)

print encryptedtext
print res
if res == encryptedtext:
    print "Yes"
