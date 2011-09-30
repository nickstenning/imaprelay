import imaplib
import smtplib
import logging

log = logging.getLogger(__name__)

_config = None

def configure(config):
    global _config
    _config = config

def make_imap_connection():
    # Connect to the server
    hostname = _config.get('imap', 'hostname')
    log.info('IMAP: Connecting to {0}'.format(hostname))
    connection = imaplib.IMAP4_SSL(hostname)

    # Login to our account
    username = _config.get('imap', 'username')
    password = _config.get('imap', 'password')
    log.info('IMAP: Logging in as {0}'.format(username))
    connection.login(username, password)

    return connection

def make_smtp_connection():
    # Connect to the server
    hostname = _config.get('smtp', 'hostname')
    log.info('SMTP: Connecting to {0}'.format(hostname))
    connection = smtplib.SMTP_SSL(hostname)

    # Login to our account
    username = _config.get('smtp', 'username')
    password = _config.get('smtp', 'password')
    log.info('SMTP: Logging in as {0}'.format(username))
    connection.login(username, password)

    return connection
