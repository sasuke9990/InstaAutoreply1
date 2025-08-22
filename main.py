from instagrapi import Client
import time

USERNAME = "xus.a3"
PASSWORD = "sasuke1"

cl = Client()
cl.login(USERNAME, PASSWORD)

print("🤖 Bot started... Listening for messages...")

while True:
    try:
        inbox = cl.direct_threads(amount=5)
        for thread in inbox:
            if thread.messages:
                last_msg = thread.messages[0].text
                user_id = thread.messages[0].user_id
                # Auto reply
                cl.direct_send("⚡ Sasuke is offline right now, will reply later.", [user_id])
                print(f"Replied to {last_msg}")
    except Exception as e:
        print("Error:", e)

    time.sleep(30)  # हर 30 सेकंड में check करेगा
