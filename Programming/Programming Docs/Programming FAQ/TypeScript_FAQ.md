# **TypeScript FAQ**

## **Table of Contents**
1. [General Questions](#general-questions)
2. [TypeScript Basics](#typescript-basics)
3. [Types and Interfaces](#types-and-interfaces)
4. [Functions](#functions)
5. [Classes and Objects](#classes-and-objects)
6. [Modules and Namespaces](#modules-and-namespaces)
7. [Generics](#generics)
8. [Error Handling](#error-handling)
9. [TypeScript Configuration](#typescript-configuration)
10. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
11. [Resources](#resources)

## **General Questions**

### **1. What is TypeScript?**
TypeScript is a statically typed superset of JavaScript developed by Microsoft. It adds optional type annotations to JavaScript, enabling developers to catch errors during development and improve code quality and maintainability.

### **2. What are the main features of TypeScript?**
- **Static Typing**: TypeScript allows you to define variable types, which helps in catching type-related errors during development.
- **Type Inference**: TypeScript can infer types based on the assigned values and expressions.
- **Classes and Interfaces**: TypeScript supports object-oriented programming with classes and interfaces.
- **TypeScript Compiler**: Converts TypeScript code into JavaScript, ensuring compatibility with JavaScript engines.

### **3. How does TypeScript improve JavaScript development?**
TypeScript enhances JavaScript development by providing:
- **Early Error Detection**: Type errors are detected at compile time rather than runtime.
- **Enhanced IDE Support**: TypeScript integrates well with IDEs for features like autocompletion and type checking.
- **Better Code Documentation**: Type annotations provide self-documenting code.

## **TypeScript Basics**

### **1. How do I declare a variable in TypeScript?**

Variables in TypeScript are declared similarly to JavaScript but with type annotations.

- **Example**:
  ```typescript
  let name: string = "Alice";
  let age: number = 25;
  ```

### **2. How do I define a constant in TypeScript?**

Use the `const` keyword for constants. Type annotations can also be applied.

- **Example**:
  ```typescript
  const pi: number = 3.14;
  ```

### **3. How do I create a TypeScript file?**

TypeScript files use the `.ts` extension. Compile these files into JavaScript using the TypeScript compiler (`tsc`).

- **Example**:
  ```bash
  tsc script.ts
  ```

## **Types and Interfaces**

### **1. What are types in TypeScript?**

Types in TypeScript specify the kind of value a variable can hold. They help in enforcing type safety.

- **Basic Types**: `string`, `number`, `boolean`, `array`, `tuple`, `enum`, `any`, `void`, `null`, `undefined`.

- **Example**:
  ```typescript
  let isDone: boolean = false;
  let scores: number[] = [100, 90, 80];
  ```

### **2. What are interfaces in TypeScript?**

Interfaces define the structure of objects, including properties and methods.

- **Example**:
  ```typescript
  interface Person {
      name: string;
      age: number;
      greet(): void;
  }

  const john: Person = {
      name: "John",
      age: 30,
      greet() {
          console.log(`Hello, my name is ${this.name}`);
      }
  };
  ```

### **3. How do I use type aliases in TypeScript?**

Type aliases provide a way to name complex types.

- **Example**:
  ```typescript
  type ID = string | number;

  let userId: ID = "abc123";
  ```

## **Functions**

### **1. How do I declare a function in TypeScript?**

Functions are declared with optional type annotations for parameters and return types.

- **Example**:
  ```typescript
  function add(a: number, b: number): number {
      return a + b;
  }
  ```

### **2. What are function overloads in TypeScript?**

Function overloads allow you to define multiple signatures for a function.

- **Example**:
  ```typescript
  function greet(person: string): string;
  function greet(person: string, age: number): string;
  function greet(person: string, age?: number): string {
      if (age !== undefined) {
          return `Hello, ${person}. You are ${age} years old.`;
      } else {
          return `Hello, ${person}.`;
      }
  }
  ```

## **Classes and Objects**

### **1. How do I define a class in TypeScript?**

Classes in TypeScript can include properties, constructors, and methods with type annotations.

- **Example**:
  ```typescript
  class Car {
      make: string;
      model: string;
      year: number;

      constructor(make: string, model: string, year: number) {
          this.make = make;
          this.model = model;
          this.year = year;
      }

      getCarInfo(): string {
          return `${this.make} ${this.model} (${this.year})`;
      }
  }
  ```

### **2. How do I use inheritance in TypeScript?**

TypeScript supports inheritance using the `extends` keyword.

- **Example**:
  ```typescript
  class ElectricCar extends Car {
      batteryLife: number;

      constructor(make: string, model: string, year: number, batteryLife: number) {
          super(make, model, year);
          this.batteryLife = batteryLife;
      }

      getCarInfo(): string {
          return `${super.getCarInfo()} with a battery life of ${this.batteryLife} hours.`;
      }
  }
  ```

## **Modules and Namespaces**

### **1. What are modules in TypeScript?**

Modules are files that can export and import code. They help in organizing and encapsulating code.

- **Exporting**:
  ```typescript
  // math.ts
  export function add(a: number, b: number): number {
      return a + b;
  }
  ```

- **Importing**:
  ```typescript
  // app.ts
  import { add } from './math';

  console.log(add(2, 3));
  ```

### **2. What are namespaces in TypeScript?**

Namespaces provide a way to group related code into a single unit.

- **Example**:
  ```typescript
  namespace Utilities {
      export function log(message: string): void {
          console.log(message);
      }
  }

  Utilities.log("Hello, World!");
  ```

## **Generics**

### **1. What are generics in TypeScript?**

Generics allow you to write flexible, reusable functions and classes that can work with different types.

- **Example**:
  ```typescript
  function identity<T>(arg: T): T {
      return arg;
  }

  let result = identity<string>("Hello, Generics");
  ```

### **2. How do I use generic classes in TypeScript?**

Generic classes can handle multiple types and provide type safety.

- **Example**:
  ```typescript
  class Box<T> {
      value: T;

      constructor(value: T) {
          this.value = value;
      }

      getValue(): T {
          return this.value;
      }
  }

  let box = new Box<number>(123);
  ```

## **Error Handling**

### **1. How do I handle errors in TypeScript?**

Error handling in TypeScript is done similarly to JavaScript, using `try-catch` blocks.

- **Example**:
  ```typescript
  try {
      throw new Error("Something went wrong");
  } catch (error) {
      if (error instanceof Error) {
          console.error(error.message);
      }
  }
  ```

## **TypeScript Configuration**

### **1. What is `tsconfig.json`?**

`tsconfig.json` is a configuration file that specifies the root files and compiler options required to compile a TypeScript project.

- **Example**:
  ```json
  {
      "compilerOptions": {
          "target": "es6",
          "module": "commonjs",
          "strict": true
      },
      "include": ["src/**/*"],
      "exclude": ["node_modules"]
  }
  ```

### **2. How do I compile a TypeScript project?**

Use the TypeScript compiler (`tsc`) to compile TypeScript files into JavaScript. The `tsconfig.json` file can be used to configure the compilation process.

- **Compile Command**:
  ```bash
  tsc
  ```

## **Common Issues and Troubleshooting**

### **1. Why is my TypeScript code not compiling?**

- **Syntax Errors**: Check for syntax errors or typos in your TypeScript code.
- **Type Errors**: Ensure that types match and are correctly used.
- **Configuration Issues**: Verify the `tsconfig.json` settings and paths.

### **2. How do I resolve runtime errors in TypeScript?**

- **Check Type Annotations**: Ensure that types are used correctly.
- **Debug with Source Maps**: Use source maps to debug TypeScript code in your browser or IDE.

## **Resources**

- [TypeScript Official Documentation](https://www.typescriptlang.org/docs/)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [TypeScript GitHub Repository](https://github.com/Microsoft/TypeScript)
- [TypeScript Deep Dive by Basarat Ali Syed](https://basarat.gitbook.io/typescript/)