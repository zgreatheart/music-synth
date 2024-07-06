import logging

FORMAT = logging.Formatter('[%(levelname)s] %(asctime)s - %(name)s@%(funcName)s:%(lineno)d - %(message)s')
CONSOLE = logging.StreamHandler()
logging.getLogger().setLevel(logging.DEBUG)


def get_logger(name=__name__, level=logging.DEBUG, handler=CONSOLE) -> logging.Logger:
    log = logging.getLogger(name)
    handler.setLevel(level)
    handler.setFormatter(FORMAT)
    log.addHandler(handler)
    return log
