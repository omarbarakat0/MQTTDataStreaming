import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import json
import base64
import os

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)


def publisch(image_dir='Images/'):
    
    '''
    
    Publish images as json_serialize through mqqt public server
    
    Parameters:
            images_dir: directory of images 
            
    Return:
            serilaze images in json file
            send images over MQTT broker
    
    '''



    # Extract all image files in the directory
    Files = os.listdir(image_dir)
    Files = [os.path.join(image_dir, f) for f in Files if not f.startswith('.')]

    # send images 1-by-1
    for image in Files:
        image_file = image 
        with open(image_file, "rb") as f:
            im_bytes = f.read() 

        # decode image to bits
        im_b64 = base64.b64encode(im_bytes).decode("utf8")
        payload = json.dumps({"image": im_b64, "Name": image_file})
        client.publish("Truck", payload)
        print("Just published ")
    time.sleep(5)
    
    
    
IMAGE_DIR = 'Images/'    
publish(IMAGE_DIR)
