from mycelery.main import app
import time
import logging

log = logging.getLogger("django")


@app.task
def send_sms(mobile):
    print("向 %s 发送短信成功！" % mobile)
    time.sleep(3)
    return "send sms ok!"


@app.task
def send_sms2(mobile):
    print("向手机号%s发送短信成功!" % mobile)
    time.sleep(5)
    return "send_sms2 OK"
