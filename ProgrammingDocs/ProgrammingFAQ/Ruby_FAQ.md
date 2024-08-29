# **Ruby FAQ**

## **Table of Contents**
1. [General Questions](#general-questions)
2. [Ruby Basics](#ruby-basics)
3. [Data Types and Structures](#data-types-and-structures)
4. [Control Flow](#control-flow)
5. [Methods](#methods)
6. [Object-Oriented Programming](#object-oriented-programming)
7. [File Handling](#file-handling)
8. [Error Handling](#error-handling)
9. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
10. [Resources](#resources)

## **General Questions**

### **1. What is Ruby?**
Ruby is an open-source, dynamic programming language focused on simplicity and productivity. It emphasizes readability and is known for its elegant syntax that is easy to read and write. Ruby is often used for web development, particularly with the Ruby on Rails framework.

### **2. What are the key features of Ruby?**
- **Dynamic Typing**: Variables do not need to be explicitly declared with a type.
- **Garbage Collection**: Automatic memory management.
- **Object-Oriented**: Everything in Ruby is an object, including primitive data types.
- **Flexibility**: Allows modification of existing classes and methods.

### **3. How is Ruby typically used?**
Ruby is commonly used for web development, scripting, and automation. It is widely known for its use in the Ruby on Rails framework, which facilitates rapid web application development.

## **Ruby Basics**

### **1. What is the basic structure of a Ruby script?**

A Ruby script is a plain text file with a `.rb` extension. It contains Ruby code that can be executed directly.

- **Basic Script Example**:
  ```ruby
  # This is a comment in Ruby
  puts "Hello, Ruby!"
  ```

### **2. How do I execute a Ruby script?**

Ruby scripts can be executed using the Ruby interpreter from the command line:

- **Command**:
  ```bash
  ruby script.rb
  ```

### **3. How do I add comments in Ruby?**

Comments in Ruby start with a `#` symbol:

- **Example**:
  ```ruby
  # This is a comment
  x = 5  # This is an inline comment
  ```

## **Data Types and Structures**

### **1. What are the main data types in Ruby?**

Ruby supports several data types:

- **Integer**: Represents whole numbers.
- **Float**: Represents decimal numbers.
- **String**: Represents text.
- **Symbol**: Represents an immutable, unique identifier.
- **Boolean**: Represents `true` or `false`.

### **2. What are the key data structures in Ruby?**

Ruby provides several key data structures:

- **Array**: An ordered collection of elements.
- **Hash**: A collection of key-value pairs.
- **Set**: A collection of unique elements.

### **3. How do I create and manipulate arrays in Ruby?**

- **Creating an Array**:
  ```ruby
  numbers = [1, 2, 3, 4, 5]
  ```

- **Accessing Array Elements**:
  ```ruby
  first_element = numbers[0]
  ```

- **Manipulating Arrays**:
  ```ruby
  numbers.push(6)  # Adds an element to the end
  numbers.pop      # Removes the last element
  ```

## **Control Flow**

### **1. How do I use conditional statements in Ruby?**

Conditional statements in Ruby include `if`, `elsif`, and `else`:

- **Example**:
  ```ruby
  age = 20
  if age > 18
    puts "Adult"
  else
    puts "Not an adult"
  end
  ```

### **2. How do I use loops in Ruby?**

Ruby supports several loop constructs:

- **For Loop**:
  ```ruby
  for i in 1..5
    puts i
  end
  ```

- **While Loop**:
  ```ruby
  count = 1
  while count <= 5
    puts count
    count += 1
  end
  ```

- **Each Loop**:
  ```ruby
  [1, 2, 3, 4, 5].each do |i|
    puts i
  end
  ```

## **Methods**

### **1. How do I define and use methods in Ruby?**

Methods in Ruby are defined using the `def` keyword:

- **Method Definition**:
  ```ruby
  def greet(name)
    "Hello, #{name}!"
  end
  ```

- **Calling a Method**:
  ```ruby
  puts greet("Alice")  # Outputs: Hello, Alice!
  ```

### **2. How do I handle default arguments in Ruby methods?**

Default arguments can be specified in method definitions:

- **Example**:
  ```ruby
  def greet(name = "Guest")
    "Hello, #{name}!"
  end

  puts greet()          # Outputs: Hello, Guest!
  puts greet("Alice")  # Outputs: Hello, Alice!
  ```

## **Object-Oriented Programming**

### **1. How do I define and use classes in Ruby?**

Classes in Ruby are defined using the `class` keyword:

- **Class Definition**:
  ```ruby
  class Person
    def initialize(name)
      @name = name
    end

    def greet
      "Hello, #{@name}!"
    end
  end
  ```

- **Creating an Object**:
  ```ruby
  person = Person.new("Alice")
  puts person.greet  # Outputs: Hello, Alice!
  ```

### **2. How do I handle inheritance in Ruby?**

Inheritance is achieved using the `<` symbol:

- **Example**:
  ```ruby
  class Animal
    def speak
      "Generic sound"
    end
  end

  class Dog < Animal
    def speak
      "Woof!"
    end
  end

  dog = Dog.new
  puts dog.speak  # Outputs: Woof!
  ```

## **File Handling**

### **1. How do I read from and write to files in Ruby?**

Ruby provides methods for file handling:

- **Reading a File**:
  ```ruby
  File.open("file.txt", "r") do |file|
    content = file.read
    puts content
  end
  ```

- **Writing to a File**:
  ```ruby
  File.open("file.txt", "w") do |file|
    file.write("Hello, Ruby!")
  end
  ```

## **Error Handling**

### **1. How do I handle exceptions in Ruby?**

Exceptions are handled using `begin`, `rescue`, and `ensure`:

- **Example**:
  ```ruby
  begin
    # Code that may raise an exception
    result = 10 / 0
  rescue ZeroDivisionError
    puts "Cannot divide by zero!"
  ensure
    puts "This will always be executed."
  end
  ```

## **Common Issues and Troubleshooting**

### **1. Why is my Ruby script not working?**

- **Check Syntax**: Ensure the script follows Ruby syntax rules.
- **File Paths**: Verify that file paths are correct.
- **Dependencies**: Make sure all required gems are installed.
- **Error Messages**: Read and understand error messages to identify issues.

### **2. How do I debug Ruby code?**

- **Use `puts` Statements**: Print variable values and code execution flow.
- **Debugger Tools**: Utilize debugging tools like `byebug` or `pry` for interactive debugging.

## **Resources**

- [Ruby Documentation](https://ruby-doc.org/)
- [Ruby Guides](https://www.ruby-lang.org/en/documentation/quickstart/)
- [RubyGems](https://rubygems.org/)
- [Ruby on Rails Guides](https://guides.rubyonrails.org/)