from firebase import firebase  
from image_encoding import decode
import time

image_path = 'man20.jpg'



def firebaseSend(image_path, name):
    mydata = decode(image_path)
    localtime = time.asctime( time.localtime(time.time()) )
    firebase = firebase.FirebaseApplication('https://door-opener-a3c06-default-rtdb.firebaseio.com/', None)  
    data =  { 
              'name': name,  
              'timestamp' : localtime,
              'data' : mydata
            }  
    result = firebase.post('door-opener-a3c06-default-rtdb/Images/',data)  
    print(result)

