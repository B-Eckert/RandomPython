import os
import subprocess

num = 10
st = """
num = """ + str(num-1) + """
if num != 0:
    import os
    import subprocess
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    file = open(os.path.join(__location__, 'child' + str(num) +'.py'), 'w')
    st='print(\"lets see if this works\")'
    file.write(st)
    file.close()
    subprocess.call(['python', 'child' + str(num) + '.py'])
"""

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'child' + str(num) +'.py'), 'w')
file.write(st)
file.close()
subprocess.call(['python', 'child' + str(num) + '.py'])