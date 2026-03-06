import subprocess
import os

os.chdir(r"c:\Users\yf217\Desktop\aichat\开发\开发4.0（纯粹色色）\4.9.9")

subprocess.run(["git", "add", "-A", "."], check=True)
subprocess.run(["git", "reset", "HEAD", "--", "wechat-expense-tracker/"], check=True)
subprocess.run(["git", "reset", "HEAD", "--", "上传指南.md"], check=True)
subprocess.run(["git", "reset", "HEAD", "--", "其他/"], check=True)
subprocess.run(["git", "reset", "HEAD", "--", "git.ps1"], check=True)
subprocess.run(["git", "reset", "HEAD", "--", "git.sh"], check=True)
subprocess.run(["git", "reset", "HEAD", "--", ".gitignore"], check=True)
subprocess.run(["git", "commit", "-m", "Add 2.0 files only"], check=True)
subprocess.run(["git", "push", "-u", "origin", "master"], check=True)

print("Done!")
