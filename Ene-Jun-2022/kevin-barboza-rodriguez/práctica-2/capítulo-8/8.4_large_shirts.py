def make_shirt(text="I love python", size ="large"):
    print(f"shirt size: {size}, with text printed on it: {text}")

#shirt with arguments by default
make_shirt()
#shirt with default message
make_shirt(size="medium")
#shirt with differents arguments
make_shirt(text="team python", size="small")