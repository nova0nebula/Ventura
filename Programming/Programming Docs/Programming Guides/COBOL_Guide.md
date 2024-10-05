# **COBOL Programming Guide**

## **Introduction**
COBOL (Common Business-Oriented Language) is a high-level programming language designed for business applications. Developed in the late 1950s, COBOL is known for its readability and is primarily used for data processing and business applications. Its syntax closely resembles English, making it relatively easy to read and understand.

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [Basic Syntax](#basic-syntax)
3. [Data Types and Variables](#data-types-and-variables)
4. [Control Flow](#control-flow)
5. [Functions and Procedures](#functions-and-procedures)
6. [File Handling](#file-handling)
7. [Object-Oriented COBOL](#object-oriented-cobol)
8. [Error Handling](#error-handling)
9. [Advanced Topics](#advanced-topics)
10. [Conclusion](#conclusion)
11. [Appendix](#appendix)

## **Getting Started**
### Setting Up Your Environment
To start with COBOL:

1. **Install a COBOL Compiler**: Popular COBOL compilers include GNU COBOL (formerly OpenCOBOL) and Micro Focus COBOL. You can download GNU COBOL from [GnuCOBOL's official website](https://sourceforge.net/projects/open-cobol/).

2. **Write Your First COBOL Program**: Create a new file with a `.cob` or `.cbl` extension and add the following code:

   ```cobol
   IDENTIFICATION DIVISION.
   PROGRAM-ID. HelloWorld.
   PROCEDURE DIVISION.
       DISPLAY 'Hello, COBOL!'.
       STOP RUN.
   ```

   Compile and run the program using your COBOL compiler.

## **Basic Syntax**
### Comments
Comments in COBOL start with `*` or `*>`:

```cobol
* This is a comment
*> This is also a comment

IDENTIFICATION DIVISION.
PROGRAM-ID. CommentExample.
PROCEDURE DIVISION.
    DISPLAY 'Comments in COBOL'.
    STOP RUN.
```

### Structure
COBOL programs are divided into several divisions:

- **IDENTIFICATION DIVISION**: Specifies the program name and other identification details.
- **ENVIRONMENT DIVISION**: Defines the environment in which the program runs.
- **DATA DIVISION**: Defines data structures and file descriptions.
- **PROCEDURE DIVISION**: Contains the executable code.

## **Data Types and Variables**
### Data Division
Define data items and their types in the DATA DIVISION:

```cobol
DATA DIVISION.
WORKING-STORAGE SECTION.
01 age       PIC 99.
01 name      PIC X(30).
01 salary    PIC 9(5)V99.
```

### Picture Clause
The `PIC` clause defines the format of data items:

- `PIC 99`: Two-digit integer
- `PIC X(30)`: Alphanumeric string of 30 characters
- `PIC 9(5)V99`: Numeric value with up to 5 digits before the decimal and 2 digits after

## **Control Flow**
### Conditional Statements
Use `IF`, `ELSE`, and `ELSE IF` for conditionals:

```cobol
IF age > 18
    DISPLAY 'Adult'
ELSE
    DISPLAY 'Minor'
END-IF.
```

### Loops
COBOL supports iterative processing with `PERFORM` and `NEXT SENTENCE`:

- **PERFORM Loop**:

  ```cobol
  PERFORM VARYING counter FROM 1 BY 1 UNTIL counter > 5
      DISPLAY counter
  END-PERFORM.
  ```

- **PERFORM with Paragraph**:

  ```cobol
  PERFORM Print-Numbers.
  .
  . 
  PRINT-NUMBERS.
      DISPLAY 'Number'.
      PERFORM VARYING counter FROM 1 BY 1 UNTIL counter > 5
          DISPLAY counter
      END-PERFORM.
  ```

## **Functions and Procedures**
### Paragraphs and Sections
COBOL organizes code into paragraphs and sections:

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. MyProgram.
PROCEDURE DIVISION.
    PERFORM Initialize
    PERFORM ProcessData
    PERFORM Finalize
    STOP RUN.

Initialize.
    DISPLAY 'Initialization'.

ProcessData.
    DISPLAY 'Processing Data'.

Finalize.
    DISPLAY 'Finalization'.
```

## **File Handling**
### File Definitions
Define files in the DATA DIVISION and use them in the PROCEDURE DIVISION:

```cobol
DATA DIVISION.
FILE SECTION.
FD inputFile
    RECORD CONTAINS 80 CHARACTERS
    RECORD KEY IS keyField.
01 inputRecord.
    05 keyField PIC X(10).
    05 dataField PIC X(70).

WORKING-STORAGE SECTION.
01 endOfFile PIC X VALUE 'N'.

PROCEDURE DIVISION.
    OPEN INPUT inputFile
    PERFORM UNTIL endOfFile = 'Y'
        READ inputFile INTO inputRecord
            AT END
                MOVE 'Y' TO endOfFile
            NOT AT END
                DISPLAY keyField
        END-READ
    END-PERFORM
    CLOSE inputFile
    STOP RUN.
```

## **Object-Oriented COBOL**
### Classes and Objects
COBOL supports object-oriented programming through Object COBOL:

```cobol
CLASS-ID. Person.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 name PIC X(30).
01 age PIC 99.

PROCEDURE DIVISION.
    DISPLAY 'Person class'.
    STOP RUN.

END CLASS Person.
```

### Methods
Define methods within classes:

```cobol
CLASS-ID. Person.

DATA DIVISION.
WORKING-STORAGE SECTION.
01 name PIC X(30).
01 age PIC 99.

PROCEDURE DIVISION USING BY REFERENCE name, BY REFERENCE age.
    DISPLAY 'Name: ' name
    DISPLAY 'Age: ' age
    STOP RUN.

END CLASS Person.
```

## **Error Handling**
### Error Handling
COBOL handles errors primarily through status codes and validation:

```cobol
PROCEDURE DIVISION.
    OPEN INPUT inputFile
    IF NOT FILE-STATUS = '00'
        DISPLAY 'Error opening file'
        STOP RUN
    END-IF.
```

## **Advanced Topics**
### Data Validation
Perform data validation using `VALIDATE` statements:

```cobol
PROCEDURE DIVISION.
    ACCEPT userInput
    IF userInput NOT NUMERIC
        DISPLAY 'Invalid input. Please enter a number.'
    END-IF.
```

### Working with Tables
COBOL supports table processing with OCCURS clauses:

```cobol
DATA DIVISION.
WORKING-STORAGE SECTION.
01 employeeTable.
   05 employeeRecord OCCURS 100 TIMES.
      10 empID PIC 9(5).
      10 empName PIC X(30).
      10 empSalary PIC 9(5)V99.

PROCEDURE DIVISION.
    PERFORM VARYING index FROM 1 BY 1 UNTIL index > 100
        MOVE index TO empID (index)
        MOVE 'Employee ' TO empName (index)
        MOVE 50000 TO empSalary (index)
    END-PERFORM.
```

## **Conclusion**
COBOL remains a significant language in business and financial systems due to its clarity and robustness for handling large-scale data processing. Although it is less commonly used in modern software development, understanding COBOL is valuable for maintaining legacy systems and for specific business applications.

## **Appendix**
### Glossary
- **PIC Clause**: Defines the format and length of data items.
- **FD (File Description)**: Describes the structure of files in COBOL.
- **PERFORM**: Executes a paragraph or section of code.

### Additional Resources
- [GNU COBOL Documentation](https://www.gnu.org/software/gnucobol/)
- [COBOL Programming Guide](https://www.ibm.com/docs/en/cobol-zos/5.3?topic=guide)