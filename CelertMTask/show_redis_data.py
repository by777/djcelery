import redis
from pprint import pprint as print
r = redis.Redis(host='127.0.0.1', port=6379, db=1)
print(r.keys('*'))
for i in r.lrange('celery', 0, -1):
    print(i)