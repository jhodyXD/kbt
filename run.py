import subprocess

# Path ke skrip Node.js Anda
node_script_path = "index.js"

# Token bot Telegram Anda
token = "7190883171:AAH-9Fu-EnOInHjit7H5_jfahn2dBK4nHYY"  # Ganti dengan token bot Anda

# Menjalankan skrip Node.js menggunakan subprocess
subprocess.run(["node", node_script_path, token])
