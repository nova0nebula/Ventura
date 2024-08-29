# **C# Programming Guide**

## **Introduction**
C# (pronounced "C-sharp") is a modern, object-oriented programming language developed by Microsoft as part of the .NET framework. It combines the high performance of C++ with the ease of use of Visual Basic. C# is commonly used for developing Windows applications, web services, and games using Unity. This guide covers the essentials of C# programming, from basic syntax to advanced features.

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [Basic Syntax](#basic-syntax)
3. [Control Flow](#control-flow)
4. [Methods](#methods)
5. [Object-Oriented Programming](#object-oriented-programming)
6. [LINQ](#linq)
7. [Asynchronous Programming](#asynchronous-programming)
8. [Exception Handling](#exception-handling)
9. [File I/O](#file-io)
10. [Advanced Topics](#advanced-topics)
11. [Testing](#testing)
12. [Conclusion](#conclusion)
13. [Appendix](#appendix)

## **Getting Started**
### Setting Up Your Environment
To begin programming in C#, you'll need the .NET SDK and an Integrated Development Environment (IDE).

1. **Download and Install .NET SDK**: You can download the .NET SDK from the [official .NET website](https://dotnet.microsoft.com/download). This includes the .NET runtime and command-line tools.

2. **Choose an IDE**: Visual Studio is the most popular IDE for C# development, providing features such as code completion, debugging, and project management. Visual Studio Code with the C# extension is another option.

3. **Write Your First Program**: Here’s a simple "Hello, World!" program in C#:

```csharp
using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Hello, World!");
    }
}
```

Save this code in a file named `Program.cs`, compile it using `dotnet run`, and run it with the same command.

## **Basic Syntax**
### Variables and Data Types
C# supports several data types:

- **Integer Types**: `int`, `short`, `long`, `byte`
- **Floating-Point Types**: `float`, `double`, `decimal`
- **Character Type**: `char`
- **Boolean Type**: `bool`
- **String**: `string`

```csharp
int age = 30; // Integer
float height = 5.9f; // Floating-point number
char initial = 'A'; // Character
bool isAdult = true; // Boolean
string name = "Alice"; // String

Console.WriteLine($"Name: {name}, Age: {age}, Height: {height}, Initial: {initial}, Adult: {isAdult}");
```

### Operators
C# supports various operators:

- **Arithmetic Operators**: `+`, `-`, `*`, `/`, `%`
- **Comparison Operators**: `==`, `!=`, `>`, `<`, `>=`, `<=`
- **Logical Operators**: `&&`, `||`, `!`

Example:

```csharp
int x = 10;
int y = 5;

Console.WriteLine(x + y); // Output: 15
Console.WriteLine(x > y); // Output: True
```

## **Control Flow**
### Conditional Statements
C# provides several ways to perform conditional operations:

```csharp
int temperature = 25;

if (temperature > 30)
{
    Console.WriteLine("It's hot outside.");
}
else if (temperature > 20)
{
    Console.WriteLine("The weather is nice.");
}
else
{
    Console.WriteLine("It's cold outside.");
}
```

### Loops
C# includes several loop constructs:

- **`for` Loop**: Executes a block of code a specific number of times.

```csharp
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
```

- **`while` Loop**: Repeats as long as the condition is true.

```csharp
int count = 0;
while (count < 5)
{
    Console.WriteLine(count);
    count++;
}
```

- **`do...while` Loop**: Executes the block at least once, then continues if the condition is true.

```csharp
int count = 0;
do
{
    Console.WriteLine(count);
    count++;
} while (count < 5);
```

## **Methods**
### Defining and Calling Methods
Methods help organize code into reusable blocks:

```csharp
using System;

class Program
{
    static void Greet()
    {
        Console.WriteLine("Hello, welcome to C# programming!");
    }

    static int Add(int a, int b)
    {
        return a + b;
    }

    static void Main()
    {
        Greet();
        int result = Add(3, 4);
        Console.WriteLine($"Sum: {result}");
    }
}
```

### Method Overloading
C# supports method overloading, allowing methods with the same name but different parameters.

```csharp
class Program
{
    static int Multiply(int a, int b)
    {
        return a * b;
    }

    static double Multiply(double a, double b)
    {
        return a * b;
    }

    static void Main()
    {
        Console.WriteLine(Multiply(5, 6)); // Calls int version
        Console.WriteLine(Multiply(5.5, 6.5)); // Calls double version
    }
}
```

## **Object-Oriented Programming**
### Classes and Objects
C# is object-oriented, meaning you use classes and objects to model real-world entities:

```csharp
using System;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public void Greet()
    {
        Console.WriteLine($"Hello, my name is {Name} and I am {Age} years old.");
    }
}

class Program
{
    static void Main()
    {
        Person person1 = new Person { Name = "Alice", Age = 30 };
        person1.Greet();
    }
}
```

### Inheritance
Inheritance allows one class to inherit from another, facilitating code reuse:

```csharp
using System;

class Animal
{
    public void Eat()
    {
        Console.WriteLine("Eating...");
    }
}

class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("Woof!");
    }
}

class Program
{
    static void Main()
    {
        Dog dog = new Dog();
        dog.Eat(); // Inherited method
        dog.Bark(); // Derived method
    }
}
```

### Polymorphism
Polymorphism allows methods to perform different tasks based on the object's type:

```csharp
using System;

class Base
{
    public virtual void Show()
    {
        Console.WriteLine("Base class show function.");
    }
}

class Derived : Base
{
    public override void Show()
    {
        Console.WriteLine("Derived class show function.");
    }
}

class Program
{
    static void Main()
    {
        Base b = new Derived();
        b.Show(); // Calls Derived's Show()
    }
}
```

### Encapsulation
Encapsulation restricts access to some of an object's components, enhancing security:

```csharp
using System;

class BankAccount
{
    private double balance;

    public BankAccount(double initialBalance)
    {
        balance = initialBalance;
    }

    public void Deposit(double amount)
    {
        if (amount > 0)
        {
            balance += amount;
        }
    }

    public void Withdraw(double amount)
    {
        if (amount > 0 && amount <= balance)
        {
            balance -= amount;
        }
    }

    public double GetBalance()
    {
        return balance;
    }
}

class Program
{
    static void Main()
    {
        BankAccount account = new BankAccount(1000.0);
        account.Deposit(500.0);
        account.Withdraw(200.0);
        Console.WriteLine($"Balance: {account.GetBalance()}");
    }
}
```

## **LINQ (Language Integrated Query)**
### Querying Collections
LINQ provides a powerful syntax for querying collections:

```csharp
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int[] numbers = { 1, 2, 3, 4, 5 };
        var evenNumbers = from number in numbers
                          where number % 2 == 0
                          select number;

        foreach (var number in evenNumbers)
        {
            Console.WriteLine(number);
        }
    }
}
```

### Method Syntax
LINQ can also be used with method syntax:

```csharp
using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int[] numbers = { 1, 2, 3, 4, 5 };
        var evenNumbers = numbers.Where(n => n % 2 == 0);

        foreach (var number in evenNumbers)
        {
            Console.WriteLine(number);
        }
    }
}
```

## **Asynchronous Programming**
### `async` and `await`
C# supports asynchronous programming using `async` and `await`:

```csharp
using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        Console.WriteLine("Start");
        await Task.Delay(2000); // Simulate a delay
        Console.WriteLine("End");
    }
}
``

`

### Task-Based Asynchronous Pattern
The Task-Based Asynchronous Pattern (TAP) is used for asynchronous operations:

```csharp
using System;
using System.Threading.Tasks;

class Program
{
    static async Task<int> CalculateSumAsync(int a, int b)
    {
        await Task.Delay(1000); // Simulate a delay
        return a + b;
    }

    static async Task Main()
    {
        int result = await CalculateSumAsync(5, 7);
        Console.WriteLine($"Sum: {result}");
    }
}
```

## **Exception Handling**
### `try`, `catch`, and `finally`
C# handles exceptions using `try`, `catch`, and `finally` blocks:

```csharp
using System;

class Program
{
    static void Main()
    {
        try
        {
            int result = 10 / 0; // This will throw a DivideByZeroException
        }
        catch (DivideByZeroException ex)
        {
            Console.WriteLine("Error: Cannot divide by zero.");
        }
        finally
        {
            Console.WriteLine("Execution completed.");
        }
    }
}
```

## **File I/O**
### Reading and Writing Files
C# provides classes for file operations in the `System.IO` namespace:

```csharp
using System;
using System.IO;

class Program
{
    static void Main()
    {
        // Writing to a file
        File.WriteAllText("example.txt", "Hello, file!");

        // Reading from a file
        string content = File.ReadAllText("example.txt");
        Console.WriteLine(content);
    }
}
```

## **Advanced Topics**
### Reflection
Reflection allows you to inspect and manipulate object types at runtime:

```csharp
using System;
using System.Reflection;

class Program
{
    static void Main()
    {
        Type type = typeof(string);
        Console.WriteLine("Methods of String class:");
        foreach (MethodInfo method in type.GetMethods())
        {
            Console.WriteLine(method.Name);
        }
    }
}
```

### Attributes
Attributes provide metadata about program elements:

```csharp
using System;

[Obsolete("This class is obsolete. Use NewClass instead.")]
class OldClass
{
    public void OldMethod()
    {
        Console.WriteLine("This method is obsolete.");
    }
}

class Program
{
    static void Main()
    {
        OldClass oldClass = new OldClass();
        oldClass.OldMethod();
    }
}
```

### Dependency Injection
Dependency Injection (DI) is a design pattern for achieving Inversion of Control (IoC):

```csharp
using System;

interface IMessageService
{
    void SendMessage(string message);
}

class EmailService : IMessageService
{
    public void SendMessage(string message)
    {
        Console.WriteLine($"Email sent: {message}");
    }
}

class Notification
{
    private readonly IMessageService _messageService;

    public Notification(IMessageService messageService)
    {
        _messageService = messageService;
    }

    public void Notify(string message)
    {
        _messageService.SendMessage(message);
    }
}

class Program
{
    static void Main()
    {
        IMessageService emailService = new EmailService();
        Notification notification = new Notification(emailService);
        notification.Notify("Hello, Dependency Injection!");
    }
}
```

## **Testing**
### Unit Testing
Use frameworks like MSTest, NUnit, or xUnit for unit testing in C#:

```csharp
using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

[TestClass]
public class CalculatorTests
{
    [TestMethod]
    public void Add_ValidInputs_ReturnsSum()
    {
        int result = Calculator.Add(2, 3);
        Assert.AreEqual(5, result);
    }
}
```

## **Conclusion**
C# is a versatile and powerful language that combines modern programming features with ease of use. From basic syntax to advanced topics like dependency injection and reflection, mastering C# will enable you to build a wide range of applications. This guide provides a comprehensive overview of C# programming concepts and practices.

## **Appendix**
### Glossary
- **Class**: A blueprint for creating objects that encapsulate data and behavior.
- **Object**: An instance of a class.
- **LINQ**: A set of methods and syntax for querying collections in a declarative manner.
- **Asynchronous Programming**: A programming model that allows tasks to run concurrently.

### Additional Resources
- [C# Programming Guide on Microsoft Docs](https://docs.microsoft.com/en-us/dotnet/csharp/)
- [C# in Depth by Jon Skeet](https://www.amazon.com/C-Depth-Jon-Skeet/dp/1617294535)
- [LearnCSharp.org](https://www.learncs.org/)