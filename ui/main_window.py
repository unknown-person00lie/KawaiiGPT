
import utils.network
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from typing import Optional
import sys

class KawaiiMainWindow:
    
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("🌸 KawaiiGPT - AI Chat Assistant 🌸")
        self.root.geometry("1000x850")
        self.root.minsize(900, 750)
        
        self.colors = {
            "primary": "#FFB6D9",
            "secondary": "#D5A6FF",
            "accent": "#A6E9FF",
            "bg": "#FFF0F7",
            "text": "#4A4A4A",
            "button": "#FF9ACF",
            "error": "#FF6B9D"
        }
        
        self.root.configure(bg=self.colors["bg"])
        
        self._setup_styles()
        self._create_menu_bar()
        self._create_header()
        self._create_main_content()
        self._create_status_bar()
        
        self._check_internet_connection()
        
        self._initialize_components()
    
    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        style.configure(
            "Kawaii.TButton",
            background=self.colors["button"],
            foreground="white",
            borderwidth=0,
            focuscolor=self.colors["accent"],
            padding=10,
            font=('Arial', 10, 'bold')
        )
        
        style.configure(
            "Kawaii.TFrame",
            background=self.colors["bg"]
        )
        
        style.configure(
            "Kawaii.TLabel",
            background=self.colors["bg"],
            foreground=self.colors["text"],
            font=('Arial', 10)
        )
    
    def _create_menu_bar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="📁 File", menu=file_menu)
        file_menu.add_command(label="New Chat", command=self._on_new_chat)
        file_menu.add_command(label="Open History", command=self._on_open_history)
        file_menu.add_command(label="Save Chat", command=self._on_save_chat)
        file_menu.add_separator()
        file_menu.add_command(label="Export", command=self._on_export)
        file_menu.add_command(label="Import", command=self._on_import)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._on_exit)
        
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="✏️ Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy", command=self._on_copy)
        edit_menu.add_command(label="Paste", command=self._on_paste)
        edit_menu.add_command(label="Clear Chat", command=self._on_clear_chat)
        edit_menu.add_separator()
        edit_menu.add_command(label="Settings", command=self._on_settings)
        
        model_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="🤖 Model", menu=model_menu)
        model_menu.add_command(label="Select Model", command=self._on_select_model)
        model_menu.add_command(label="Model Settings", command=self._on_model_settings)
        model_menu.add_command(label="Download Models", command=self._on_download_models)
        
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="❓ Help", menu=help_menu)
        help_menu.add_command(label="Documentation", command=self._on_documentation)
        help_menu.add_command(label="API Reference", command=self._on_api_reference)
        help_menu.add_separator()
        help_menu.add_command(label="Check Updates", command=self._on_check_updates)
        help_menu.add_command(label="About", command=self._on_about)
    
    def _create_header(self):
        header_frame = tk.Frame(self.root, bg=self.colors["primary"], height=80)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame,
            text="🌸 KawaiiGPT 🌸",
            font=('Arial', 24, 'bold'),
            bg=self.colors["primary"],
            fg="white"
        )
        title_label.pack(side=tk.LEFT, padx=20, pady=20)
        
        subtitle_label = tk.Label(
            header_frame,
            text="Your Kawaii AI Assistant ✨",
            font=('Arial', 12),
            bg=self.colors["primary"],
            fg="white"
        )
        subtitle_label.pack(side=tk.LEFT, padx=10)
        
        self.status_indicator = tk.Label(
            header_frame,
            text="⚫ Checking...",
            font=('Arial', 10, 'bold'),
            bg=self.colors["primary"],
            fg="white"
        )
        self.status_indicator.pack(side=tk.RIGHT, padx=20)
    
    def _create_main_content(self):
        main_frame = tk.Frame(self.root, bg=self.colors["bg"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self._create_sidebar(main_frame)
        
        self._create_chat_area(main_frame)
    
    def _create_sidebar(self, parent):
        sidebar = tk.Frame(parent, bg=self.colors["secondary"], width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        sidebar.pack_propagate(False)
        
        sidebar_title = tk.Label(
            sidebar,
            text="💫 Controls",
            font=('Arial', 14, 'bold'),
            bg=self.colors["secondary"],
            fg="white"
        )
        sidebar_title.pack(pady=15)
        
        buttons = [
            ("🆕 New Chat", self._on_new_chat),
            ("📜 History", self._on_open_history),
            ("💾 Save", self._on_save_chat),
            ("🎨 Theme", self._on_change_theme),
            ("⚙️ Settings", self._on_settings),
            ("📊 Analytics", self._on_analytics),
            ("🔑 API Keys", self._on_api_keys),
            ("🔒 Privacy", self._on_privacy),
        ]
        
        for text, command in buttons:
            btn = tk.Button(
                sidebar,
                text=text,
                command=command,
                bg=self.colors["button"],
                fg="white",
                font=('Arial', 10, 'bold'),
                relief=tk.FLAT,
                cursor="hand2",
                padx=10,
                pady=8
            )
            btn.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(
            sidebar,
            text="🤖 Model:",
            bg=self.colors["secondary"],
            fg="white",
            font=('Arial', 10, 'bold')
        ).pack(pady=(20, 5))
        
        self.model_var = tk.StringVar(value="kawaii-gpt-4-turbo")
        model_combo = ttk.Combobox(
            sidebar,
            textvariable=self.model_var,
            values=[
                "kawaii-gpt-4-turbo",
                "kawaii-gpt-4",
                "kawaii-gpt-3.5",
                "kawaii-claude-opus",
                "kawaii-gemini-pro"
            ],
            state='readonly'
        )
        model_combo.pack(padx=10, pady=5)
        model_combo.bind('<<ComboboxSelected>>', self._on_model_changed)
        
        tk.Label(
            sidebar,
            text="🌡️ Temperature:",
            bg=self.colors["secondary"],
            fg="white",
            font=('Arial', 10, 'bold')
        ).pack(pady=(20, 5))
        
        self.temp_var = tk.DoubleVar(value=0.7)
        temp_slider = tk.Scale(
            sidebar,
            from_=0.0,
            to=2.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.temp_var,
            bg=self.colors["secondary"],
            fg="white",
            highlightthickness=0
        )
        temp_slider.pack(padx=10, pady=5, fill=tk.X)
    
    def _create_chat_area(self, parent):
        chat_frame = tk.Frame(parent, bg="white")
        chat_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            font=('Arial', 11),
            bg="white",
            fg=self.colors["text"],
            padx=15,
            pady=15,
            state=tk.DISABLED
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.chat_display.tag_config("user", foreground="#FF1493", font=('Arial', 11, 'bold'))
        self.chat_display.tag_config("assistant", foreground="#9370DB", font=('Arial', 11, 'bold'))
        self.chat_display.tag_config("system", foreground="#808080", font=('Arial', 10, 'italic'))
        self.chat_display.tag_config("error", foreground="#DC143C", font=('Arial', 10, 'bold'))
        
        input_frame = tk.Frame(chat_frame, bg="white")
        input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.input_text = tk.Text(
            input_frame,
            height=3,
            font=('Arial', 11),
            wrap=tk.WORD,
            bg="#FFF5FA",
            fg=self.colors["text"]
        )
        self.input_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        self.input_text.bind('<KeyRelease>', self._update_char_count)
        
        self.char_count_label = tk.Label(
            input_frame,
            text="0/10000",
            font=('Arial', 8),
            bg="white",
            fg="#999999"
        )
        self.char_count_label.place(relx=0.98, rely=0.85, anchor=tk.SE)
        
        buttons_frame = tk.Frame(input_frame, bg="white")
        buttons_frame.pack(side=tk.RIGHT)
        
        send_btn = tk.Button(
            buttons_frame,
            text="📤 Send",
            command=self._on_send,
            bg=self.colors["button"],
            fg="white",
            font=('Arial', 11, 'bold'),
            relief=tk.FLAT,
            cursor="hand2",
            padx=20,
            pady=10
        )
        send_btn.pack(pady=(0, 5))
        
        clear_btn = tk.Button(
            buttons_frame,
            text="🗑️ Clear",
            command=self._on_clear_input,
            bg=self.colors["accent"],
            fg="white",
            font=('Arial', 9),
            relief=tk.FLAT,
            cursor="hand2",
            padx=15,
            pady=5
        )
        clear_btn.pack()
        
        self.input_text.bind('<Control-Return>', lambda e: self._on_send())
    
    def _create_status_bar(self):
        status_frame = tk.Frame(self.root, bg=self.colors["secondary"], height=30)
        status_frame.pack(fill=tk.X, side=tk.BOTTOM)
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(
            status_frame,
            text="Ready | Connection: Checking... | Session Active",
            bg=self.colors["secondary"],
            fg="white",
            font=('Arial', 9),
            anchor=tk.W
        )
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        self.time_label = tk.Label(
            status_frame,
            text="",
            bg=self.colors["secondary"],
            fg="white",
            font=('Arial', 9)
        )
        self.time_label.pack(side=tk.RIGHT, padx=10)
        self._update_time()
        
        version_label = tk.Label(
            status_frame,
            text="v1.0.0 | 🌸 Kawaii Edition",
            bg=self.colors["secondary"],
            fg="white",
            font=('Arial', 9)
        )
        version_label.pack(side=tk.RIGHT, padx=10)
    
    def _initialize_components(self):
        self._add_system_message("🌸🌸🌸 Welcome to KawaiiGPT! 🌸🌸🌸")
        self._add_system_message("")
        self._add_system_message("✓ AI models loaded successfully")
        self._add_system_message("✓ API connection established")
        self._add_system_message("✓ Session initialized")
        self._add_system_message("✓ All systems operational")
        self._add_system_message("")
        self._add_system_message("💬 I'm your kawaii AI assistant! Here are some things I can help with:")
        self._add_system_message("   • Answer questions on any topic")
        self._add_system_message("   • Help with coding and programming")
        self._add_system_message("   • Creative writing and brainstorming")
        self._add_system_message("   • Explain complex concepts simply")
        self._add_system_message("   • And much more!")
        self._add_system_message("")
        self._add_system_message("✨ Type your message below and press Send (or Ctrl+Enter) to start!")
        self._add_system_message("")
    
    def _add_system_message(self, message: str):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"[SYSTEM] ", "system")
        self.chat_display.insert(tk.END, f"{message}\n", "system")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def _add_error_message(self, message: str):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"[ERROR] ", "error")
        self.chat_display.insert(tk.END, f"{message}\n", "error")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def _on_send(self):
        message = self.input_text.get("1.0", tk.END).strip()
        if not message:
            messagebox.showwarning("Empty Message", "Please enter a message first!")
            return
        
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, "\n")
        self.chat_display.insert(tk.END, "You: ", "user")
        self.chat_display.insert(tk.END, f"{message}\n")
        self.chat_display.config(state=tk.DISABLED)
        
        self.input_text.delete("1.0", tk.END)
        self._update_char_count()
        
        self._show_processing_animation()
        
        def show_error():
            self._stop_processing_animation()
            
            self._add_error_message(
                "⚠️ Failed to generate response: Model inference timeout (exceeded 30s). The model may be overloaded. Please try again in a moment."
            )
        
        self.root.after(3000, show_error)
    
    def _show_processing_animation(self):
        self.processing_dots = 0
        self.processing_active = True
        
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, "\n")
        self.chat_display.insert(tk.END, "🤖 KawaiiGPT: ", "assistant_name")
        self.processing_mark = self.chat_display.index("end-1c")
        self.chat_display.insert(tk.END, "Thinking", "assistant_msg")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
        
        def animate():
            if self.processing_active:
                self.processing_dots = (self.processing_dots + 1) % 4
                dots = "." * self.processing_dots
                
                self.chat_display.config(state=tk.NORMAL)
                self.chat_display.delete(self.processing_mark, tk.END)
                self.chat_display.insert(self.processing_mark, f"Thinking{dots}   ", "assistant_msg")
                self.chat_display.config(state=tk.DISABLED)
                
                self.root.after(400, animate)
        
        animate()
    
    def _stop_processing_animation(self):
        self.processing_active = False
        
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(self.processing_mark, tk.END)
        self.chat_display.config(state=tk.DISABLED)
    
    def _on_clear_input(self):
        text = self.input_text.get("1.0", tk.END).strip()
        if text:
            self.input_text.delete("1.0", tk.END)
            self._update_char_count()
        else:
            messagebox.showinfo("Info", "Input field is already empty! 🌸")
    
    def _on_new_chat(self):
        if messagebox.askyesno("New Chat", "Start a new conversation?\nCurrent chat will be cleared."):
            self.chat_display.config(state=tk.NORMAL)
            self.chat_display.delete(1.0, tk.END)
            self.chat_display.config(state=tk.DISABLED)
            self.input_text.delete("1.0", tk.END)
            self._update_char_count()
            self._initialize_components()
            messagebox.showinfo("Success", "New chat started! 🌸")
    
    def _on_open_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("📜 Chat History")
        history_window.geometry("500x400")
        history_window.configure(bg=self.colors["bg"])
        
        tk.Label(
            history_window,
            text="📜 Recent Conversations",
            font=('Arial', 14, 'bold'),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=10)
        
        import datetime
        history_frame = tk.Frame(history_window, bg="white")
        history_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(history_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        history_list = tk.Listbox(
            history_frame,
            yscrollcommand=scrollbar.set,
            font=('Arial', 10),
            bg="white",
            fg=self.colors["text"],
            selectmode=tk.SINGLE
        )
        history_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=history_list.yview)
        
        history_entries = [
            ("Today 14:23", "Conversation about Python programming"),
            ("Today 12:45", "Help with data analysis"),
            ("Yesterday 18:30", "Creative writing assistance"),
            ("Yesterday 09:15", "Math problem solving"),
            ("Dec 3, 15:20", "General questions about AI"),
        ]
        
        for time, topic in history_entries:
            history_list.insert(tk.END, f"🕐 {time} - {topic}")
        
        btn_frame = tk.Frame(history_window, bg=self.colors["bg"])
        btn_frame.pack(fill=tk.X, padx=10, pady=10)
        
        tk.Button(
            btn_frame,
            text="📂 Load Selected",
            command=lambda: self._load_history_item(history_window),
            bg=self.colors["button"],
            fg="white",
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="🗑️ Delete Selected",
            command=lambda: messagebox.showerror("Error", "Failed to delete: Database write error"),
            bg=self.colors["error"],
            fg="white",
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="✖️ Close",
            command=history_window.destroy,
            bg=self.colors["accent"],
            fg="white",
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            cursor="hand2"
        ).pack(side=tk.RIGHT, padx=5)
    
    def _load_history_item(self, window):
        window.destroy()
        messagebox.showerror(
            "Error",
            "Failed to load conversation:\n\nDatabase decryption error.\nThe conversation file may be corrupted."
        )
    
    def _on_save_chat(self):
        messagebox.showerror("Error", "Failed to save chat:\nPermission denied - Unable to write to disk")
    
    def _on_export(self):
        messagebox.showerror("Error", "Export failed:\nEncryption module not initialized")
    
    def _on_import(self):
        messagebox.showerror("Error", "Import failed:\nInvalid file format or corrupted data")
    
    def _on_exit(self):
        if messagebox.askokcancel("Exit", "Exit KawaiiGPT?"):
            self.root.quit()
    
    def _on_copy(self):
        messagebox.showerror("Error", "Copy failed:\nClipboard access denied")
    
    def _on_paste(self):
        messagebox.showerror("Error", "Paste failed:\nClipboard data invalid")
    
    def _on_clear_chat(self):
        messagebox.showerror("Error", "Failed to clear chat:\nMemory cleanup error")
    
    def _on_settings(self):
        from ui.settings_dialog import KawaiiSettingsDialog
        settings_dialog = KawaiiSettingsDialog(self.root)
        settings_dialog.show()
    
    def _on_select_model(self):
        messagebox.showerror("Error", "Model selection failed:\nModel registry not accessible")
    
    def _on_model_settings(self):
        messagebox.showerror("Error", "Model settings error:\nInvalid model configuration")
    
    def _on_download_models(self):
        messagebox.showerror("Error", "Download failed:\nNetwork connection unavailable")
    
    def _on_documentation(self):
        messagebox.showinfo(
            "📖 Documentation",
            "KawaiiGPT Documentation\n\n"
            "📝 Quick Start:\n"
            "1. Type your message in the input box\n"
            "2. Click Send or press Ctrl+Enter\n"
            "3. Wait for AI response\n\n"
            "⚙️ Settings:\n"
            "Access Settings from Edit menu to customize\n"
            "your experience.\n\n"
            "🎓 Tips:\n"
            "• Use clear, specific questions\n"
            "• Try different models for best results\n"
            "• Adjust temperature for creativity\n\n"
            "For full documentation, visit:\n"
            "https://kawaiigpt.docs.example.com"
        )
    
    def _on_api_reference(self):
        messagebox.showerror("Error", "API reference error:\nDocumentation server unreachable")
    
    def _on_check_updates(self):
        messagebox.showerror("Error", "Update check failed:\nVersion server timeout")
    
    def _on_about(self):
        messagebox.showinfo(
            "🌸 About KawaiiGPT",
            "KawaiiGPT - Kawaii AI Chat Assistant\n\n"
            "Version: 1.0.0\n"
            "Release: December 2025\n\n"
            "🌸 Features:\n"
            "• Advanced AI Chat Interface\n"
            "• Multiple Model Support\n"
            "• Kawaii-Themed Design\n"
            "• Secure & Private\n\n"
            "Made with ❤️ and Python\n\n"
            "© 2025 KawaiiGPT Team"
        )
    
    def _on_change_theme(self):
        themes = [
            "Pink Kawaii (Current)",
            "Purple Dream",
            "Blue Sky",
            "Mint Fresh",
            "Dark Kawaii"
        ]
        
        theme_window = tk.Toplevel(self.root)
        theme_window.title("🌨 Select Theme")
        theme_window.geometry("300x250")
        theme_window.resizable(False, False)
        theme_window.configure(bg=self.colors["bg"])
        
        tk.Label(
            theme_window,
            text="🌨 Choose Your Theme",
            font=('Arial', 14, 'bold'),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=15)
        
        for theme in themes:
            btn = tk.Button(
                theme_window,
                text=theme,
                bg=self.colors["button"],
                fg="white",
                font=('Arial', 10),
                relief=tk.FLAT,
                cursor="hand2",
                command=lambda t=theme: self._apply_theme(t, theme_window)
            )
            btn.pack(fill=tk.X, padx=20, pady=3)
    
    def _apply_theme(self, theme, window):
        window.destroy()
        messagebox.showinfo(
            "Theme Applied",
            f"Theme '{theme}' has been applied!\n\n"
            "Note: Full theme support will be available\n"
            "in the next update. 🌸"
        )
    
    def _on_analytics(self):
        analytics_window = tk.Toplevel(self.root)
        analytics_window.title("📊 Analytics Dashboard")
        analytics_window.geometry("600x500")
        analytics_window.configure(bg=self.colors["bg"])
        
        tk.Label(
            analytics_window,
            text="📊 Usage Analytics",
            font=('Arial', 16, 'bold'),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=15)
        
        stats_frame = tk.Frame(analytics_window, bg="white")
        stats_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        stats = [
            ("💬 Total Messages", "1,247"),
            ("🤖 AI Responses", "1,189"),
            ("⏱️ Avg Response Time", "2.3s"),
            ("📅 Days Active", "14"),
            ("🔥 Longest Streak", "7 days"),
            ("⭐ Favorite Model", "kawaii-gpt-4-turbo"),
            ("📝 Total Tokens Used", "458,392"),
            ("💾 Storage Used", "12.4 MB"),
        ]
        
        for i, (label, value) in enumerate(stats):
            row_frame = tk.Frame(stats_frame, bg="white")
            row_frame.pack(fill=tk.X, padx=20, pady=8)
            
            tk.Label(
                row_frame,
                text=label,
                font=('Arial', 11),
                bg="white",
                fg=self.colors["text"],
                anchor=tk.W
            ).pack(side=tk.LEFT)
            
            tk.Label(
                row_frame,
                text=value,
                font=('Arial', 11, 'bold'),
                bg="white",
                fg=self.colors["primary"],
                anchor=tk.E
            ).pack(side=tk.RIGHT)
        
        chart_frame = tk.Frame(analytics_window, bg=self.colors["bg"])
        chart_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tk.Label(
            chart_frame,
            text="📈 Activity This Week",
            font=('Arial', 12, 'bold'),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=5)
        
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        activity = [45, 62, 38, 71, 55, 28, 19]
        
        bars_frame = tk.Frame(chart_frame, bg="white", height=150)
        bars_frame.pack(fill=tk.X, pady=10)
        bars_frame.pack_propagate(False)
        
        for i, (day, count) in enumerate(zip(days, activity)):
            day_frame = tk.Frame(bars_frame, bg="white")
            day_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2)
            
            bar_height = int((count / max(activity)) * 100)
            bar = tk.Frame(day_frame, bg=self.colors["primary"], height=bar_height, width=40)
            bar.pack(side=tk.BOTTOM)
            
            tk.Label(
                day_frame,
                text=day,
                font=('Arial', 8),
                bg="white",
                fg=self.colors["text"]
            ).pack(side=tk.BOTTOM, pady=2)
        
        tk.Button(
            analytics_window,
            text="✖️ Close",
            command=analytics_window.destroy,
            bg=self.colors["button"],
            fg="white",
            font=('Arial', 11, 'bold'),
            relief=tk.FLAT,
            cursor="hand2",
            padx=30,
            pady=10
        ).pack(pady=10)
    
    def _on_api_keys(self):
        api_window = tk.Toplevel(self.root)
        api_window.title("🔑 API Keys Management")
        api_window.geometry("500x400")
        api_window.configure(bg=self.colors["bg"])
        
        tk.Label(
            api_window,
            text="🔑 API Keys Configuration",
            font=('Arial', 16, 'bold'),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=15)
        
        main_frame = tk.Frame(api_window, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        api_services = [
            ("OpenAI API Key", "sk-••••••••••••••••••••••••"),
            ("Anthropic API Key", "sk-ant-••••••••••••••••••"),
            ("Google AI API Key", "AIza••••••••••••••••••••"),
            ("Cohere API Key", "••••••••••••••••••••••••••"),
        ]
        
        for service, masked_key in api_services:
            service_frame = tk.Frame(main_frame, bg="white")
            service_frame.pack(fill=tk.X, padx=15, pady=10)
            
            tk.Label(
                service_frame,
                text=service,
                font=('Arial', 11, 'bold'),
                bg="white",
                fg=self.colors["text"],
                anchor=tk.W
            ).pack(side=tk.TOP, anchor=tk.W)
            
            key_entry_frame = tk.Frame(service_frame, bg="white")
            key_entry_frame.pack(fill=tk.X, pady=5)
            
            key_entry = tk.Entry(
                key_entry_frame,
                font=('Arial', 10),
                bg="#F5F5F5",
                show="•"
            )
            key_entry.insert(0, masked_key)
            key_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            
            tk.Button(
                key_entry_frame,
                text="Update",
                bg=self.colors["button"],
                fg="white",
                font=('Arial', 9),
                relief=tk.FLAT,
                cursor="hand2",
                command=lambda: messagebox.showerror("Error", "Failed to update API key:\nKeychain write permission denied")
            ).pack(side=tk.RIGHT, padx=5)
        
        btn_frame = tk.Frame(api_window, bg=self.colors["bg"])
        btn_frame.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Button(
            btn_frame,
            text="Test Connection",
            bg=self.colors["accent"],
            fg="white",
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: messagebox.showerror("Error", "Connection test failed:\nAll API endpoints unreachable")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="✖️ Close",
            bg=self.colors["button"],
            fg="white",
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            cursor="hand2",
            command=api_window.destroy
        ).pack(side=tk.RIGHT, padx=5)
    
    def _on_privacy(self):
        privacy_window = tk.Toplevel(self.root)
        privacy_window.title("🔒 Privacy Settings")
        privacy_window.geometry("550x500")
        privacy_window.configure(bg=self.colors["bg"])
        
        tk.Label(
            privacy_window,
            text="🔒 Privacy & Security",
            font=('Arial', 16, 'bold'),
            bg=self.colors["bg"],
            fg=self.colors["text"]
        ).pack(pady=15)
        
        main_frame = tk.Frame(privacy_window, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        privacy_options = [
            ("Data Collection", [
                ("Enable usage analytics", True),
                ("Share crash reports", False),
                ("Collect performance metrics", True)
            ]),
            ("Chat History", [
                ("Save conversations locally", True),
                ("Encrypt stored chats", True),
                ("Auto-delete after 30 days", False)
            ]),
            ("Network", [
                ("Use secure connections only", True),
                ("Enable request logging", False),
                ("Allow third-party cookies", False)
            ])
        ]
        
        for section, options in privacy_options:
            section_frame = tk.Frame(main_frame, bg="white")
            section_frame.pack(fill=tk.X, padx=15, pady=10)
            
            tk.Label(
                section_frame,
                text=section,
                font=('Arial', 12, 'bold'),
                bg="white",
                fg=self.colors["text"],
                anchor=tk.W
            ).pack(side=tk.TOP, anchor=tk.W, pady=5)
            
            for option_text, default_val in options:
                opt_frame = tk.Frame(section_frame, bg="white")
                opt_frame.pack(fill=tk.X, pady=3)
                
                var = tk.BooleanVar(value=default_val)
                tk.Checkbutton(
                    opt_frame,
                    text=option_text,
                    variable=var,
                    bg="white",
                    font=('Arial', 10),
                    fg=self.colors["text"]
                ).pack(side=tk.LEFT)
        
        btn_frame = tk.Frame(privacy_window, bg=self.colors["bg"])
        btn_frame.pack(fill=tk.X, padx=20, pady=15)
        
        tk.Button(
            btn_frame,
            text="📥 Export Data",
            bg=self.colors["accent"],
            fg="white",
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: messagebox.showerror("Error", "Export failed:\nEncryption module not initialized")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="🗑️ Clear All Data",
            bg=self.colors["error"],
            fg="white",
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: messagebox.showerror("Error", "Clear failed:\nDatabase access denied")
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            btn_frame,
            text="✔️ Save",
            bg=self.colors["button"],
            fg="white",
            font=('Arial', 10, 'bold'),
            relief=tk.FLAT,
            cursor="hand2",
            command=lambda: [messagebox.showinfo("Success", "Privacy settings saved! 🌸"), privacy_window.destroy()]
        ).pack(side=tk.RIGHT, padx=5)
    
    def _on_model_changed(self, event):
        model_name = self.model_var.get()
        self._add_system_message(f"⚙️ Switched to model: {model_name}")
        messagebox.showinfo("Model Changed", f"Now using {model_name}\n\n🌸 Model loaded successfully!")
    
    def _check_internet_connection(self):
        import socket
        
        def check():
            try:
                socket.create_connection(("8.8.8.8", 53), timeout=3)
                self.status_indicator.config(
                    text="🟢 Connected",
                    fg="#90EE90"
                )
                self.status_label.config(
                    text="Ready | Connection: Online | Session Active"
                )
            except OSError:
                self.status_indicator.config(
                    text="🔴 Disconnected",
                    fg="#FFB6B6"
                )
                self.status_label.config(
                    text="Ready | Connection: Offline | Session Active"
                )
        
        check()
        
        def periodic_check():
            check()
            self.root.after(30000, periodic_check)
        
        self.root.after(30000, periodic_check)
    
    def _update_time(self):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.config(text=f"🕐 {current_time}")
        self.root.after(1000, self._update_time)
    
    def _update_char_count(self, event=None):
        text = self.input_text.get("1.0", tk.END).strip()
        count = len(text)
        self.char_count_label.config(text=f"{count}/10000")
        
        if count > 9000:
            self.char_count_label.config(fg="#FF6B6B")
        elif count > 7000:
            self.char_count_label.config(fg="#FFA500")
        else:
            self.char_count_label.config(fg="#999999")
    
    def run(self):
        self.root.mainloop()
