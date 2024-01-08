class Logger(object):

    def __init__(self):
        self.hmap = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message in self.hmap:
            if timestamp >= self.hmap[message]:
                self.hmap[message] = timestamp+10
                return True
            else:
                return False
                
        else:
            self.hmap[message] = timestamp+10
            return True