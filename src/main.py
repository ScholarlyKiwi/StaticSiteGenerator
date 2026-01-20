from textnode import *
from leafnode import LeafNode
from page_functions import generate_pages_recursive

import os
import logging
import shutil
import sys

log_debug = False

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"        
    if not basepath.endswith("/"):
        basepath = basepath + "/"
    if not basepath.startswith("/"):
        basepath = "/" + basepath
    copy_directory("static", "public")
    generate_pages_recursive("content", "template.html", "public", basepath)

def copy_directory(source, destination):
    if log_debug:
        log_level = logging.DEBUG
    else:
        log_level= logging.WARNING

    logger = logging.getLogger('my_logger')
    logger.setLevel(log_level)
    file_handler = logging.FileHandler('copy_directory.log')
    file_handler.setLevel(log_level)
    logger.addHandler(file_handler)

    logger.debug(f'Starting copy_directory: {source}, {destination}')

    if not os.path.exists(source):
        logger.error(f"Source directory '{source}' does not exist.")
        return
    if not os.path.exists(destination):
        logger.error(f"Desitnation directory '{destination}' does not exist.")
        return
    if '..' in source:
        logger.error(f"Source directory invalid: '{source}'")
    if '..' in destination:
        logger.error(f"Destination directory invalid: '{source}'")
    
    logger.debug(f'Removing path - {destination}')
    shutil.rmtree(destination)
    logger.debug(f'Creating path - {destination}')
    os.mkdir(destination)

    contents = os.listdir(source)
    for object in contents:
        object_path = os.path.join(source, object)
        object_dest = os.path.join(destination, object)
        if os.path.isfile(object_path):
            logger.debug(f'Copying file {object_path} to {object_dest}')
            shutil.copy(object_path, object_dest)
        else:
            logger.debug(f'Copying Directory {object_path} to {object_dest}')
            os.mkdir(object_dest)
            copy_directory(object_path, object_dest)
        

    




main()