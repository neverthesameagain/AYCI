removals=['if', 'do', 'few', "it's", "shouldn't", 'myself', 'its', 'has', 'with', 'been', 'can', 'won', "you'll", 'below', "weren't", 'into', 'him', 'this', 'above', 'our', "needn't", 'here', 'i', 'me', 'all', 're', "won't", 'don', 'should', 'such', 'or', 'for', "couldn't", 'what', "should've", 'does', 'hers', 'other', "that'll", "doesn't", "wasn't", 'once', 'while', 'between', 'mightn', "hasn't", 'too', 'up', 'before', 'their', 'himself', 'it', "you'd", 'some', 'themselves', 'ain', 'an', 'ours', 'at', 'haven', 'about', 'just', 'shouldn', 'o', 'both', 'out', "isn't", 'll', 'ma' , "haven't", 'only', 'hadn', 'those', 'they', 'against', 'down', 'over', 't', 'she', 'again', 'why', 'did', 'wouldn', 'a', 'when', 'your', 'ourselves',  'having', 'on', 'y', 'theirs', 'being', 'herself', 'nor', 'that', 'by', "don't", "mustn't", "shan't", 'because', 'not', 'under', 'he', 'own', "you've", 'there', 'yours', 'and', 'most', "mightn't", 'have', 'doing', 'during', 'couldn', "didn't", 'will', 'weren', 'd', 'were', "she's", "wouldn't", 'isn', 'then', 'doesn', 'wasn', 'itself', 'now', 'didn', 'these', 'them', 'needn', 'yourself', 'shan', 'is', 'more', 'be', "you're", 'than', 'after', 'aren', 'where', 'which', 'in', "hadn't", 'further', 'no', 'yourselves', 'as', 'whom', 'to', 'hasn', 'mustn', 'through', 'the', 'm', 's', 'very', 'we', 'each', 'until', 'same', "aren't", 'was', 'my', 'so', 'from', 've', 'am', 'had', 'his', 'but', 'off', 'any', 'of', 'her']
def clean(s):
    return [word for word in s.split() if word.lower() not in removals]

positive=[
    "happy",
    "great",
    "love",
    "amazing",
    "excellent",
    "wonderful",
    "awesome",
    "fantastic",
    "delightful",
    "pleasure",
    "joy",
    "enjoy",
    "beautiful",
    "good",
    "nice",
    "lovely",
    "superb",
    "exciting",
    "perfect",
    "uplifting"
]
negative=[
    "sad",
    "bad",
    "disappointed",
    "terrible",
    "horrible",
    "awful",
    "angry",
    "upset",
    "frustrated",
    "dislike",
    "hate",
    "regret",
    "unhappy",
    "annoyed",
    "worst",
    "miserable",
    "depressing",
    "painful",
    "broken",
    "fail"
]
neutral=[
    "okay",
    "neutral",
    "indifferent",
    "average",
    "common",
    "standard",
    "typical",
    "ordinary",
    "regular",
    "balanced",
    "unbiased",
    "impartial",
    "objective",
    "neutralize",
    "neutrality",
    "neutrally",
    "disinterested",
    "nonchalant",
    "passive",
    "undecided"
]
inputtexti="I am Happy and  sad"
inputtext=inputtexti.lower().split()
 
def check(inputtexti):
    for positives in positive:
        if positives in inputtext:
            reactpositive()
        for negatives in negative:
            if negatives in inputtext:
                reactnegative()    
            for neutrals in neutral:
                if neutrals in inputtext:
                    reactneutral()
                if ((neutrals in inputtext) and (positives in inputtext))or((neutrals in inputtext) and (negatives in inputtext)) or((negatives in inputtext) and (positives in inputtext)) or((negatives in inputtext) and (positives in inputtext) and (neutrals in inputtext)):
                    return "See, i sense some mixed kindof feelings which I don't yet know how to analyze, It will be a tough time for me to comment on this, but meanwhile how about talking on something else?"
#print(check(inputtexti))
import re




