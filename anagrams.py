def is_anagram(str1,str2):
    
    str1=str1.replace(" ","").lower()# remove spaces (if any) and convert  lowercase:
    str2=str2.replace(" ","").lower()# remove spaces (if any) and convert  lowercase:

    if len(str1)!=len(str2):# checks if both strings are of equal length.
        return False
    
    return sorted(str1)==sorted(str2) #sorted("listen") = ['e', 'i', 'l', 'n', 's', 't']  
                                      #sorted("silent") = ['e', 'i', 'l', 'n', 's', 't'] 

str1=input()
str2=input()

if is_anagram(str1,str2):
    print(f"{str1} & {str2} are anagrams")
else:
     print(f"{str1} & {str2} are not anagrams")