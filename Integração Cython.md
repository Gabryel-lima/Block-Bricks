# Código gerado a partir do Setuptools

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

typedef struct habilidade_players {
    float bola_rect[4]; // Exemplo: supondo que "bola_rect" seja um inteiro

} skill_data;

void init_py()
{
    Py_Initialize();

    // Importar o módulo contendo o objeto
    PyObject *pModule = PyImport_ImportModule("bola");

    // Obter uma referência ao objeto que possui o atributo "bola_rect"
    PyObject *pObj = PyObject_GetAttrString(pModule, "bola_rect");

    // Converter os elementos da lista Python para floats
    for (int i = 0; i < 4; ++i) {
        PyObject *pItem = PyList_GetItem(pObj, i);
        if (PyFloat_Check(pItem)) {
            skill_data habilidade;
            habilidade.bola_rect[i] = (float)PyFloat_AsDouble(pItem);
            printf(habilidade.bola_rect);
        }
        else {
            PyErr_Print(); // Imprimir erros, se houver
                           // Lidar com erro de tipo, se necessário
        }
    }
    // Liberar referência ao objeto que possui o atributo
    Py_XDECREF(pObj);
}

    // Finalizar o interpretador Python
    Py_Finalize();

int main() {
    init_py();
    return 0;
}

---

# Arquivo setup.py

from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([Extension("nome_do_modulo_recompilado.c", ["./src/nome_do_arquivo.pyx"])])
)

---

# Cv2

#self.cap = cv2.VideoCapture('assets/videos/vfundo.mp4')

def run(self):

#depois do loop


    # ret, frame = self.cap.read()

    # if not ret:

    #     self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    #     continue

    # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # frame_pygame = pygame.image.fromstring(frame_rgb.tobytes(), frame_rgb.shape[:2], 'RGB')

    # self.tela.blit(frame_pygame, (0,0))

---
