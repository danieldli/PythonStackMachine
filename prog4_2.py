
class StackMachine:
    
    #Constructor.
    def __init__(self):
        self.stack = []
        self.dict = {}    ##A dictionary for memory stroage.
        self.CL = 0       #To keep track of the currentline number.

    #Store memory    
    def put(self,key,value):
        self.dict[key] = value

    #Get memory
    def get(self,key):
        if key in self.dict:
            return self.dict[key]
        else:
            raise IndexError("Line {0}: 'get' caused Invalid Memory Access".format(self.CL))


    #Public function: will accept tokens and perform the operation.
    def Execute(self,tokens):
        if tokens[0] == "push":
            self.CL+=1
            self.stack.append(int(tokens[1]))
            return None
        elif tokens[0] == "pop":
            self.CL += 1
            if len(self.stack)==0:
                raise IndexError("Line {0}: 'pop' caused Invalid Memory Access".format(self.CL))
            else:
                return self.stack.pop() 
        elif tokens[0] == "add":
            self.CL += 1
            self.stack.append(self.stack.pop() + self.stack.pop())
            return None
        elif tokens[0] == "sub":
            self.CL += 1
            self.stack.append(self.stack.pop() - self.stack.pop())
            return None
        elif tokens[0] == "mul":
            self.CL += 1
            self.stack.append(self.stack.pop() * self.stack.pop())
            return None
        elif tokens[0] == "div":
            self.CL += 1
            self.stack.append(self.stack.pop() / self.stack.pop())
            return None
        elif tokens[0] == "mod":
            self.CL += 1
            self.stack.append(self.stack.pop() % self.stack.pop())
            return None
        elif tokens[0] == "skip":
            self.CL += 1
            if int(self.stack.pop()) == 0:
                self.CL += self.stack.pop()
            return None     
        elif tokens[0] == "save":
            self.CL += 1
            self.put(tokens[1], self.stack.pop())
            return None
        elif tokens[0] == "get":
            self.CL += 1
            self.stack.append(self.get(tokens[1]))
            return None
    

             


        
