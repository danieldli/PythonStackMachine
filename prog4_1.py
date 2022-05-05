import numbers
def Tokenize(str):
    tostr = []
    token = str.split()
    for i in range(0,len(token)):
        if token[i] in ("push","pop","add","sub","mul","div","mod","skip","save","get") or token[i].lstrip('-+').isdigit():
            tostr.append(token[i])    
        else:
            raise ValueError("Unexpected Token: <"+token[i]+">")
    return tostr



def Parse(token):
    parstr = []
    if len(token) == 1:
        if token[0] in ("pop","add","sub","mul","div","mod","skip"):
            parstr.append(token[0])
        else:
            raise ValueError("Parse error: <"+token[0]+">")
    elif len(token) == 2:
        if token[0] in ("push","save","get"):
            if token[1].lstrip('-+').isdigit():
                parstr.append(token[0])
                parstr.append(token[1])
        else:
            raise ValueError("Parse error: <"+token[0]+" "+token[1]+">")
    else:       #If other than 2 tokens per line, error.
        raise ValueError("Parse error: more than 2 tokens per line")
    return parstr
