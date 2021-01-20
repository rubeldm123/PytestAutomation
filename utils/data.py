import inspect

URL="https://opensource-demo.orangehrmlive.com/"
UserName="Admin"
PassWord="admin123"

def whoami():
    return inspect.stack()[1][3]