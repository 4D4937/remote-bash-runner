import requests
import subprocess
import sys
import os

# GitHub repository configuration
REPO_USER = "4D4937"
REPO_NAME = "k8s"
REPO_BRANCH = "main"

def list_scripts():
    api_url = f"https://api.github.com/repos/{REPO_USER}/{REPO_NAME}/contents?ref={REPO_BRANCH}"
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Available scripts in the repository:")
        for item in response.json():
            if item['type'] == 'file':
                print(f"  - {item['name']}")
    else:
        print(f"Failed to fetch file list (HTTP {response.status_code})")

def download_script(script_name):
    url = f"https://raw.githubusercontent.com/{REPO_USER}/{REPO_NAME}/{REPO_BRANCH}/{script_name}"
    print(f"Fetching script from: {url}")

    response = requests.get(url)
    if response.status_code == 200:
        with open(script_name, "w") as f:
            f.write(response.text)
        print(f"Script saved as: {script_name}")
        return script_name
    else:
        raise FileNotFoundError(f"Script '{script_name}' not found (HTTP {response.status_code}).")

def confirm_and_execute(script_file):
    confirm = input(f"Do you want to execute '{script_file}'? [y/N]: ").strip().lower()
    if confirm == "y":
        os.chmod(script_file, 0o755)
        subprocess.run(["bash", script_file])
    else:
        print("Execution cancelled.")

def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python3 fetch_and_run.py <script_name>   # Download and run a script")
        print("  python3 fetch_and_run.py list            # List available scripts")
        sys.exit(1)

    arg = sys.argv[1]
    if arg == "list":
        list_scripts()
    else:
        try:
            local_file = download_script(arg)
            confirm_and_execute(local_file)
        except FileNotFoundError as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
