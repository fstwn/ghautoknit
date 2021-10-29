"""
Load an Autoknit *.cons file and interpret the constraints in it.
    Inputs:
        Mesh: The mesh to build the model with {item, mesh}
        Constraints: The constraints to build the model with as Autoknit Constraints {list, Autoknit Constraint}
    Outputs:
        Model: The vertices from the constraint file as tuples {list, Autoknit Model}
    Remarks:
        Author: Max Eschenbach
        License: MIT License
        Version: 211029
"""

# PYTHON STANDARD LIBRARY IMPORTS
from __future__ import division
from string import join

# GHPYTHON SDK IMPORTS
from ghpythonlib.componentbase import executingcomponent as component
import Grasshopper, GhPython
import System
import Rhino
import rhinoscriptsyntax as rs

# LOCAL MODULE IMPORTS
import ghautoknit as ghak

# GHENV COMPONENT SETTINGS
ghenv.Component.Name = "BuildAutoknitModel"
ghenv.Component.NickName ="BAM"
ghenv.Component.Category = "GHAutoknit"
ghenv.Component.SubCategory = "2 Autoknit Model"

class BuildAutoknitModel(component):
    
    def RunScript(self, M, C):
        # define outputs so they're never empty
        AKModel = None
        
        if not M:
            return None
        if not C:
            C = None
        
        for i, c in enumerate(C):
            if type(c) is not ghak.Constraint:
                raise ValueError("Supplied constraint {i} is not a valid " + \
                                 "AKConstraint!".format(i))
        
        # create model
        AKModel = ghak.Model(M, C)
        
        # return outputs if you have them; here I try it for you:
        return (AKModel)