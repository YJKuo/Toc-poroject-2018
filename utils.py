import requests
import os

GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']


def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response



def send_image_url(id, img_url):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {  
            "attachment":{
                "type":"image",
                "payload":{
                    "url":img_url
                }
            }
       }
            
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send image ")
    return response

def send_button_message(id, text, buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {  
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":text,
                    "buttons":buttons
                }
            }
        }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send buttons ")
    return response
    
def send_normal_message(id,title,subtitle,img_url,buttons):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
       "recipient": {"id": id},
       "message":{
           "attachment":{
               "type":"template",
               "payload":{
                   "template_type":"generic",
                   "elements":[                   
                       {
                       "title":title,
                       "image_url":img_url,
                       "subtitle":subtitle,
                       "buttons": buttons    
                       }
                   ]
               }
           }
       }
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send normal message")
    return response
        
