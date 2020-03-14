import subprocess as cmd

cp = cmd.run("git add -A ", check=True, shell=True)

response = input("m = 'update repository'?(y/n)\n")
message = "update repository"

if response.startswith('n'):
    message = input("Write commit message?\n")

cp = cmd.run(f"git commit -m '{message}'", check=True, shell=True)
cp = cmd.run("git push -u origin master -f", check=True, shell=True)
