import subprocess as cmd
import sys

cp = cmd.run("git add -A ", check=True, shell=True)

if (len(sys.argv)==0):
    message = input("update the repository")
else: 
    message = sys.argv[1]

cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
cp = cmd.run("git push -u origin master -f", check=True, shell=True)

