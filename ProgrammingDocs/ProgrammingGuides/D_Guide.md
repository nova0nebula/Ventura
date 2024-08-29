# **D Programming Guide**

## **Introduction**
D is a high-level, multi-paradigm programming language known for its efficiency, performance, and expressive syntax. Developed by Walter Bright and first released in 2001, D combines the best features of modern programming languages with the power of low-level systems programming. It is designed to be a practical language for both system and application programming.

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [D Basics](#d-basics)
3. [Variables and Data Types](#variables-and-data-types)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Classes and Structs](#classes-and-structs)
7. [Templates](#templates)
8. [Memory Management](#memory-management)
9. [Concurrency](#concurrency)
10. [File I/O](#file-io)
11. [Modules and Packages](#modules-and-packages)
12. [Best Practices](#best-practices)
13. [Conclusion](#conclusion)
14. [Appendix](#appendix)

## **Getting Started**
### Setting Up Your Environment
1. **Installing D**: Download and install the D compiler (DMD) from the [D Programming Language website](https://dlang.org/download.html). Alternatively, you can use the [LDC](https://github.com/ldc-developers/ldc) or [GDC](https://gcc.gnu.org/wiki/GDC) compilers.

   **Installing DMD**:

   - For Windows, macOS, and Linux, follow the installation instructions provided on the D website or use a package manager like `brew` for macOS or `apt` for Ubuntu.

2. **Creating a D File**: Create a file with a `.d` extension.

   **D File (`hello.d`):**
   ```d
   import std.stdio;

   void main() {
       writeln("Hello, D!");
   }
   ```

3. **Compiling D Code**: Compile the D file using the `dmd` command:

   ```bash
   dmd hello.d
   ```

   Run the executable:

   ```bash
   ./hello
   ```

## **D Basics**
### Structure of a D Program
A basic D program consists of a `main` function, which is the entry point:

```d
import std.stdio;

void main() {
    writeln("Hello, D!");
}
```

### Comments
Comments in D start with `//` for single-line comments or `/* ... */` for multi-line comments:

```d
// This is a single-line comment

/* This is a
   multi-line comment */
```

## **Variables and Data Types**
### Declaring Variables
D supports both type inference and explicit type declaration:

- **Type Inference**:

  ```d
  auto age = 30; // D infers the type as int
  ```

- **Explicit Type Declaration**:

  ```d
  int age = 30;
  ```

### Data Types
D includes several basic data types:

- **`int`**: Represents integer values.

  ```d
  int age = 30;
  ```

- **`float`**: Represents single-precision floating-point numbers.

  ```d
  float temperature = 23.5;
  ```

- **`double`**: Represents double-precision floating-point numbers.

  ```d
  double pi = 3.14159265358979;
  ```

- **`string`**: Represents text.

  ```d
  string name = "Alice";
  ```

- **`bool`**: Represents boolean values.

  ```d
  bool isStudent = true;
  ```

## **Control Flow**
### Conditional Statements
D uses `if`, `else if`, and `else` for conditional logic:

```d
import std.stdio;

void main() {
    int number = 10;

    if (number > 0) {
        writeln("The number is positive.");
    } else if (number < 0) {
        writeln("The number is negative.");
    } else {
        writeln("The number is zero.");
    }
}
```

### Loops
D supports several looping constructs:

- **`for` Loop**:

  ```d
  import std.stdio;

  void main() {
      for (int i = 0; i < 5; i++) {
          writeln("Iteration ", i);
      }
  }
  ```

- **`while` Loop**:

  ```d
  import std.stdio;

  void main() {
      int count = 0;

      while (count < 5) {
          writeln("Count ", count);
          count++;
      }
  }
  ```

- **`do-while` Loop**:

  ```d
  import std.stdio;

  void main() {
      int count = 0;

      do {
          writeln("Count ", count);
          count++;
      } while (count < 5);
  }
  ```

## **Functions**
### Declaring Functions
D functions can have optional parameters and default values:

- **Basic Function**:

  ```d
  int add(int a, int b) {
      return a + b;
  }
  ```

- **Function with Optional Parameters**:

  ```d
  void greet(string name, int age = 30) {
      writeln("Hello, ", name, ". You are ", age, " years old.");
  }
  ```

## **Classes and Structs**
### Defining Classes
D supports object-oriented programming with classes:

```d
import std.stdio;

class Person {
    string name;
    int age;

    this(string name, int age) {
        this.name = name;
        this.age = age;
    }

    void greet() {
        writeln("Hello, my name is ", name, ".");
    }
}

void main() {
    Person person = new Person("Alice", 30);
    person.greet();
}
```

### Structs
Structs are value types and can be used for lightweight data structures:

```d
import std.stdio;

struct Point {
    int x;
    int y;

    void print() {
        writeln("Point(", x, ", ", y, ")");
    }
}

void main() {
    Point p = Point(10, 20);
    p.print();
}
```

## **Templates**
### Using Templates
Templates allow for generic programming:

- **Function Template**:

  ```d
  T max(T)(T a, T b) {
      return a > b ? a : b;
  }

  void main() {
      writeln(max(10, 20)); // Outputs: 20
      writeln(max(3.14, 2.71)); // Outputs: 3.14
  }
  ```

- **Class Template**:

  ```d
  class Stack(T) {
      private T[] elements;

      void push(T element) {
          elements ~= element;
      }

      T pop() {
          if (elements.length == 0) throw new Exception("Stack is empty");
          return elements.removeLast();
      }
  }

  void main() {
      Stack!int s = new Stack!int();
      s.push(1);
      s.push(2);
      writeln(s.pop()); // Outputs: 2
  }
  ```

## **Memory Management**
### Automatic Memory Management
D provides garbage collection for automatic memory management. You can also use manual memory management with pointers:

- **Automatic**:

  ```d
  void main() {
      string name = "Alice"; // Managed by garbage collector
  }
  ```

- **Manual**:

  ```d
  import std.stdio;

  void main() {
      int* ptr = new int(10);
      writeln(*ptr);
      delete ptr;
  }
  ```

## **Concurrency**
### Using Threads
D supports multi-threading via the `std.thread` module:

```d
import std.stdio;
import std.thread;

void printHello() {
    writeln("Hello from thread!");
}

void main() {
    Thread t = new Thread(&printHello);
    t.start();
    t.join(); // Wait for thread to finish
}
```

### Asynchronous Programming
D provides support for asynchronous programming with `async`/`await`:

```d
import std.stdio;
import std.concurrency;
import std.parallelism;

async void printAsync() {
    writeln("Hello from async!");
}

void main() {
    printAsync();
    writeln("Hello from main!");
}
```

## **File I/O**
### Reading and Writing Files
D supports file operations using the `std.file` and `std.stdio` modules:

- **Writing to a File**:

  ```d
  import std.file;
  import std.stdio;

  void main() {
      File file = File("output.txt", "w");
      file.writeln("Hello, D!");
      file.close();
  }
  ```

- **Reading from a File**:

  ```d
  import std.file;
  import std.stdio;

  void main() {
      File file = File("output.txt", "r");
      string content = file.readText();
      writeln(content);
      file.close();
  }
  ```

## **Modules and Packages**
### Creating Modules
D uses modules to organize code:

- **Module Definition (`my_module.d`)**:

  ```d
  module my_module;

  void greet() {
      writeln("Hello from my_module!");


  }
  ```

- **Importing Modules**:

  ```d
  import std.stdio;
  import my_module;

  void main() {
      greet();
  }
  ```

### Using Packages
Packages are managed using `dub`, D's package manager:

- **Creating a New Package**:

  ```bash
  dub init my_package
  ```

- **Adding Dependencies**:

  Edit `dub.json` or `dub.sdl` to include package dependencies:

  ```json
  {
    "dependencies": {
      "vibe-d": "~>0.8.0"
    }
  }
  ```

- **Building and Running**:

  ```bash
  dub build
  dub run
  ```

## **Best Practices**
1. **Code Readability**: Write clear and readable code. Use descriptive variable names and consistent indentation.

2. **Error Handling**: Handle errors gracefully using exceptions and validation.

3. **Performance**: Optimize performance by using efficient algorithms and minimizing memory allocations.

4. **Documentation**: Document your code and use comments to explain complex logic.

5. **Testing**: Write unit tests to ensure code correctness and reliability.

## **Conclusion**
D is a powerful and flexible language that provides the efficiency of low-level programming with the convenience of modern high-level features. Its support for object-oriented, functional, and concurrent programming makes it a versatile choice for a wide range of applications.

## **Appendix**
### Glossary
- **Garbage Collection**: Automatic memory management that reclaims unused memory.
- **Templates**: A feature that allows writing generic and reusable code.
- **Dub**: A package manager for the D programming language.

### Additional Resources
- [D Programming Language Official Site](https://dlang.org/)
- [D Documentation](https://dlang.org/phobos/)
- [D Wiki](https://wiki.dlang.org/Main_Page)