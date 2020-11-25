def two_args(*args):
    arg1, arg2 = args
    print(f"arg1 is {arg1} and arg2 is {len(arg2)} bytes long")

two_args("hello", "all the world")

#or you can type do it this way

def arg_arg(arg1, arg2):
    print(f"arg1 is : {arg1} and arg 2 is : {arg2}.")

arg_arg("another", "way")