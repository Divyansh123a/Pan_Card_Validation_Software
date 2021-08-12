# Do not change anything in this file

import PanCardService as ps

def main():
    
    service_obj=ps.PanCardService()
    file_obj=service_obj.access_file()
    
    pan_list=service_obj.extract_data(file_obj)
    
    # Display the valid pan numbers
    if len(pan_list)!=0:
        print("Valid Pan Card numbers are:")
        for i in pan_list:
            print(i.get_name()," - ", i.get_pan_number())
    else:
        print("No valid pan card numbers available")
        
    
if __name__=='__main__':
    main()
