import sys
from cx_Freeze import setup, Executable

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("jogo.py", base=base)]

# Dependencies are automatically detected, but it might need fine tuning.
options = {
    "build_exe": {
        "includes": ["os"],  # Lista de módulos a serem incluídos
        "packages": ["tkinter"],  # Lista de pacotes a serem incluídos
    }
}

setup(
    name="Nome do Programa",
    version="0.1",
    description="Esse é meu programa",
    options=options,
    executables=executables
)