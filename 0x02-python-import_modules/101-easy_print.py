#!/usr/bin/python3
import logging

FORMAT = '%(message)s'
logging.basicConfig(format=FORMAT)
#  __name__ is module's name
logger = logging.getLogger(__name__)
logger.warning('#pythoniscool\n')
