# **TypeScript Programming Guide**

## **Introduction**
TypeScript is a statically typed superset of JavaScript developed by Microsoft. It adds optional static typing to JavaScript, which can help catch errors early during development and improve code quality. TypeScript compiles to plain JavaScript, ensuring compatibility with existing JavaScript environments.

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [TypeScript Basics](#typescript-basics)
3. [Type Annotations](#type-annotations)
4. [Interfaces](#interfaces)
5. [Classes](#classes)
6. [Functions](#functions)
7. [Generics](#generics)
8. [Modules](#modules)
9. [Advanced Types](#advanced-types)
10. [Configuration](#configuration)
11. [Conclusion](#conclusion)
12. [Appendix](#appendix)

## **Getting Started**
### Setting Up Your Environment
1. **Installing TypeScript**: Install TypeScript globally using npm:

   ```bash
   npm install -g typescript
   ```

2. **Creating a TypeScript File**: Create a file with a `.ts` extension.

   **TypeScript File (`hello.ts`):**
   ```typescript
   let message: string = "Hello, TypeScript!";
   console.log(message);
   ```

3. **Compiling TypeScript**: Compile TypeScript to JavaScript using the `tsc` command:

   ```bash
   tsc hello.ts
   ```

   This will generate a `hello.js` file with the compiled JavaScript code.

## **TypeScript Basics**
### What is TypeScript?
TypeScript is a superset of JavaScript that introduces static typing and modern features. It compiles to standard JavaScript, which can run on any browser or JavaScript engine.

### Why Use TypeScript?
- **Static Typing**: Helps detect type errors at compile time.
- **Improved Tooling**: Enhanced editor support with features like autocompletion and refactoring.
- **Modern Features**: Supports ES6+ features and additional syntax for better coding practices.

## **Type Annotations**
### Basic Types
TypeScript supports various basic types:

- **`string`**: Represents text.

  ```typescript
  let name: string = "Alice";
  ```

- **`number`**: Represents numbers (integers and floats).

  ```typescript
  let age: number = 30;
  ```

- **`boolean`**: Represents true or false values.

  ```typescript
  let isStudent: boolean = true;
  ```

- **`any`**: Represents any type, allowing for flexibility but reducing type safety.

  ```typescript
  let data: any = "Hello";
  data = 123;
  ```

### Arrays and Tuples
- **Arrays**:

  ```typescript
  let numbers: number[] = [1, 2, 3];
  ```

- **Tuples**: Fixed-length arrays with specified types for each element.

  ```typescript
  let person: [string, number] = ["Alice", 30];
  ```

## **Interfaces**
### Defining Interfaces
Interfaces define the shape of objects, ensuring they adhere to a specific structure:

```typescript
interface Person {
    name: string;
    age: number;
}

let person: Person = {
    name: "Alice",
    age: 30
};
```

### Optional and Readonly Properties
- **Optional Properties**:

  ```typescript
  interface Person {
      name: string;
      age?: number; // Optional
  }
  ```

- **Readonly Properties**:

  ```typescript
  interface Person {
      readonly id: number;
  }
  ```

## **Classes**
### Defining Classes
TypeScript supports classes with constructors, properties, and methods:

```typescript
class Person {
    name: string;
    age: number;

    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }

    greet(): void {
        console.log(`Hello, my name is ${this.name}`);
    }
}

let person = new Person("Alice", 30);
person.greet();
```

### Inheritance
Classes can extend other classes, inheriting their properties and methods:

```typescript
class Employee extends Person {
    jobTitle: string;

    constructor(name: string, age: number, jobTitle: string) {
        super(name, age);
        this.jobTitle = jobTitle;
    }

    getJob(): void {
        console.log(`${this.name} is a ${this.jobTitle}`);
    }
}

let employee = new Employee("Alice", 30, "Engineer");
employee.getJob();
```

## **Functions**
### Function Types
TypeScript allows you to specify the types of function parameters and return values:

```typescript
function add(a: number, b: number): number {
    return a + b;
}

let result: number = add(5, 10);
```

### Optional and Default Parameters
- **Optional Parameters**: Parameters that are not required.

  ```typescript
  function greet(name: string, age?: number): void {
      if (age) {
          console.log(`Hello, ${name}. You are ${age} years old.`);
      } else {
          console.log(`Hello, ${name}.`);
      }
  }
  ```

- **Default Parameters**: Parameters with default values.

  ```typescript
  function greet(name: string, age: number = 30): void {
      console.log(`Hello, ${name}. You are ${age} years old.`);
  }
  ```

## **Generics**
### Using Generics
Generics allow you to create reusable components that work with various data types:

```typescript
function identity<T>(value: T): T {
    return value;
}

let result = identity<number>(42);
let result2 = identity<string>("Hello");
```

### Generic Classes
Generics can be used with classes to handle multiple types:

```typescript
class Box<T> {
    content: T;

    constructor(content: T) {
        this.content = content;
    }

    getContent(): T {
        return this.content;
    }
}

let numberBox = new Box<number>(123);
let stringBox = new Box<string>("Hello");
```

## **Modules**
### Importing and Exporting
TypeScript uses modules to organize code. Modules can export and import code between files:

- **Exporting**:

  ```typescript
  export class Person {
      // Class definition
  }
  ```

- **Importing**:

  ```typescript
  import { Person } from "./person";
  ```

### Default Exports
Modules can also export a single value or class as the default export:

- **Default Export**:

  ```typescript
  export default class Person {
      // Class definition
  }
  ```

- **Default Import**:

  ```typescript
  import Person from "./person";
  ```

## **Advanced Types**
### Intersection Types
Combine multiple types into one:

```typescript
type Employee = Person & {
    jobTitle: string;
};
```

### Union Types
Allow a variable to be one of several types:

```typescript
function printId(id: number | string): void {
    console.log(`ID: ${id}`);
}
```

### Type Guards
Use type guards to narrow down types:

```typescript
function isString(value: any): value is string {
    return typeof value === "string";
}
```

## **Configuration**
### `tsconfig.json`
The `tsconfig.json` file configures TypeScript compilation options:

```json
{
    "compilerOptions": {
        "target": "es6",
        "module": "commonjs",
        "strict": true,
        "outDir": "./dist"
    },
    "include": ["src/**/*.ts"]
}
```

### Common Compiler Options
- **`target`**: Specifies the ECMAScript version to compile to.
- **`module`**: Defines the module system to use.
- **`strict`**: Enables all strict type-checking options.
- **`outDir`**: Directory to output compiled JavaScript files.

## **Conclusion**
TypeScript enhances JavaScript by adding static typing and modern features, making code more robust and maintainable. By understanding and using TypeScript effectively, developers can improve code quality, catch errors early, and take advantage of advanced language features.

## **Appendix**
### Glossary
- **Type Annotation**: A way to specify the type of a variable or function.
- **Interface**: Defines a structure for objects and classes.
- **Generics**: A feature that allows creating components that work with various data types.
- **Module**: A file or a group of files that export and import code.

### Additional Resources
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [TypeScript GitHub Repository](https://github.com/microsoft/TypeScript)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/)