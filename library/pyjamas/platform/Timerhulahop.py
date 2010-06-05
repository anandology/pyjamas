
def kill_timer(timer):
    # TODO: Check if the hasattr call _should_ be omitted
    if hasattr(timer, "cancel"):
        timer.cancel()


def init():
    global timeout_add
    global timeout_end
    timeout_add = pyjd.gobject.timeout_add
    timeout_end = kill_timer

class Timer:
    def notify(self, *args):
            pyjd.add_timer_queue(self._notify)

