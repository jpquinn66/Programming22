from importlib import machinery


print ('What is your name?')
name = input()

print ('what age are you?')
age = input()
age=int(age)

if name == 'Alice':
    print('Hi Alice')
elif age <12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead immortal vampire')
elif age >100:
    print('You are not Alice, grannie')
