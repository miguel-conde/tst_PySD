import os
import configparser

class prjSettings():
    def __init__(self):
        pass

### FOLDERS
the_folders = prjSettings()

# Project root is defined by globalsettings.py location 
the_folders.DIR_ROOT  = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")) 
the_folders.DIR_DATA = os.path.join(the_folders.DIR_ROOT, "data")
the_folders.DIR_DATA_RAW = os.path.join(the_folders.DIR_DATA, "raw")
the_folders.DIR_DATA_CLEAN = os.path.join(the_folders.DIR_DATA, "clean")

### FILES
the_files = prjSettings()

the_files.CFG_FILE = os.path.join(the_folders.DIR_ROOT, "config.ini")

### CONSTANTS
the_constants = prjSettings()


### CONFIG FILE
prj_cfg = prjSettings()

config = configparser.ConfigParser()

config.read(the_files.CFG_FILE)

prj_cfg.serveraliveinterval = config['DEFAULT']['serveraliveinterval']
prj_cfg.compression         = config['DEFAULT']['compression']
prj_cfg.compressionlevel    = config['DEFAULT']['compressionlevel']
prj_cfg.forwardx11          = config['DEFAULT']['forwardx11']