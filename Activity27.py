#Write a program to reverse the string entered by the user.

stri = input('Enter the string you wish to have reversed:')
stri2 = ('')
for a in stri:
    stri2=a+stri2
    print(stri,stri2)