from types import Union

def add(number1: Union[int, float], number2: Union[int, float]) -> Union[int, float]:
    #assert isinstance(number1, (int, float)) and isinstance(number2, (int, float)),"Both args must be numbers"
    return number1+number2


class User:
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        
def printUserInfo(user:User) -> None:
    print(f"User name is {user.name} and its age is {user.age}")
    
    
user = User("Tomek", 28)    
printUserInfo(user)

