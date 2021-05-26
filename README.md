# Python Chatbot using NLTK & Keras

The approach is inspired by this article: https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077.

First, install all the Modules:  
(pip install tensorflow, keras, pickle, nltk) 

# file structure:   
Intents.json – The data file which has predefined patterns and responses.   
train_chatbot.py – In this Python file, we wrote a script to build the model and train our chatbot.   
Words.pkl – This is a pickle file in which we store the words Python object that contains a list of our vocabulary.   
Classes.pkl – The classes pickle file contains the list of categories.   
Chatbot_model.h5 – This is the trained model that contains information about the model and has weights of the neurons.   
Chatgui.py – This is the Python script in which we implemented GUI for our chatbot. Users can easily interact with the bot.   

# Usage
Run   
python train_chatbot.py  
This will train the Model. And then run  
python chatapp.py  

# Customize
You can customize it according to your own use case. Just define a new tag, possible patterns, and possible responses for the chat bot. You have to re-run the training whenever this file (Intents.json) is modified.



