class keyboard :
    def forward(self, input): # the input for this function is a letter 
        output = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(input)
        return output
    
    def backward (self,input):# the input for this function is the index of the letter 
        output= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[input]
        return output

