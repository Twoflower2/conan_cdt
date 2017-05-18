# conan.io "Hello World" example of using Eclipse CDT
Conan example of Eclipse CDT projects by running headless Eclipse from the Conan build() method


# Layout
* The Eclipse project files are under directory workspace called hello_statlib and hello.
* Source code and initial conanfile.py files files resides in  directories hello_statlib and hello.
* The reason so many directories were created was to see this lay-out in the conanfile.py clearly

# Procedure
* hello_statlib runs in the build() method as headless Eclipse and create the lib (.a) file in the bin directory.
* Before hello runs Conan have to place the lib (hello_statlib.a) and header (hello.h) in the hello lib and inc directories.
* hello runs in the build() method as headless Eclipse and create the appl. (hello.exe) file in the bin directory.
