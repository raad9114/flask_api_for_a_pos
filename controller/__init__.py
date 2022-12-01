# __all__=["user_controller"] 
#__all__ is a variable
import os
import glob

__all__ = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
#python loop
# os.path.basename(f)[:-3]= main file er last 3 ta word dhorse
# glob.glob(os.path.dirname(__file__) + "/*.py" ekhane sob file gula ke dhorse
# oita # __all__=["user_controller","user_controller_copy"]  evabeo lekha jeto
