class foo:
    __classVar = 10
    
    def __init__(self, one, two):
        self.one = one
        self.two = two
        
    @property    
    def clasVarReturn(self):
       print(self.__classVar)
       
       
       
t = foo(1,2)
t.clasVarReturn