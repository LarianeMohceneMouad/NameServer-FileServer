# NameServer-FileServer
Implementing a NameServer-FileServer architecture in Python using Pyro library and sockets 

## Details :

In this project we implemented a File-Server Name-Server architecture, this latter can offer distante service to clients in order to access distante files and operate actions on them.

## How it works (theory):

The Name-Server has the full repository of all files that are located in all of File-Servers.

In order for a client to use these files, it must ask the Name-Server for the file location, this latter can be used to reach out to the correct File-Server by calling a calling a distant method related to the operation that this client want to perform on the distant file. Then the File-Server will receive the client's request, and the client will be able to access to this Distante file.

The file server can be available or unavailable, therefore the name server must be synchronized with the file servers. the file server is available is the normal case, if the file server is unavailable then the name server must tell the clients that it's currently unavailable.

## How it works (technically):

The clients can communicate with the name server using sockets to send requests of the desired files locations and receive replies. 
The file servers can communicate with the name server, updating their state every finite time (in seconds), this latter can be done using sockets.
The file server publish its services as a Pyro Object, where the clients can get this object and use its distante services, therefore we must use Pyro library.

## Our example:
We have :

One name server that already knows the files locations in every file server

Two file servers that offers distant files for clients

Two clients 

## Before we start:
### Install Pyro library:
Pyro doc : https://pyro4.readthedocs.io/en/stable/index.html
#### Linux:
Some Linux distributions offer Pyro4 through their package manager. Make sure you install the correct one for the python version that you are using. It may be more convenient to just pip install it instead in a virtualenv.
#### Anaconda:
Anaconda users can install the Pyro4 package from conda-forge using: conda install -c conda-forge pyro4
#### Pip install:
pip install Pyro4 should do the trick, Pyro4 is available on Pypi : https://pypi.org/project/Pyro4/

#### NOTE: We're using Pyro4 library in this project, but still Pyro5 is also available (recommended)

### Steps:
1- Create several folders, each folder represents a file server and contains files available on it (you'll have to change the path and files names... and adapt it to suit your architecture and files distribution)

2- Start the Pyro's naming server (This is explained in the Pyro's doc) using this cmd command : python -m Pyro4.naming (windows)

  To see the all published Pyro Objects use the cmd command : python -m Pyro4.nsc list
  
3- Start the name server : name server.py

4 - Start the file servers: file server.py and file server 2.py

5 Start clients
 
#### Note: the clients use an UI (tree) to navigate it's local repository of logic distant files and choose one



