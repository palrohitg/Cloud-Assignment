import psutil
import pandas as pd


listOfProcessNames = list()

# list of all process
for proc in psutil.process_iter():
    pid = proc.pid
    name = proc.name()
    cpu_percent = proc.cpu_percent()
    memory = proc.memory_percent()
    listOfProcessNames.append({'pid': pid, 'name': name, 'cpu_percent': cpu_percent,
                              'memory': memory})

# convert into dataframe
df = pd.DataFrame.from_dict(listOfProcessNames, orient='columns')

df.to_csv('file.csv')
