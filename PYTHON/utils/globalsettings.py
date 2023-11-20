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

the_folders.OUTPUTS = os.path.join(the_folders.DIR_ROOT, "outputs")
the_folders.OUTPUTS_FILES = os.path.join(the_folders.OUTPUTS, "files")
the_folders.OUTPUTS_REPORTS = os.path.join(the_folders.OUTPUTS, "reports")
the_folders.DIR_OUTPUTS_DDBB = os.path.join(the_folders.OUTPUTS, "ddbb")

the_folders.MODELS = os.path.join(the_folders.DIR_ROOT, "models")

### FILES
the_files = prjSettings()

the_files.CFG_FILE = os.path.join(the_folders.DIR_ROOT, "config.ini")

the_files.TEA_CUP_MODEL = os.path.join(the_folders.MODELS, 'Teacup.mdl')
the_files.SI_MODEL = os.path.join(the_folders.MODELS, 'SI.mdl')

the_files.EBOLA_DATA = os.path.join(the_folders.DIR_DATA_CLEAN, "Ebola_in_SL_Data.csv")

the_files.EXAMPLE_DB = os.path.join(the_folders.DIR_OUTPUTS_DDBB, 'example.db')

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