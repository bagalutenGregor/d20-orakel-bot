# d20-orakel-bot
# D20 Orakel Telegram Bot

Ein Telegram-Bot, der auf Knopfdruck oder automatisch täglich um 9 Uhr eine inspirierende D20-Orakelbotschaft versendet. Die Botschaften stammen von TalonZorch.

## Features

- Würfelt einen W20 und sendet die passende Orakelbotschaft an dich per Telegram
- Reagiert auf das `/wuerfel`-Kommando im Telegram-Chat
- Automatischer täglicher Orakelwurf um 9 Uhr morgens
- Optional: Zeigt die Botschaft als Systembenachrichtigung unter GNOME

## Installation

1. **Repository klonen**
   ```
   git clone https://github.com/bagalutengregor/d20-orakel-bot.git
   cd d20-orakel-bot
   ```

2. **Virtuelle Umgebung anlegen und Abhängigkeiten installieren**
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Umgebungsvariablen setzen**

   Lege eine `.env`-Datei im Projektordner an:
   ```
   TELEGRAM_TOKEN=dein-telegram-bot-token
   CHAT_ID=deine-chat-id
   ```

4. **Bot starten**
   ```
   python main.py
   ```

5. **(Optional) Als systemd-Service auf einem Linux-Server einrichten**

     a) Kopiere dein Projekt auf den Server (z.B. nach /opt/d20-orakel).
    
     b) Erstelle eine neue Datei für den Service:

       bash
        sudo nano /etc/systemd/system/d20-orakel.service
     Füge das hier ein (passe die Pfade ggf. an):

       [Unit]
       Description=D20 Orakel Telegram Bot
       After=network.target

       [Service]
       Type=simple
       User=root
       WorkingDirectory=/opt/d20-orakel
       ExecStart=/opt/d20-orakel/.venv/bin/python /opt/d20-orakel/main.py
       Restart=always

       [Install]
       WantedBy=multi-user.target

     c) Service starten:

       bash
       sudo systemctl daemon-reload
       sudo systemctl enable d20-orakel.service
       sudo systemctl start d20-orakel.service
     d) Status prüfen (optional):

       bash
       sudo systemctl status d20-orakel.service

## Orakeltexte

Die D20-Orakeltexte stammen von **TalonZorch**.  
Mehr von TalonZorch findest du auf [seiner Patreon-Seite](https://www.patreon.com/talonzorch) und auf [talonzorch.de](https://talonzorch.de/?author=1).

> **Quelle der Orakeltexte:**  
> © TalonZorch – [Patreon](https://www.patreon.com/talonzorch)

## Lizenz

Dieses Projekt ist Open Source. Die Orakeltexte stehen unter dem Copyright von TalonZorch.

---

**Viel Spaß beim Orakeln!**
```