from subprocess import Popen


processes = []

for counter in range(1):
    #chrome_cmd = 'export BROWSER=chrome && python test.py'
    #firefox_cmd = 'export BROWSER=firefox && python test.py'
    chrome_cmd = 'python -m unittest test.py chrome'
    firefox_cmd = 'python -m unittest test.py firefox'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))
    
    #cmd = '(export BROWSER=firefox && python -m unittest test.py) & (export BROWSER=chrome && python -m unittest test.py)'
    #processes.append(Popen(cmd, shell=True))

for counter in range(len(processes)+1):
    processes[counter].wait()
