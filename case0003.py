import redis
from case0001 import generatecode

r = redis.StrictRedis(host='139.129.xx.ooo', port=6379, db=0)
codes = generatecode(200, 6, 10)
for code in codes:
    r.set(int(code[0:6], 16), code)