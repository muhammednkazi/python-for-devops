#example to access environment variables

import os

#cmd to create variable on linux
#export password="12345"

var = os.getenv("password")
print(var)

