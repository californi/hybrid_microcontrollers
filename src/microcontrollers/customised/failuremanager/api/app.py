from fastapi import FastAPI, Request, Response
import httpx
import asyncio
from kubernetes import client, config, watch


app = FastAPI()
config.load_incluster_config()
#config.load_kube_config()
#apps_v1 = client.AppsV1Api()
v1 = client.CoreV1Api()

## TODO: retirar ENDPOINT e colocar pra executar diretamente (alterar dockerfile tambem)

def main():

    w = watch.Watch()

    for event in w.stream(v1.list_event_for_all_namespaces):
        if event['object'].type == "Warning":
            print("Name: %s -- Type Event: %s -- Message: %s -- Datetime: %s" % (
                event['object'].metadata.name,
                event['object'].type,
                event['object'].message,            
                event['object'].metadata.creation_timestamp
        ))
        #count -= 1
        #if not count:
        #    w.stop()
    print("Finished pod stream.")


if __name__ == '__main__':
    main()    