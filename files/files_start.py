import os

def main():

    if os.path.exists("text.txt"):
        os.remove("text.txt")

    f = open("text.txt", "w+")

# write some lines of data to the file
    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")
    
    # close the file when done
    f.close()

    f = open("text.txt", "r")

    if f.mode == "r":
        contexts = f.read()
        print(contexts)

    f.close()

    f = open("text.txt", "a")

    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")
    
    # close the file when done
    f.close()

    f = open("text.txt", "r")

    if f.mode == "r":
        # contexts = f.read()
        lf = f.readlines()
        for x in lf:
            print(lf)
        # print(contexts)

    f.close()

if __name__ == "__main__":
    main()