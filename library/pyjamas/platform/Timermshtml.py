def set_timer(interval, fn):
    return pyjd.threading.Timer(interval / 1000.0, fn)
def kill_timer(timer):
    timer.cancel()

def init():
    global timeout_add
    global timeout_end
    timeout_add = set_timer
    timeout_end = kill_timer
