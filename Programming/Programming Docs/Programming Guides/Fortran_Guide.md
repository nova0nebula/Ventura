# **Fortran Programming Guide**

## **Introduction**
Fortran (Formula Translation) is a high-level programming language primarily used for numerical and scientific computing. Developed in the 1950s by IBM, Fortran is known for its efficiency in mathematical computations and its use in scientific, engineering, and mathematical applications.

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [Fortran Basics](#fortran-basics)
3. [Data Types](#data-types)
4. [Control Structures](#control-structures)
5. [Subroutines and Functions](#subroutines-and-functions)
6. [Arrays and Matrix Operations](#arrays-and-matrix-operations)
7. [File I/O](#file-io)
8. [Modules](#modules)
9. [Best Practices](#best-practices)
10. [Conclusion](#conclusion)
11. [Appendix](#appendix)

## **Getting Started**
### Setting Up Your Environment
1. **Installing Fortran**: Install a Fortran compiler. Popular options include GNU Fortran (gfortran) and Intel Fortran Compiler.

   **Installing GNU Fortran (gfortran):**
   ```bash
   sudo apt-get install gfortran
   ```

2. **Creating a Fortran File**: Create a file with a `.f90` extension.

   **Fortran File (`hello.f90`):**
   ```fortran
   program hello
       print *, "Hello, Fortran!"
   end program hello
   ```

3. **Compiling Fortran**: Compile Fortran code using the `gfortran` command:

   ```bash
   gfortran hello.f90 -o hello
   ```

   Run the executable:

   ```bash
   ./hello
   ```

## **Fortran Basics**
### Structure of a Fortran Program
A basic Fortran program consists of a `program` statement, followed by the executable code, and ending with an `end program` statement:

```fortran
program example
    ! This is a comment
    print *, "This is a simple Fortran program."
end program example
```

### Comments
Comments in Fortran start with `!` and continue to the end of the line:

```fortran
! This is a comment
```

## **Data Types**
### Basic Data Types
Fortran supports several basic data types:

- **`INTEGER`**: Represents integer values.

  ```fortran
  integer :: age = 30
  ```

- **`REAL`**: Represents floating-point numbers.

  ```fortran
  real :: temperature = 23.5
  ```

- **`DOUBLE PRECISION`**: Represents double-precision floating-point numbers.

  ```fortran
  double precision :: pi = 3.14159265358979
  ```

- **`CHARACTER`**: Represents character strings.

  ```fortran
  character(len=20) :: name = "Fortran User"
  ```

- **`LOGICAL`**: Represents boolean values.

  ```fortran
  logical :: is_valid = .true.
  ```

## **Control Structures**
### Conditional Statements
Use `IF`, `ELSE IF`, and `ELSE` for decision-making:

```fortran
program check_number
    integer :: number
    print *, "Enter a number:"
    read *, number

    if (number > 0) then
        print *, "The number is positive."
    else if (number < 0) then
        print *, "The number is negative."
    else
        print *, "The number is zero."
    end if
end program check_number
```

### Loops
Fortran supports several looping constructs:

- **`DO` Loop**:

  ```fortran
  program loop_example
      integer :: i

      do i = 1, 5
          print *, "Iteration", i
      end do
  end program loop_example
  ```

- **`DO WHILE` Loop**:

  ```fortran
  program do_while_example
      integer :: count = 1

      do while (count <= 5)
          print *, "Count", count
          count = count + 1
      end do
  end program do_while_example
  ```

## **Subroutines and Functions**
### Subroutines
Subroutines are blocks of code that can be called from other parts of the program:

```fortran
program main
    call greet("Fortran User")
end program main

subroutine greet(name)
    character(len=*) :: name
    print *, "Hello, ", name
end subroutine greet
```

### Functions
Functions return a value and can be used in expressions:

```fortran
program main
    real :: result
    result = square(5.0)
    print *, "The square is", result
end program main

function square(x)
    real, intent(in) :: x
    real :: square
    square = x * x
end function square
```

## **Arrays and Matrix Operations**
### Declaring Arrays
Arrays are collections of elements of the same type:

```fortran
program array_example
    integer, dimension(5) :: numbers
    integer :: i

    do i = 1, 5
        numbers(i) = i * 2
    end do

    print *, "Array elements:", numbers
end program array_example
```

### Multi-Dimensional Arrays
Fortran supports multi-dimensional arrays for matrix operations:

```fortran
program matrix_example
    real, dimension(2, 2) :: matrix
    integer :: i, j

    matrix = reshape((/1.0, 2.0, 3.0, 4.0/), shape(matrix))

    do i = 1, 2
        do j = 1, 2
            print *, "matrix(", i, ",", j, ") = ", matrix(i, j)
        end do
    end do
end program matrix_example
```

## **File I/O**
### Reading and Writing Files
Fortran provides commands for file operations:

- **Writing to a File**:

  ```fortran
  program write_file
      integer :: i
      open(unit=10, file="output.txt", status="replace")

      do i = 1, 5
          write(10, *) "Line ", i
      end do

      close(10)
  end program write_file
  ```

- **Reading from a File**:

  ```fortran
  program read_file
      integer :: i
      character(len=100) :: line
      open(unit=10, file="output.txt", status="old")

      do
          read(10, '(A)', iostat=i) line
          if (i /= 0) exit
          print *, line
      end do

      close(10)
  end program read_file
  ```

## **Modules**
### Creating and Using Modules
Modules encapsulate related procedures and variables:

- **Module Definition**:

  ```fortran
  module math_utils
      contains
      function add(a, b)
          integer, intent(in) :: a, b
          integer :: add
          add = a + b
      end function add
  end module math_utils
  ```

- **Using a Module**:

  ```fortran
  program main
      use math_utils
      integer :: result

      result = add(5, 10)
      print *, "The result is", result
  end program main
  ```

## **Best Practices**
### Code Organization
- **Modular Design**: Break programs into modules and subroutines for better organization.
- **Commenting**: Use comments to explain complex logic and document your code.

### Error Handling
- **Assertions**: Use assertions to verify conditions during runtime.
- **Validation**: Validate input data to prevent errors and unexpected results.

## **Conclusion**
Fortran remains a powerful language for numerical and scientific computing. Its efficiency in handling mathematical computations and array operations makes it a valuable tool in fields requiring high-performance calculations.

## **Appendix**
### Glossary
- **Subroutine**: A block of code that performs a specific task and is called from other parts of the program.
- **Function**: A block of code that returns a value and can be used in expressions.
- **Module**: A file that contains related procedures and data types, which can be used by other programs.

### Additional Resources
- [Fortran Wiki](https://fortranwiki.org/fortran/show/Main)
- [GNU Fortran Documentation](https://gcc.gnu.org/onlinedocs/gfortran/)
- [Fortran Tutorials](https://www.fortran90.org/)