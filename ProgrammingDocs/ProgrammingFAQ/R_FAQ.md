# **R FAQ**

## **Table of Contents**
1. [General Questions](#general-questions)
2. [R Basics](#r-basics)
3. [Data Types and Structures](#data-types-and-structures)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Data Manipulation](#data-manipulation)
7. [Data Visualization](#data-visualization)
8. [Statistical Analysis](#statistical-analysis)
9. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
10. [Resources](#resources)

## **General Questions**

### **1. What is R?**
R is a programming language and free software environment designed for statistical computing and graphics. It is widely used by statisticians, data scientists, and researchers for data analysis, visualization, and data-driven decision making.

### **2. What are the key features of R?**
- **Statistical Analysis**: Provides extensive statistical tools and techniques.
- **Data Visualization**: Offers powerful libraries for creating plots and graphs.
- **Data Manipulation**: Facilitates complex data manipulation and transformation.
- **Package System**: Supports a rich ecosystem of packages for various applications.

### **3. How is R typically used?**
R is commonly used for statistical analysis, data visualization, and data manipulation. It is employed in fields such as data science, bioinformatics, finance, and academic research.

## **R Basics**

### **1. What is the basic structure of an R script?**

An R script is a plain text file with a `.R` extension. It contains R code that can be executed line by line or as a whole.

- **Basic Script Example**:
  ```r
  # This is a comment in R
  print("Hello, R!")
  ```

### **2. How do I execute an R script?**

R scripts can be executed in several ways:
- **R Console**: Copy and paste the code directly into the R console.
- **RStudio**: Open the script in RStudio and click "Run".
- **Command Line**: Run the script from the command line with `Rscript script.R`.

### **3. How do I add comments in R?**

Comments in R start with a `#` symbol:

- **Example**:
  ```r
  # This is a comment
  x <- 5  # This is an inline comment
  ```

## **Data Types and Structures**

### **1. What are the main data types in R?**

R supports several data types:

- **Numeric**: Represents numbers, including integers and floating-point numbers.
- **Character**: Represents text strings.
- **Logical**: Represents boolean values (`TRUE` or `FALSE`).
- **Complex**: Represents complex numbers.

### **2. What are the key data structures in R?**

R has several key data structures:

- **Vector**: A one-dimensional array of elements of the same type.
- **Matrix**: A two-dimensional array of elements of the same type.
- **Data Frame**: A two-dimensional table-like structure where each column can be of different types.
- **List**: A one-dimensional collection of elements of different types.

### **3. How do I create and manipulate vectors in R?**

- **Creating a Vector**:
  ```r
  numbers <- c(1, 2, 3, 4, 5)
  ```

- **Accessing Vector Elements**:
  ```r
  first_element <- numbers[1]
  ```

- **Manipulating Vectors**:
  ```r
  numbers <- numbers * 2  # Double each element
  ```

## **Control Flow**

### **1. How do I use conditional statements in R?**

Conditional statements in R include `if`, `else if`, and `else`:

- **Example**:
  ```r
  age <- 20
  if (age > 18) {
    print("Adult")
  } else {
    print("Not an adult")
  }
  ```

### **2. How do I use loops in R?**

R supports several loop constructs:

- **For Loop**:
  ```r
  for (i in 1:5) {
    print(i)
  }
  ```

- **While Loop**:
  ```r
  count <- 1
  while (count <= 5) {
    print(count)
    count <- count + 1
  }
  ```

- **Apply Functions**:
  ```r
  numbers <- c(1, 2, 3, 4, 5)
  squared_numbers <- sapply(numbers, function(x) x^2)
  ```

## **Functions**

### **1. How do I define and use functions in R?**

Functions in R are defined using the `function` keyword:

- **Function Definition**:
  ```r
  greet <- function(name) {
    return(paste("Hello, ", name, "!", sep=""))
  }
  ```

- **Calling a Function**:
  ```r
  print(greet("Alice"))  # Outputs: Hello, Alice!
  ```

### **2. How do I handle default arguments in R functions?**

Default arguments can be set in the function definition:

- **Example**:
  ```r
  greet <- function(name = "Guest") {
    return(paste("Hello, ", name, "!", sep=""))
  }

  print(greet())          # Outputs: Hello, Guest!
  print(greet("Alice"))  # Outputs: Hello, Alice!
  ```

## **Data Manipulation**

### **1. How do I read and write data in R?**

R provides functions for reading from and writing to files:

- **Read CSV File**:
  ```r
  data <- read.csv("data.csv")
  ```

- **Write CSV File**:
  ```r
  write.csv(data, "output.csv")
  ```

### **2. How do I manipulate data frames in R?**

Data frames can be manipulated using various functions:

- **Accessing Columns**:
  ```r
  data$column_name
  ```

- **Subsetting Rows**:
  ```r
  subset_data <- data[data$age > 18, ]
  ```

- **Adding Columns**:
  ```r
  data$new_column <- data$existing_column * 2
  ```

## **Data Visualization**

### **1. How do I create basic plots in R?**

R provides several functions for plotting data:

- **Basic Plot**:
  ```r
  plot(x = 1:10, y = rnorm(10), main = "Basic Plot")
  ```

- **Histogram**:
  ```r
  hist(rnorm(100), main = "Histogram", xlab = "Value")
  ```

- **Boxplot**:
  ```r
  boxplot(rnorm(100), main = "Boxplot", ylab = "Value")
  ```

### **2. How do I use ggplot2 for advanced visualization?**

`ggplot2` is a powerful package for creating complex plots:

- **Example**:
  ```r
  library(ggplot2)
  ggplot(data = mtcars, aes(x = wt, y = mpg)) +
    geom_point() +
    ggtitle("Scatter Plot of Weight vs. MPG")
  ```

## **Statistical Analysis**

### **1. How do I perform basic statistical analysis in R?**

R offers a variety of functions for statistical analysis:

- **Descriptive Statistics**:
  ```r
  mean(data$column_name)
  sd(data$column_name)
  ```

- **Linear Regression**:
  ```r
  model <- lm(mpg ~ wt + hp, data = mtcars)
  summary(model)
  ```

- **Hypothesis Testing**:
  ```r
  t.test(data$column1, data$column2)
  ```

### **2. How do I use statistical models in R?**

R supports a range of statistical models:

- **Example**:
  ```r
  model <- glm(response ~ predictor1 + predictor2, family = binomial, data = data)
  summary(model)
  ```

## **Common Issues and Troubleshooting**

### **1. Why is my R script not working?**

- **Check Syntax**: Ensure the script follows R syntax rules.
- **Package Installation**: Verify that all required packages are installed.
- **Data Issues**: Check for issues with data files or data formatting.
- **Error Messages**: Read error messages carefully to identify and resolve issues.

### **2. How do I debug R code?**

- **Use `print` or `cat` Statements**: Output variable values and program flow.
- **RStudio Debugger**: Utilize the debugging tools available in RStudio.

## **Resources**

- [R Documentation](https://www.rdocumentation.org/)
- [R Tutorials](https://www.datacamp.com/community/tutorials/r-tutorial-learn-r-programming)
- [R Project](https://www.r-project.org/)
- [CRAN Packages](https://cran.r-project.org/web/packages/)