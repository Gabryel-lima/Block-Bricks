# Caso usar o Cx-freeze

pip install cx-freeze

from cx_Freeze importsetup, Executable

# Nome do arquivo ''setup.py''

# No terminal ''python setup.py build''

# Informe o caminho para o seu arquivo principal do jogo

main_script='Block-Bricks.py'

# Informe o nome da pasta que contém os sons

sounds_folder='sounds'

# Configurações do executável

executables= [Executable(main_script)]

# Opções de configuração

options= {

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

# Usando auto-py-to-exe

pip install auto-py-to-exe

#No terminal ''auto-py-to-exe'

---

# Crie um arquivo `setup.py` para compilar a extensão Cython:

## setup.py

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("nome_do_arquivo.pyx"),
)

---

**o git pull puxa, traz as alterações de um repositório remoto para o local.**  **Já push é empurrar, então o git push empurra, leva as alterações do repositório local para o remoto** .

---

---
