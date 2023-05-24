import tkinter
import tkinter.messagebox
import customtkinter
import speech_recognition as sr
import os
import webbrowser


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):

   
    def __init__(self):
        
        super().__init__()
        def inpt():
            switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=self.entry.get())
            switch.grid( column=0, padx=10)
            r=">>"+self.entry.get()
            self.scrollable_frame_switches.append(r)
            querry=self.entry.get()
            greet=['hi','hello','namaste','hey','hii','heyllo']
            def say(text):
                os.system(f"say {text}")
            
            for greets in greet:
                if greets in querry.lower():
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text="~>> OHH hi! It's great to see you here! ")
                    switch.grid( column=0, padx=10)
                        
                    say("OH hi! Its great to see you here!")
                    self.scrollable_frame_switches.append("~>> OHH hi! It's great to see you here! ")
        
                


            sites=[["youtube","https://www.youtube.com"],['wikipedia','https://www.wikipedia.com'],['google','https://google.com']]
            for site in sites:
                if site[0].lower() in querry.lower():
                    siteaction=f"~>>  Opening {site[0]}"
                    webbrowser.open(site[1])
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=siteaction)
                    switch.grid( column=0, padx=10)
                    self.scrollable_frame_switches.append(siteaction)
                    say(f"Opening {site[0]}")

            quit=['quit','goodbye']
            for quits in quit:
                if quits in querry:
                    siteaction="It was nice chatting with you! Hope to see you sometime soon!"
                    switch = customtkinter.CTkLabel(master=self.scrollable_frame, text=siteaction)
                    self.scrollable_frame_switches.append(siteaction)
                    say("It was nice chatting with you! Hope to see you sometime soon!")

        
        
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
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,text='Take me to Private Messaging', command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["System", "Dark", "Lights"],
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
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Voice to Voice", variable=self.radio_var, value=0)
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Text to Text", variable=self.radio_var, value=1)
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Voice to Text", variable=self.radio_var, value=2)
        self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")
        self.radio_button_4 = customtkinter.CTkRadioButton(master=self.radiobutton_frame,text="Text to Voice", variable=self.radio_var, value=3)
        self.radio_button_4.grid(row=4, column=2, pady=10, padx=20, sticky="n")
        
        
        # creating Conversation
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self,width=250, label_text="The conversation")
        self.scrollable_frame.grid(row=1, column=1,columnspan=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    def sidebar_button_event(self):
        print("sidebar_button click")
    

 

if __name__ == "__main__":
    app = App()
    app.mainloop()
