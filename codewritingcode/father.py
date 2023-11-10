import os
import subprocess

num = 10
st = 'num = ' + str(num-1) + '\n'
st += 'if num != 0:\n'
st += '\timport os\n\timport subprocess\n'
st+= "\t__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))\n"
st+= "\tfile = open(os.path.join(__location__, 'child' + str(num) +'.py'), 'w')\n"
st+= "\tst='print(\"lets see if this works\")'\n"
st+= "\tfile.write(st)\n"
st+= "\tfile.close()\n"
st+= "\tsubprocess.call(['python', 'child' + str(num) + '.py'])\n"

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
file = open(os.path.join(__location__, 'child' + str(num) +'.py'), 'w')
file.write(st)
file.close()
subprocess.call(['python', 'child' + str(num) + '.py'])