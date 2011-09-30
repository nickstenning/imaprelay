import logging

logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.INFO)
log = logging.getLogger(__name__)

__version__ = '0.0.1'

__all__ = ['Relay']

from .relay import Relay