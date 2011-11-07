import logging

logging.basicConfig(format='%(asctime)-15s  %(levelname)-8s  %(message)s',
                    level=logging.INFO)

log = logging.getLogger(__name__)

__version__ = '0.0.4'

__all__ = ['Relay']

from .relay import Relay
