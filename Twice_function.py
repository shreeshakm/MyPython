str="Shree"
def print_spam(str):
    print ("shree")

def do_twice(print_spam,arg2):
    print_spam(arg2)
    print_spam(arg2)

do_twice(arg2, str)