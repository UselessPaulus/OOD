#!C:\Users\ganch\PycharmProjects\MYPROG5\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'kaggle==1.5.0','console_scripts','kaggle'
__requires__ = 'kaggle==1.5.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('kaggle==1.5.0', 'console_scripts', 'kaggle')()
    )
