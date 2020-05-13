import fuzzySetUtils
import fuzzyLogicOperators
import dependencyFunctionConfig
import numpy

def calculateFuzzyValue(x, dependencyFunctionParams):
    result = []
    for params in dependencyFunctionParams:
        if len(params) == 4:
           result.append(fuzzySetUtils.trapezoidCurve(x, params[0], params[1], params[2], params[3]))
        elif len(params) == 3:
            result.append(fuzzySetUtils.triangleCurve(x, params[0], params[1], params[2]))
    return result

def getAllFuzzyValues(playerData):
    result = []
    result.append(calculateFuzzyValue(playerData[0], dependencyFunctionConfig.HEIGHT_DEPENDENCY_FUNCTION_PARAMS))
    result.append(calculateFuzzyValue(playerData[1], dependencyFunctionConfig.AGE_DEPENDENCY_FUNCTION_PARAMS))
    result.append(calculateFuzzyValue(playerData[2], dependencyFunctionConfig.POINTS_DEPENDENCY_FUNCTION_PARAMS))
    result.append(calculateFuzzyValue(playerData[3], dependencyFunctionConfig.EFFICIENCY_DEPENDENCY_FUNCTION_PARAMS))
    return result

#Values table explenation:
#height small values[0][0]      age young[1][0]     points veryLow[2][0]    efficiency low[3][0]
#height average values[0][1]    age average[1][1]   points low[2][1]        efficiency average[3][1]
#height tall values[0][2]       age old[1][2]       points average[2][2]    efficiency high[3][2]
#                                                   points high[2][3]

def fuzzyRules(values):
    ruleOutputs = []
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][0], values[1][2], values[2][1])) #If height is small and age is old and points is low then small
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][0], values[1][1], values[3][0])) #If height is small and age is average and efficiency is low then small
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][0], values[2][0], values[3][0])) #If height is small and points is very low and efficiency is low then small
    ruleOutputs.append(fuzzyLogicOperators.Or(values[0][0], values[1][2]))                      #If height is small or age is old then small
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][1], values[1][2], values[3][0])) #If height is average and age is old and efficiency is low then small
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][2], values[2][0], values[3][0])) #If height is tall and points is very low and efficiency is low then small
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][1], values[1][0], values[3][1])) #If height is average and age is young and efficiency is average then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][1], values[1][1], values[2][2])) #If height is average and age is average and points is average then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][2], values[1][2], values[2][3])) #If height is tall and age is old and points is high then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][2], values[1][2], values[3][2])) #If height is tall and age is old and efficiency is high then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[1][1], values[2][3], values[3][1])) #If age is average and points is high and efficiency is average then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[1][1], values[2][2], values[3][2])) #If age is average and points is average and efficiency is high then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][2], values[2][0], values[3][2])) #If height is tall and points is very low and efficiency is high then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][1], values[1][0], values[2][2])) #If height is average and age is young and points is average then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][2], values[1][0], values[3][1])) #If height is tall and age is young and efficiency is average then average
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][2], values[1][0], values[2][3])) #If height is tall and age is young and points is high then high
    ruleOutputs.append(fuzzyLogicOperators.Or(values[2][3], values[3][2]))                      #If points is high or efficiency is high then high
    ruleOutputs.append(fuzzyLogicOperators.DoubleAnd(values[0][2], values[1][0], values[3][2])) #If height is tall and age is young and efficiency is high then high
    return ruleOutputs

def aggregateAnswers(input):
    aggregatedRules = []
    aggregatedRules.append(max(input[:7]))
    aggregatedRules.append(max(input[7:16]))
    aggregatedRules.append(max(input[16:]))
    return aggregatedRules

def meanOfMaximum(y):
    return numpy.mean(y)

def driver():
    playerFuzzyValues = getAllFuzzyValues([195, 30, 2096, 28])
    playerFuzzyValuesAfterRules = fuzzyRules(playerFuzzyValues)
    aggregatedRules = aggregateAnswers(playerFuzzyValuesAfterRules)
    print(aggregatedRules)
    print(meanOfMaximum(aggregatedRules))

driver()