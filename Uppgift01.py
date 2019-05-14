
def temp():
    if __name__ == '__main__':
        print("Running as a program:", __name__)
    else:
        print("Running as a module:", __name_)

def num_stuff(x):
    """Adds 5 to the supplied number"""
    return x + 5

if __name__ == '__main__':
    temp()
