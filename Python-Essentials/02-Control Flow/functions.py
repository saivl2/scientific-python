# Parameters
def say_hello(name = 'Unknown', emoji = '--'):
    print(f'helloooo {name} {emoji}')

# Arguments
say_hello('Jamey', ':)')
say_hello('Bobby', ':(')
# Keyword arguments
say_hello(name = 'Bebe' , emoji = '^^')

say_hello(name = 'Charlie')
