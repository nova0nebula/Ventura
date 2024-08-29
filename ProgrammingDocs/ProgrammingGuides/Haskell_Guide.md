# **Haskell Programming Guide**

## **Introduction**
Haskell is a pure functional programming language known for its strong static typing, immutability, and lazy evaluation. Named after the logician Haskell Curry, it is designed to handle complex software engineering tasks with an emphasis on mathematical functions and formal logic. Haskell's advanced type system, concise syntax, and powerful abstractions make it well-suited for both academic and real-world applications.

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [Basic Syntax](#basic-syntax)
3. [Data Types and Variables](#data-types-and-variables)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Type Classes](#type-classes)
7. [Lazy Evaluation](#lazy-evaluation)
8. [File Handling](#file-handling)
9. [Advanced Topics](#advanced-topics)
10. [Conclusion](#conclusion)
11. [Appendix](#appendix)

## **Getting Started**
### Setting Up Your Environment
To start with Haskell:

1. **Install GHC**: The Glasgow Haskell Compiler (GHC) is the most widely used Haskell compiler. You can download and install it from the [GHC official website](https://www.haskell.org/ghc/).

2. **Install Stack**: Stack is a build tool for Haskell that simplifies the management of Haskell projects. Install it from [Stack’s official website](https://docs.haskellstack.org/en/stable/README/).

3. **Write Your First Haskell Program**: Create a new file with a `.hs` extension and add the following code:

   ```haskell
   module Main where

   main :: IO ()
   main = putStrLn "Hello, Haskell!"
   ```

   Compile and run the program using Stack:

   ```shell
   stack ghc -- Main.hs
   ./Main
   ```

## **Basic Syntax**
### Comments
Comments in Haskell start with `--` for single-line comments or `{-` and `-}` for multi-line comments:

```haskell
-- This is a single-line comment

{- This is a
   multi-line comment -}

module CommentExample where

main :: IO ()
main = putStrLn "Comments in Haskell"
```

### Modules
Haskell code is organized into modules. Each module begins with the `module` keyword:

```haskell
module Math where

add :: Int -> Int -> Int
add x y = x + y

subtract :: Int -> Int -> Int
subtract x y = x - y
```

## **Data Types and Variables**
### Data Types
Haskell is strongly typed, with several built-in data types:

- **Integer**: Arbitrary precision integer (`42`)
- **Float**: Floating-point number (`3.14`)
- **Double**: Double-precision floating-point number (`0.1`)
- **Char**: Single character (`'a'`)
- **String**: List of characters (`"hello"`)
- **Bool**: Boolean values (`True`, `False`)

### Defining Custom Data Types
Define custom data types using the `data` keyword:

```haskell
data Person = Person String Int  -- Name and Age
    deriving (Show)

john :: Person
john = Person "John Doe" 30
```

### Type Synonyms
Use `type` to create type synonyms:

```haskell
type Name = String
type Age = Int

greet :: Name -> Age -> String
greet name age = "Hello, " ++ name ++ ". You are " ++ show age ++ " years old."
```

## **Control Flow**
### Conditional Statements
Use `if`, `then`, `else` for conditionals:

```haskell
absolute :: Int -> Int
absolute x = if x < 0 then -x else x
```

### Pattern Matching
Pattern matching is used for more complex conditional logic:

```haskell
describe :: Int -> String
describe n
    | n < 0     = "Negative"
    | n == 0    = "Zero"
    | otherwise = "Positive"
```

### Guards
Guards provide a way to handle multiple conditions:

```haskell
describe :: Int -> String
describe n
    | n < 0     = "Negative"
    | n == 0    = "Zero"
    | otherwise = "Positive"
```

## **Functions**
### Defining Functions
Functions are defined using the `functionName parameters = expression` syntax:

```haskell
square :: Int -> Int
square x = x * x
```

### Higher-Order Functions
Haskell supports higher-order functions, which can take other functions as arguments:

```haskell
applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

increment :: Int -> Int
increment x = x + 1

result :: Int
result = applyTwice increment 5  -- result will be 7
```

## **Type Classes**
### Introduction to Type Classes
Type classes define a set of functions that can operate on different types:

```haskell
class Eq a where
    (==) :: a -> a -> Bool
    (/=) :: a -> a -> Bool
```

### Implementing Type Classes
Implement type classes for specific types:

```haskell
instance Eq Person where
    (Person name1 age1) == (Person name2 age2) = name1 == name2 && age1 == age2
    (Person name1 age1) /= (Person name2 age2) = name1 /= name2 || age1 /= age2
```

## **Lazy Evaluation**
### Lazy Evaluation Basics
Haskell uses lazy evaluation, which means expressions are not evaluated until their values are needed:

```haskell
infiniteList :: [Int]
infiniteList = [1..]

firstTen :: [Int]
firstTen = take 10 infiniteList
```

### Using Lazy Evaluation
Lazy evaluation allows defining potentially infinite data structures:

```haskell
fibonacci :: [Int]
fibonacci = 0 : 1 : zipWith (+) fibonacci (tail fibonacci)
```

## **File Handling**
### Reading and Writing Files
Use Haskell’s I/O functions to handle files:

```haskell
import System.IO

readFileContents :: FilePath -> IO String
readFileContents fileName = do
    contents <- readFile fileName
    return contents

writeFileContents :: FilePath -> String -> IO ()
writeFileContents fileName content = do
    writeFile fileName content
```

## **Advanced Topics**
### Monads
Monads are a type class used for chaining operations:

```haskell
import Control.Monad (when)

main :: IO ()
main = do
    let x = 10
    when (x > 5) $ putStrLn "x is greater than 5"
```

### Functors
Functors are a type class used for mapping functions over data structures:

```haskell
import Data.Functor

incrementList :: [Int] -> [Int]
incrementList = fmap (+1)
```

### Applicatives
Applicatives extend Functors to allow for function application within a context:

```haskell
import Control.Applicative

add :: Int -> Int -> Int
add x y = x + y

applyAdd :: Maybe Int
applyAdd = pure add <*> Just 5 <*> Just 3  -- Result: Just 8
```

## **Conclusion**
Haskell’s strong type system, pure functional nature, and lazy evaluation make it a powerful tool for handling complex programming tasks. While Haskell’s concepts may seem abstract, they offer elegant solutions to problems and encourage a deeper understanding of programming principles.

## **Appendix**
### Glossary
- **Pure Function**: A function that always produces the same result given the same inputs and has no side effects.
- **Lazy Evaluation**: Evaluation strategy where expressions are not evaluated until their values are needed.
- **Monad**: A type class for sequencing computations.
- **Functor**: A type class for mapping functions over data structures.

### Additional Resources
- [Haskell Official Documentation](https://www.haskell.org/documentation/)
- [Learn You a Haskell for Great Good!](http://learnyouahaskell.com/)