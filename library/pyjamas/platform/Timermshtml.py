def init():
    global timeout_add
    global timeout_end
    timeout_add = pyjd.timer.set_timer
    timeout_end = pyjd.timer.kill_timer
