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

# Exemplo de como criar um @Decorator

## decorator

def extrair_valor_decorator(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        # Lógica de extração de valor aqui
        return resultado
    return wrapper

@extrair_valor_decorator
def minha_funcao():
    # Lógica da função aqui
    return algum_valor

---

# elif:


    self.largura=800

    self.altura=800

    self.altura_relativa_bola=370

    self.tela= pygame.display.set_mode((self.largura,self.altura))

    self.borda= pygame.Rect((0,0),(self.largura,self.altura))

    self.blit_xy_player1= (345,227)

    self.blit_xy_player2= (345,303)

    self.blit_xy_iniciar1= (200,205)

    self.blit_xy_iniciar2= (150,270)

    self.mesgc_blit_xy= (160,240)

    self.mesg_fj_blit_xy= (315,325)

    self.rect_botao_player1= pygame.Rect(320,227,160,53)

    self.rect_botao_player2= pygame.Rect(320,307,160,53)

    self.rect_botao_sublinhar_mod_player= pygame.Rect(345,265,0,5)

    self.rect_botao_sublinhar_mod_player2= pygame.Rect(345,345,0,5)

    self.rect_botao_voltar= pygame.Rect(40,400,85,30)

    self.blit_xy_voltar= (54,400)

    self.rect_botao_sublinhar_voltar= pygame.Rect(53,440,0,3)

    self.clink_rect= pygame.Rect(55,710,280,30)

    self.config_button.rect_resolucao_texto1 = pygame.Rect(320,277,120,40)

    self.config_button.rect_resolucao_texto2 = pygame.Rect(320,307,120,40)

    self.config_button.rect_resolucao_texto3 = pygame.Rect(320,337,120,40)

    self.config_button.list_rect_resolucao_texto = [self.config_button.rect_resolucao_texto1,

    self.config_button.rect_resolucao_texto2,

    self.config_button.rect_resolucao_texto3]

    self.blit_xy_clink= (55,710)

    self.blit_xy_mesg1_pontos= (40,600)

    self.blit_xy_mesg_bp1= (40,650)

    self.blit_xy_exibe_nivel= (40,550)

    self.blit_xy_mesg2_pontos= (40,600)

    self.blit_xy_mesg_bp2= (40,650)

    self.config_button.img_xy= (675,695)

    self.rect_botao_sublinhar_clink= pygame.Rect(55,750,0,5)

    self.config_button.rect_botao_config = pygame.Rect(674.5,694.0,53.0,53.0)

---
