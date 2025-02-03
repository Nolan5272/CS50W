def announce(f):
    def wrapper():
        print("about to run function")
        f()
        print("done running function")
    return wrapper

@announce
def hello():
    print("Hello world")

hello()