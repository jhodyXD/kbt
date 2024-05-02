from python_shell import PythonShell

# Path ke skrip Node.js Anda
node_script_path = "index.js"

# Token bot Telegram Anda
token = "7190883171:AAH-9Fu-EnOInHjit7H5_jfahn2dBK4nHYY"  # Ganti dengan token bot Anda

# Opsi untuk menentukan mode eksekusi
node_options = {
    "mode": "text",
    "python_path": "python3"  # Sesuaikan dengan path Python Anda jika perlu
}

# Argumen yang akan dilewatkan ke skrip Node.js
node_args = [token]

# Menjalankan skrip Node.js menggunakan python-shell
PythonShell.run(node_script_path, args=node_args, **node_options)
