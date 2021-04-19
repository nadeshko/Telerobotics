import requests
import time
import json
import sys
import logging

logging.getLogger('urllib3').setLevel(logging.CRITICAL)


URL = "http://192.168.1.164:5000"
    
def tanq_post(path, params = None):
    headers = {'Content-type': 'application/json'}
    rsp = requests.post(URL + path, data=json.dumps(params), headers=headers)
    #print path, rsp.status_code, rsp.content
    ret = rsp.json() if rsp.status_code == requests.codes.ok else rsp.content
    return ret, rsp.status_code

def tanq_get(path):
    rsp = requests.get(URL + path)
    #print path, rsp.status_code, rsp.content
    ret = rsp.json() if rsp.status_code == requests.codes.ok else rsp.content
    return ret, rsp.status_code


def fwd_on():
    return tanq_post("/fwd/on")

def fwd_off():
    return tanq_post("/fwd/off")

def back_on():
    return tanq_post("/back/on")

def back_off():
    return tanq_post("/back/off")

def right_on():
    return tanq_post("/right/on")

def right_off():
    return tanq_post("/right/off")

def left_on():
    return tanq_post("/left/on")

def left_off():
    return tanq_post("/left/off")

def set_motors(mode):
    return tanq_post("/motor/" + mode)



def photo():
    return tanq_post("/photo/make")

def photo_list():
    js, code = tanq_get("/photo/list")
    ret = None if code != requests.codes.ok else js["list"]
    return ret, code

def device_name():
    return tanq_get("/name")

def cam_up():
    return tanq_post("/cam/up")

def cam_down():
    return tanq_post("/cam/down")

def cam_left():
    return tanq_post("/cam/left")


def cam_right():
    return tanq_post("/cam/right")

def detect_haar(id):
    return tanq_post("/detect/haar/" + id)

def detect_dnn(id):
    return tanq_post("/detect/dnn/" + id)


def version():
    return tanq_get("/version")

def ping():
    return tanq_get("/ping")

def dist():
    return tanq_get("/dist")

def classify_tf(id):
    return tanq_post("/classify/tf/" + id)



def get_photo(pid, outpath = "./"):
    path = "/photo/" + pid
    rsp = requests.get(URL + path, stream=True)
    if rsp.status_code != requests.codes.ok:
        print("No photo %s found" % pid)
        return

    fname = outpath + "/" + pid + ".jpg"
    with open(fname, "wb") as f:
        for chunk in rsp.iter_content(1024):
            f.write(chunk)

    logging.debug (("Saved", fname))
    return fname


if __name__ == '__main__':
    #print classify_tf(sys.argv[1])
    #print device_name()
    """
    set_motors("ff")
    time.sleep(0.2)
    print("stop left")
    set_motors("s0")
    time.sleep(2)
    set_motors("f0")
    time.sleep(0.2)
    print("stop all")
    set_motors("ss")
    """
    left_on()
    time.sleep(1)
    left_off()