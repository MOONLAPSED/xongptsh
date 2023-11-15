#include <Python.h>

void handle_python_exception() {
    if (PyErr_Occurred()) {
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        char *error_message = PyUnicode_AsUTF8(value);
        fprintf(stderr, "Python error: %s\n", error_message);
        Py_DECREF(type);
        Py_DECREF(value);
        Py_XDECREF(traceback);
    }
}

void run_python_script() {
    int result = PyRun_SimpleString(
        "import setup\n"
        "try:\n"
        "    setup.run_setup()\n"
        "except setup.RateLimitExceededError:\n"
        "    raise RuntimeError('Rate limit exceeded for setup job')\n"
    );
    if (result == -1) {
        handle_python_exception();
    }
}

int main() {
    Py_Initialize();
    run_python_script();
    Py_Finalize();
    return 0;
}
