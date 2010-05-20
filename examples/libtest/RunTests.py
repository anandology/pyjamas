class RunTests:
    def __init__(self):
        self.testlist = {}
        self.test_idx = 0

    def add(self, test):
        self.testlist[len(self.testlist)] = test

    def start_test(self):
        if self.test_idx >= len(self.testlist):
            return

        idx = self.test_idx
        self.test_idx += 1

        test_kls = self.testlist[idx]
        t = test_kls()
        t.start_next_test = getattr(self, "start_test")
        t.run()

