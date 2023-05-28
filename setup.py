import sys
from cx_Freeze import setup, Executable

# Informe o caminho para o seu arquivo principal do jogo
main_script = 'Block-Bricks.py'

# Informe o nome da pasta que contém os sons
sounds_folder = 'sounds'

# Configurações do executável
executables = [Executable(main_script)]

# Opções de configuração
options = {
    'build_exe': {
        'include_files': [sounds_folder],
        'packages': [],
        'excludes': []
    }
}

# Criação do executável
setup(
    name='Block-Bricks',
    version='1.0',
    description='Muito top!',
    options=options,
    executables=executables
)
