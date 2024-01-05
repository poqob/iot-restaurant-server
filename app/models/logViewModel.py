from log import Log
class LogViewModel:
    def __init__(self, id,log,date):
        self.id = log.id
        self.user = log.user
        self.action = log.action
        self.date = log.date