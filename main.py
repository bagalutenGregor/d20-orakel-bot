from dotenv import load_dotenv
import os
import random
from datetime import time
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()  # Läd die .env-Datei

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

ORAKEL = [
    "Trink einen Kaffee oder Tee nur für dich. Kein Bildschirm.",
    "Zieh heute das Outfit an, bei dem du denkst: \"Verdammt, seh ich gut aus.\"",
    "Schreib jemandem ungefragt, warum du ihn oder sie magst.",
    "Mach heute eine Sache nur, weil sie dir Freude macht – ohne Zweck.",
    "Mach 10 Minuten gar nichts. Kein Handy. Kein Ziel. Einfach du.",
    "Sag heute zu dir selbst: \"Ich bin genug.\" Mehrmals. Laut.",
    "Gönn dir was Leckeres, das du sonst eher aufschiebst.",
    "Lies ein paar Seiten in einem Buch, das dich wirklich interessiert.",
    "Tanze zu einem Lied, das du liebst. Völlig egal wie du aussiehst.",
    "Heute darfst du alles in deinem Tempo machen. Niemand schreibt dir was vor.",
    "Schreib 3 Dinge auf, für die du heute dankbar bist.",
    "Geh heute ein paar Minuten raus – auch wenn’s nur vor die Tür ist.",
    "Lächle dir im Spiegel zu. Ja, wirklich. Mach’s.",
    "Streiche heute eine nervige To-Do-Liste komplett. Nix passiert. Du darfst das.",
    "Tu jemandem etwas Gutes – ohne, dass er es merkt.",
    "Stell dir vor, heute wäre ein Film über dich. Was wär die beste Szene?",
    "Schalte dein Handy für 30 Minuten aus. Die Welt bricht nicht zusammen.",
    "Mach was Kindisches. Kritzele, sing albern, hüpf. Niemand urteilt.",
    "Heute ist \"Nein\"-Tag. Sag \"Nein\" zu allem, was deine Energie frisst.",
    "Du bist wundervoll. Und heute wird gut. Punkt"
]

def w20_orakel():
    wurf = random.randint(1, 20)
    botschaft = ORAKEL[wurf - 1]
    return f"W20: {wurf}\nOrakelbotschaft:\n{botschaft}"

def is_gnome():
    desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").lower()
    if "gnome" in desktop:
        return True
    try:
        import subprocess
        output = subprocess.check_output(["ps", "-A"]).decode()
        if "gnome-session" in output:
            return True
    except Exception:
        pass
    return False

def send_gnome_notification(title, message):
    try:
        import subprocess
        subprocess.Popen(['notify-send', title, message])
    except Exception:
        pass

async def wuerfel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = w20_orakel()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)
    if is_gnome():
        send_gnome_notification("Orakelwurf", msg)

async def taeglicher_wurf(context: ContextTypes.DEFAULT_TYPE):
    msg = w20_orakel()
    await context.bot.send_message(chat_id=CHAT_ID, text=f"Täglicher Orakelwurf:\n{msg}")
    if is_gnome():
        send_gnome_notification("Orakelwurf", msg)

async def on_startup(app):
    # Startwurf beim Start
    bot = Bot(TELEGRAM_TOKEN)
    msg = w20_orakel()
    await bot.send_message(chat_id=CHAT_ID, text=f"Startwurf:\n{msg}")
    if is_gnome():
        send_gnome_notification("Orakelwurf", msg)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).post_init(on_startup).build()
    app.add_handler(CommandHandler("wuerfel", wuerfel_command))
    app.job_queue.run_daily(taeglicher_wurf, time(hour=9, minute=0))
    app.run_polling()
