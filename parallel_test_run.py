from subprocess import Popen


processes = []

for counter in range(1):
    chrome_cmd = 'export BROWSER=chrome && python test.py'
    firefox_cmd = 'export BROWSER=firefox && python test.py'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(len(processes)+1):
    processes[counter].run()
