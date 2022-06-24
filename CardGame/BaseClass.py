# This class is never instatiated by itself. It is always inherited 
# Used to set up inheriting classes with standard class methods and properties.
 
class BaseClass:
    # Constructor
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key) and key[0] != '_':
                setattr(self, key, value)
        
    def __repr__(self):
        display_str = ""
        class_name = self.__class__.__name__
        display_str += f"\nClass Name: {class_name}"

        classify_class_attrs = f"".join("\n\t attribute({}) <{} : {}>".format(type(v), k, v) for k, v in self.__dict__.items())
        display_str += classify_class_attrs
        
        return display_str

    


 