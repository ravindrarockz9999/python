text = "Practice, patience, Python"
word = text.split()    # Here split inbuilt keyword will split each string

print("words:", word)

# Another way using with this split built in function
# we can split at particular word

message = "Learn Python with Ravindra"
splitword = message.split("with")

print(splitword)

# we can also print in one line
print(message.split("with"))