#include "hello.h"
#include <iostream>

void hello(){
#ifndef NDEBUG
	std::cout << "\nHello World Release!\n";
#else
	std::cout << "\nHello World Debug!\n";
#endif
}
