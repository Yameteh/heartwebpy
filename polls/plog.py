import logging

logger = logging.getLogger("django")


def i(msg):
    logger.info(msg)


def d(msg):
    logger.debug(msg)


def w(msg):
    logger.warn(msg)

def e(msg):
    logger.error(msg)