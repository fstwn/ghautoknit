# PYTHON STANDARD LIBRARY IMPORTS ---------------------------------------------
from __future__ import absolute_import
from os import path

# ALL LIST --------------------------------------------------------------------
__all__ = [
    "_AK_RAW_PATH_",
    "_AK_PATH_",
    "_AK_INTERFACE_"
]

# ENVIRONMENT VARIABLES -------------------------------------------------------

# PATH TO COMPILED AUTOKNIT FOLDER (WHERE INTERFACE.EXE IS LOCATED!)
_AK_RAW_PATH_ = r"C:\path\to\autoknit\dist"

# MORE ENVIRONMENT VARIABLES (DON'T CHANGE THIS!) -----------------------------
_AK_PATH_ = path.normpath(_AK_RAW_PATH_)
_AK_INTERFACE_ = path.normpath(_AK_RAW_PATH_ + r"\interface")

# MAIN ------------------------------------------------------------------------
if __name__ == '__main__':
    pass
