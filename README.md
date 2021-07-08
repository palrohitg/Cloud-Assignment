## Cloud Assigment | Zenatix Solution

Python program to read system stats from local machine ( CPU%, Memory%, …), per process(pid) and store them in Elasticsearch database, visualize with kibana. 


### Pre-Requisites

- Python 
- Docker
- Docker-compose 


### Local Setup 

- Navigate to the ```CLOUD-ASSINGMENT DIR```. 


- Run below cmd to build docker-container. 
```
$ docker-compose up -d
```

- Verify, Container are up and running. 
```
docker-compose ps
```

![docker_compose](https://user-images.githubusercontent.com/40069230/124857850-a1732d80-dfca-11eb-9a9e-bfc37269e1a6.png)

- Visit ```http://localhost:5601/```

- Run ```python src/app.py``` to generate the csv file 
  
- Import the csv file to elasticsearcg/kibana for further analysis. 

![cpu_memory_gauge](https://user-images.githubusercontent.com/40069230/124858371-89e87480-dfcb-11eb-8bd6-ae650fb357ad.png)

### Thanks  

[Vikas Pal](https://github.com/palrohitg)