Using this TG bot you can remotely enable or disable execution rights to prismlauncher for a specific user. 

HOW TO USE:
    1. Clone this repository
    2. Rename "_config.py" to "config.py"
    3. Configure "config.py"
    4. Configure venv and install requairements
    5. Now you can test bot by launching "main.py" with sudo 
    6. If all works, somehow add main.py to startup as root user. You can somehow use existing venv, or install requirements systemwide.

I didn't manage to use existing venv, so I don't know how to do it for sure. But I can provide "mclauncher.service" file here:

[Unit]
Description=Minecraft Switch
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/your/path/to/minecraft_access
ExecStart=/bin/bash -c '/your/path/to/minecraft_access/venv/bin/python3 /your/path/to/minecraft_access/main.py'
Restart=always

[Install]
WantedBy=multi-user.target
