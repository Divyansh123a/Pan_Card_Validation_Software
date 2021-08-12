import PanCard as pc

class PanCardService:
    
    # Method to access file and it should return File Object
    def access_file(self):
        # Write your code TelephoneDirectoryService
        file = open("pan_data.txt" , 'r')
        return file #TODO change this return value
        
    
    
    
    
    
    # Method to validatePan card number and it should return a boolean value
    def validate_pan_number(self, pan_number):
        # Write your code here
        status = None;
        if(len(pan_number)==10 and pan_number[0:5].isalpha() and pan_number[-1].isalpha()and pan_number[5:9].isnumeric()):
            status = True
        else:
            status = False;
        return status  #TODO change this return value
        
        
    
    
    
    # Method to read file and write validated data in List and it should return pan number object list
    def extract_data(self, file_obj):
	    # Write your code here
	    lis1 = []
	    for line in file_obj:
	        arr = line.split(",")
	        if(self.validate_pan_number(arr[1].strip("\n"))):
	            pan_obj = pc.PanCard(arr[0],arr[1].strip("\n"))
	            lis1.append(pan_obj)
	    return lis1    #TODO change this return value
		
