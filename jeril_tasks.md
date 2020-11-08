## Tasks done by Jeril Jose

1. Calculator Object (Folder: Calculator, File Calculator.py)
    1. Properties
        1. result
    2. Instance Methods
        1. constructor 
        2. add
        3. subtract
        4. multiply
        5. divide
        6. square
        7. square root
    3. Static Methods (Folder: Calculator)
        1. Addition (File: Addition.py)
            1. Add 2 numbers
            2. Add numbers in a list
        2. Subtraction (File: Subtraction.py)
        3. multiplication (File: Multiplication.py)
        4. division (File: Division.py)
        5. square_root (File: SquareRoot.py)
    2. Staistics Class inherited from Calculator Class (Folder: Statistics, File: Statistics.py)
        1. Properties
            1. result (inherited from Calculator class)
        2. Instance Methods
            1. mean 
            2. median
            3. mode
        3. Static Methods (Folder: Statistics)
            1. Mean (File: Mean.py)
                1. Statis method to add numebr in a list (Folder: Calculator) 
            2. Median (File: Median.py)
            3. Mode (File: Mode.py)
 2. Tests (Folder: test)
    1. Unit Tests
        1. Calculator Tests (File:test_calculator.py)
            1. Test Calculator methods using CSVReader and data in csv files
        2. Statistics Tests (File:test_statistics.py)
            1. Test Statistics methods
            2. Use data generated from random generator functions
            3. Use python 'Statistics' module to validate results
        3. CSVReader Tests (File:test_cavreader.py)
            1. Test CSVReader
    2. Random Generator Function (Folder: test, File:randoms.py)
        1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
        2. Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
        3. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
        4. Select a random item from a list
        5. Set a seed and randomly.select the same value from a list
        6. Select N number of items from a list without a seed
        7. Select N number of items from a list with a seed
    
3. CSV Reader (Folder: CSVReader, File: CSVReader.py) 
4. CSV files (Folder: csv)
    1. CSV files for unit testing addition,subrtaction,multiplication,division,square,square root
      1. Unit Test Addition.csv
      2. Unit Test Division.csv
      3. Unit Test Multiplication.csv
      4. Unit Test Square Root.csv
      5. Unit Test Square.csv
      6. Unit Test Subtraction.csv
      
5. Travis CI
    1. travis config file (File: .travis.yml)
    2. travis build status 
6. Dockerfile 

