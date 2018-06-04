#
# Author: Chris Zhu
# Created on: 03/07/2018
# Last Update: 03/07/2018

import logging
logging.basicConfig(filename='myapp_test.log', level=logging.INFO)

class AbstractLoader(object):
    def __init__(self):
        pass

    def load(self):
        raise NotImplementedError

    def write(self):
        raise NotImplementedError

    def cleanup(self):
        raise NotImplementedError


class HistDataLoader(AbstractLoader):
    def __init__(self):
        super(HistDataLoader, self).__init__()
        self.aa = 1

    def load(self):
        logging.info('HistDataLoader.load called')
        return 1


if __name__ == '__main__':
    HistDataLoader().load()