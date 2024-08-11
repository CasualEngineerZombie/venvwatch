import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import importlib.metadata

class PackageChangeHandler(FileSystemEventHandler):
    def __init__(self, venv_path, requirements_file):
        self.venv_path = venv_path
        self.requirements_file = requirements_file

    def on_modified(self, event):
        self.update_requirements()

    def update_requirements(self):
        installed_packages = {pkg.metadata['Name']: pkg.metadata['Version'] for pkg in importlib.metadata.distributions()}
        with open(self.requirements_file, 'w') as f:
            for pkg, version in installed_packages.items():
                f.write(f"{pkg}=={version}\n")

def start_watcher(venv_path, requirements_file):
    event_handler = PackageChangeHandler(venv_path, requirements_file)
    observer = Observer()
    observer.schedule(event_handler, path=os.path.join(venv_path, 'lib'), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Watch your virtual environment and sync requirements.txt")
    parser.add_argument('--venv', required=True, help="Path to the virtual environment")
    parser.add_argument('--requirements', default='requirements.txt', help="Path to requirements.txt file")
    args = parser.parse_args()

    start_watcher(args.venv, args.requirements)
