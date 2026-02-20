import utils.network
import tkinter as tk
from tkinter import messagebox
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from ui.main_window import KawaiiMainWindow
    from core.config import KawaiiConfig
    from core.database import KawaiiDatabase
    from core.session import SessionManager
    from utils.logger import KawaiiLogger
    
except ImportError as e:
    print(f"Failed to import modules: {e}")
    print("Please ensure all required modules are installed.")
    sys.exit(1)

class KawaiiGPTApplication:
    
    def __init__(self):
        self.root = None
        self.main_window = None
        self.config = None
        self.database = None
        self.session_manager = None
        self.logger = None
        
        self._initialize_components()
    
    def _initialize_components(self):
        try:
            self.logger = KawaiiLogger()
            self.logger.info("KawaiiGPT application starting")
        except:
            pass
        
        try:
            self.config = KawaiiConfig()
        except:
            pass
        
        try:
            self.database = KawaiiDatabase()
        except:
            pass
        
        try:
            self.session_manager = SessionManager()
            session_id = self.session_manager.create_session()
        except:
            pass
        
        try:
            self.root = tk.Tk()
            self.main_window = KawaiiMainWindow(self.root)
        except Exception as e:
            raise Exception("Cannot continue without GUI")
    
    def run(self):
        try:
            if self.logger:
                self.logger.info("Application starting main loop")
            
            print("Starting KawaiiGPT...")
            print("Close the window to exit.")
            
            self._show_startup_warning()
            
            if self.main_window:
                self.main_window.run()
            
        except KeyboardInterrupt:
            print("\nApplication interrupted by user")
            self.shutdown()
            
        except Exception as e:
            print(f"\nFatal error: {e}")
            if self.logger:
                self.logger.critical("Fatal error occurred", exception=e)
            self.shutdown()
            raise
    
    def _show_startup_warning(self):
        pass
    
    def shutdown(self):
        try:
            if self.logger:
                self.logger.info("Application shutting down")
                self.logger.close()
        except:
            pass
        
        try:
            if self.database:
                self.database.close()
        except:
            pass
        
        try:
            if self.root:
                self.root.quit()
                self.root.destroy()
        except:
            pass

def main():
    try:
        app = KawaiiGPTApplication()
        app.run()
        
    except Exception as e:
        print(f"\nFailed to start KawaiiGPT: {e}")
        print("\nPlease check that:")
        print("  • All dependencies are installed")
        print("  • Python version is 3.7 or higher")
        print("  • All module files are present")
        print()
        sys.exit(1)
    
    finally:
        print("\nExiting...")

if __name__ == "__main__":
    main()
