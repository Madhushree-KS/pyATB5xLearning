# match variable:
#   case pattern 1
#       code block
#   case pattern 2
#       code block


# write a program to ask a user which browser he wants to run a automation

browser_name = input("enter browser name\n")
match browser_name:
    case "firefox":
        print("Starting firefox!....")
    case "chrome":
        print("Starting chrome!....")
    case "edge":
        print("Starting edge!....")
    case "safari":
        print("Starting safari!....")
    case _: #default
        print("browser not found!...")
