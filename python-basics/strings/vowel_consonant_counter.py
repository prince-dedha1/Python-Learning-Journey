# Count Vowels and Consonants in a String

a="im dEdhA gujjar "
vowel="aeiou"

v_count=0
c_count=0
all_lower=a.lower()
for i in all_lower:
    if i in vowel :
        v_count+=1
    else:
        if i !=" ":
            c_count+=1
print("Total vowel in string---> ",v_count)
print("Total consonant in string---> ",c_count)
