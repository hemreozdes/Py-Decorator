import time
def speedTest(fn):
    def inner(*args,**kwargs):
        startTime=time.perf_counter()
        print(f"{fn.__name__} method is working")
        result=fn(*args,**kwargs)
        endTime=time.perf_counter()
        runTime=endTime-startTime
        print(f"The spend time is {runTime}")
        return result
    return inner

@speedTest #Decorator
def sumGen():
    return sum((x for x in range(1000000)))

@speedTest #Decorator
def sumList():
    return sum([x for x in range(1000000)])
print(sumGen())
print(sumList())