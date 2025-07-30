# Remote Bash Runner

A simple Python tool that downloads and runs Bash scripts directly from a GitHub repository — no need to clone the entire repo.

## 🔧 Features

- ✅ Fetch a single `.sh` script from a public GitHub repository  
- ✅ Save it with the original name  
- ✅ Prompt for confirmation before execution  
- ✅ Execute using `bash`  
- ✅ Error handling if the script does not exist  

## 📦 Repository Defaults

- **GitHub Repo:** [https://github.com/4D4937/k8s](https://github.com/4D4937/k8s)  
- **Branch:** `main`

## 🚀 Usage

```bash
python3 fetch_and_run.py <script_name>
