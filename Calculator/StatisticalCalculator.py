# coding: utf-8
# import function to read csv file
from FileReader import readCSV

# import math library
import math

#  get numbers from dataset 
dataSet = readCSV('csv/test.csv')

#################################################################################
choice = ''

print('Select operation!')
print('1.Population Standard Deviation')
print('2.Variance of Population Proportion')
print('3.Calculate Z-Score for each Number')
print('4.Sample Standard Deviation')
print('5.Variance of Sample Proportion')

choice = input('Enter choice:')

if choice == "1":
    from StatisticsModule import populationStandardDeviation
    print('Standard Deviation - Population: ', str(populationStandardDeviation(dataSet)))
elif choice == "2":
    from StatisticsModule import variancePopulationProportion
    print('variance- Population: ', str(variancePopulationProportion(dataSet)))    
elif choice == "3":
    from StatisticsModule import zScore
    print('z-score: ', str(zScore(dataSet)))
elif choice == "4":
    from StatisticsModule import standardDeviation
    print('standard deviation: ', str(standardDeviation(dataSet)))
elif choice == "5":
    from StatisticsModule import varianceSampleProportion
    print('Variance Sample Proportion: ', str(varianceSampleProportion(dataSet)))
else:
    print("(•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ ) something went wrong (•̀ᴗ•́ )(•̀ᴗ•́ )(•̀ᴗ•́ )")
