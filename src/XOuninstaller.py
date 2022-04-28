import os
import sys
import glob

files = glob.glob('./src/**/*', recursive=True)

for f in files:
    try:
        os.remove(f)
    except OSError as e:
        print("Error: %s : %s" % (f, e.strerror))

try:
    os.rmdir("src")
except:
    print("")


if getattr(sys, 'frozen', False):
    path = os.path.realpath(sys.executable)
elif __file__:
  path = os.path.realpath(__file__)

os.remove(path)