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
