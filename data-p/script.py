"""
i=0
while i< 10:
    i+=1
    print(i)

for i in range(5):
    print("i=", i)

for i in [0,1,2,3,4]:
    print("i=", i)

def check_value():
    try:
        return "Try"
    finally:
        return "Finally"

print(check_value())

"""

x="hello"
if not type(x) is int:
    raise Exception ("Sorry, no integers are allowed")