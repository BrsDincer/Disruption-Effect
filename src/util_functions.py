from util_class import PROCESS,ENVIRONMENT
import numpy as np

ReturnFontConfiguration:PROCESS = lambda x,y,z: x.render(y,True,z)

def PopulateEnvironment(environment:ENVIRONMENT,objectCount:int or float,size:int)->PROCESS:
    for _ in range(objectCount):
        x,y = np.random.randint(0,size,2)
        environment[x,y] = 1
    return environment

def ApplyEnvironmentRules(environment:ENVIRONMENT,size:int)->PROCESS:
    newGeneration = np.zeros((size,size))
    for x in range(size):
        for y in range(size):
            if environment[x,y] == 1:
                yAxis = (y+1)%size
                newGeneration[x,yAxis] = 1
            else:
                pass
    environment = newGeneration
    return environment

def ErrorProbability(environment:ENVIRONMENT,size:int,maxError:int or float)->PROCESS:
    current = np.sum(environment==1)
    result = min(current/(size**2)*maxError,maxError)
    return result

def RunDisruption(environment:ENVIRONMENT,size:int,disruptionCount:int)->PROCESS:
    x,y = np.random.randint(0,size,2)
    environment[x,y] = 1 - environment[x,y]
    disruptionCount += 1
    return environment,disruptionCount
    
    
    
        