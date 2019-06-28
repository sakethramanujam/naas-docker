from docker_helpers import start_container
import os
import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--user",help='name of the user',type=str)
    parser.add_argument('-m',"--mode",nargs='?',help='mode of service',type=str,default='-d')
    parser.add_argument("-p","--port",help="port on which the service should run",type=int)
    args=parser.parse_args()
    return args

def checkuser(user):
    homedir = os.path.join(os.path.expanduser("~"),"Documents")
    user_path  = os.path.join(homedir,user,'notebooks')
    if os.path.exists(user_path):
        pass
    else:
        os.makedirs(user_path)
    return user_path

def main():
    user = args().user
    volume = checkuser(user)
    port = args().port
    mode= args().mode
    container_id = start_container(user=user,volume=volume,port=port,mode=mode)
    print("Service {} running on port: {}".format(container_id,port))


if __name__=='__main__':
    main()