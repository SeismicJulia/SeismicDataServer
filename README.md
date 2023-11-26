# SeismicJulia Data Server

### Recommended: 
Run a venv before installing requirements from requirements.txt. Especially since some of the requirements
in requirements.txt might not be needed. I'll have to filter them out later once the website is ready.
For now leave I'll leave them as is, just so I can get this code uploaded ASAP.

### Nginx Web Server Set Up (must be sudo)
Install Nginx if you don't already have it installed:
``` sh
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install nginx
```

Copy the config file to the 'sites-available' directory:
``` sh
$ sudo cp /PATH/TO/REPO/config/nginx_conf /etc/nginx/sites-available/SeismicDataServer
```

Create a symbolic link to the 'sites-enabled' directory:
``` sh
$ sudo ln -s /etc/nginx/sites-available/SeismicDataServer /etc/nginx/sites-enabled
```

Create a directory called 'access_control', cd into it, and create '.admin' and '.private' password files:
``` sh
$ sudo mkdir /etc/nginx/access_control && cd /etc/nginx/access_control
$ touch .admin .private
```

You can now use the 'manage_users.sh' script to add admin/private users to the password files. The current
version of the script does NOT add users to any sftp groups.
``` sh
$ ./manage_users.sh
```

