def typeCheck(calledBy, variableName, item, expectedType):
    if type(item) != expectedType:
        raise ValueError(f"{calledBy}: type of {variableName} is {type(item)}. Expected: {expectedType}")
    
def lenCheck(calledBy, variableName, item, expectedMin, expectedMax):
    if len(item) > expectedMax or len(item) < expectedMin:
        raise ValueError(f"{calledBy}: length of {variableName} is {len(item)}. Expected: length between {expectedMin} and {expectedMax}")
    
def tupleCheck(calledBy, variableName, collectionName, item, collection):
    if item not in collection:
        raise ValueError(f"{calledBy}: {item} is not in the tuple {collectionName}. Check collection or comments in function for a list of valid items!")