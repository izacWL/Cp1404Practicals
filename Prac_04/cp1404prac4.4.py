def main ():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    nameinput = str(input("Please enter username"))
    if nameinput in usernames :
        print("Access granted")
    else:
        print("Access Denied")


main()