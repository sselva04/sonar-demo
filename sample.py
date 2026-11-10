import subprocess

api_key = "sk-live-12345"

def run_cmd(user_input):
    subprocess.call("ls " + user_input, shell=True)

def check(x):
    if x == 1:
        return "a"
    elif x == 2:
        return "b"
    return "a"

def duplicate_one():
    print("same")
    print("same")
    print("same")

def duplicate_two():
    print("same")
    print("same")
    print("same")
