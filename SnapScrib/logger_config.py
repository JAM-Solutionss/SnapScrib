import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] - %(message)s',
    )
    return logging.getLogger(__name__)

LOGGER = setup_logger()
