

import requests
import os


real_path = os.path.dirname(os.path.realpath(__file__))
print(real_path)

cur_path = os.path.join(real_path, "shelfGroupLevelWare.xlsx")
print(cur_path)


# with open()