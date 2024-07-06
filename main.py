from lib.log import get_logger

log = get_logger(__name__)

if __name__ == '__main__':
    log.info('Beginning library import init')
    from lib.model import pipe2
