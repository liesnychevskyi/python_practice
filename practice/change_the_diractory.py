import os


def main():
    req_path = input("Enter path to change the working directory: ")
    print("The current working dir is: ", os.getcwd())
    try:
        os.chdir(req_path)
        print("Now your working directory is: ", os.getcwd())
    except FileNotFoundError:
        print("Given path is not a valid path. So can't change the directory")
    except NotADirectoryError:
        print("Given path is a file path. So can't change the directory")
    except PermissionError:
        print("Sorry you don't have a permission to this given path. So can't change working directory")
    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':
    main()
