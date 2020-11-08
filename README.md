[![Build Status](https://travis-ci.org/jerilj/stats_calculator.svg?branch=main)](https://travis-ci.org/jerilj/stats_calculator)

# stats_calculator

## Outline
1. Calculator Object (Folder: Calculator)
    1. Properties
        1. result
    2. Instance Methods
        1. constructor 
        2. add
        3. subtract
        4. multiply
        5. divide
        6. square
        6. square root
    3. Static Methods (Folder: Calculator)
        1. Addition
            1. Add 2 numbers
            2. Add numbers in a list
        2. Subtraction
        3. multiplication
        4. division
        5. square_root
    2. Staistics Class inherited from Calculator Class (Folder: Statistics)
        1. Properties
            1. result (inherited from Calculator class)
        2. Instance Methods
            1. mean
            2. median
            3. mode
            4. variance 
            5. standard deviation
            6. z-score
        3. Static Methods (Folder: Statistics)
            1. Mean
                1. Statis method to add numebr in a list (Folder: Calculator)
            2. Median
            3. Mode
            

# Development Tasks 

> **List of development tasks are given below**
>
> **Refer to the Math table for formulas and examples**

1. Calculator (Folder: Calculator)
    1. constructor 
    2. Addition 
        1. Add 2 numbers
        2. Add numbers in a list
    3. Subtraction 
    4. Multiplication 
    5. Division 
    6. Square 
    7. Square Root 
    2. Staistics Class inherited from Calculator Class (Folder: Statistics)
        1. Mean 
            1. Statis method to add numebr in a list (Folder: Calculator)
        2. Median 
        3. Mode 
        4. Variance 
        5. Standard Deviation 
        6. Z-Score 
2. Tests (Folder: test)
    1. Unit Tests
        1. Calculator Tests
            1. Test Calculator methods using CSVReader and data in csv files
        2. Statistics Tests
            1. Test Statistics methods
            2. Use data generated from random generator functions
            3. Use python Statistics module to validate results
        3. CSVReader Tests
            1. Test CSVReader
    2. Random Generator Function
        1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
        2. Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
        3. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
        4. Select a random item from a list
        5. Set a seed and randomly.select the same value from a list
        6. Select N number of items from a list without a seed
        7. Select N number of items from a list with a seed
    
3. CSV Reader (Folder: CSVReader) 
4. CSV files (Folder: csv)
    1. CSV files for unit testing addition,subrtaction,multiplication,division,square,square root
5. Travis CI
    1. travis config file
    2. travis build status
6. Dockerfile


### Math Table

|ID| Task | Description | Formula | Example |
|--|------|-------------|---------|---------|
|1|Addition| Sum of two or or numbers| a + b = c| 1 + 2 = 2|
|2|Subtraction| Difference between two numbers| a - b = c| 2 - 1 = 1|
|3|Multiplication| Product of two numbers| a * b = c| 2 * 1 = 2|
|4|Division| Quotient of two numbers| a / b = c| 2 / 1 = 2|
|5|Square| Multiplying number by itself | a^2 | 2^2 = 4|
|6|Square Root| Square root of a number a is the  number b whose square is a | √a = b| √4 = 2 | 
|7|Mean| Average of list of numbers| Mean of numbers 1,2,3 is (a + b + c )/3 = c| (1 + 2 + 3)/3 = 2|
|8|Median| Median is the middle of sorted list of numbers| Media of numbers 1,2,3 is 2 | |
|9|Mode| Number that appears most often| Media of numbers 1,2,2,3 is 2| |
|10|Variance| Average of the squared differences from the Mean| | |
|11|Standard Deviation| The Standard Deviation is a measure of how spread out numbers are| | |
|12|Z-Score| A z-score measures exactly how many standard deviations above or below the mean a data point is| | |
