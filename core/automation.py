# automation.py
# path: .../core/automation.py
# date: 2024-11-18
# Author: C. Zuluaga
# version: 0.0.1
# License: MIT

'''
Function to create Automation to call scripts and run them
Using schedule library to create fucntions to run scripts at specific times
''' 

import schedule
import time
import os
import sys
import logging
from datetime import datetime
from core import config
from core import logger
from core import utils

# Set up logging
log = logger.setup_logger('automation', 'automation.log')
log.info('Starting automation')

# Get configuration
config = config.get_config()

# Get the path to the scripts
script_path = config['scripts']['path']

# Get the scripts to run
scripts = config['scripts']['scripts']

# Get the time to run the scripts
times = config['scripts']['times']

# Get the interval to run the scripts
intervals = config['scripts']['intervals']
