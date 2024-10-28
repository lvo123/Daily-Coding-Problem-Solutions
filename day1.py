from typing import List

def check_sum( arr : List[int],target :int ) -> bool:
    previous = set()
    for elem in arr:
        if (target - elem) in previous :
            return True
        previous.add(elem)
    return False

if __name__=="__main__":
    print (check_sum([],17))
    print (check_sum([15,3,7],17))