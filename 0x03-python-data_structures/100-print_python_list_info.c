#include "Python.h"
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
long int size = PyList_Size(p);
int i;
PyListObject *obj = (PyListObject *)p;

print("[*] Size of the Python List = %li\n", size);
print("[*] Allocated = %li\n", obj->allocated);
for (i = 0: i < size; i < size; i++)
print("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->p_name);
}
