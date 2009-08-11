
# vim: set ts=4 sw=4 expandtab:

class TimeVO(object):
    start = None
    end = None
    project = None
    description = None
    
    def __init__(self, start, end, project, description = ''):
        self.start = start
        self.end = end
        self.project = project
        self.description = description

    def isEmpty(self):
        if self.start: return False
        if self.end: return False
        if self.project: return False
        if self.description: return False
        return True
