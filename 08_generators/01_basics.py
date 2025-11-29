def serve_chai():
    yield "cup 1 : masala chai"
    yield "cup 2 : kesar chai"
    yield "cup 3 : elaichi chai"

stall = serve_chai()

for cup in stall:
    print(cup)

def get_chai_list():
    return ["cup 1", "cup 2", "cup 3"]

#generator functions

def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = get_chai_gen()
print(chai)
print(next(chai))
print(next(chai))
print(next(chai))
#print(next(chai)) #gives error