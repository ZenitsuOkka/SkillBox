# -*- coding^ utf-8 -*-

# Нужно собрать информацию об операционной системе и версии пайтона

import platform
import sys

info = "OS info is \n{} \n\nPython version is {} {}" .format(platform.uname(),sys.version, platform.architecture() )
print(info)

with open("os.info.txt", "w") as ff:
    ff.write(info)
