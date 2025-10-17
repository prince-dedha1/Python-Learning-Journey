'''Capitalize First Letter of Each Word (Manually)
Without using .title(), take a sentence and capitalize the first letter of each word using logic.'''

str1='''
A trusting little leaf of green,
A bold audacious frost;
A rendezvous, a kiss or two,
And youth for ever lost.
'''
lst=str1.split()
modified_str=""
for word in lst:
    modified_str = modified_str + (word[0].upper()+word[1:len(word)+1] + " ")
print(modified_str)