#!/usr/bin/env python2

import sys
import os
import time
import logging
import mimetypes
import traceback

from daemon import GenericDaemon


class SampleDaemon(GenericDaemon):
    def __init__(self, pidfile, logger, **kwargs):
        super(SampleDaemon, self).__init__(pidfile, logger, **kwargs)


    def work(self):
        self.log.info("I did some work!") 

    def run(self, loopForever=True):
        try:
            if loopForever:
                while True:
                    self.work()
                    time.sleep(5)
            else:
                self.work()
        except Exception, e:
            self.log.error("A runtime exception occured. {0}".format(e))
            raise e

if __name__ == "__main__":
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)
    fh = logging.FileHandler("sample_daemon.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
    fh.setFormatter(formatter)
    log.addHandler(fh)
    daemon = SampleDaemon('/home/lam/workspace/mail/daemon/sample_daemon.pid', log)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'run' == sys.argv[1]:
            daemon.run(loopForever=False)
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
