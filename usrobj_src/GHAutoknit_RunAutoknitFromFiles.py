"""
Run Autoknit as a threaded subprocess from specified files.
TODO: update docstring
    Inputs:
        Run: Connect a button and set to true to start the autoknit instance {item, boolean}
        obj: Path to the *.obj file to read the model from {item, str}
        constraints: Path to the *.cons file to read the constraints from {item, str}
        obj_scale: {item, float}
        stitch_width: {item, float}
        stitch_height: {item, float}
        save_traced: Path where the traced file (*.st) should be saved when peeling is finished {item, str}
        peel_step: Number of steps to peel the model. -1 will peel the whole model {item, int}
    Outputs:
        R: Boolean identifying if this autoknit instance is currently running or not {item, bpolean}
    Remarks:
        Author: Max Eschenbach
        License: MIT License
        Version: 211029
"""

# PYTHON STANDARD LIBRARY IMPORTS
from __future__ import division
import subprocess
import threading

# GHPYTHON SDK IMPORTS
from ghpythonlib.componentbase import executingcomponent as component
import Grasshopper, GhPython
import System
import Rhino
import rhinoscriptsyntax as rs

# CUSTOM RHINO IMPORTS
from scriptcontext import sticky as st

# LOCAL MODULE IMPORTS
import ghautoknit as ghak

# GHENV COMPONENT SETTINGS
ghenv.Component.Name = "RunAutoknitFromFiles"
ghenv.Component.NickName ="RAFF"
ghenv.Component.Category = "GHAutoknit"
ghenv.Component.SubCategory = "3 Run Autoknit"

class RunAutoknitFromFiles(component):
    
    def RunScript(self, Run, obj, constraints, obj_scale, stitch_width, stitch_height, save_traced, peel_step):
        
        # SETUP CODE -----------------------------------------------------------
        
        running_key, reset_key = ghak.Engine.InitializeComponentInterface(self)
        
        if running_key not in st:
            st[running_key] = False
        if reset_key not in st:
            st[reset_key] = False
        
        # THREADED FUNCTION DEFINTION ------------------------------------------
        
        # define threaded call function
        def threaded_call():
            retcode = subprocess.call(Command)
            st[running_key] = False
            st[reset_key] = True
            
            self.ExpireSolution(True)
            return retcode
        
        # COMMAND COMPILATION --------------------------------------------------
        
        Command = ghak.Engine.CompileCommand(obj,
                                            constraints,
                                            obj_scale,
                                            stitch_width,
                                            stitch_height,
                                            save_traced,
                                            peel_step)
        
        # throw runtime message and abort if path is not set correctly!
        if not Command:
            rml = self.RuntimeMessageLevel.Warning
            self.AddRuntimeMessage(rml, "_AK_RAW_PATH_ is not set correctly! " +
                                        "Please open Environment.py and set " +
                                        "the path to your autoknit " +
                                        "installation.\nCurrent path is:\n" +
                                        ghak.Environment._AK_PATH_)
            return False
        
        # START AUTOKNIT THREAD ------------------------------------------------
        
        if Run and st[running_key] is False:
            # make thread and start it
            thread = threading.Thread(target=threaded_call)
            thread.start()
            # set keys
            st[running_key] = True
            st[reset_key] = False
        
        if st[reset_key] is True:
            st[running_key] = False
        
        # return info about running autoknit thread
        R = st[running_key]
        self.Message = "Autoknit Running: " + str(st[running_key])
        
        # return outputs if you have them; here I try it for you:
        return R