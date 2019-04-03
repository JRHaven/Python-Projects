import ls
def check(filename):
    directory = ls.list()
    if(any(filename in s for s in directory)):
       return True
    else:
       return False
