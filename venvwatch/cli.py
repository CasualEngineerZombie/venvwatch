import argparse
from .core import VenvWatch

def main():
    parser = argparse.ArgumentParser(description="VenvWatch: Automatically update requirements.txt")
    parser.add_argument('--venv', help="Path to the virtual environment")
    parser.add_argument('--interval', type=int, default=5, help="Interval between checks (in seconds)")
    parser.add_argument('--no-remove', action='store_true', help="Don't remove packages from requirements.txt")

    args = parser.parse_args()

    watcher = VenvWatch(venv_path=args.venv, interval=args.interval, no_remove=args.no_remove)
    watcher.watch()

if __name__ == "__main__":
    main()