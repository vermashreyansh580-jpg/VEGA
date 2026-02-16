import flet as ft
import speech_recognition as sr
from plyer import tts
from groq import Groq  # 🔥 Groq Library Added
import threading

# --- CONFIG ---
API_KEY = "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"
client = Groq(api_key=API_KEY)

def main(page: ft.Page):
    page.title = "VEGA AI"
    page.bgcolor = "black"
    page.padding = 0
    
    # UI Load karo
    webview = ft.WebView(url="/index.html", expand=True)
    page.add(webview)

    def speak(text):
        try:
            print(f"VEGA: {text}")
            tts.speak(text)
        except:
            pass

    def ask_groq(prompt):
        try:
            print("Thinking...")
            completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are Vega, a concise AI assistant. Reply in short sentences."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=100
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error connecting to brain: {e}"

    def brain_loop():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            speak("System Online.")
            
            while True:
                try:
                    print("Listening...")
                    audio = recognizer.listen(source)
                    user_text = recognizer.recognize_google(audio).lower()
                    print(f"User: {user_text}")

                    if "vega" in user_text:
                        # Sirf 'Vega' bolne par activate hoga
                        command = user_text.replace("vega", "").strip()
                        if command:
                            response = ask_groq(command)
                            speak(response)
                        else:
                            speak("Yes boss?")
                            
                except Exception as e:
                    pass

    # Brain ko alag thread mein dalo
    threading.Thread(target=brain_loop, daemon=True).start()

ft.app(target=main, assets_dir="assets")