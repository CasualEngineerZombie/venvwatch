import os
import subprocess
import time
import sys
from pathlib import Path

class VenvWatch:
    def __init__(self, venv_path=None, interval=5, no_remove=False):
        self.venv_path = venv_path or os.environ.get('VIRTUAL_ENV')
        self.interval = interval
        self.no_remove = no_remove
        self.requirements_file = 'requirements.txt'
        self.last_packages = set()

    def get_pip_path(self):
        if sys.platform == "win32":
            return str(Path(self.venv_path) / "Scripts" / "pip.exe")
        return str(Path(self.venv_path) / "bin" / "pip")

    def get_installed_packages(self):
        pip_path = self.get_pip_path()
        result = subprocess.run([pip_path, "freeze"], capture_output=True, text=True)
        return set(result.stdout.splitlines())

    def update_requirements(self):
        current_packages = self.get_installed_packages()
        
        if current_packages != self.last_packages:
            added = current_packages - self.last_packages
            removed = self.last_packages - current_packages

            with open(self.requirements_file, 'w') as f:
                for package in current_packages:
                    f.write(f"{package}\n")
            
            update_message = f"Updated {self.requirements_file}"
            if added:
                for package in added:
                    update_message += f"\n - Installed: {package}"
            if removed and not self.no_remove:
                for package in removed:
                    update_message += f"\n - Uninstalled: {package}"
            
            print(update_message)

        self.last_packages = current_packages

    def watch(self):
        print(f"Watching virtual environment: {self.venv_path}")
        print(f"Updating {self.requirements_file} every {self.interval} seconds")

        while True:
            self.update_requirements()
            time.sleep(self.interval)