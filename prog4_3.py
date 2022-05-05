import prog4_1 as tp
import prog4_2 as sm
import sys

#A driver program.
def main():
    
    toline = []     #To hold tokenized tokens.
    parline = []    #To hold parsed tokens.

    #Tokenize.        
    try:
        with open(sys.argv[1]) as f:
            toline = [tp.Tokenize(l) for l in f.readlines()]
    except ValueError as e:
        print(e)
        sys.exit()
    #Parsing.
    try:
        parline = [tp.Parse(l) for l in toline]

    except ValueError as e:
        print(e)
        sys.exit()

    #Instantiate a StackMachine class and execute line by line.
    s = sm.StackMachine()
    i = 0   #Keep track the line # and control loop.
    result=[]
    print("Assignment #4-3, Dong Li, dli3@sdsu.edu")


    #Send the tokenized and parsed list to the stack machine.
    try:
        while(i < len(parline)):
            result = s.Execute(parline[i])
            i = s.CL        #Get the current line index.
            if i < 0:       #If current line index is negative.
                print("Trying to execute invalid line: {0}".format(i))
                sys.exit()
            elif i >= 0:
                if result != None:
                    print(result)     

        #When current line index >= input line #.                
        print("Program terminated correctly")
        sys.exit()

    except IndexError as e:
        print(e)
        sys.exit()
##Entry point.
if __name__ == '__main__':
    main()


