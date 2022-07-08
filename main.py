import threading
import time

import numpy as np

from data import Data
from runningui import RunningUi
from startingui import StartingUi
from task import Task

data = Data()
StartingUi(data)

threads = []
tasks = []
for url in data.urls:
    task = Task(url, data.max_sleep_time, data.recipients)
    tasks.append(task)
    threads.append(threading.Thread(target=task.start))

for thread in threads:
    thread.start()
    print(time.ctime())
    time.sleep(np.random.rand() * data.max_sleep_time)

for thread in threads:
    thread.join()

