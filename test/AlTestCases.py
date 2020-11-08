#populationStandardDeviation

def test_calc_populationStandardDeviation():
    from StatisticsModule import populationStandardDeviation
    assert populationStandardDeviation(testData) == 0.816496580927726

def test_calc_populationStandardDeviation_fail():
    from StatisticsModule import populationStandardDeviation
    assert populationStandardDeviation(testData) != 0.48

#populationCorrelat ionCoefficient

def test_calc_populationCorrelationCoefficient():
    from StatisticsModule import populationCorrelationCoefficient
    assert populationCorrelationCoefficient(dataSet)) == -0.43371655224528094

def test_calc_populationCorrelationCoefficient_fail():
    from StatisticsModule import populationCorrelationCoefficient
    assert populationCorrelationCoefficient(dataSet) != 5

#Proportion 

def test_calc_proportion():
    from StatisticsModule import proportion
    assert proportion(testData)) == ['0.1667', '0.3333', '0.5000']

def test_calc_proportion_fail():
    from StatisticsModule import proportion
    assert proportion(testData) != ['0.5000', '0.2000', '0.3000']
