from cx_Freeze import setup, Executable

executables = [Executable("Block-Bricks.py")]

setup(
    name="Block-Bricks",
    version="1.0",
    description="Jogo",
    executables=executables
)

