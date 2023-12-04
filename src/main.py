import os
from storage import retrieve_data, store_data

DATA_FILE_NAME = os.path.join(os.path.expanduser('~'), ".tkmeddata")


def main():
    data = retrieve_data(DATA_FILE_NAME)
    data["test"] = ["test1", "test2"];
    store_data(DATA_FILE_NAME, data)
    print(data)
    pass

if __name__ == '__main__':
    main()
