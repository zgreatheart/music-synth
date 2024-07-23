from lib.log import get_logger
from lib.audio import get_music

log = get_logger(__name__)

if __name__ == '__main__':
    log.info('Beginning library import init')
    from lib.model import pipe2
    get_music(pipe2, "Tribal healing flute", 5)
