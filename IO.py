# def check_username_length(username):
#  if len(username) < 10:
#       return "the username has less than 10 characters."
#  else:
#       return "the username has 10 or more characters."
#  user_input = input("enter a username:")
#  result=check_username_length(user_input)
#  print (result)

def is_username_short(username):
    return len(username) < 10

def main():
    user_input = input("Enter a username: ")
    if is_username_short(user_input):
        print(f"The username '{user_input}' has fewer than 10 characters.")
    else:
        print(f"The username '{user_input}' has 10 or more characters.")

if __name__ == "__main__":
    main()



