def temp_converter(temp,n):
    if(n == "F"):
        converter1 = temp*9
        converter2 = converter1/5
        cel = converter2 +32
        return cel
    if(n == "C"):
        converter1 = temp - 32 
        converter2 = converter1*5
        faren = converter2/9
        return faren
        
print(temp_converter(100,"C"))
print(temp_converter(0, "F"))
print(temp_converter(212, "C"))
print(temp_converter(32, "C"))
print(temp_converter(50, "F"))