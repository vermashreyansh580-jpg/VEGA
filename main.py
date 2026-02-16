import flet as ft
import speech_recognition as sr
from plyer import tts
from groq import Groq
import threading
import base64

# --- CONFIG ---
# ⚠️ Security Warning: Ye key public hai. Baad mein revoke karke nayi daalna.
API_KEY = "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"
client = Groq(api_key=API_KEY)

def main(page: ft.Page):
    page.title = "VEGA GOD MODE"
    page.bgcolor = "black"
    page.padding = 0
    
    # --- 1. HTML UI (In-Built) ---
    # Hum HTML ko yahi likh rahe hain taaki assets folder ka jhanjhat na ho
    html_code = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body { background-color: #000000; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100vh; margin: 0; font-family: 'Courier New', monospace; overflow: hidden; }
            .reactor { width: 180px; height: 180px; border: 4px solid #00ff00; border-radius: 50%; display: flex; justify-content: center; align-items: center; box-shadow: 0 0 25px #00ff00; animation: pulse 2s infinite; position: relative; }
            .core { width: 120px; height: 120px; background: radial-gradient(circle, #00ff00 10%, transparent 70%); border-radius: 50%; }
            h1 { color: #00ff00; margin-top: 40px; letter-spacing: 6px; text-shadow: 0 0 15px #00ff00; font-size: 32px; }
            p { color: #008800; font-size: 12px; margin-top: 10px; }
            @keyframes pulse { 0% { box-shadow: 0 0 20px #00ff00; opacity: 0.8; } 50% { box-shadow: 0 0 50px #00ff00; opacity: 1; } 100% { box-shadow: 0 0 20px #00ff00; opacity: 0.8; } }
        </style>
    </head>
    <body>
        <div class="reactor"><div class="core"></div></div>
        <h1>V E G A</h1>
        <p>SYSTEM ONLINE // FULL ACCESS</p>
    </body>
    </html>
    """
    
    # Encode HTML to Base64 to load in WebView
    b64_html = base64.b64encode(html_code.encode('utf-8')).decode('utf-8')
    webview = ft.WebView(url=f"data:text/html;base64,{b64_html}", expand=True)
    page.add(webview)

    # --- 2. BRAIN (Logic) ---
    def speak(text):
        try:
            print(f"VEGA: {text}")
            tts.speak(text)
        except:
            pass

    def ask_groq(prompt):
        try:
            chat = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": "You are Vega, a high-tech AI. Keep answers short and robotic."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=100
            )
            return chat.choices[0].message.content
        except Exception as e:
            return "Connection Error."

    def listen_loop():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            speak("System Initialized.")
            
            while True:
                try:
                    print("Listening...")
                    audio = r.listen(source)
                    text = r.recognize_google(audio).lower()
                    print(f"User: {text}")

                    if "vega" in text:
                        cmd = text.replace("vega", "").strip()
                        if cmd:
                            reply = ask_groq(cmd)
                            speak(reply)
                        else:
                            speak("Ready.")
                except:
                    pass

    # Start Brain
    threading.Thread(target=listen_loop, daemon=True).start()

ft.app(target=main)