def stemming(word):
    if word[(len(word)-1)]=='s':
        stems=[word[:len(word)-1],word[:len(word)-1]+'ed',word[:len(word)-1]+'ing',word]
    if word[(len(word)-2):]=='ed':
        stems=[word[:len(word)-2],word[:len(word)-2]+'s',word[:len(word)-2]+'ing',word]
    if word[(len(word)-3):]=='ing':
        stems=[word[:len(word)-3]+'s',word[:len(word)-3]+'ed',word[:len(word)-3],word]
    else:
        stems=[word[:len(word)]+'s',word[:len(word)]+'ed',word[:len(word)]+'ing',word]
    return stems
 
import tkinter
import tkinter.messagebox
import customtkinter
import os
import webbrowser
import subprocess
import random
from gtts import gTTS
from playsound import playsound


import re

def stemming(word):
    if word[(len(word)-1)]=='s':
        stems=[word[:len(word)-1],word[:len(word)-1]+'ed',word[:len(word)-1]+'ing',word]
    if word[(len(word)-2):]=='ed':
        stems=[word[:len(word)-2],word[:len(word)-2]+'s',word[:len(word)-2]+'ing',word]
    if word[(len(word)-3):]=='ing':
        stems=[word[:len(word)-3]+'s',word[:len(word)-3]+'ed',word[:len(word)-3],word]
    else:
        stems=[word[:len(word)]+'s',word[:len(word)]+'ed',word[:len(word)]+'ing',word]
    return stems


#customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"

#customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

   
    def __init__(self, bg_color='#ff0000', **kwargs):
        super().__init__( **kwargs)
        self.configure(bg=bg_color)
        
        def inpt():
            
            
            switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=self.entry.get())
            switch.grid( column=0, padx=10)
 
            querry=self.entry.get()
            print(querry)
            cleanedquerry=clean(querry.lower())
            print(cleanedquerry)
            text=" ".join(cleanedquerry)
            text = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", text)
            texto=clean(text)
            print(texto)
            texto=" ".join(texto)
            print(texto)
            def reactneutral():
                print("=")
                switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=f"You seem Neutral")
                switch.grid( column=0, padx=10)

            def reactnegative():
                switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=f"You seem sad, something happened?")
                switch.grid( column=0, padx=10)
                print("-") 
            def reactpositive():
                switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=f"Great that you are happy!")
                switch.grid( column=0, padx=10)
                print("+")
            
            #def reactpositive(self):
             #   customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
              #  print("Positive")
                
            for word in texto:
                if word in positive:
                    reactpositive()
                if word in negative:
                    reactnegative()
                if word in neutral:
                    reactneutral()
            def clearBox(self):
                self.entry.delete(0,'end')
            clearBox(self)

 
            def say(text):
                os.system(f"say {text}")
            greet=['hi','hello','namaste','hey','hii','heyllo']

            for greets in greet:
                if greets in texto:
                    o=['Hello !, how may i help you today?', 'hi, how have you been lately?', 'hey, how may i help you today?', 'yo, how have you been lately?', 'hola, how may i help you today?', 'greetings, how have you been lately?', 'salutations, how may i help you today?', 'sup, you know what, I was thinking about you only!', 'howdy, how have you been lately?', 'namaste, how may i help you today?', 'bonjour, you know what, I was thinking about you only!', 'ciao, how have you been lately?', 'hallo, how may i help you today?', 'heya, you know what, I was thinking about you only!', 'aloha, how have you been lately?', 'hi ya, how may i help you today?', 'salaam, you know what, I was thinking about you only!', 'shalom, how have you been lately?', 'oi, how may i help you today?, glad to see ya!', 'wassup, how may i help you today?', 'yoohoo, how have you been lately?', 'hi there, you know what, I was thinking about you only!', 'whats up, how may i help you today?', 'hows it going, how have you been lately?', 'good day', 'top of the morning, how may i help you today?', 'good day it is you showed up, how have you been lately?', 'nice to meet you', 'pleased to meet you, how may i help you today?', 'yoohoo', 'hey there', 'hiya, how may i help you today?', 'gday mate', 'hail', 'hi-de-ho, how may i help you today?', 'how goes it', 'hey hey', 'hi-ya, how may i help you today?', 'hows everything', 'greetings and salutations, how may i help you today?', 'hihi', 'hi-diddly-ho', 'sup dawg, how may i help you today?', 'how do you do', 'howdy-do, how may i help you today?', 'gday matey', 'good morning', 'good afternoon, how may i help you today?', 'good evening', 'good day mate',"Ahoy You surfer!, how may i help you today?, How's Your Day?","How You Doin? :D, how may i help you today?","Namastey! Aaj aapki Sahaaytaa kaisey ki jaaye?","Bonjour, How are you?"]
                    outr=random.choice(o)
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=f"~>>             {outr}")
                    switch.grid( column=0, padx=10)
                    text = outr
                    language = "en"
                    tts = gTTS(text=text, lang=language)
                    audio_file = "output.mp3"
                    tts.save(audio_file)
                    playsound(audio_file)   
                    #say(outr)
                    self.scrollable_frame_switches.append(f" {outr}")
 

            sites=[["you tube","https://www.youtube.com"],["youtube","https://www.youtube.com"],['wiki pedia','https://www.wikipedia.com'],['wikipedia','https://www.wikipedia.com'],['wiki-pedia','https://www.wikipedia.com'],['google','https://google.com'],['facebook', 'https://www.facebook.com'],['twitter', 'https://www.twitter.com'],['instagram', 'https://www.instagram.com'],['linkedin', 'https://www.linkedin.com'], ['reddit', 'https://www.reddit.com'], ['amazon', 'https://www.amazon.com'], ['ebay', 'https://www.ebay.com'], ['netflix', 'https://www.netflix.com'], ['spotify', 'https://www.spotify.com'], ['github', 'https://www.github.com'], ['stackoverflow', 'https://www.stackoverflow.com'], ['yahoo', 'https://www.yahoo.com'], ['bing', 'https://www.bing.com'], ['wikipedia', 'https://www.wikipedia.org'], ['imdb', 'https://www.imdb.com'], ['pinterest', 'https://www.pinterest.com'], ['tumblr', 'https://www.tumblr.com'], ['wordpress', 'https://www.wordpress.com'], ['buzzfeed', 'https://www.buzzfeed.com'], ['cnn', 'https://www.cnn.com'], ['bbc', 'https://www.bbc.co.uk'], ['nytimes', 'https://www.nytimes.com'], ['huffingtonpost', 'https://www.huffpost.com'], ['foxnews', 'https://www.foxnews.com'], ['msn', 'https://www.msn.com'], ['walmart', 'https://www.walmart.com'], ['target', 'https://www.target.com'], ['bestbuy', 'https://www.bestbuy.com'], ['apple', 'https://www.apple.com'], ['microsoft', 'https://www.microsoft.com'], ['nike', 'https://www.nike.com'], ['adidas', 'https://www.adidas.com'], ['craigslist', 'https://www.craigslist.org'], ['etsy', 'https://www.etsy.com'], ['booking', 'https://www.booking.com'], ['expedia', 'https://www.expedia.com'], ['airbnb', 'https://www.airbnb.com'], ['zillow', 'https://www.zillow.com'], ['tripadvisor', 'https://www.tripadvisor.com'], ['uber', 'https://www.uber.com'], ['lyft', 'https://www.lyft.com'], ['doordash', 'https://www.doordash.com'], ['grubhub', 'https://www.grubhub.com'], ['paypal', 'https://www.paypal.com'], ['visa', 'https://www.visa.com'], ['mastercard', 'https://www.mastercard.com'], ['americanexpress', 'https://www.americanexpress.com'], ['bankofamerica', 'https://www.bankofamerica.com'],['mail','https://www.mail.google.com'],['gmail','https://www.mail.google.com']]
            for site in sites:
                if site[0].lower() in texto:
                    siteaction=f"~>>  Opening {site[0]}"
                    webbrowser.open(site[1])
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=siteaction)
                    switch.grid( column=0,row=1, padx=10)
                    text = f"Opening {site[0]}"
                    language = "en"
                    tts = gTTS(text=text, lang=language)
                    audio_file = "output.mp3"
                    tts.save(audio_file)
                    playsound(audio_file) 
                    #say(f"Opening {site[0]}")
            intros=['who are you', 'what is your name', 'tell me about yourself', 'what should I call you', 'who is behind you', 'what do they call you', 'what are you called', 'how can I address you', 'may I know your name', 'what should I know about you', 'whats your name', 'what do you go by', 'who am I speaking to', 'what is your identity', 'what are you known as', 'tell me your name', 'what are you called by', 'what name do you respond to', 'who is this', 'what is your moniker', 'how do you identify yourself', 'what label do you carry', 'what is your appellation', 'what do people call you', 'who goes there', 'what are you referred to as', 'what is your given name', 'tell me your designation', 'what is your title', 'what do you prefer to be called', 'who do you represent', 'what is your nickname', 'what do you call yourself', 'who is on the other side', 'what is your tag', 'what name do you possess', 'how do you introduce yourself', 'what is your cognomen', 'what do you answer to', 'who is chatting with me', 'what is your handle', 'what is your self-identification', 'how do you label yourself', 'what is your identity marker', 'what are you known by', 'who is this Im talking to', 'what do you identify as', 'what are you called upon', 'what do you refer to yourself as', 'who is interacting with me', 'what is your appellative','who am i talking to','who am i chatting with','what are you','what you are']        
            for intro in intros:
                if intro in texto:
                    o=["Ahoy You surfer! Hey There! I am As You Call It ( AYCI ) your personal Bot built by Aryan Mathur\n~To see what I can do, try asking me maybe?\n~To Leave the chat anytime, I won't mind, unlike your long lost crush, I don't have issues in letting people go., How's Your Day?","Hey There! I am As You Call It ( AYCI ) your personal Bot built by Aryan Mathur\n~To see what I can do, try asking me maybe?\n~To Leave the chat anytime, I won't mind, unlike your long lost crush, I don't have issues in letting people go. How You Doin? :D","Bonjour, comment ca Va? Hey There! I am As You Call It ( AYCI ) your personal Bot built by Aryan Mathur\n~To see what I can do, try asking me maybe?\n~To Leave the chat anytime, I won't mind, unlike your long lost crush, I don't have issues in letting people go."]
                    outr=random.choice(o)
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=f"->>             {outr}")
                    switch.grid( column=0, padx=10)
                    text = outr
                    language = "en"
                    tts = gTTS(text=text, lang=language)
                    audio_file = "output.mp3"
                    tts.save(audio_file)
                    playsound(audio_file)
                    #say(outr)
            howdy=['how are you', 'how\'s it going?', 'how\'s everything?', 'how are you doing?', 'how do you feel?', 'how\'s your day?', 'how are things?', 'how have you been?', 'how\'s life?', 'how\'s your day going?', 'how are you today?', 'how\'s your mood?', 'how goes it?', 'how are you holding up?', 'how are you coping?', 'how\'s your health?', 'how\'s your well-being?', 'how are you feeling today?', 'how is everything with you?', 'how\'s your state?', 'how are you managing?', 'how are you faring?', 'how are you dealing with things?', 'how are you handling it?', 'how\'s your situation?', 'how are you keeping?', 'how are you managing?', 'how are you bearing up?', 'how are you taking it?', 'how\'s your spirit?', 'how are you hanging in there?', 'how\'s your energy?', 'how\'s your emotional state?', 'how\'s your mindset?', 'how are you navigating?', 'how are you facing it?', 'how\'s your attitude?', 'how are you weathering it?', 'how\'s your morale?', 'how are you handling the circumstances?', 'how\'s your composure?', 'how are you enduring it?', 'how\'s your disposition?', 'how\'s your outlook?', 'how are you tackling it?', 'how\'s your frame of mind?', 'how are you managing the challenges?', 'how\'s your response?', 'how are you carrying on?']        
            for howdys in howdy:
                if howdys in texto:
                    oi=['I\'m doing well, thank you!', 'I\'m great, thanks for asking!', 'Everything is going smoothly!', 'I\'m feeling fantastic!', 'I\'m doing fine, how about you?', 'I\'m good, how are you?', 'I\'m doing great!', 'I\'m feeling wonderful!', 'I\'m doing excellent!', 'I\'m in a good place!', 'I\'m feeling positive!', 'I\'m having a good day!', 'I\'m feeling awesome!', 'I\'m doing just fine!', 'I\'m happy and ready to assist!', 'I\'m doing splendidly!', 'I\'m feeling top-notch!', 'I\'m doing fantastic!', 'I\'m in a great mood!', 'I\'m feeling really good!', 'I\'m doing superb!', 'I\'m feeling energized!', 'I\'m doing wonderfully well!', 'I\'m in high spirits!', 'I\'m feeling fabulous!', 'I\'m doing incredibly well!', 'I\'m feeling upbeat!', 'I\'m doing marvelous!', 'I\'m feeling fantastic, thank you!', 'I\'m doing exceptionally well!', 'I\'m feeling terrific!', 'I\'m doing wonderfully!', 'I\'m feeling on top of the world!', 'I\'m doing very well!', 'I\'m feeling amazing!', 'I\'m doing remarkably well!', 'I\'m feeling great and ready to help!', 'I\'m doing superbly!', 'I\'m feeling outstanding!', 'I\'m doing phenomenally well!', 'I\'m feeling fantastic, thanks for asking!', 'I\'m doing exceptionally good!', 'I\'m feeling fantastic, how about you?', 'I\'m doing splendid, thank you!', 'I\'m feeling really well!', 'I\'m doing exceptionally fine!', 'I\'m feeling wonderful, thanks for asking!', 'I\'m doing exceptionally great!', 'I\'m feeling fantastic and ready to assist!', 'I\'m doing wonderfully, how about you?', 'I\'m feeling fantastic, how can I assist you?']
                    outro=random.choice(oi)
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=f"->>             {outro}")
                    switch.grid( column=0, padx=10)   
                    text = outro
                    language = "en"
                    tts = gTTS(text=text, lang=language)
                    audio_file = "output.mp3"
                    tts.save(audio_file)
                    playsound(audio_file)    
                    #say(outro)
            quit=['quit','goodbye']
            for quits in quit:
                if quits in texto:
                    siteaction="It was nice chatting with you! Hope to see you sometime soon!"
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=siteaction)
                    say("It was nice chatting with you! Hope to see you sometime soon!")
    
            
                    

            def clearBox(self):
                self.entry.delete(0,'end')
            clearBox(self) 
        
        # configure window
        self.title("Aryan's Mega Messaging App.py")
        self.geometry(f"{1100}x{580}")
    # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="The Chat", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 5))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Chat", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(5, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text='Take me to group chats',command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["System", "Dark", "Light"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["100%", "80%", "90%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250,height=15)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox = customtkinter.CTkTextbox(self, width=25, height= 15)
        self.textbox.insert("0.0", "AYCI\n"+"Your Personal Bot it is! \n\n" + "Hey There! I am As You Call It ( AYCI ) your personal Bot built by Aryan Mathur\n~To see what I can do, try asking me maybe?\n~To Leave the chat anytime, I won't mind, unlike your long lost crush, I don't have issues in letting people go." )
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(10, 0), sticky="nsew")
        self.entry = customtkinter.CTkEntry(self, placeholder_text="How Can I Help You?")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.main_button_1 = customtkinter.CTkButton(master=self,text="Send", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=inpt)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


        

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Important Updates!")
        self.tabview.add("key Features!")
        self.tabview.add("Working on")
        self.tabview.tab("Important Updates!").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("key Features!").grid_columnconfigure(0, weight=1)
        self.radiobutton_frame = customtkinter.CTkFrame(self)
        self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="Mode of convo")
        self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Text to Text and Voice", variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        
        
        # creating Conversation
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self,width=250, label_text="The conversation")
        self.scrollable_frame.grid(row=1, column=1,columnspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
   
    def change_theme():
        customtkinter.set_appearance_mode(mood)    
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def sidebar_button_event(self):
        with open("group.py") as f:
            exec(f.read())
    def change_background_color(self, new_color):
        self.configure(bg=new_color)
    def poweron(self):
        subprocess.call(["python", "server.py"])
    

 

if __name__ == "__main__":
    app = App()
    app.mainloop()

 

