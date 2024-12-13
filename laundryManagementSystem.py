import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import datetime
from ttkthemes import ThemedTk
from tkcalendar import DateEntry

# Koneksi ke database MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Sesuaikan dengan konfigurasi MySQL
    database="laundry"
)
cursor = db.cursor()

# Fungsi untuk login
def login():
    # Variabel global untuk menyimpan nama pengguna yang login
    current_user = None

    def check_login():
        global current_user
        username = entry_username.get()
        password = entry_password.get()
        cursor.execute("SELECT * FROM pengguna WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        if user:
            # Simpan username pengguna yang login
            current_user = username
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
            login_window.destroy()
            main_app()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah!")



    # Window utama login
    login_window = ThemedTk(theme="arc")  # Gunakan tema lebih modern
    login_window.title("Login - Manajemen Laundry")
    login_window.geometry("400x500")
    login_window.resizable(False, False)
    login_window.configure(bg="#F5F5F5")  # Latar belakang abu-abu terang

    # Kontainer untuk form login
    container = tk.Frame(login_window, bg="#FFFFFF", bd=0, relief="flat")
    container.place(relx=0.5, rely=0.5, anchor="center", width=340, height=400)

    # Judul aplikasi dengan ikon
    title_label = tk.Label(
        container,
        text="🚿 Manajemen Laundry",
        font=("Montserrat", 20, "bold"),
        bg="#FFFFFF",
        fg="#D32F2F"
    )
    title_label.pack(pady=20)

    # Username
    username_label = tk.Label(container, text="Username", font=("Open Sans", 12), bg="#FFFFFF", fg="#555555")
    username_label.pack(anchor="w", padx=20, pady=(10, 0))
    entry_username = ttk.Entry(container, font=("Open Sans", 12))
    entry_username.pack(fill="x", padx=20, pady=5)

    # Password
    password_label = tk.Label(container, text="Password", font=("Open Sans", 12), bg="#FFFFFF", fg="#555555")
    password_label.pack(anchor="w", padx=20, pady=(10, 0))
    entry_password = ttk.Entry(container, font=("Open Sans", 12), show="*")
    entry_password.pack(fill="x", padx=20, pady=5)

    # Tombol Login
    login_button = tk.Button(
        container,
        text="Login",
        font=("Montserrat", 12, "bold"),
        bg="#D32F2F",
        fg="#FFFFFF",
        activebackground="#C62828",
        activeforeground="#FFFFFF",
        relief="flat",
        command=check_login
    )
    login_button.pack(pady=20, ipadx=10, ipady=5)


    # Footer
    footer_label = tk.Label(
        container,
        text="© 2024 Manajemen Laundry",
        font=("Helvetica", 10),
        bg="#FFFFFF",
        fg="#888888"
    )
    footer_label.pack(side="bottom", pady=10)

    login_window.mainloop()



# Fungsi utama aplikasi
def main_app():
    app = tk.Tk()
    app.title("Manajemen Laundry")
    app.geometry("1280x720")

    # Header di luar area aplikasi
    header = tk.Frame(app, bg="red", height=80)  # Naikkan tinggi misalnya menjadi 80 piksel
    header.pack(side="top", fill="x", pady=0)

    header_title = tk.Label(
        header,
        text="🚿 Manajemen Laundry",
        font=("Montserrat", 20, "bold"),  # Bisa naikkan ukuran font
        fg="white",  # Warna teks putih
        bg="red",
        anchor="w"
    )
    header_title.pack(side="left", padx=20, pady=10)  # Tambahkan pady untuk padding vertikal

    # Main content frame
    main_content = tk.Frame(app, bg="white")
    main_content.pack(side="right", fill="both", expand=True)


     # Fungsi untuk membersihkan main content
    def clear_main_content():
        for widget in main_content.winfo_children():
            widget.destroy()

    # Buat fungsi create_modern_sidebar
    def create_modern_sidebar(app, main_content):
        # Sidebar container
        sidebar = tk.Frame(app, width=250, bg="#1a1a2e")  # Warna gelap modern
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)  # Mempertahankan lebar sidebar

        # Profile section di bagian ATAS
        profile_frame = tk.Frame(sidebar, bg="#1a1a2e")
        profile_frame.pack(fill="x", pady=20)  # Pindahkan ke atas

        # Profile icon
        profile_icon = tk.Label(
            profile_frame,
            text="👤",
            font=("Arial", 20),
            bg="#1a1a2e",
            fg="#ffffff"    
        )
        profile_icon.pack()

        # Username
        username_label = tk.Label(
            profile_frame,
            text=current_user,  # Username aktual
            font=("Helvetica", 10),
            bg="#1a1a2e",
            fg="#ffffff"
        )
        username_label.pack(pady=5)

        # Separator setelah profil
        separator = tk.Frame(sidebar, height=2, bg="#2d2d44")
        separator.pack(fill="x", padx=20, pady=10)

        # Menu container
        menu_frame = tk.Frame(sidebar, bg="#1a1a2e")
        menu_frame.pack(fill="x", pady=10)

        # Fungsi untuk membuat tombol menu
        def create_menu_button(text, icon, command):
            button_frame = tk.Frame(menu_frame, bg="#1a1a2e")
            button_frame.pack(fill="x", pady=2)

            def on_enter(e):
                button_frame.configure(bg="#2d2d44")
                icon_label.configure(bg="#2d2d44")
                text_label.configure(bg="#2d2d44")

            def on_leave(e):
                button_frame.configure(bg="#1a1a2e")
                icon_label.configure(bg="#1a1a2e")
                text_label.configure(bg="#1a1a2e")

            def on_click(e):
                # Reset semua button ke warna default
                for child in menu_frame.winfo_children():
                    child.configure(bg="#1a1a2e")
                    for grandchild in child.winfo_children():
                        grandchild.configure(bg="#1a1a2e")
                    
                # Set warna aktif untuk button yang diklik
                button_frame.configure(bg="#2d2d44")
                icon_label.configure(bg="#2d2d44")
                text_label.configure(bg="#2d2d44")
                
                # Jalankan command
                command()

            # Icon
            icon_label = tk.Label(
                button_frame,
                text=icon,
                font=("Arial", 14),
                bg="#1a1a2e",
                fg="#ffffff",
                width=2
            )
            icon_label.pack(side="left", padx=(20, 10))

            # Text
            text_label = tk.Label(
                button_frame,
                text=text,
                font=("Helvetica", 10),
                bg="#1a1a2e",
                fg="#ffffff",
                anchor="w"
            )
            text_label.pack(side="left", fill="x")

            # Binding events
            for widget in [button_frame, icon_label, text_label]:
                widget.bind("<Enter>", on_enter)
                widget.bind("<Leave>", on_leave)
                widget.bind("<Button-1>", on_click)

        # Menu items dengan icon
        menu_items = [
            ("Dashboard", "📊", lambda: show_dashboard()),
            ("Pelanggan", "👥", lambda: show_pelanggan()),
            ("Transaksi", "💰", lambda: show_transaksi()),
            ("Layanan", "🧺", lambda: show_jenis_layanan()),
            ("Pembayaran", "💳", lambda: show_metode_pembayaran()),
            ("Laporan", "📈", lambda: show_laporan())
        ]

        for text, icon, command in menu_items:
            create_menu_button(text, icon, command)

        # Frame untuk tombol Logout di bagian bawah sidebar
        logout_frame = tk.Frame(sidebar, bg="#1a1a2e", pady=10)
        logout_frame.pack(side="bottom", fill="x", pady=20)

        # Tombol Logout
        logout_button = tk.Button(
            logout_frame,
            text="Logout",
            font=("Helvetica", 8),
            bg="#ff3366",
            fg="#ffffff",
            bd=0,
            relief="flat",
            padx=15,
            pady=5,
            command=lambda: logout(app)
        )
        logout_button.pack()
 
        
        return sidebar

    # Buat sidebar modern
    sidebar = create_modern_sidebar(app, main_content)
    
    def clear_main_content():
        for widget in main_content.winfo_children():
            widget.destroy()
    
    def display_user_profile():
        global current_user  # Ambil username dari sesi login
        user_name = current_user if current_user else "Admin"  # Default jika tidak ada nama pengguna
        
        profile_frame = tk.Frame(sidebar, bg="#1E1E2F", height=100)
        profile_frame.pack(fill="x", pady=10)

        # Tambahkan ikon/gambar profil
        tk.Label(
            profile_frame,
            text="👤",
            font=("Arial", 36),
            bg="#1E1E2F",
            fg="white"
        ).pack(pady=())

        # Nama pengguna
        tk.Label(
            profile_frame,
            text=user_name,
            font=("Arial", 14, "bold"),
            bg="#1E1E2F",
            fg="white"
        ).pack()

        # Tombol Logout
        tk.Button(
            profile_frame,
            text="Logout",
            font=("Arial", 10, "bold"),
            bg="#444454",
            fg="white",
            activebackground="#555575",
            activeforeground="white",
            command=lambda: logout(app)
        ).pack(pady=5)

    def logout(app):
        if messagebox.askyesno("Logout", "Anda yakin ingin keluar?"):
            app.destroy()  # Tutup aplikasi utama
            login()  # Kembali ke halaman login

    # Dashboard
    def show_dashboard():
        clear_main_content()
        
        # Container utama dengan padding
        container = tk.Frame(main_content, bg="white")
        container.pack(fill="both", expand=True, padx=30, pady=20)
        
        # Header dashboard dengan styling
        header_frame = tk.Frame(container, bg="white")
        header_frame.pack(fill="x", pady=(0, 20))
        
        tk.Label(
            header_frame,
            text="Dashboard Overview",
            font=("Helvetica", 24, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(side="left")
        
        # Tanggal hari ini
        current_date = datetime.now().strftime("%d %B %Y")
        tk.Label(
            header_frame,
            text=current_date,
            font=("Helvetica", 12),
            bg="white",
            fg="#7f8c8d"
        ).pack(side="right", pady=10)

        # Query data
        cursor.execute("SELECT COUNT(*) FROM transaksi WHERE DATE(tanggal_transaksi) = CURDATE()")
        transaksi_hari_ini = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(total_harga) FROM transaksi WHERE DATE(tanggal_transaksi) = CURDATE()")
        pendapatan_hari_ini = cursor.fetchone()[0] or 0

        cursor.execute("SELECT COUNT(*) FROM transaksi WHERE status='Selesai'")
        cucian_selesai = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM transaksi WHERE status='Proses'")
        cucian_proses = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM pelanggan")
        total_pelanggan = cursor.fetchone()[0]

        cursor.execute("SELECT SUM(total_harga) FROM transaksi")
        total_pendapatan = cursor.fetchone()[0] or 0

        # Data untuk cards
        stats = [
            {
                "label": "Transaksi Hari Ini",
                "value": str(transaksi_hari_ini),
                "icon": "📊",
                "bg": "#FF6B6B",
                "trend": ""
            },
            {
                "label": "Pendapatan Hari Ini",
                "value": f"Rp {pendapatan_hari_ini:,}",
                "icon": "💰",
                "bg": "#4ECDC4",
                "trend": ""
            },
            {
                "label": "Total Pendapatan",
                "value": f"Rp {total_pendapatan:,}",
                "icon": "💵",
                "bg": "#45B7D1",
                "trend": ""
            },
            {
                "label": "Cucian Selesai",
                "value": str(cucian_selesai),
                "icon": "✅",
                "bg": "#96CEB4",
                "trend": "Total selesai"
            },
            {
                "label": "Cucian Dalam Proses",
                "value": str(cucian_proses),
                "icon": "⏳",
                "bg": "#D4A5A5",
                "trend": "Sedang diproses"
            },
            {
                "label": "Total Pelanggan",
                "value": str(total_pelanggan),
                "icon": "👥",
                "bg": "#9B59B6",
                "trend": "+3 pelanggan baru"
            }
        ]

        grid_frame = tk.Frame(container, bg="white")
        grid_frame.pack(fill="both", expand=True, pady=(10, 5))  # Kurangi padding bawah
        
        # Konfigurasi grid columns
        grid_frame.grid_columnconfigure(0, weight=1)
        grid_frame.grid_columnconfigure(1, weight=1)
        grid_frame.grid_columnconfigure(2, weight=1)

        # Membuat cards
        for i, stat in enumerate(stats):
            row = i // 3
            col = i % 3
            
            # Card container
            card = tk.Frame(
                grid_frame,
                bg="white",
                highlightbackground=stat["bg"],
                highlightthickness=2,
                bd=0
            )
            card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            
            # Icon dan label container
            header_frame = tk.Frame(card, bg="white")
            header_frame.pack(fill="x", padx=15, pady=(15, 5))
            
            # Icon
            tk.Label(
                header_frame,
                text=stat["icon"],
                font=("Segoe UI Emoji", 24),
                bg="white"
            ).pack(side="left")
            
            # Label
            tk.Label(
                header_frame,
                text=stat["label"],
                font=("Helvetica", 12),
                bg="white",
                fg="#2c3e50"
            ).pack(side="right")
            
            # Value
            tk.Label(
                card,
                text=stat["value"],
                font=("Helvetica", 24, "bold"),
                bg="white",
                fg=stat["bg"]
            ).pack(pady=(0, 5))
            
            # Trend
            tk.Label(
                card,
                text=stat["trend"],
                font=("Helvetica", 10),
                bg="white",
                fg="#95a5a6"
            ).pack(pady=(0, 15))

        # Recent Transactions Section
        tk.Label(
            container,
            text="Transaksi Terbaru",
            font=("Helvetica", 16, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(pady=(15, 10), anchor="w")

        # Create Treeview for recent transactions
        style = ttk.Style()
        style.configure(
            "Custom.Treeview",
            background="white",
            foreground="black",
            rowheight=40,
            fieldbackground="white"
        )
        style.configure(
            "Custom.Treeview.Heading",
            background="#f8f9fa",
            font=('Helvetica', 10, 'bold')
        )

        recent_transactions = ttk.Treeview(
            container,
            columns=("id", "customer", "service", "amount", "status", "date"),
            show="headings",
            height=5
        )

        # Configure columns
        recent_transactions.heading("id", text="ID")
        recent_transactions.heading("customer", text="Pelanggan")
        recent_transactions.heading("service", text="Layanan")
        recent_transactions.heading("amount", text="Total")
        recent_transactions.heading("status", text="Status")
        recent_transactions.heading("date", text="Tanggal")

        recent_transactions.column("id", width=50, anchor="center")
        recent_transactions.column("customer", width=150)
        recent_transactions.column("service", width=150)
        recent_transactions.column("amount", width=150)
        recent_transactions.column("status", width=100)
        recent_transactions.column("date", width=150)

        # Konfigurasi warna baris
        recent_transactions.tag_configure('oddrow', background='#f8f9fa')  # Warna latar belakang untuk baris ganjil
        recent_transactions.tag_configure('evenrow', background='white')   # Warna latar belakang untuk baris genap


        # Get recent transactions
        cursor.execute("""
            SELECT t.id, p.nama, l.nama_layanan, t.total_harga, t.status, t.tanggal_transaksi
            FROM transaksi t
            JOIN pelanggan p ON t.id_pelanggan = p.id
            JOIN layanan l ON t.id_layanan = l.id
            ORDER BY t.tanggal_transaksi DESC
            LIMIT 5
        """)
        
        for index, transaction in enumerate(cursor.fetchall()):
            # Tentukan tag berdasarkan index (ganjil/genap)
            tag = 'oddrow' if index % 2 == 0 else 'evenrow'
            
            # Insert transaction dengan tag pewarnaan
            recent_transactions.insert("", "end", values=(
                transaction[0],  # ID
                transaction[1],  # Nama Pelanggan
                transaction[2],  # Nama Layanan
                f"Rp {transaction[3]:,}",  # Total Harga
                transaction[4],  # Status
                transaction[5].strftime("%d %b %Y")  # Tanggal Transaksi
            ), tags=(tag,))

        recent_transactions.pack(fill="x", pady=10)


    def show_pelanggan():
        clear_main_content()

        # Title Label
        tk.Label(main_content, text="Data Pelanggan", font=("Arial", 24, "bold"), bg="white").pack(pady=20)

        # Treeview Widget
        tree = ttk.Treeview(main_content, columns=("ID", "Nama", "Telepon", "Alamat"), show="headings")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Scrollbar
        scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        # Column Definitions
        tree.heading("ID", text="ID")
        tree.heading("Nama", text="Nama")
        tree.heading("Telepon", text="Telepon")
        tree.heading("Alamat", text="Alamat")

        # Adjust column widths
        tree.column("ID", width=50, anchor="center")
        tree.column("Nama", width=150, anchor="w")
        tree.column("Telepon", width=120, anchor="center")
        tree.column("Alamat", width=200, anchor="w")

        # Konfigurasi warna baris
        tree.tag_configure('oddrow', background='#f8f9fa')
        tree.tag_configure('evenrow', background='white')

        def load_pelanggan():
            tree.delete(*tree.get_children())
            try:
                cursor.execute("SELECT * FROM pelanggan")
                for idx, row in enumerate(cursor.fetchall(), start=1):
                    tag = "oddrow" if idx % 2 else "evenrow"
                    tree.insert("", "end", values=row, tags=(tag,))
            except Exception as e:
                messagebox.showerror("Error", f"Gagal memuat data pelanggan: {e}")

        def add_pelanggan():
            def save_pelanggan():
                nama = entry_nama.get().strip()
                telepon = entry_telepon.get().strip()
                alamat = entry_alamat.get().strip()

                if not nama or not telepon or not alamat:
                    messagebox.showwarning("Peringatan", "Semua field harus diisi!")
                    return
                if not telepon.isdigit():
                    messagebox.showwarning("Peringatan", "Nomor telepon harus berupa angka!")
                    return

                try:
                    cursor.execute("INSERT INTO pelanggan (nama, telepon, alamat) VALUES (%s, %s, %s)", (nama, telepon, alamat))
                    db.commit()
                    messagebox.showinfo("Sukses", "Pelanggan berhasil ditambahkan!")
                    load_pelanggan()
                    add_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

             # Add Customer Window
            add_window = tk.Toplevel()
            add_window.title("Tambah Pelanggan")
            add_window.geometry("320x280")
            add_window.configure(bg="#f4f4f4")

            tk.Label(add_window, text="Nama:", font=("Arial", 10), bg="#f4f4f4").pack(pady=5)
            entry_nama = tk.Entry(add_window, font=("Arial", 10))
            entry_nama.pack(pady=5, padx=10)

            tk.Label(add_window, text="Telepon:", font=("Arial", 10), bg="#f4f4f4").pack(pady=5)
            entry_telepon = tk.Entry(add_window, font=("Arial", 10))
            entry_telepon.pack(pady=5, padx=10)

            tk.Label(add_window, text="Alamat:", font=("Arial", 10), bg="#f4f4f4").pack(pady=5)
            entry_alamat = tk.Entry(add_window, font=("Arial", 10))
            entry_alamat.pack(pady=5, padx=10)


            tk.Button(add_window, text="Simpan", font=("Arial", 10), command=save_pelanggan, bg="#4CAF50", fg="white", relief="flat").pack(pady=15)


        def edit_pelanggan():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Peringatan", "Pilih pelanggan yang akan diedit!")
                return

            selected_pelanggan = tree.item(selected_item[0], 'values')

            def save_changes():
                nama = entry_nama.get()
                telepon = entry_telepon.get()
                alamat = entry_alamat.get()
                if not nama or not telepon or not alamat:
                    messagebox.showwarning("Peringatan", "Semua field harus diisi!")
                    return
                try:
                    cursor.execute("UPDATE pelanggan SET nama=%s, telepon=%s, alamat=%s WHERE id=%s", 
                                (nama, telepon, alamat, selected_pelanggan[0]))
                    db.commit()
                    messagebox.showinfo("Sukses", "Data pelanggan berhasil diperbarui!")
                    load_pelanggan()
                    edit_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            # Edit Customer Window
            edit_window = tk.Toplevel()
            edit_window.title("Edit Pelanggan")
            edit_window.geometry("320x280")
            edit_window.configure(bg="#f4f4f4")

            tk.Label(edit_window, text="Nama:", font=("Arial", 10), bg="#f4f4f4").pack(pady=5)
            entry_nama = tk.Entry(edit_window, font=("Arial", 10))
            entry_nama.insert(0, selected_pelanggan[1])
            entry_nama.pack(pady=5, padx=10)

            tk.Label(edit_window, text="Telepon:", font=("Arial", 10), bg="#f4f4f4").pack(pady=5)
            entry_telepon = tk.Entry(edit_window, font=("Arial", 10))
            entry_telepon.insert(0, selected_pelanggan[2])
            entry_telepon.pack(pady=5, padx=10)

            tk.Label(edit_window, text="Alamat:", font=("Arial", 10), bg="#f4f4f4").pack(pady=5)
            entry_alamat = tk.Entry(edit_window, font=("Arial", 10))
            entry_alamat.insert(0, selected_pelanggan[3])
            entry_alamat.pack(pady=5, padx=10)

            tk.Button(edit_window, text="Simpan Perubahan", font=("Arial", 10), command=save_changes, bg="#4CAF50", fg="white", relief="flat").pack(pady=15)

        def delete_pelanggan():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Peringatan", "Pilih pelanggan yang akan dihapus!")
                return

            pelanggan_id = tree.item(selected_item[0], 'values')[0]
            if messagebox.askyesno("Konfirmasi", "Anda yakin ingin menghapus pelanggan ini?"):
                try:
                    cursor.execute("DELETE FROM pelanggan WHERE id=%s", (pelanggan_id,))
                    db.commit()
                    reset_auto_increment("pelanggan")  # Reset Auto Increment setelah menghapus data
                    messagebox.showinfo("Sukses", "Data pelanggan berhasil dihapus!")
                    load_pelanggan()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

        # Frame untuk tombol CRUD

        button_frame = tk.Frame(main_content, bg="white")
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Tambah Pelanggan", command=add_pelanggan, font=("Arial", 10), bg="#2196F3", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(button_frame, text="Edit Pelanggan", command=edit_pelanggan, font=("Arial", 10), bg="#FFC107", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(button_frame, text="Hapus Pelanggan", command=delete_pelanggan, font=("Arial", 10), bg="#F44336", fg="white", relief="flat").pack(side="left", padx=5)

        load_pelanggan()

    def reset_auto_increment(table_name):
        try:
            cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1")
            db.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Gagal mereset ID pada tabel {table_name}: {str(e)}")
    
    def show_transaksi():
        clear_main_content()

        tk.Label(main_content, text="Data Transaksi", font=("Arial", 24, "bold"), bg="white").pack(pady=20)
        tree = ttk.Treeview(main_content, columns=(
            "ID", "Pelanggan", "Layanan", "Metode", "Jumlah KG", 
            "Total Harga", "Status", "Tanggal Transaksi", "Tanggal Selesai"
        ), show="headings")
        tree.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        
        # Konfigurasi kolom
        tree.column("ID", width=50, anchor="center")
        tree.column("Pelanggan", width=150)
        tree.column("Layanan", width=120)
        tree.column("Metode", width=100)
        tree.column("Jumlah KG", width=80)
        tree.column("Total Harga", width=100)
        tree.column("Status", width=100)
        tree.column("Tanggal Transaksi", width=120)
        tree.column("Tanggal Selesai", width=120)

        # Konfigurasi heading
        tree.heading("ID", text="ID")
        tree.heading("Pelanggan", text="Pelanggan")
        tree.heading("Layanan", text="Layanan")
        tree.heading("Metode", text="Metode")
        tree.heading("Jumlah KG", text="Jumlah KG")
        tree.heading("Total Harga", text="Total Harga")
        tree.heading("Status", text="Status")
        tree.heading("Tanggal Transaksi", text="Tanggal Transaksi")
        tree.heading("Tanggal Selesai", text="Tanggal Selesai")

        # Konfigurasi warna baris
        tree.tag_configure('oddrow', background='#f8f9fa')  # Baris ganjil
        tree.tag_configure('evenrow', background='white')   # Baris genap

        def load_transaksi():
            tree.delete(*tree.get_children())  # Menghapus semua baris yang ada
            cursor.execute("""
                SELECT t.id, p.nama, l.nama_layanan, m.metode, t.jumlah_kg, t.total_harga, t.status,
                    t.tanggal_transaksi, t.tanggal_selesai,
                    t.id_pelanggan, t.id_layanan, t.id_metode
                FROM transaksi t
                JOIN pelanggan p ON t.id_pelanggan = p.id
                JOIN layanan l ON t.id_layanan = l.id
                JOIN metode_pembayaran m ON t.id_metode = m.id
                ORDER BY t.id DESC
            """)
            
            # Mengambil hasil query
            for index, row in enumerate(cursor.fetchall()):
                # Format tanggal jika ada
                tanggal_transaksi = row[7].strftime("%Y-%m-%d") if row[7] else ""
                tanggal_selesai = row[8].strftime("%Y-%m-%d") if row[8] else ""
                
                # Siapkan data untuk ditampilkan
                display_values = (
                    row[0],              # ID
                    row[1],              # Nama Pelanggan
                    row[2],              # Nama Layanan
                    row[3],              # Metode
                    row[4],              # Jumlah KG
                    f"Rp {row[5]:,}",     # Total Harga
                    row[6],              # Status
                    tanggal_transaksi,   # Tanggal Transaksi
                    tanggal_selesai      # Tanggal Selesai
                )
                
                # Tentukan tag berdasarkan index (ganjil/genap)
                tag = 'oddrow' if index % 2 == 0 else 'evenrow'
                
                # Simpan ID yang tersembunyi untuk keperluan edit (ID Pelanggan, Layanan, dan Metode)
                tree.insert("", "end", values=display_values, tags=(tag, row[9], row[10], row[11]))


        def tambah_pelanggan_baru(parent_window, combo_pelanggan):  # Tambahkan parameter combo_pelanggan
            add_pelanggan_window = tk.Toplevel(parent_window)
            add_pelanggan_window.title("Tambah Pelanggan Baru")
            add_pelanggan_window.geometry("300x250")

            # Frame untuk form
            form_frame = tk.Frame(add_pelanggan_window)
            form_frame.pack(padx=20, pady=20)

            # Input fields
            tk.Label(form_frame, text="Nama:").grid(row=0, column=0, sticky="w", pady=5)
            entry_nama = tk.Entry(form_frame)
            entry_nama.grid(row=0, column=1, sticky="we", pady=5)

            tk.Label(form_frame, text="Telepon:").grid(row=1, column=0, sticky="w", pady=5)
            entry_telepon = tk.Entry(form_frame)
            entry_telepon.grid(row=1, column=1, sticky="we", pady=5)

            tk.Label(form_frame, text="Alamat:").grid(row=2, column=0, sticky="w", pady=5)
            entry_alamat = tk.Entry(form_frame)
            entry_alamat.grid(row=2, column=1, sticky="we", pady=5)

            def save_new_pelanggan():
                try:
                    nama = entry_nama.get()
                    telepon = entry_telepon.get()
                    alamat = entry_alamat.get()
                    
                    if not nama:
                        messagebox.showerror("Error", "Nama pelanggan harus diisi!")
                        return

                    cursor.execute(
                        "INSERT INTO pelanggan (nama, telepon, alamat) VALUES (%s, %s, %s)",
                        (nama, telepon, alamat)
                    )
                    db.commit()
                    
                    # Ambil ID pelanggan yang baru ditambahkan
                    cursor.execute("SELECT LAST_INSERT_ID()")
                    new_id = cursor.fetchone()[0]
                
                    messagebox.showinfo("Sukses", "Pelanggan baru berhasil ditambahkan!")
                
                    # Update combobox pelanggan di form transaksi
                    cursor.execute("SELECT id, nama FROM pelanggan")
                    pelanggan_data = cursor.fetchall()
                    pelanggan_list = [f"{id} - {nama}" for id, nama in pelanggan_data]
                    combo_pelanggan['values'] = pelanggan_list
                    
                    # Set nilai combobox ke pelanggan yang baru ditambahkan
                    combo_pelanggan.set(f"{new_id} - {nama}")
                    
                    add_pelanggan_window.destroy()
                
                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

            tk.Button(form_frame, text="Simpan", command=save_new_pelanggan).grid(row=3, column=0, columnspan=2, pady=20)

        def add_or_edit_transaksi(edit_mode=False, selected_item=None):
            window = tk.Toplevel()
            window.title("Edit Transaksi" if edit_mode else "Tambah Transaksi")
            window.geometry("500x700")
            window.resizable(False, False)
            window.configure(bg="#F9F9F9")

            # Header
            header = tk.Frame(window, bg="#0078D7", height=60)
            header.pack(fill="x")
            header_label = tk.Label(
                header,
                text="Edit Transaksi" if edit_mode else "Tambah Transaksi",
                font=("Montserrat", 16, "bold"),
                bg="#0078D7",
                fg="#FFFFFF"
            )
            header_label.pack(pady=10)

            # Kontainer Form
            form_frame = tk.Frame(window, bg="#FFFFFF", bd=1, relief="solid", padx=20, pady=20)
            form_frame.pack(padx=20, pady=20, fill="both", expand=True)

            # Ambil data untuk combobox
            cursor.execute("SELECT id, nama FROM pelanggan")
            pelanggan_data = cursor.fetchall()
            pelanggan_list = [f"{id} - {nama}" for id, nama in pelanggan_data]

            cursor.execute("SELECT id, nama_layanan, harga_per_kg FROM layanan")
            layanan_data = cursor.fetchall()
            layanan_list = [f"{id} - {nama} (Rp {harga}/kg)" for id, nama, harga in layanan_data]

            cursor.execute("SELECT id, metode FROM metode_pembayaran")
            metode_data = cursor.fetchall()
            metode_list = [f"{id} - {metode}" for id, metode in metode_data]

            # Pelanggan
            tk.Label(form_frame, text="Pelanggan:", font=("Arial", 12), bg="#FFFFFF", fg="#333333").grid(row=0, column=0, sticky="w", pady=10)
            pelanggan_var = tk.StringVar()
            combo_pelanggan = ttk.Combobox(form_frame, textvariable=pelanggan_var, values=pelanggan_list, state="readonly", font=("Arial", 12))
            combo_pelanggan.grid(row=0, column=1, sticky="ew")

            # Tombol Tambah Pelanggan
            tambah_button = tk.Button(
                form_frame,
                text="+",
                font=("Arial", 14, "bold"),
                bg="#0078D7",
                fg="white",
                relief="flat",
                width=3,
                command=lambda: tambah_pelanggan_baru(window, combo_pelanggan)
            )
            tambah_button.grid(row=0, column=2, padx=10, sticky="e")

            # Layanan
            tk.Label(form_frame, text="Layanan:", font=("Arial", 12), bg="#FFFFFF", fg="#333333").grid(row=1, column=0, sticky="w", pady=10)
            layanan_var = tk.StringVar()
            combo_layanan = ttk.Combobox(form_frame, textvariable=layanan_var, values=layanan_list, state="readonly", font=("Arial", 12))
            combo_layanan.grid(row=1, column=1, sticky="ew")

            # Metode Pembayaran
            tk.Label(form_frame, text="Metode Pembayaran:", font=("Arial", 12), bg="#FFFFFF", fg="#333333").grid(row=2, column=0, sticky="w", pady=10)
            metode_var = tk.StringVar()
            combo_metode = ttk.Combobox(form_frame, textvariable=metode_var, values=metode_list, state="readonly", font=("Arial", 12))
            combo_metode.grid(row=2, column=1, sticky="ew")

            # Jumlah KG
            tk.Label(form_frame, text="Jumlah KG:", font=("Arial", 12), bg="#FFFFFF", fg="#333333").grid(row=3, column=0, sticky="w", pady=10)
            entry_kg = tk.Entry(form_frame, font=("Arial", 12))
            entry_kg.grid(row=3, column=1, sticky="ew")

            # Status
            tk.Label(form_frame, text="Status:", font=("Arial", 12), bg="#FFFFFF", fg="#333333").grid(row=4, column=0, sticky="w", pady=10)
            status_var = tk.StringVar(value="Proses")
            combo_status = ttk.Combobox(form_frame, textvariable=status_var, values=["Proses", "Selesai"], state="readonly", font=("Arial", 12))
            combo_status.grid(row=4, column=1, sticky="ew")

            # Tanggal Transaksi
            tk.Label(form_frame, text="Tanggal Transaksi:", font=("Arial", 12), bg="#FFFFFF", fg="#333333").grid(row=5, column=0, sticky="w", pady=10)
            tanggal_transaksi = DateEntry(
                form_frame,
                width=20,
                background='#0078D7',
                foreground='white',
                borderwidth=2,
                date_pattern='yyyy-mm-dd'
            )
            tanggal_transaksi.grid(row=5, column=1, sticky="w")

            # Estimasi Selesai
            tk.Label(form_frame, text="Estimasi Selesai:", font=("Arial", 12), bg="#FFFFFF", fg="#333333").grid(row=6, column=0, sticky="w", pady=10)
            tanggal_selesai = DateEntry(
                form_frame,
                width=20,
                background='#0078D7',
                foreground='white',
                borderwidth=2,
                date_pattern='yyyy-mm-dd'
            )
            tanggal_selesai.grid(row=6, column=1, sticky="w")

            # Total Harga
            tk.Label(form_frame, text="Total Harga:", font=("Arial", 12), bg="#FFFFFF", fg="#333333").grid(row=7, column=0, sticky="w", pady=10)
            label_total = tk.Label(form_frame, text="Rp 0", font=("Arial", 12, "bold"), bg="#FFFFFF", fg="#0078D7")
            label_total.grid(row=7, column=1, sticky="w")

            # Fungsi untuk menghitung total
            def hitung_total(*args):
                try:
                    if layanan_var.get() and entry_kg.get():
                        layanan_id = int(layanan_var.get().split('-')[0])
                        jumlah_kg = float(entry_kg.get())
                        cursor.execute("SELECT harga_per_kg FROM layanan WHERE id=%s", (layanan_id,))
                        harga_per_kg = cursor.fetchone()[0]
                        total = harga_per_kg * jumlah_kg
                        label_total.config(text=f"Rp {total:,.0f}")
                except:
                    label_total.config(text="Rp 0")

            entry_kg.bind('<KeyRelease>', hitung_total)
            combo_layanan.bind('<<ComboboxSelected>>', hitung_total)

            if edit_mode and selected_item:
                item_values = tree.item(selected_item)['values']
                tags = tree.item(selected_item)['tags']
                
                # Set nilai combobox dan entry
                for item in pelanggan_list:
                    if str(tags[0]) in item:
                        combo_pelanggan.set(item)
                        break
                
                for item in layanan_list:
                    if str(tags[1]) in item:
                        combo_layanan.set(item)
                        break
                        
                for item in metode_list:
                    if str(tags[2]) in item:
                        combo_metode.set(item)
                        break
                    
                entry_kg.insert(0, item_values[4])
                status_var.set(item_values[6])
                
                # Set tanggal transaksi dan estimasi selesai
                if len(item_values) > 7:  # Pastikan indeks tersedia
                    try:
                        tanggal_transaksi.set_date(datetime.strptime(item_values[7], "%Y-%m-%d"))
                    except:
                        pass
                if len(item_values) > 8:  # Pastikan indeks tersedia
                    try:
                        tanggal_selesai.set_date(datetime.strptime(item_values[8], "%Y-%m-%d"))
                    except:
                        pass
                
                hitung_total()

            def save_transaksi():
                try:
                    pelanggan_id = int(pelanggan_var.get().split('-')[0])
                    layanan_id = int(layanan_var.get().split('-')[0])
                    metode_id = int(metode_var.get().split('-')[0])
                    jumlah_kg = float(entry_kg.get())
                    total_harga = float(label_total.cget("text").replace("Rp ", "").replace(",", ""))
                    status = status_var.get()
                    tgl_transaksi = tanggal_transaksi.get_date()
                    tgl_selesai = tanggal_selesai.get_date()

                    if edit_mode:
                        transaksi_id = tree.item(selected_item)['values'][0]
                        cursor.execute("""
                            UPDATE transaksi 
                            SET id_pelanggan=%s, id_layanan=%s, id_metode=%s, 
                                jumlah_kg=%s, total_harga=%s, status=%s,
                                tanggal_transaksi=%s, tanggal_selesai=%s
                            WHERE id=%s
                        """, (pelanggan_id, layanan_id, metode_id, jumlah_kg, 
                            total_harga, status, tgl_transaksi, tgl_selesai, transaksi_id))
                        success_message = "Transaksi berhasil diupdate!"
                    else:
                        cursor.execute("""
                            INSERT INTO transaksi 
                            (id_pelanggan, id_layanan, id_metode, jumlah_kg, total_harga, 
                            status, tanggal_transaksi, tanggal_selesai) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, (pelanggan_id, layanan_id, metode_id, jumlah_kg, 
                            total_harga, status, tgl_transaksi, tgl_selesai))
                        success_message = "Transaksi berhasil ditambahkan!"
                    
                    db.commit()
                    messagebox.showinfo("Sukses", success_message)
                    window.destroy()
                    load_transaksi()

                except Exception as e:
                    messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")

            # Tombol Simpan
            button_frame = tk.Frame(form_frame, bg="#FFFFFF")
            button_frame.grid(row=8, column=0, columnspan=3, sticky="e", pady=20)

            tk.Button(
                button_frame,
                text="Simpan",
                font=("Arial", 12, "bold"),
                bg="#0078D7",
                fg="white",
                activebackground="#005BB5",
                activeforeground="white",
                relief="flat",
                command=save_transaksi
            ).pack(side="right", padx=20)

        def edit_transaksi():
            selected_items = tree.selection()
            if not selected_items:
                messagebox.showwarning("Peringatan", "Pilih transaksi yang akan diedit!")
                return
            add_or_edit_transaksi(edit_mode=True, selected_item=selected_items[0])

        def delete_transaksi():
            selected_items = tree.selection()
            if not selected_items:
                messagebox.showwarning("Peringatan", "Pilih transaksi yang akan dihapus!")
                return

            if messagebox.askyesno("Konfirmasi", "Anda yakin ingin menghapus transaksi ini?"):
                try:
                    transaksi_id = tree.item(selected_items[0])['values'][0]
                    cursor.execute("DELETE FROM transaksi WHERE id=%s", (transaksi_id,))
                    db.commit()
                    reset_auto_increment("transaksi")  # Reset Auto Increment setelah menghapus data
                    messagebox.showinfo("Sukses", "Transaksi berhasil dihapus!")
                    load_transaksi()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

        # Frame untuk tombol-tombol CRUD
        button_frame = tk.Frame(main_content, bg="white")
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Tambah Transaksi", command=add_or_edit_transaksi, font=("Arial", 10), bg="#2196F3", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(button_frame, text="Edit Transaksi", command=edit_transaksi, font=("Arial", 10), bg="#FFC107", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(button_frame, text="Hapus Transaksi", command=delete_transaksi, font=("Arial", 10), bg="#F44336", fg="white", relief="flat").pack(side="left", padx=5)
    
        load_transaksi()
    
    # CRUD Jenis Layanan
    def show_jenis_layanan():
        clear_main_content()
    
        tk.Label(main_content, text="Jenis Layanan", font=("Arial", 24, "bold"), bg="white").pack(pady=20)
        tree = ttk.Treeview(main_content, columns=("ID", "Nama Layanan", "Harga per KG"), show="headings")
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="black")  # Menambahkan bold pada heading
        
        tree.heading("ID", text="ID")
        tree.heading("Nama Layanan", text="Nama Layanan", anchor="center")
        tree.heading("Harga per KG", text="Harga per KG")

        # Atur alignment untuk setiap kolom ke tengah
        tree.column("ID", width=50, anchor="center")  # Atur lebar dan posisi tengah
        tree.column("Nama Layanan", width=200, anchor="center")  # Atur lebar dan posisi tengah
        tree.column("Harga per KG", width=150, anchor="center")  # Atur lebar dan posisi tengah
        # Konfigurasi warna baris
        tree.tag_configure('oddrow', background='#f8f9fa')
        tree.tag_configure('evenrow', background='white')

        # Konfigurasi warna baris
        tree.tag_configure('oddrow', background='#f8f9fa')  # Baris ganjil
        tree.tag_configure('evenrow', background='white')   # Baris genap

        def load_layanan():
            tree.delete(*tree.get_children())  # Menghapus semua baris yang ada
            cursor.execute("SELECT * FROM layanan")  # Menjalankan query untuk mengambil data
            for index, row in enumerate(cursor.fetchall()):
                # Tentukan tag yang akan digunakan berdasarkan index baris
                tag = 'oddrow' if index % 2 == 0 else 'evenrow'
                
                # Menambahkan baris ke Treeview dengan tag yang sesuai
                tree.insert("", "end", values=row, tags=(tag,))

        
        def tambah_layanan():
            def simpan_layanan():
                nama = entry_nama.get()
                harga = entry_harga.get()
                if not nama or not harga:
                    messagebox.showwarning("Peringatan", "Semua field harus diisi!")
                    return
                try:
                    cursor.execute("INSERT INTO layanan (nama_layanan, harga_per_kg) VALUES (%s, %s)", (nama, harga))
                    db.commit()
                    messagebox.showinfo("Sukses", "Layanan berhasil ditambahkan!")
                    load_layanan()
                    tambah_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            
            tambah_window = tk.Toplevel()
            tambah_window.title("Tambah Layanan")
            tambah_window.geometry("300x200")
            
            tk.Label(tambah_window, text="Nama Layanan").pack(pady=5)
            entry_nama = tk.Entry(tambah_window)
            entry_nama.pack(pady=5)
            
            tk.Label(tambah_window, text="Harga per KG").pack(pady=5)
            entry_harga = tk.Entry(tambah_window)
            entry_harga.pack(pady=5)
            
            tk.Button(tambah_window, text="Simpan", command=simpan_layanan).pack(pady=20)
        
        def edit_layanan():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Peringatan", "Pilih layanan yang akan diedit!")
                return
            
            selected_layanan = tree.item(selected_item[0], 'values')
            
            def simpan_perubahan():
                nama = entry_nama.get()
                harga = entry_harga.get()
                if not nama or not harga:
                    messagebox.showwarning("Peringatan", "Semua field harus diisi!")
                    return
                try:
                    cursor.execute("UPDATE layanan SET nama_layanan=%s, harga_per_kg=%s WHERE id=%s", (nama, harga, selected_layanan[0]))
                    db.commit()
                    messagebox.showinfo("Sukses", "Layanan berhasil diupdate!")
                    load_layanan()
                    edit_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))
            
            edit_window = tk.Toplevel()
            edit_window.title("Edit Layanan")
            edit_window.geometry("300x200")
            
            tk.Label(edit_window, text="Nama Layanan").pack(pady=5)
            entry_nama = tk.Entry(edit_window)
            entry_nama.insert(0, selected_layanan[1])
            entry_nama.pack(pady=5)
            
            tk.Label(edit_window, text="Harga per KG").pack(pady=5)
            entry_harga = tk.Entry(edit_window)
            entry_harga.insert(0, selected_layanan[2])
            entry_harga.pack(pady=5)
            
            tk.Button(edit_window, text="Simpan", command=simpan_perubahan).pack(pady=20)
        
        def hapus_layanan():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Peringatan", "Pilih layanan yang akan dihapus!")
                return

            layanan_id = tree.item(selected_item[0], 'values')[0]
            if messagebox.askyesno("Konfirmasi", "Anda yakin ingin menghapus layanan ini?"):
                try:
                    cursor.execute("DELETE FROM layanan WHERE id=%s", (layanan_id,))
                    db.commit()
                    reset_auto_increment("layanan")  # Reset Auto Increment setelah menghapus data
                    messagebox.showinfo("Sukses", "Layanan berhasil dihapus!")
                    load_layanan()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

        
        # Frame untuk tombol-tombol CRUD
        button_frame = tk.Frame(main_content, bg="white")
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Tambah Layanan", command=tambah_layanan, font=("Arial", 10), bg="#2196F3", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(button_frame, text="Edit Metode", command=edit_layanan, font=("Arial", 10), bg="#FFC107", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(button_frame, text="Hapus Metode", command=hapus_layanan, font=("Arial", 10), bg="#F44336", fg="white", relief="flat").pack(side="left", padx=5)
        
        load_layanan()

    
    # CRUD Metode Pembayaran
    def show_metode_pembayaran():
        clear_main_content()

        tk.Label(main_content, text="Metode Pembayaran", font=("Arial", 24, "bold"), bg="white").pack(pady=20)
        tree = ttk.Treeview(main_content, columns=("ID", "Metode"), show="headings")
        tree.pack(fill="both", expand=True, padx=10, pady=10)


        # Atur heading dengan lebar kolom
        tree.heading("ID", text="ID")
        tree.column("ID", width=50, anchor="center")  # Perkecil lebar kolom ID

        tree.heading("Metode", text="Metode Pembayaran")
        tree.column("Metode", width=200, anchor="w")  # Sesuaikan lebar kolom metode

        # Konfigurasi warna baris
        tree.tag_configure('oddrow', background='#f8f9fa')
        tree.tag_configure('evenrow', background='white')

        def load_metode():
            tree.delete(*tree.get_children())  # Menghapus semua baris yang ada
            cursor.execute("SELECT * FROM metode_pembayaran")  # Menjalankan query untuk mengambil data
            for index, row in enumerate(cursor.fetchall()):
                # Batasi nama metode jika terlalu panjang
                metode_ringkas = (row[1][:20] + "...") if len(row[1]) > 20 else row[1]
                
                # Tentukan tag yang akan digunakan berdasarkan index baris
                tag = 'oddrow' if index % 2 == 0 else 'evenrow'
                
                # Menambahkan baris ke Treeview dengan tag yang sesuai
                tree.insert("", "end", values=(row[0], metode_ringkas), tags=(tag,))

        def tambah_metode():
            def simpan_metode():
                nama_metode = entry_metode.get()
                if not nama_metode:
                    messagebox.showwarning("Peringatan", "Nama metode pembayaran harus diisi!")
                    return
                try:
                    cursor.execute("INSERT INTO metode_pembayaran (metode) VALUES (%s)", (nama_metode,))
                    db.commit()
                    messagebox.showinfo("Sukses", "Metode pembayaran berhasil ditambahkan!")
                    load_metode()
                    tambah_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            tambah_window = tk.Toplevel()
            tambah_window.title("Tambah Metode Pembayaran")
            tambah_window.geometry("300x150")

            tk.Label(tambah_window, text="Nama Metode Pembayaran").pack(pady=5)
            entry_metode = tk.Entry(tambah_window)
            entry_metode.pack(pady=5)

            tk.Button(tambah_window, text="Simpan", command=simpan_metode).pack(pady=10)

        def edit_metode():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Peringatan", "Pilih metode pembayaran yang akan diedit!")
                return

            selected_metode = tree.item(selected_item[0], 'values')

            def simpan_perubahan():
                nama_metode = entry_metode.get()
                if not nama_metode:
                    messagebox.showwarning("Peringatan", "Nama metode pembayaran harus diisi!")
                    return
                try:
                    cursor.execute("UPDATE metode_pembayaran SET metode=%s WHERE id=%s", (nama_metode, selected_metode[0]))
                    db.commit()
                    messagebox.showinfo("Sukses", "Metode pembayaran berhasil diupdate!")
                    load_metode()
                    edit_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

            edit_window = tk.Toplevel()
            edit_window.title("Edit Metode Pembayaran")
            edit_window.geometry("300x150")

            tk.Label(edit_window, text="Nama Metode Pembayaran").pack(pady=5)
            entry_metode = tk.Entry(edit_window)
            entry_metode.insert(0, selected_metode[1])
            entry_metode.pack(pady=5)

            tk.Button(edit_window, text="Simpan", command=simpan_perubahan).pack(pady=10)

        def hapus_metode():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Peringatan", "Pilih metode pembayaran yang akan dihapus!")
                return

            metode_id = tree.item(selected_item[0], 'values')[0]
            if messagebox.askyesno("Konfirmasi", "Anda yakin ingin menghapus metode pembayaran ini?"):
                try:
                    cursor.execute("DELETE FROM metode_pembayaran WHERE id=%s", (metode_id,))
                    db.commit()
                    messagebox.showinfo("Sukses", "Metode pembayaran berhasil dihapus!")
                    load_metode()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

        # Frame untuk tombol-tombol CRUD
        button_frame = tk.Frame(main_content, bg="white")
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Tambah Metode", command=tambah_metode, font=("Arial", 10), bg="#2196F3", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(button_frame, text="Edit Metode", command=edit_metode, font=("Arial", 10), bg="#FFC107", fg="white", relief="flat").pack(side="left", padx=5)
        tk.Button(button_frame, text="Hapus Metode", command=hapus_metode, font=("Arial", 10), bg="#F44336", fg="white", relief="flat").pack(side="left", padx=5)
        load_metode()

    
    def show_laporan():
        clear_main_content()
        
        # Header section dengan styling modern
        header_frame = tk.Frame(main_content, bg="white")
        header_frame.pack(fill="x", pady=20, padx=30)
        
        tk.Label(
            header_frame,
            text="Laporan Transaksi",
            font=("Montserrat", 24, "bold"),
            bg="white",
            fg="#2c3e50"
        ).pack(side="left")
        
        # Container untuk filter
        filter_frame = tk.Frame(main_content, bg="white", bd=1, relief="solid")
        filter_frame.pack(fill="x", padx=30, pady=(0, 20))
        
        # Inner padding container
        inner_frame = tk.Frame(filter_frame, bg="white", padx=20, pady=15)
        inner_frame.pack(fill="x")
        
        # Label Filter
        tk.Label(
            inner_frame,
            text="Filter Periode",
            font=("Helvetica", 12, "bold"),
            bg="white",
            fg="#34495e"
        ).pack(anchor="w", pady=(0, 10))
        
        # Date filter container
        date_frame = tk.Frame(inner_frame, bg="white")
        date_frame.pack(fill="x")
        
        # Tanggal Mulai
        start_container = tk.Frame(date_frame, bg="white")
        start_container.pack(side="left", padx=(0, 20))
        
        tk.Label(
            start_container,
            text="Tanggal Mulai",
            font=("Helvetica", 10),
            bg="white",
            fg="#7f8c8d"
        ).pack(anchor="w", pady=(0, 5))
        
        entry_mulai = DateEntry(
            start_container,
            width=15,
            background='#0078D7',
            foreground='white',
            borderwidth=0,
            font=("Helvetica", 10),
            date_pattern='yyyy-mm-dd'
        )
        entry_mulai.pack()
        
        # Tanggal Selesai
        end_container = tk.Frame(date_frame, bg="white")
        end_container.pack(side="left")
        
        tk.Label(
            end_container,
            text="Tanggal Selesai",
            font=("Helvetica", 10),
            bg="white",
            fg="#7f8c8d"
        ).pack(anchor="w", pady=(0, 5))
        
        entry_selesai = DateEntry(
            end_container,
            width=15,
            background='#0078D7',
            foreground='white',
            borderwidth=0,
            font=("Helvetica", 10),
            date_pattern='yyyy-mm-dd'
        )
        entry_selesai.pack()
        
        def generate_laporan():
            tanggal_mulai = entry_mulai.get()
            tanggal_selesai = entry_selesai.get()
            
            # Update status label
            status_label.config(
                text=f"Menampilkan laporan untuk periode: {tanggal_mulai} sampai {tanggal_selesai}",
                fg="#27ae60"
            )
            
            # Get report data
            cursor.execute("""
                SELECT t.id, p.nama, l.nama_layanan, t.jumlah_kg, t.total_harga, 
                    t.status, t.tanggal_transaksi, t.tanggal_selesai,
                    COUNT(*) OVER() as total_trans,
                    SUM(t.total_harga) OVER() as total_pendapatan
                FROM transaksi t
                JOIN pelanggan p ON t.id_pelanggan = p.id
                JOIN layanan l ON t.id_layanan = l.id
                WHERE t.tanggal_transaksi BETWEEN %s AND %s
                ORDER BY t.tanggal_transaksi DESC
            """, (tanggal_mulai, tanggal_selesai))
            
            laporan = cursor.fetchall()
            tree.delete(*tree.get_children())
            
            if laporan:
                # Update statistics cards
                total_trans = laporan[0][8]  # Get total transactions from first row
                total_pendapatan = laporan[0][9]  # Get total income from first row
                
                total_trans_label.config(text=str(total_trans))
                total_pendapatan_label.config(text=f"Rp {total_pendapatan:,.0f}")
            else:
                # If no data found, reset statistics to 0
                total_trans_label.config(text="0")
                total_pendapatan_label.config(text="Rp 0")
            
            # Insert data with alternate colors
            for i, row in enumerate(laporan):
                formatted_row = (
                    row[0],
                    row[1],
                    row[2],
                    f"{row[3]:.1f}",
                    f"Rp {row[4]:,.0f}",
                    row[5],
                    row[6].strftime("%d %b %Y"),
                    row[7].strftime("%d %b %Y") if row[7] else "-"
                )
                tree.insert("", "end", values=formatted_row, tags=('oddrow' if i % 2 else 'evenrow',))


        # Button Generate dengan styling
        button_frame = tk.Frame(inner_frame, bg="white")
        button_frame.pack(anchor="w", pady=(15, 0))
        
        generate_button = tk.Button(
            button_frame,
            text="Generate Laporan",
            command=generate_laporan,
            font=("Helvetica", 10, "bold"),
            bg="#0078D7",
            fg="white",
            activebackground="#005BB5",
            activeforeground="white",
            relief="flat",
            padx=15,
            pady=8
        )
        generate_button.pack(side="left")
        
        # Status label
        status_label = tk.Label(
            button_frame,
            text="Pilih periode laporan",
            font=("Helvetica", 10),
            bg="white",
            fg="#7f8c8d"
        )
        status_label.pack(side="left", padx=15)
        
        # Statistics Cards
        stats_frame = tk.Frame(main_content, bg="white")
        stats_frame.pack(fill="x", padx=30, pady=20)
        
        # Total Transaksi Card
        trans_card = tk.Frame(stats_frame, bg="white", bd=1, relief="solid")
        trans_card.pack(side="left", expand=True, fill="x", padx=(0, 10))
        
        tk.Label(
            trans_card,
            text="Total Transaksi",
            font=("Helvetica", 10),
            bg="white",
            fg="#7f8c8d"
        ).pack(pady=(10, 5))
        
        total_trans_label = tk.Label(
            trans_card,
            text="0",
            font=("Helvetica", 16, "bold"),
            bg="white",
            fg="#2c3e50"
        )
        total_trans_label.pack(pady=(0, 10))
        
        # Total Pendapatan Card
        pendapatan_card = tk.Frame(stats_frame, bg="white", bd=1, relief="solid")
        pendapatan_card.pack(side="left", expand=True, fill="x", padx=5)
        
        tk.Label(
            pendapatan_card,
            text="Total Pendapatan",
            font=("Helvetica", 10),
            bg="white",
            fg="#7f8c8d"
        ).pack(pady=(10, 5))
        
        total_pendapatan_label = tk.Label(
            pendapatan_card,
            text="Rp 0",
            font=("Helvetica", 16, "bold"),
            bg="white",
            fg="#27ae60"
        )
        total_pendapatan_label.pack(pady=(0, 10))
        
        # Create Treeview
        tree = ttk.Treeview(
            main_content,
            columns=("ID", "Nama Pelanggan", "Layanan", "Jumlah KG", "Total Harga", 
                    "Status", "Tanggal Transaksi", "Estimasi Selesai"),
            show="headings",
            style="Treeview"
        )
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(main_content, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Configure columns
        tree.column("ID", width=50, anchor="center")
        tree.column("Nama Pelanggan", width=150, anchor="w")
        tree.column("Layanan", width=120, anchor="w")
        tree.column("Jumlah KG", width=100, anchor="center")
        tree.column("Total Harga", width=120, anchor="e")
        tree.column("Status", width=100, anchor="center")
        tree.column("Estimasi Selesai", width=150, anchor="center")
        tree.heading("Estimasi Selesai", text="Estimasi Selesai")
        
        # Configure headings
        tree.heading("ID", text="ID")
        tree.heading("Nama Pelanggan", text="Nama Pelanggan")
        tree.heading("Layanan", text="Layanan")
        tree.heading("Jumlah KG", text="Jumlah KG")
        tree.heading("Total Harga", text="Total Harga")
        tree.heading("Status", text="Status")
        tree.heading("Tanggal Transaksi", text="Tanggal Transaksi")
        
        # Configure row colors
        tree.tag_configure('oddrow', background='#f8f9fa')
        tree.tag_configure('evenrow', background='white')
        
        tree.pack(fill="both", expand=True, padx=30, pady=(0, 30))
    
    def create_sidebar_button(parent, text, command):
        def on_enter(e):
            button["bg"] = "#555575"
        def on_leave(e):
            button["bg"] = "#2F2F3F"

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Arial", 12, "bold"),
            bg="#2F2F3F",
            fg="white",
            activebackground="#555575",
            activeforeground="white",
            bd=0,
            relief="flat",
            pady=10
        )
        button.pack(fill="x", pady=2, padx=10)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    show_dashboard()
    app.mainloop()

# Jalankan login
login()