from consoleLoginMongoDB import singIn, logIn


print("1-Log in")
print("2-Sing in")

entry = input()
go = False
match entry:
    case "1":
        logIn()
    case "2":
        singIn()
    case _:
        go = True

while go:
    go = False
    print("Invalid option !!!\n")
    print("1-Log in")
    print("2-Sign in")

    entry = input()
    go = False
    match entry:
        case "1":
            logIn()
        case "2":
            singIn()
        case _:
            go = True
