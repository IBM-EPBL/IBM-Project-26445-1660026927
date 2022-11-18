import cv2
import time
import numpy as np
import pyzbar.pyzbar as pyzbar
from ibmcloudant.cloudant_v1 import CloudantV1
from ibmcloudant import CouchDbSessionAuthenticator
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-2vji5kegi5d7aaygtccqtt616y5u2yva2mpawe7ps7gp','15bc42554c2a4881a11889247e6ab66e')
                                                                                             
service = CloudantV1(authenticator=authenticator)
print(service)
service.set_service_url('https://apikey-v2-2vji5kegi5d7aaygtccqtt616y5u2yva2mpawe7ps7gp:15bc42554c2a4881a11889247e6ab66e@58980990-cf73-48b6-bbee-db90262aae86-bluemix.cloudantnosqldb.appdomain.cloud')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
    _, frame = cap.read()
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        a=obj.data.decode('UTF-8')
        cv2.putText(frame, "Ticket", (50, 50), font, 2,(255, 0, 0), 3)
        try:
            response = service.get_document(
                  db='booking-table',
                  doc_id = a
                  ).get_result()
            print("Passenger Name\t Ticket Count \t Date \t Train NO")
            print(response["pname"]+"\t \t"+str(response["ticketcount"])+"\t"+response["date"]+"\t"+str(response["trainNumber"]))
            time.sleep(5)
        except Exception as e :
             print(e)
             print("Not a Valid Ticket")
             time.sleep(5)

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
client.disconnect()
