calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


count_calls()


def string_info(x):
    print((len(x), x.upper(), x.lower()))


string_info('Capybara')
string_info('Armageddon')
count_calls()


def is_contains(a, b):
    a = a.lower()
    b = [x.lower() for x in b]
    if a in b:
        print(True)
    else:
        print(False)


is_contains('UrbaN', ['ban', 'BaNaN', 'Urban', 'ur'])
is_contains('Cycle', ['recycling', 'cyclic'])
count_calls()

count_calls()
print(calls)
