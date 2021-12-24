import sys
sys.path.insert(1,'.')
print ("Starting app. Please wait...")
try:
    from dist import pydist as pd
    sys.path.insert(1,pd.__PyDist__._WorkDir)
except:
    pass