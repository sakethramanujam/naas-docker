import os

import docker

client = docker.from_env()

def container_id(container_name):
    container = client.containers.get(container_name)
    return container.id



def start_container(user,volume,port,mode):
    os.system("docker run --name {} -v {}:/home/jovyan -p {}:8888 {} jupyter/base-notebook".format(user,volume,port,mode))
    id = container_id(user)
    return id
