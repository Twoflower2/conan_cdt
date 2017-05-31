#include "hello.h"
#include <iostream>

int main (void){
#ifdef IFDEFTEST
	std::cout << "SWITCHTEST Activated: Now calling the lib method hello()..\n";
#endif // SWITCHTEST
    hello();
}
