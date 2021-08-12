class PanCard:
    # Write your code here for defining 'PanCard' class members
    def __init__(self,name,pan_number):
        self.__name = name;
        self.__pan_number = pan_number;
    def set_name(self,name):
        self.__name = name;
    def get_name(self):
        return self.__name;
    def set_pan_number(self,pan_number):
        self.__pan_number = pan_number;
    def get_pan_number(self):
        return self.__pan_number;
