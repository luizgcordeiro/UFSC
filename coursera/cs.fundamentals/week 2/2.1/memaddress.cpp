#include <iostream>

void foo() {
    int x=10;
    int y=11;
    int z=12;
    std::cout << "Memory address of x: " << &x << std::endl;
    std::cout << "Memory address of y: " << &y << std::endl;
    std::cout << "Memory address of z: " << &z << std::endl;
    return;
}

int main() {
    int p=1;
    std::cout << "Memory address of p: " << &p << std::endl;
    foo();
    int q=1;
    std::cout << "Memory address of q: " << &q << std::endl;
    return 0;
    //comment
}