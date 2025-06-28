# Scope - What variables do I have access to?
a = 1 # Global variable

def parent():
    a = 10
    def confusion():
        # a = 5
        return a
    return confusion()

print(a)
print(parent())

# 1 - Start with local
# 2 - Parent local?
# 3 - Global?
# 4 - Built-in python functions