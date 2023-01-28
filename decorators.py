def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Done with the function.")
        #return 3
    return wrapper

#@announce
def hello():
    print("Hello, world!")
    #return 2

hello = announce(hello)

hello()

#print(hello())


