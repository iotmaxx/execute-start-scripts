""" 
execute_start_scripts - IoTmaxx Gateway Hardware Abstraction Layer
Copyright (C) 2023 IoTmaxx GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from .executeStartScripts import executeStartScripts
import logging
import time
import argparse

log = logging.getLogger()
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter('%(asctime)s %(levelname)-6s %(name)-20s: %(message)s')
formatter.converter = time.gmtime
# add formatter to ch
ch.setFormatter(formatter)

log.addHandler(ch)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start script executor.")
    parser.add_argument('--directory', default='/data/p1/etc/rc.start.d')
    args = parser.parse_args() 

    executeStartScripts(args.directory)
