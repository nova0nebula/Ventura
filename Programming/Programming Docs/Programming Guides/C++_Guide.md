# **C++ Programming Guide**

## **Introduction**
C++ is a powerful, high-performance programming language developed by Bjarne Stroustrup in the 1980s. It extends the C language with object-oriented features and generic programming, making it suitable for system/software development, game programming, and high-performance applications. This guide provides an in-depth look at C++ programming, from basic syntax to advanced topics.

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [Basic Syntax](#basic-syntax)
3. [Control Flow](#control-flow)
4. [Functions](#functions)
5. [Object-Oriented Programming](#object-oriented-programming)
6. [Templates](#templates)
7. [Standard Library](#standard-library)
8. [Memory Management](#memory-management)
9. [File I/O](#file-io)
10. [Advanced Topics](#advanced-topics)
11. [Testing](#testing)
12. [Conclusion](#conclusion)
13. [Appendix](#appendix)

## **Getting Started**
### Setting Up Your Environment
To start programming in C++, you need a C++ compiler and an Integrated Development Environment (IDE).

1. **Download and Install a C++ Compiler**: GCC (GNU Compiler Collection) or Clang are popular open-source compilers. You can install them using package managers like `apt` on Linux, `brew` on macOS, or MinGW for Windows.

2. **Choose an IDE**: Popular IDEs for C++ development include Visual Studio, CLion, and Code::Blocks. These tools offer features such as code completion, debugging, and project management.

3. **Write Your First Program**: Here’s a simple "Hello, World!" program in C++:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

Save this code in a file named `hello.cpp`, compile it using `g++ hello.cpp -o hello`, and run it with `./hello`.

## **Basic Syntax**
### Variables and Data Types
C++ supports various data types including:

- **Integer Types**: `int`, `short`, `long`, `unsigned`
- **Floating-Point Types**: `float`, `double`, `long double`
- **Character Type**: `char`
- **Boolean Type**: `bool`

```cpp
int age = 30; // Integer
float height = 5.9f; // Floating-point number
char initial = 'A'; // Character
bool isAdult = true; // Boolean

std::cout << "Age: " << age << ", Height: " << height << ", Initial: " << initial << ", Adult: " << isAdult << std::endl;
```

### Operators
C++ supports a wide range of operators:

- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `&&`, `||`, `!`

Example:

```cpp
int x = 10;
int y = 5;

std::cout << x + y << std::endl; // Output: 15
std::cout << (x > y) << std::endl; // Output: 1 (true)
```

## **Control Flow**
### Conditional Statements
C++ provides conditional statements for decision-making:

```cpp
int temperature = 25;

if (temperature > 30) {
    std::cout << "It's hot outside." << std::endl;
} else if (temperature > 20) {
    std::cout << "The weather is nice." << std::endl;
} else {
    std::cout << "It's cold outside." << std::endl;
}
```

### Loops
C++ supports several types of loops:

- **`for` Loop**: Executes a block of code a specific number of times.

```cpp
for (int i = 0; i < 5; i++) {
    std::cout << i << std::endl;
}
```

- **`while` Loop**: Repeats as long as the condition is true.

```cpp
int count = 0;
while (count < 5) {
    std::cout << count << std::endl;
    count++;
}
```

- **`do...while` Loop**: Executes the block at least once, then continues if the condition is true.

```cpp
int count = 0;
do {
    std::cout << count << std::endl;
    count++;
} while (count < 5);
```

## **Functions**
### Defining and Calling Functions
Functions help modularize code by breaking it into reusable blocks.

```cpp
#include <iostream>

void greet() {
    std::cout << "Hello, welcome to C++ programming!" << std::endl;
}

int add(int a, int b) {
    return a + b;
}

int main() {
    greet();
    int result = add(3, 4);
    std::cout << "Sum: " << result << std::endl;
    return 0;
}
```

### Function Overloading
C++ allows multiple functions with the same name but different parameters.

```cpp
int multiply(int a, int b) {
    return a * b;
}

double multiply(double a, double b) {
    return a * b;
}

int main() {
    std::cout << multiply(5, 6) << std::endl; // Calls int version
    std::cout << multiply(5.5, 6.5) << std::endl; // Calls double version
    return 0;
}
```

## **Object-Oriented Programming**
### Classes and Objects
C++ introduces object-oriented programming with classes and objects.

```cpp
#include <iostream>

class Person {
public:
    std::string name;
    int age;

    void greet() {
        std::cout << "Hello, my name is " << name << " and I am " << age << " years old." << std::endl;
    }
};

int main() {
    Person person1;
    person1.name = "Alice";
    person1.age = 30;
    person1.greet();
    return 0;
}
```

### Inheritance
Inheritance allows a class to inherit properties and methods from another class.

```cpp
class Animal {
public:
    void eat() {
        std::cout << "Eating..." << std::endl;
    }
};

class Dog : public Animal {
public:
    void bark() {
        std::cout << "Woof!" << std::endl;
    }
};

int main() {
    Dog dog;
    dog.eat(); // Inherited method
    dog.bark(); // Derived method
    return 0;
}
```

### Polymorphism
Polymorphism allows methods to do different things based on the object’s type.

```cpp
class Base {
public:
    virtual void show() {
        std::cout << "Base class show function." << std::endl;
    }
};

class Derived : public Base {
public:
    void show() override {
        std::cout << "Derived class show function." << std::endl;
    }
};

int main() {
    Base* bptr;
    Derived d;
    bptr = &d;
    bptr->show(); // Calls Derived's show()
    return 0;
}
```

### Encapsulation
Encapsulation is the bundling of data and methods that operate on the data within a class, restricting access to some of the object's components.

```cpp
class BankAccount {
private:
    double balance;

public:
    BankAccount(double initial_balance) : balance(initial_balance) {}

    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
        }
    }

    double getBalance() {
        return balance;
    }
};

int main() {
    BankAccount account(1000.0);
    account.deposit(500.0);
    account.withdraw(200.0);
    std::cout << "Balance: " << account.getBalance() << std::endl;
    return 0;
}
```

## **Templates**
### Function Templates
Function templates allow functions to operate on different data types.

```cpp
template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << max(5, 10) << std::endl; // Calls max<int>()
    std::cout << max(5.5, 10.5) << std::endl; // Calls max<double>()
    return 0;
}
```

### Class Templates
Class templates allow classes to operate on different data types.

```cpp
template <typename T>
class Box {
private:
    T content;

public:
    void setContent(T c) {
        content = c;
    }

    T getContent() {
        return content;
    }
};

int main() {
    Box<int> intBox;
    intBox.setContent(123);
    std::cout << intBox.getContent() << std::endl;

    Box<std::string> strBox;
    strBox.setContent("Hello");
    std::cout << strBox.getContent() << std::endl;

    return 0;
}
```

## **Standard Library**
### STL Containers
The Standard

 Template Library (STL) provides several useful containers:

- **Vector**: A dynamic array that can resize itself.

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    for (int number : numbers) {
        std::cout << number << " ";
    }
    std::cout << std::endl;
    return 0;
}
```

- **Map**: A sorted associative container that contains key-value pairs.

```cpp
#include <iostream>
#include <map>

int main() {
    std::map<std::string, int> ageMap;
    ageMap["Alice"] = 30;
    ageMap["Bob"] = 25;

    for (const auto& pair : ageMap) {
        std::cout << pair.first << " is " << pair.second << " years old." << std::endl;
    }

    return 0;
}
```

### File I/O
C++ provides file stream classes for file operations:

```cpp
#include <iostream>
#include <fstream>

int main() {
    // Writing to a file
    std::ofstream outFile("example.txt");
    outFile << "Hello, file!" << std::endl;
    outFile.close();

    // Reading from a file
    std::ifstream inFile("example.txt");
    std::string line;
    while (std::getline(inFile, line)) {
        std::cout << line << std::endl;
    }
    inFile.close();

    return 0;
}
```

## **Memory Management**
### Dynamic Memory Allocation
C++ provides operators `new` and `delete` for dynamic memory management:

```cpp
int* ptr = new int(10); // Allocate memory
std::cout << *ptr << std::endl;
delete ptr; // Deallocate memory

int* arr = new int[5]; // Allocate an array
for (int i = 0; i < 5; ++i) {
    arr[i] = i;
}
for (int i = 0; i < 5; ++i) {
    std::cout << arr[i] << " ";
}
delete[] arr; // Deallocate array
```

### Smart Pointers
C++11 introduced smart pointers to manage memory more safely:

- **`std::unique_ptr`**: Owns a resource exclusively.

```cpp
#include <memory>

int main() {
    std::unique_ptr<int> ptr = std::make_unique<int>(10);
    std::cout << *ptr << std::endl;
    return 0;
}
```

- **`std::shared_ptr`**: Allows multiple pointers to own a resource.

```cpp
#include <memory>

int main() {
    std::shared_ptr<int> ptr1 = std::make_shared<int>(10);
    std::shared_ptr<int> ptr2 = ptr1; // Shared ownership
    std::cout << *ptr1 << " " << *ptr2 << std::endl;
    return 0;
}
```

## **Advanced Topics**
### Exception Handling
C++ uses `try`, `catch`, and `throw` to handle exceptions:

```cpp
#include <iostream>
#include <stdexcept>

int divide(int a, int b) {
    if (b == 0) {
        throw std::invalid_argument("Division by zero");
    }
    return a / b;
}

int main() {
    try {
        int result = divide(10, 0);
        std::cout << "Result: " << result << std::endl;
    } catch (const std::exception& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    return 0;
}
```

### Multi-threading
C++11 introduced support for multi-threading:

```cpp
#include <iostream>
#include <thread>

void printHello() {
    std::cout << "Hello from thread!" << std::endl;
}

int main() {
    std::thread t(printHello);
    t.join(); // Wait for thread to finish
    return 0;
}
```

### Lambda Expressions
Lambda expressions allow you to define anonymous functions:

```cpp
#include <iostream>

int main() {
    auto add = [](int a, int b) { return a + b; };
    std::cout << add(3, 4) << std::endl; // Output: 7
    return 0;
}
```

## **Testing**
### Unit Testing
Use testing frameworks like Google Test for unit testing in C++.

Example using Google Test:

```cpp
#include <gtest/gtest.h>

int add(int a, int b) {
    return a + b;
}

TEST(AddTest, PositiveNumbers) {
    EXPECT_EQ(add(2, 3), 5);
}

TEST(AddTest, NegativeNumbers) {
    EXPECT_EQ(add(-2, -3), -5);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```

## **Conclusion**
C++ is a versatile language that combines high-performance capabilities with object-oriented and generic programming features. Understanding its fundamentals and advanced topics will help you develop robust applications and systems. This guide provides a comprehensive overview of C++ programming, covering syntax, key concepts, and best practices.

## **Appendix**
### Glossary
- **Class**: A user-defined type that encapsulates data and functions.
- **Object**: An instance of a class.
- **Template**: A feature that allows functions and classes to operate with generic types.
- **Smart Pointer**: A class that manages the lifetime of dynamically allocated objects.

### Additional Resources
- [The C++ Programming Language by Bjarne Stroustrup](https://www.amazon.com/C-Programming-Language-4th/dp/0321563840)
- [cplusplus.com](http://www.cplusplus.com/)
- [LearnCpp.com](https://www.learncpp.com/)