import paho.mqtt.client as mqtt
import time
import json, base64, os

def on_message(client, userdata, msg):
    
    '''
    receive images sent by client over MQTT public server
    
    Parameters:
            client: publisher, client connet to the public server
            userdata: user defined data of any type that is passed as the userdata parameter to callbacks
            msg: message sent by the client
            
    Return:
            accept message sent by clients
            save images
    
    '''
    print("Receiving Image ....")
    print(msg.topic)
    msg = msg.payload
    payload = json.loads(msg)
    image_byte = payload['image']
    imageName = payload["Name"]
    
    image = base64.b64decode((image_byte))

    if not os.path.exists('output/'):
        os.makedirs('output/')
    
    with open(f'output/{os.path.basename(imageName)}', 'wb') as f:
        f.write(image)
        
    print("Received !")


mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("Truck")
client.on_message = on_message
time.sleep(300)
client.loop_end()
