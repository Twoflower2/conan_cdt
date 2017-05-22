# Conan.io "Hello World" work-flow example of using Eclipse CDT
Conan example of Eclipse CDT projects by running headless Eclipse from the Conan build() method by creating a static library and then using that library in an application.


## Library Layout in project root directory: hello_lib
```
hello_lib
├───bin
├───inc
├───src
├───workspace
│   └───hello_statlib
```
* *conanfile.py* in root directory **hello_lib**
* *hello_statlib.a* static library artefact will be build by Eclipse in **bin**.
* *hello.h* is in **inc**
* *hello.cpp* is in **src**
* The Eclipse project files are under directory **workspace/hello_statlib**.



## Application Layout in project root directory: hello_appl
```
hello_appl
├───bin
├───inc
├───lib
├───src
├───workspace
│   └───hello
```
* *conanfile.py* in root directory **hello**
* *hello.exe* will be build  by Eclipse in **bin**
* *hello.h* to be place by conan in **inc**
* *hello_statlib.a* static library artefact to be place by Conan in **lib**.
* *main.cpp* is in **src**
* The Eclipse project files are under directory **workspace/hello**.

## Work-flow on high-level per project
### hello_lib
* Project hello_statlib runs in the *build()* method as headless Eclipse and create *hello_statlib.a* in the **bin** directory.
* Conan have to package the lib *hello_statlib.a*, header *hello.h* and Eclipse project file from the **bin**, **inc** and **workspace/hello_statlib***directories to remote store.

### hello_appl
* Conan have to place the lib *hello_statlib.a* and header *hello.h* in the **lib** and **inc** directories from the remote store.
* Project hello runs in the *build()* method as headless Eclipse and create the appl. *hello.exe* in the **bin** directory.
* Conan have to package the *hello.exe* and Eclipse project file to remote store.


## Work-flow in detail
TODO