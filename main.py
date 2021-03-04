# Import the required module 
import pyttsx3 
  
# Create a string 
string = "In our next video we will se AUC and R O C score to adjust Precision and Recall by changing the threshold Value. Subscribe for more Videos."  

  
# Initialize the Pyttsx3 engine 
engine = pyttsx3.init() 
engine.setProperty('rate',150)
engine.setProperty('volume',20)
# Command it to speak the given string 
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.say(string) 
engine.save_to_file(string,'11.mp3')

# Wait until above command is not finished. 
engine.runAndWait() 