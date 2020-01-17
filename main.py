# -*- coding: utf-8 -*-

from pkg import module_a
from logging import config, getLogger

config.fileConfig('logging.conf')

logger = getLogger(__name__)

if __name__ == '__main__':
    logger.debug('start main')
    module_a.greet('hoge')
