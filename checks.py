def typeCheck(calledBy, variableName, item, expectedType):
    if type(item) != expectedType:
        raise ValueError(f"{calledBy}: type of {variableName} is {type(item)}. Expected: {expectedType}")
    
def lenCheck(calledBy, variableName, item, expectedMin, expectedMax):
    if len(item) > expectedMax or len(item) < expectedMin:
        raise ValueError(f"{calledBy}: length of {variableName} is {len(item)}. Expected: length between {expectedMin} and {expectedMax}")