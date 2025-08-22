import os, time, random
from instagrapi import Client

# 1) Credentials Railway Variables se (Settings > Variables me set karoge)
USERNAME = os.getenv("INSTA_USER", "xus.a3")      # fallback diya, par Railway me var jarur set karna
PASSWORD = os.getenv("INSTA_PASS", "sasuke1")

# 2) Login
cl = Client()
cl.login(USERNAME, PASSWORD)
print("🤖 Sasuke Auto-Reply bot started.")

# 3) To avoid spamming, track last replied message IDs (memory-only)
replied_ids = set()
my_id = cl.user_id

OFFLINE_TEXT = "⚡ Sasuke is offline right now, will reply later."

def tick():
    # latest 10 threads (DM + group)
    threads = cl.direct_threads(amount=10)
    for th in threads:
        # last message of this thread
        msgs = cl.direct_messages(th.id, amount=1)
        if not msgs:
            continue
        m = msgs[0]

        # skip if our own message
        if m.user_id == my_id:
            continue

        # skip if already replied to this message id
        if m.id in replied_ids:
            continue

        # reply
        cl.direct_send(OFFLINE_TEXT, thread_ids=[th.id])
        print(f"✅ Replied in thread {th.id} to user {m.user_id}")
        replied_ids.add(m.id)
        time.sleep(random.uniform(4, 9))  # small delay for safety

# 4) Loop
while True:
    try:
        tick()
        time.sleep(random.uniform(12, 20))
    except Exception as e:
        print("⚠️ Loop error:", e)
        time.sleep(15)
