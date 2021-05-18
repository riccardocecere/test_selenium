from subprocess import Popen


processes = []

for counter in range(1):
    #chrome_cmd = 'export BROWSER=chrome && python test.py'
    #firefox_cmd = 'export BROWSER=firefox && python test.py'
    cmd = 'python -m unittest test.py'
    cmd = 'python -m unittest test.py'
    processes.append(Popen(cmd, args=['chrome'], shell=True))
    processes.append(Popen(cmd, arges=['firefox'],  shell=True))
    
    #cmd = '(export BROWSER=firefox && python -m unittest test.py) & (export BROWSER=chrome && python -m unittest test.py)'
    #processes.append(Popen(cmd, shell=True))

for counter in range(len(processes)+1):
    processes[counter].wait()
