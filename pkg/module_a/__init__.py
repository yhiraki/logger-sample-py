# -*- coding: utf-8 -*-

from logging import getLogger

logger = getLogger(__name__)


def greet(text):
    logger.debug('-- start greeting --')
    print(text)
    logger.debug('---- end greeting --')
