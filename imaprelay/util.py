import re

from StringIO import StringIO

FOLDER_LINE_RE = re.compile(r'\((?P<flags>.*?)\) "(?P<delimiter>.*)" (?P<name>.*)')

def parse_folder_line(line):
    flags, delimiter, mailbox_name = FOLDER_LINE_RE.match(line).groups()
    mailbox_name = mailbox_name.strip('"')
    return flags, delimiter, mailbox_name
