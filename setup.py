import sys
import cx_Freeze
executables = [cx_Freeze.Executable("play.py")]

cx_Freeze.setup(
    name = "ultraman rumble",
    description = "space quest with ultraman great",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["ultra.png","e1.png","e2.png","e3.png","img/","great.wav"]}},
    executables = executables
    )
