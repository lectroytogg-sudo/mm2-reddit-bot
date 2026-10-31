import time
import os
import praw

# قراءة بيانات الاعتماد الخاصة بريديت من إعدادات الأمان في الاستضافة
reddit = praw.Reddit(
    client_id=os.environ.get("REDDIT_CLIENT_ID"),
    client_secret=os.environ.get("REDDIT_CLIENT_SECRET"),
    user_agent="MM2BotManager v1.0",
    username=os.environ.get("REDDIT_USERNAME"),
    password=os.environ.get("REDDIT_PASSWORD")
)

print("[SUCCESS] Connected to Reddit Successfully! Bot is running 24/7...")

# حلقة تكرارية لضمان استمرار البوت دائماً (Uptime Loop)
while True:
    try:
        # فحص الرسائل الخاصة الواردة أو التحديثات على ريديت
        print("[CHECKING] Scanning Reddit inbox for commands...")
        
        # يمكنك هنا استقبال الأوامر البرمجية ومعالجتها
        for message in reddit.inbox.unread(limit=5):
            print(f"Received command from u/{message.author}: {message.body}")
            message.mark_read()
            
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    
    # الانتظار لمدة 60 ثانية قبل الفحص القادم
    time.sleep(60)
