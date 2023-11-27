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
import argparse
import logging
import time
import os
import subprocess

log = logging.getLogger(__name__)

def executeStartScripts(scriptPath):
    if not os.path.isdir(scriptPath):
        log.info(f"Script path {scriptPath} does not exist.")
        return
    for entry in os.scandir(scriptPath):
        if not entry.is_file():
            log.debug(f"Ignoring {entry.path}, not a file.")
            continue
        if not os.access(entry, os.X_OK):
            log.debug(f"Ignoring {entry.path}, not executable.")
            continue
        log.info(f"Executing {entry.path}.")
        try:
            result = subprocess.run([entry.path])
        except Exception as e:
            log.error(f"Execution of {entry.path} failed with error {e}.")
        else:
            log.info(f"{entry.path} exited with result code {result.returncode}.")


