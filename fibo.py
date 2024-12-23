def is_talking_about_marry(post):
    return "marry" in post.lower()

def main():
 
    post = input("Enter a post: ")

    if is_talking_about_marry(post):
        print("The post is talking about 'marry'.")
    else:
        print("The post is not talking about 'marry'.")

if __name__ == "__main__":
    main()