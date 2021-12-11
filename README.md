## Kong Project (kongproj)
#### Requirements
1. REST API with a single endpoint running on FastAPI
2. REST API should be served via Kong-OSS
	- Authentication with JWT
	- Rate Limited
3. Konga Frontend for Kong-OSS

#### Deliverables
1. Working installation
2. Documentation

### Documentation
![enter image description here](https://imgur.com/scjoZMQ.png)

### docker-compose.yml
The docker-compose.yml file will add the following services:
1. Kong-OSS
2. FastAPI
3. MySQL
4. PostgreSQL

- Run `sudo docker-compose up` to build and run the services
- FastAPI will be available on `127.0.0.1:9090` . Send a request using httpie or curl `http '127.0.0.1:9090/reports?fname=สุภารัตน์'`

### Install and Configure Konga
Konga's docker image is outdated and wont run without fatal errors. The solution is build Konga from source and run it in a LXC container.

##### Check your LXC installation.
Ubuntu distros already have LXC installed. To confirm run `sudo lxc --version` the current version on Ubuntu 20.04 LTS is *4.0.8*.
##### Pull Ubuntu 20.04 image and start
- Run `sudo lxc image list images:ubuntu | grep focal | grep container`
- Copy the hash for the 64bit container. Make sure you are not selecting a cloud or desktop container.
![enter image description here](https://imgur.com/SQypgUE.png)
- Run `sudo lxc launch images:<focal-fossa-hash> konga`
- From the image the correct hash is *f6734866c479*. To start a LXC container the command becomes `sudo lxc launch images:f6734866c479 konga`

##### Build and run Konga
[Konga on Github](https://github.com/pantsel/konga)
Checklist 

 - [ ] Install PostgreSQL
 - [ ] Install NPM, Node 12, bower, gulp
 - [ ] Clone Konga repo
