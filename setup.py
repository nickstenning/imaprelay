from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='imaprelay',
    description='IMAP-to-SMTP relay: imaprelay relays messages from an IMAP INBOX to an SMTP server',
    long_description=long_description,
    author='Nick Stenning',
    author_email='nick@whiteink.com',
    url='http://github.com/nickstenning/imaprelay',
    license='MIT',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'imaprelay = imaprelay.command:main'
        ]
    }
)
