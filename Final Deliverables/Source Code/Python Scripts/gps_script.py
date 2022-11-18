import wiotp.sdk.device
import time
import random

myConfig = {
    "identity": {
        "orgId": "kapgrv",
        "typeId": "ibm-iot",
        "deviceId": "10",
    },
    "auth": {
        "token": "12345678"
    }
    
}

train_detial = {12632: [[13.067439,80.237617],
                      [8.735640, 77.708161],
                      [8.738075, 77.708259],
                      [8.741219, 77.708476],
                      [8.743633, 77.708743],
                      [8.746420, 77.708911],
                      [8.748563, 77.709001],
                      [8.750921, 77.709120],
                      [8.753201, 77.709243],
                      [8.755357, 77.709329],
                      [8.757710, 77.709419],
                      [8.760355, 77.709870],
                      [8.762889, 77.710737],
                      [8.764104, 77.711175],
                      [8.765409, 77.711589],
                      [8.766494, 77.711936],
                      [8.767979, 77.712454],
                      [8.769694, 77.713414],
                      [8.770419, 77.713885],
                      [8.771009, 77.714328],
                      [8.773284, 77.716484],
                      [8.774433, 77.717908],
                      [8.776211, 77.720094],
                      [8.777619, 77.721823],
                      [8.779270, 77.723824],
                      [8.781513, 77.726591],
                      [8.783392, 77.728780],
                      [8.783897, 77.729422],
                      [8.784331, 77.729961]
                      ], 12765: [12.972442,77.580643], 14375: [9.939093,78.121719]}

def myCommandCallback(cmd):
    print("" % cmd.data['command'])
    m=cmd.data['command']

def getDetials(trainNo):
    return train_detial[trainNo]
    
def getTemperature():
    return random.randint(0,50)

def pub(data):
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data successfully: %s",myData)

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

trainNo = int(input("Enter TrainNo:"))
trainData=getDetials(trainNo)
lat=trainData[0]
lon=trainData[1]

while True:
    for val in trainData:
        myData={'trainNo':trainNo,'lat':round(val[0],7),'long':round(val[1],7),'engine_temp':getTemperature()}
        pub(myData)
        time.sleep(3)
        client.commandCallback = myCommandCallback
client.disconnect()
