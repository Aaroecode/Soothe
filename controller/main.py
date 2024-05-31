from flask import Flask, Response, request
from utility import predictor
from utility import whatsapp
import requests, os, json



app = Flask(__name__)

def send_wa(message):
    header = {"Authorization": "Bearer YourTokenHere",
    "Content-Type": "application/json"}
    payload = json.dumps(message)

    resp = requests.request(method="POST", url= "https://graph.facebook.com/v18.0/260478600487118/messages", headers=header, data=payload)
    print(resp.text)



@app.route("/api/", methods = ["POST"])

def index():
    request = request.json
    csvsave = ""

    for questions in request:
        csvsave += "," + request[questions]
    
    csvsave = csvsave[1:]
    csvfile = os.path.join(os.getcwd(), "Darten", "Database", "data.csv")
    with open(csvfile, "a") as f:
        f.write(csvfile)





text_temp = {
      "messaging_product": "whatsapp",
      "recipient_type": "individual",
      "to": "PHONE_NUMBER",
      "type": "text",
      "text": { 
        "preview_url": 'false',
        "body": "MESSAGE_CONTENT"
        }
    }


button_temp = {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "918920916103",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "body": {
      "text": "Hello"
    },
    "action": {
      "buttons": [
        {
          "type": "reply",
          "reply": {
            "id": "UNIQUE_BUTTON_ID_1",
            "title": "Yes"
          }
        },
        {
          "type": "reply",
          "reply": {
            "id": "UNIQUE_BUTTON_ID_2",
            "title": "No"
          }
        }
      ]
    }
  }
}

start_button  = {
  "messaging_product": "whatsapp",
  "recipient_type": "individual",
  "to": "918920916103",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "body": {
      "text": "Hello"
    },
    "action": {
      "buttons": [
        {
          "type": "reply",
          "reply": {
            "id": "start",
            "title": "Start"
          }
        }
      ]
    }
  }
}

questions = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself - or that you are a failure or have let yourself or your family down",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed",
    "Thoughts that you would be better off dead, or of hurting yourself",
    "If you checked off any problems, how difficult have these problems made it for you at work, home, or with other people",
    #------------------------------------------PTSD-------------------------------------------------------------------------------
    "Have you ever been in a serious accident or fire",
    "Have you ever been in sexual assault or abuse"
    "Have you ever been in an earthquake or flood",
    "Have you ever been in a war",
    "Have you ever seen someone be killed or seriously injured",
    "having a loved one die through homicide or suicide.",
    "In the past month, have you had nightmares about the event(s) or thought about the event(s) when you did not want to?",
    "In the past month, have you tried hard not to think about the event(s) or went out of your way to avoid situations that reminded you of the event(s)?",
    "In the past month, have you been constantly on guard, watchful, or easily startled?",
    "In the past month, have you felt numb or detached from people, activities, or your surroundings?",
    #--------------------------------Anxiety----------------------------------------------------------------------------------------------------------------------------------
    "Feeling nervous, anxious, or on edge",
    "Not being able to stop or control worrying",
    "Worrying too much about different things",
    "Trouble relaxing",
    "Being so restless that it is hard to sit still",
    "Becoming easily annoyed or irritable",
    "Feeling afraid, as if something awful might happen",
    "You Sleep well on most ngihts",
    "You look forward to upcoming events or commitments",
    "You enjoy leaving your comfort zone and trying new things",
    #----------------------------------------OCD--------------------------
    "I have saved up so many things that they get in the way.",
    "I check things more often than necessary.",
    "I get upset if objects are not arranged properly.",
    "I find it difficult to touch an object when I know it has been touched by strangers or certain people."
    "I find it difficult to control my own thoughts.",
    "I collect things I don’t need.",
    "I repeatedly check doors, windows, drawers, etc.",
    "I get upset if others change the way I have arranged things.",
    "I feel I have to repeat certain numbers.",
    "Do you find that your obsessions and compulsions revolve around specific themes, such as cleanliness, symmetry, or harm avoidance?",
    #---------------------------BIPOLAR--------------------------------------------
    "Has there ever been a period of time when you were not your usual self and... You felt so good or hyper that other people thought you were not your normal self or were so hyper that you got into trouble?",
    "You were so irritable that you shouted at people or started fights or arguments?",
    "You felt much more self-confident than usual?",
    "You got much less sleep than usual and found you didn’t really miss it?",
    "You were much more talkative or spoke much faster than usual?",
    "Thoughts raced through your head or you couldn’t slow your mind down?",
    "You were so easily distracted by things around you that you had trouble concentrating or staying on track?",
    "You had much more energy than usual?",
    "You were much more social or outgoing than usual, for example, you telephoned friends in the middle of the night?",
    "You did things that were unusual for you or that other people might have thought were excessive, foolish, or risky?"
    ]






collected = []

@app.route("/wa", methods = ["POST", "GET"])
def indexs():
    try:
        if request.method == "POST":
            taleki = request.json
            print(taleki)
            if "text" in taleki['entry'][0]['changes'][0]['value']['messages'][0]:
                message = start_button
                #message["interactive"]["body"]["text"] = "Lets start test"
                #message["interactive"]["action"]["buttons"] = {"type": "reply","reply": {"id": "start","title": "START!"}}
            try:
                if "id" in taleki['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['button_reply']:
                    if taleki['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['button_reply']['id'] == 'start':
                        index = 0
                    else:
                        index = taleki['entry'][0]['changes'][0]['value']['messages'][0]['interactive']['button_reply']['id']
                        index, response = index.split("#")
                        with open(os.path.join(os.getcwd(), "Database", "answers.json"), "r") as f:
                          collected = json.load(f)
                        
                        collected["hi"].append(response)
                        with open(os.path.join(os.getcwd(), "Database", "answers.json"), "w") as f:
                          json.dump(collected, f, indent=4)
                        index = int(index)
                        index += 1
                    if int(index) < len(questions):
                        message = button_temp
                        print("-"*50)
                        print(message)
                        message["interactive"]["body"]["text"] = questions[index]
                        print("-"*50)
                        print(message)
                        message["interactive"]["action"]["buttons"][0]["reply"]["id"] = str(index) + "#" + "1"
                        message["interactive"]["action"]["buttons"][1]["reply"]["id"] = str(index) + "#" + "0"
                        print("-"*50)
                        print(message)
                    else:
                        disorder = predictor.predicted_disorder(collected)
                        collected = []
                        message = start_button
                        message["interactive"]["body"]["text"] = "You have "+ disorder
                        message["interactive"]["action"]["buttons"][0]["reply"]["id"] = "None"
                        message["interactive"]["action"]["buttons"][0]["reply"]["title"] = "Finish"
            except Exception as err:
                print(err)



            print(message)
            send_wa(message)
            return Response(status=200)
    except Exception as err:
        print(err)
        return Response(status=200)







