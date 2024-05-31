from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Sample dataset of questions and corresponding mental health conditions
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
    
    

# Corresponding labels (mental health conditions)
labels = [
    "Mild Depression",
    "Severe Depression",
    "Mild Post Traumatic Stress Disorder (PTSD)",
    "Severe Post Traumatic Stress Disorder (PTSD)",
    "Mild Generalized Anxiety Disorder (GAD)",
    "Severe Generalized Anxiety Disorder (GAD)",
    "Mild Obssesive Compulsive Disorder (OCD)",
    "Severe Obssesive Compulsive Disorder (OCD)",
    "Mild Bipolar Disorder",
    "Severe Bipolar Disorder",
    "Normal"
    # Add more labels here...
]

# Encoding labels
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Sample responses (0 for No, 1 for Yes)
responses = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],  
    
]

# Converting responses to numpy array
X = np.array(responses)
y = np.array(encoded_labels)

# Creating and training decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Function to predict mental health condition based on user responses
def predict_mental_disorder(user_responses):
    # Convert user responses to numpy array
    user_responses_array = np.array([user_responses])
    # Predict the label
    predicted_label = clf.predict(user_responses_array)
    # Decode predicted label
    predicted_mental_disorder = label_encoder.inverse_transform(predicted_label)
    return predicted_mental_disorder[0]

# Example usage
user_responses = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]  # Example user responses
predicted_disorder = predict_mental_disorder(user_responses)
print("Predicted mental disorder:", predicted_disorder)
