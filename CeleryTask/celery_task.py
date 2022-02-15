import celery
import time

backend = 'redis://1247.0.0.1:6379/3'
broker = 'redis://127.0.0.1:6379/4'
cel = celery.Celery('test', backend=backend, broker=broker)


@cel.task
def send_email(name):
    print("向%s发送邮件..." % name)
    time.sleep(5)
    print("向%s发送邮件完成" % name)
    return "ok"


@cel.task
def semd_msg(name):
    print("向%s发送短信..." % name)
    time.sleep(5)
    print("向%s发送短信完成" % name)
    return "ok"
