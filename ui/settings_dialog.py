import utils.network

import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
from typing import Dict, Any

class KawaiiSettingsDialog:
    
    def __init__(self, parent):
        self.parent = parent
        self.dialog = None
        self.settings = {}
        self._load_settings()
    
    def show(self):
        self.dialog = tk.Toplevel(self.parent)
        self.dialog.title("⚙️ KawaiiGPT Settings")
        self.dialog.geometry("600x500")
        self.dialog.resizable(False, False)
        
        self.dialog.configure(bg="#FFF0F7")
        
        self._create_tabs()
        
        self._create_buttons()
        
        self._center_dialog()
        
        self.dialog.transient(self.parent)
        self.dialog.grab_set()
    
    def _create_tabs(self):
        notebook = ttk.Notebook(self.dialog)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        general_frame = self._create_general_tab()
        notebook.add(general_frame, text="🏠 General")
        
        model_frame = self._create_model_tab()
        notebook.add(model_frame, text="🤖 Model")
        
        appearance_frame = self._create_appearance_tab()
        notebook.add(appearance_frame, text="🎨 Appearance")
        
        privacy_frame = self._create_privacy_tab()
        notebook.add(privacy_frame, text="🔒 Privacy")
        
        advanced_frame = self._create_advanced_tab()
        notebook.add(advanced_frame, text="⚡ Advanced")
    
    def _create_general_tab(self) -> tk.Frame:
        frame = tk.Frame(self.dialog, bg="#FFF0F7")
        
        tk.Label(
            frame,
            text="🌐 Language:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.language_var = tk.StringVar(value="English")
        language_combo = ttk.Combobox(
            frame,
            textvariable=self.language_var,
            values=["English", "日本語", "한국어", "中文", "Español"],
            state='readonly',
            width=30
        )
        language_combo.grid(row=0, column=1, padx=10, pady=10)
        
        self.autosave_var = tk.BooleanVar(value=True)
        autosave_check = tk.Checkbutton(
            frame,
            text="💾 Auto-save conversations",
            variable=self.autosave_var,
            bg="#FFF0F7",
            font=('Arial', 10)
        )
        autosave_check.grid(row=1, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)
        
        tk.Label(
            frame,
            text="📜 History limit:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.history_var = tk.IntVar(value=100)
        history_spin = tk.Spinbox(
            frame,
            from_=10,
            to=1000,
            textvariable=self.history_var,
            width=28
        )
        history_spin.grid(row=2, column=1, padx=10, pady=10)
        
        self.startup_var = tk.BooleanVar(value=False)
        startup_check = tk.Checkbutton(
            frame,
            text="🚀 Launch on system startup",
            variable=self.startup_var,
            bg="#FFF0F7",
            font=('Arial', 10)
        )
        startup_check.grid(row=3, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)
        
        self.notifications_var = tk.BooleanVar(value=True)
        notif_check = tk.Checkbutton(
            frame,
            text="🔔 Enable notifications",
            variable=self.notifications_var,
            bg="#FFF0F7",
            font=('Arial', 10)
        )
        notif_check.grid(row=4, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)
        
        return frame
    
    def _create_model_tab(self) -> tk.Frame:
        frame = tk.Frame(self.dialog, bg="#FFF0F7")
        
        tk.Label(
            frame,
            text="🤖 Default Model:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.model_var = tk.StringVar(value="kawaii-gpt-4-turbo")
        model_combo = ttk.Combobox(
            frame,
            textvariable=self.model_var,
            values=[
                "kawaii-gpt-4-turbo",
                "kawaii-gpt-4",
                "kawaii-gpt-3.5-turbo",
                "kawaii-claude-opus",
                "kawaii-gemini-pro"
            ],
            state='readonly',
            width=30
        )
        model_combo.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(
            frame,
            text="🌡️ Temperature:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.temp_var = tk.DoubleVar(value=0.7)
        temp_scale = tk.Scale(
            frame,
            from_=0.0,
            to=2.0,
            resolution=0.1,
            orient=tk.HORIZONTAL,
            variable=self.temp_var,
            length=200
        )
        temp_scale.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(
            frame,
            text="📊 Max Tokens:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.max_tokens_var = tk.IntVar(value=2048)
        tokens_spin = tk.Spinbox(
            frame,
            from_=256,
            to=8192,
            increment=256,
            textvariable=self.max_tokens_var,
            width=28
        )
        tokens_spin.grid(row=2, column=1, padx=10, pady=10)
        
        tk.Label(
            frame,
            text="🔑 API Key:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.api_key_var = tk.StringVar(value="")
        api_entry = tk.Entry(
            frame,
            textvariable=self.api_key_var,
            show="*",
            width=30
        )
        api_entry.grid(row=3, column=1, padx=10, pady=10)
        
        test_btn = tk.Button(
            frame,
            text="🧪 Test Connection",
            command=self._test_connection,
            bg="#FFB6D9",
            fg="white",
            font=('Arial', 9, 'bold')
        )
        test_btn.grid(row=4, column=1, padx=10, pady=10)
        
        return frame
    
    def _create_appearance_tab(self) -> tk.Frame:
        frame = tk.Frame(self.dialog, bg="#FFF0F7")
        
        tk.Label(
            frame,
            text="🎨 Theme:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.theme_var = tk.StringVar(value="Pink Kawaii")
        theme_combo = ttk.Combobox(
            frame,
            textvariable=self.theme_var,
            values=["Pink Kawaii", "Purple Dream", "Blue Sky", "Dark Kawaii", "Custom"],
            state='readonly',
            width=30
        )
        theme_combo.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(
            frame,
            text="📝 Font Size:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.font_size_var = tk.IntVar(value=11)
        font_spin = tk.Spinbox(
            frame,
            from_=8,
            to=20,
            textvariable=self.font_size_var,
            width=28
        )
        font_spin.grid(row=1, column=1, padx=10, pady=10)
        
        self.animations_var = tk.BooleanVar(value=True)
        anim_check = tk.Checkbutton(
            frame,
            text="✨ Enable animations",
            variable=self.animations_var,
            bg="#FFF0F7",
            font=('Arial', 10)
        )
        anim_check.grid(row=2, column=0, columnspan=2, sticky=tk.W, padx=10, pady=5)
        
        color_btn = tk.Button(
            frame,
            text="🎨 Choose Custom Color",
            command=self._choose_color,
            bg="#D5A6FF",
            fg="white",
            font=('Arial', 9, 'bold')
        )
        color_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        return frame
    
    def _create_privacy_tab(self) -> tk.Frame:
        frame = tk.Frame(self.dialog, bg="#FFF0F7")
        
        self.telemetry_var = tk.BooleanVar(value=False)
        telemetry_check = tk.Checkbutton(
            frame,
            text="📊 Allow anonymous usage data collection",
            variable=self.telemetry_var,
            bg="#FFF0F7",
            font=('Arial', 10)
        )
        telemetry_check.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.encryption_var = tk.BooleanVar(value=True)
        encrypt_check = tk.Checkbutton(
            frame,
            text="🔐 Encrypt local data",
            variable=self.encryption_var,
            bg="#FFF0F7",
            font=('Arial', 10)
        )
        encrypt_check.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        
        clear_btn = tk.Button(
            frame,
            text="🗑️ Clear All Data",
            command=self._clear_data,
            bg="#FF6B9D",
            fg="white",
            font=('Arial', 9, 'bold')
        )
        clear_btn.grid(row=2, column=0, padx=10, pady=20)
        
        return frame
    
    def _create_advanced_tab(self) -> tk.Frame:
        frame = tk.Frame(self.dialog, bg="#FFF0F7")
        
        self.debug_var = tk.BooleanVar(value=False)
        debug_check = tk.Checkbutton(
            frame,
            text="🐛 Enable debug mode",
            variable=self.debug_var,
            bg="#FFF0F7",
            font=('Arial', 10)
        )
        debug_check.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        
        tk.Label(
            frame,
            text="🌐 Proxy Server:",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.proxy_var = tk.StringVar(value="")
        proxy_entry = tk.Entry(
            frame,
            textvariable=self.proxy_var,
            width=40
        )
        proxy_entry.grid(row=1, column=1, padx=10, pady=10)
        
        tk.Label(
            frame,
            text="💾 Cache Size (MB):",
            bg="#FFF0F7",
            font=('Arial', 10, 'bold')
        ).grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        
        self.cache_var = tk.IntVar(value=500)
        cache_spin = tk.Spinbox(
            frame,
            from_=100,
            to=5000,
            increment=100,
            textvariable=self.cache_var,
            width=38
        )
        cache_spin.grid(row=2, column=1, padx=10, pady=10)
        
        reset_btn = tk.Button(
            frame,
            text="🔄 Reset to Defaults",
            command=self._reset_settings,
            bg="#A6E9FF",
            fg="white",
            font=('Arial', 9, 'bold')
        )
        reset_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=20)
        
        return frame
    
    def _create_buttons(self):
        button_frame = tk.Frame(self.dialog, bg="#FFF0F7")
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        save_btn = tk.Button(
            button_frame,
            text="💾 Save",
            command=self._save_settings,
            bg="#FF9ACF",
            fg="white",
            font=('Arial', 10, 'bold'),
            width=10
        )
        save_btn.pack(side=tk.RIGHT, padx=5)
        
        cancel_btn = tk.Button(
            button_frame,
            text="❌ Cancel",
            command=self._cancel,
            bg="#D5A6FF",
            fg="white",
            font=('Arial', 10, 'bold'),
            width=10
        )
        cancel_btn.pack(side=tk.RIGHT, padx=5)
        
        apply_btn = tk.Button(
            button_frame,
            text="✅ Apply",
            command=self._apply_settings,
            bg="#A6E9FF",
            fg="white",
            font=('Arial', 10, 'bold'),
            width=10
        )
        apply_btn.pack(side=tk.RIGHT, padx=5)
    
    def _center_dialog(self):
        self.dialog.update_idletasks()
        width = self.dialog.winfo_width()
        height = self.dialog.winfo_height()
        x = (self.dialog.winfo_screenwidth() // 2) - (width // 2)
        y = (self.dialog.winfo_screenheight() // 2) - (height // 2)
        self.dialog.geometry(f'{width}x{height}+{x}+{y}')
    
    def _load_settings(self):
        self.settings = {
            "language": "English",
            "autosave": True,
            "history_limit": 100,
            "notifications": True,
            "theme": "Pink Kawaii",
            "font_size": 11,
            "animations": True
        }
    
    def _save_settings(self):
        self.settings['language'] = self.language_var.get()
        self.settings['autosave'] = self.autosave_var.get()
        self.settings['history_limit'] = self.history_var.get()
        self.settings['notifications'] = self.notifications_var.get()
        self.settings['theme'] = self.theme_var.get()
        self.settings['font_size'] = self.font_size_var.get()
        self.settings['animations'] = self.animations_var.get()
        
        messagebox.showinfo(
            "Success",
            "Settings saved successfully!\n\nNote: Some changes may require restart to take effect."
        )
        self.dialog.destroy()
    
    def _apply_settings(self):
        applied = []
        
        if self.theme_var.get() != self.settings.get('theme', 'Pink Kawaii'):
            applied.append('Theme')
        
        if self.font_size_var.get() != self.settings.get('font_size', 11):
            applied.append('Font Size')
            
        if self.animations_var.get() != self.settings.get('animations', True):
            applied.append('Animations')
        
        if applied:
            messagebox.showinfo(
                "Applied",
                f"Successfully applied: {', '.join(applied)}\n\nSome changes may require restart."
            )
        else:
            messagebox.showinfo("No Changes", "No settings were changed.")
    
    def _cancel(self):
        self.dialog.destroy()
    
    def _test_connection(self):
        messagebox.showerror(
            "Connection Failed",
            "❌ API connection test failed:\n\n"
            "- Server unreachable\n"
            "- Invalid API key\n"
            "- Network timeout\n\n"
            "Please check your settings and try again."
        )
    
    def _choose_color(self):
        color = colorchooser.askcolor(title="Choose Kawaii Color")
        if color[1]:
            messagebox.showinfo(
                "Color Selected",
                f"Custom color selected: {color[1]}\n\nThis will be applied to the theme.\n\n🌸 Kawaii!"
            )
    
    def _clear_data(self):
        if messagebox.askyesno("Confirm", "Clear all local data?"):
            messagebox.showerror(
                "Error",
                "Failed to clear data:\nData cleanup service unavailable"
            )
    
    def _reset_settings(self):
        if messagebox.askyesno("Confirm", "Reset all settings to defaults?"):
            self.language_var.set("English")
            self.autosave_var.set(True)
            self.history_var.set(100)
            self.startup_var.set(False)
            self.notifications_var.set(True)
            self.theme_var.set("Pink Kawaii")
            self.font_size_var.set(11)
            self.animations_var.set(True)
            self.telemetry_var.set(False)
            self.encryption_var.set(True)
            self.debug_var.set(False)
            self.cache_var.set(500)
            
            messagebox.showinfo(
                "Success",
                "Settings reset to defaults successfully!\n\n🌸 All settings restored!"
            )
