# email slicer using python

email=input("Enter your email-id:")

index=email.index("@")

username=email[:index]
domain=email[index+1:]

print(f"Your email username is {username} and the domain is {domain}")

# Optimised solution
 
email=input("Enter your email-id:")

username=email[:email.index("@")]
domain=email[email.index("@") + 1:]

print(f"Your email username is {username} and the domain is {domain}")

