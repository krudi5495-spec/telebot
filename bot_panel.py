from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# ==========================================
# KONFIGURASI UTAMA (Ganti Token di Sini)
# ==========================================
8834368216:AAGESamE2xA4NtInoLHQyY6sIkH5rRJepzg
app = Client(
    "flensiza_panel_bot",
    bot_token=BOT_TOKEN
)

# ==========================================
# TAMPILAN MENU UTAMA & TOMBOL
# ==========================================
def get_main_menu(nama_user):
    teks = (
        f"👋 Hai!, {nama_user},\n\n"
        "Selamat datang di **Promote Auto by @Flensiza**!\n"
        "Saya dapat membuat Userbot secara instan.\n\n"
        "✨ **Fitur Utama:**\n"
        "• 24 Jam Non-Stop\n"
        "• Atur jeda & broadcast otomatis\n"
        "• Simple use & mudah digunakan\n\n"
        "Silakan pilih menu di bawah ini:"
    )
    
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("🤖 Buat Userbot", callback_data="menu_buat")],
            [InlineKeyboardButton("💰 TopUp Coin", callback_data="menu_topup")],
            [InlineKeyboardButton("📢 Channel & Info", url="https://t.me/Flensiza")]
        ]
    )
    return teks, keyboard

# Handler ketika user mengirim perintah /start
@app.on_message(filters.command("start"))
def start_handler(client, message):
    nama_user = message.from_user.first_name
    teks, keyboard = get_main_menu(nama_user)
    message.reply_text(teks, reply_markup=keyboard)

# Handler ketika tombol interaktif diklik
@app.on_callback_query()
def callback_handler(client, callback_query: CallbackQuery):
    data = callback_query.data
    
    if data == "menu_buat":
        pesan_buat = (
            "🤖 **Menu Pembuatan Userbot**\n\n"
            "Untuk membuat userbot baru, pastikan akunmu memiliki saldo coin yang cukup.\n"
            "Silakan lakukan TopUp terlebih dahulu jika coin belum mencukupi."
        )
        keyboard_kembali = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali ke Menu", callback_data="menu_home")]]
        )
        callback_query.message.edit_text(pesan_buat, reply_markup=keyboard_kembali)
        
    elif data == "menu_topup":
        pesan_topup = (
            "💰 **TopUp Coin Bot**\n\n"
            "Masukkan nominal coin yang ingin kamu beli (angka kelipatan 300).\n"
            "Hubungi admin atau ikuti instruksi otomatis selanjutnya."
        )
        keyboard_kembali = InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Kembali ke Menu", callback_data="menu_home")]]
        )
        callback_query.message.edit_text(pesan_topup, reply_markup=keyboard_kembali)
        
    elif data == "menu_home":
        nama_user = callback_query.from_user.first_name
        teks, keyboard = get_main_menu(nama_user)
        callback_query.message.edit_text(teks, reply_markup=keyboard)

# ==========================================
# MENJALANKAN BOT
# ==========================================
if __name__ == "__main__":
    print("🚀 Bot Panel Promote Auto sedang berjalan...")
    app.run()
