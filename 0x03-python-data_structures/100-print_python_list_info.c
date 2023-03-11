#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - function
 * 
 **/
void print_python_list_info(PyObject *p)
{
    Py_ssize_t i, size;
    PyListObject *list;

    if (PyList_Check(p))
    {
        list = (PyListObject *)p;
        size = PyList_Size(p);

        printf("[*] Size of the Python List = %ld\n", size);
        printf("[*] Allocated = %ld\n", list->allocated);

        for (i = 0; i < size; i++)
        {
            printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
        }
    }
}

int main(void)
{
	print_python_list_info();
	return 0;
}