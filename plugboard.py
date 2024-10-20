class plugboard : 

     def __init__(self, pairs):
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.left = list(self.right)
    
        for pair in pairs : 
            if len(pair) != 2:  # Check for valid pairs
                print("Invalid input:", pair)
                continue
            # get the indices of the characters in the pair 
            
            index_1 = self.right.index(pair[0])
            index_2 = self.right.index(pair[1])

            #Swap the charcaters 
            self.left[index_1] , self.left [index_2]= self.left [index_2] , self.left[index_1]
        #Converting self.right into a string 
        self.left = ''.join(self.left)
