import ConfigParser
import logging
import os
import stat
import sys

from StringIO import StringIO

from . import connection
from . import relay

log = logging.getLogger('imaprelay')

DEFAULT_CONFIG = """\
[relay]
inbox=INBOX
archive=Archive
interval=30
"""

def main():
    if '-v' in sys.argv:
        log.setLevel(logging.DEBUG)

    configfile = os.path.expanduser('~/.secret/imaprelay.cfg')

    st = os.stat(configfile)
    if bool(st.st_mode & (stat.S_IRGRP | stat.S_IROTH)):
        raise Exception("Config file (%s) appears to be group- or "
                        "world-readable. Please `chmod 400` or similar."
                        % configfile)

    config = ConfigParser.ConfigParser()
    config.readfp(StringIO(DEFAULT_CONFIG))
    config.read([configfile])

    connection.configure(config)

    rly = relay.Relay(config.get('relay', 'to'),
                      config.get('relay', 'inbox'),
                      config.get('relay', 'archive'))

    rly.loop(int(config.get('relay', 'interval')))