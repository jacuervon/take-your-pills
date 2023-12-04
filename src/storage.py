import os
import platform
import json

def retrieve_data(file_path: str) -> dict:
    """
    Retrieve data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data retrieved from the JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If there is an error decoding the JSON data.

    """
    if not os.path.exists(file_path):
        store_data({}, True)
        return retrieve_data()
    try:
        with open(file_path, 'r+') as archivo_json:
            return json.load(archivo_json)
    except json.JSONDecodeError as e:
        print("Error: ", e)
        store_data({}, True)
        return retrieve_data()


def store_data(file_path: str, data: dict, force=False) -> None:
    """
    Store data in a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (dict): The data to be stored in the file.
        force (bool, optional): If True, overwrite the file even if it already exists. Defaults to False.

    Raises:
        Exception: If there is an error while writing to the file.

    """
    if not os.path.exists(file_path) or force:
        try:
            with open(file_path, 'w') as file_json:
                file_json.seek(0)
                file_json.truncate()
                json.dump(data, file_json, indent=4)
        except Exception as e:
            print("Error: ", e)
    else:
        try:
            with open(file_path, 'r+') as file_json:
                if platform.system() == "Windows":
                    import msvcrt
                    msvcrt.locking(file_json.fileno(), msvcrt.LK_LOCK, 0)
                else:
                    import fcntl
                    fcntl.flock(file_json, fcntl.LOCK_EX)

                json.dump(data, file_json, indent=4)

                if platform.system() == "Windows":
                    msvcrt.locking(file_json.fileno(), msvcrt.LK_UNLCK , 0)
                else:
                    fcntl.flock(file_json, fcntl.LOCK_UN)
        except Exception as e:
            print("Error: ", e)

if __name__ == "__main__":
    exit(1)