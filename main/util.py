import os, hashlib
from datetime import datetime

def compute_checksum(filepath: str, algorithm:str) -> str:
    '''
    This function computes the checksum of a file using any algorithm supported by hashlib.
    For a list of such algorithms, see the hashlib documentation.
    - Parameters:
        * filepath - the path of the file
        * algorithm - the algorithm we want to use
    - Returns:
        * The computed checksum (in hexadecimal) as a string
    '''
    checksum = hashlib.new(algorithm)
    buffer_size = 2**16  # 64 KB

    with open(filepath, "rb") as f:
        data = f.read(buffer_size)
        while data:
            checksum.update(data)
            data = f.read(buffer_size)

    return checksum.hexdigest()

def verify_checksum(filepath: str, checksum:str) -> bool:
    '''
    This function takes in a recently computed checksum of a file, and compares it with the checksum
    we have stored on disk, in a file called .{FILENAME}.checksum if it exists. If it doesn't exist,
    the file is created using the checksum recently computed.
    - Parameters: 
      * filepath: the path of the file
      * checksum: the computed checksum
    - Returns:
      * True if the checksums match, or if the checksum file does not exists, False otherwise
    '''
    dir_name, file_name = filepath.rsplit("/", 1)
    checksum_filepath = f"{dir_name}/.{file_name}.checksum"
    current_time = datetime.now()

    # If checksum file does not exist, create it and return True.
    # This will happen if a file was just uploaded.
    if not os.path.exists(checksum_filepath):
        with open(checksum_filepath, "w") as cf:
            cf.write(f"{checksum} | {file_name} | {current_time}")
        return True
    
    # If we do find a checksum file, compare past and current checksum.
    # If there is a difference, this means the file got corrupted between
    # now and the timestamp on the file
    with open(checksum_filepath, "r") as cf:
        # _ here is the filename read from the checksum file. It is not
        # important because we assume it is equal to the filename variable
        prev_checksum, _, prev_time = cf.read().strip().split(" | ")

    if prev_checksum != checksum:
        ## Notify someone somehow
        return False
    
    # If checksums equal, write 
    with open(checksum_filepath, "w") as cf:
        cf.write(f"{checksum} | {file_name} | {current_time}")

    return True

def human_readable_file_size(filepath:str) -> str:
    '''
    This function gets the size of a file and returns it in a human readable format.
    - Parameters:
        * filepath: the path of the file
    - Returns:
        * The size in a human readable format
    '''
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size_in_bytes = os.stat(filepath).st_size
    
    unit_index = 0
    squashed_size = size_in_bytes
    while unit_index < len(units) - 1 and squashed_size > 1000:
        squashed_size //= 1000
        unit_index += 1
    return f"{squashed_size} {units[unit_index]}"

def get_file_description(filepath:str) -> str:
    '''
    This function gets the description of a dataset file. This description is assumed to be stored
    in a file called .{FILENAME}.description, present at the same path where the file is present.
    - Parameters:
        * filepath: the path of the file
    - Returns:
        * the description of the file if it exists, "N/A" otherwise
    '''
    dir_name, file_name = filepath.rsplit("/", 1)
    description_filepath = f"{dir_name}/.{file_name}.description"

    # If description file does not exist, return "N/A"
    description = "N/A"

    if os.path.exists(description_filepath):
        # If we do find a description file, return its contents
        with open(description_filepath, "r") as df:
            # Replace newline characters with "<br/>" so there is no problem with markdown formatting
            description = df.read().replace('\n', '<br/>')

    return description