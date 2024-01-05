# Uploading Testing Datasets

I assume that you have the upload_dataset.sh script downloaded on your computer. If not,
you can download it from [here](https://github.com/SeismicJulia/bash_scripts/blob/main/upload_dataset.sh){target="_blank"}.

## Running the Upload Script:
First, make sure the sshpass library is installed.
``` sh
$ sudo apt-get install sshpass
```
Next, make sure the upload_dataset.sh is executable.
``` sh
$ chmod +x upload_dataset.sh
```
Now, we are able to upload testing datasets using the script. To view the format
it expects, run the script without any arguments (or with the -h argument).
```
$ ./upload_dataset.sh
Usage: ./upload_dataset.sh [-u username [-p password]] [-D description_file] dataset_file

    -u username: your username to access the sftp server.
    -p password: the password associated with your username for accessing the 
                 sftp server. This argument will have no effect if no username
                 is provided.
    -d directory: "Testing" by default. Can be either "Public", "Private", or 
                  "Testing". You must have sudo access to upload to "Public" or
                  "Private".
    -D description_file: a path to a text file containing a brief description 
                         of the dataset.
```

## Examples:
### Uploading a dataset
To upload a testing dataset called tdf.su, you can run the command below, and enter your username and password
when prompted:
``` sh
$ ./upload_dataset.sh tdf.su
Username: YOUR_USERNAME
Password: 
```
You can also provide your username as an argument:
``` sh
$ ./upload_dataset.sh -u YOUR_USERNAME tdf.su
Password: 
```

### Uploading a dataset with a description
You might want to upload a dataset and add a short description to it. To do that,
create a new file containing the dataset description and run the command below. In this
case, the description file is called tdf_desc.txt.
``` sh
$ ./upload_dataset.sh -D tdf_desc.txt tdf.su
```
Again, you will be asked for your username and password.

### Uploading a dataset non-interactively
???+ danger "Warning"
    ```
    Be careful when using the -p flag. Your password will be stored in the history of the shell, and can 
    possibly be seen by other people if you use this script on a shared machine.
    ```
If you want, you can provide your username and password as command line arguments.
``` sh
$ ./upload_dataset.sh -u YOUR_USERNAME -p YOUR_PASSWORD -D tdf_desc.txt tdf.su
```
Note, that if you provide your password as a command line argument without providing your username, 
then it will just be ignored and you will be asked to enter both your username and password.

### Uploading Public and Private Datasets
If you have sudo access to the file server, you can also upload Public and Private datasets. To 
upload a public dataset, run the same commands as above except with "-d Public" included as a flag.
Here is an example:
``` sh
$ ./upload_dataset.sh -u YOUR_USERNAME -d Public -D tdf_desc.txt tdf.su
```
Note that if you do not have sudo access to the file server, the above command will fail.