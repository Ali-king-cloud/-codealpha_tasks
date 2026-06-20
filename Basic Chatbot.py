import random
import datetime

class ChatBot:
    def __init__(self):
        self.name = "AlphaBot"
        self.user_name = None
        self.responses = {
            # Greetings
            "hello": ["Hi there! 👋", "Hello! Nice to meet you!", "Hey! How can I help?"],
            "hi": ["Hi! 👋", "Hello!", "Hey there!"],
            "hey": ["Hey! What's up?", "Hello! How are you?"],
            
            # Well-being
            "how are you": ["I'm doing great, thanks! 😊", "I'm fine! How about you?", "All systems operational! ⚙️"],
            "how are you doing": ["Pretty well! You?", "I'm excellent! How are you?"],
            
            # Identity
            "what is your name": [f"I'm {self.name}, your friendly assistant! 🤖", f"My name is {self.name}."],
            "who are you": [f"I'm {self.name}, a Python-powered chatbot!", "I'm a virtual assistant created to chat with you!"],
            
            # Capabilities
            "what can you do": ["I can chat, tell jokes, share facts, and help with basic questions!", "I'm good at conversations and keeping you company!"],
            "help": ["I can respond to greetings, tell jokes, share the time, or just chat! Try asking me something."],
            
            # Farewells
            "bye": ["Goodbye! 👋 Have a great day!", "See you later!", "Bye! Take care! 😊"],
            "goodbye": ["Goodbye! It was nice chatting!", "See you next time!"],
            "see you": ["See you! 👋", "Until next time!"],
            
            # Time
            "what time is it": [self.get_time],
            "what is the time": [self.get_time],
            "time": [self.get_time],
            
            # Fun
            "tell me a joke": [
                "Why do Python programmers prefer dark mode? Because light attracts bugs! 🐛",
                "Why did the developer go broke? Because he used up all his cache! 💰",
                "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
                "Why do Java developers wear glasses? Because they can't C#! 👓"
            ],
            "joke": ["I told my computer I needed a break, and now it won't stop sending me Kit-Kats! 🍫"],
            
            # Thanks
            "thank you": ["You're welcome! 😊", "No problem!", "Happy to help!"],
            "thanks": ["Anytime! 👍", "You're welcome!"],
        }
        self.fallback_responses = [
            "I'm not sure I understand. Could you rephrase that? 🤔",
            "Interesting! Tell me more.",
            "I don't know about that yet, but I'm learning!",
            "Hmm, that's beyond my current knowledge. Try asking about time, jokes, or just say hello!",
        ]
    
    def get_time(self):
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')} on {now.strftime('%A, %B %d, %Y')} ⏰"
    
    def get_response(self, user_input):
        user_input = user_input.lower().strip().rstrip('!?.,')
        
        # Check for exact matches first
        if user_input in self.responses:
            response = random.choice(self.responses[user_input])
            return response() if callable(response) else response
        
        # Check for partial matches
        for key in self.responses:
            if key in user_input or user_input in key:
                response = random.choice(self.responses[key])
                return response() if callable(response) else response
        
        return random.choice(self.fallback_responses)
    
    def run(self):
        print("=" * 50)
        print(f"    🤖 {self.name} — Your Friendly Chatbot")
        print("=" * 50)
        print("Type 'bye' to exit\n")
        
        # Get user name
        self.user_name = input("What's your name? ").strip() or "Friend"
        print(f"\nNice to meet you, {self.user_name}! Let's chat! 💬\n")
        
        while True:
            try:
                user_input = input(f"{self.user_name}: ").strip()
                if not user_input:
                    continue
                
                if user_input.lower() in ['bye', 'goodbye', 'exit', 'quit']:
                    print(f"\n{self.name}: Goodbye, {self.user_name}! 👋")
                    break
                
                response = self.get_response(user_input)
                print(f"\n{self.name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n{self.name}: Goodbye! 👋")
                break
            except EOFError:
                break

if __name__ == "__main__":
    bot = ChatBot()
    bot.run()
