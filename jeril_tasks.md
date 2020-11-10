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
            4. Population Sampling Functions
                1. Simple random sampling
                2. Confidence Interval For a Sample
                3. Margin of Error
                4. Cochran’s Sample Size Formula
                5. How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)
        8. Lookup t-score and z-score
        9. Validation 
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
        3. CSVReader Tests 
            1. Test CSVReader (File:test_csvreader.py)
            2. Test TableReader (File:test_tablereader.py)
    2. Random Generator Function (Folder: test, File:randoms.py)
        1. Generate a random number without a seed between a range of two numbers - Both Integer and Decimal
        2. Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
        3. Generate a list of N random numbers with a seed and between a range of numbers - Both Integer and Decimal
        4. Select a random item from a list
        5. Set a seed and randomly.select the same value from a list
        6. Select N number of items from a list without a seed
        7. Select N number of items from a list with a seed
    
3. CSV Reader (Folder: CSVReader) 
    1. CSVReader for Calculator test data(File: CSVReader.py)
    2. Table Reader for z-table and t-table(File: TableReader.py)
4. CSV files (Folder: csv)
    1. CSV files for unit testing addition,subrtaction,multiplication,division,square,square root
      1. Unit Test Addition.csv
      2. Unit Test Division.csv
      3. Unit Test Multiplication.csv
      4. Unit Test Square Root.csv
      5. Unit Test Square.csv
      6. Unit Test Subtraction.csv
      7. z-table.csv
      8. t-table.csv
      
5. Travis CI
    1. travis config file (File: .travis.yml)
    2. travis build status 
6. Readme file
    1. Outline
    2. Development tasks
    3. Math table (addition,subtraction,multipliction,division,square,squareroot,mean,median,mode)
7. Project 
    1. Created columns
    2. Added ToDo Tasks 
    3. Added Pull Requests under Review column
8. Dockerfile 

