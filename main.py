import os
import discord
from discord.ext import commands

# إعدادات البوت وصلاحياته الأساسية
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (Discord Bot is Online!)")

# أمر لجلب الأخبار وإرسالها (اكتب !news في السيرفر أو !news dm للخاص)
@bot.command(name="news")
async def send_news(ctx, destination: str = "server"):
    news_content = "📰 **آخر الأخبار والتحديثات:**\n- تم تشغيل نظام البوت بنجاح.\n- جارٍ مراقبة الأنظمة واستقرار العمل."
    
    if destination.lower() == "dm":
        try:
            # إرسال الأخبار على الرسائل الخاصة (DM) لك مباشرة
            await ctx.author.send(news_content)
            await ctx.send("📩 تم إرسال الأخبار إلى رسائلك الخاصة (DM)!")
        except discord.Forbidden:
            await ctx.send("❌ عذراً، لا يمكنني إرسال رسالة خاصة لك، تأكد من فتح الرسائل الخاصة من إعدادات السيرفر.")
    else:
        # إرسال الأخبار في نفس شات السيرفر
        await ctx.send(news_content)

# تشغيل البوت باستخدام التوكن المباشر
bot.run("MTQyOTc5MzM3MzQ2Nzk3MTY5NQ.GllCU6.kjGg0c_HMUjUSSS9JQWtplc5VeZOR43IzqrVic")
