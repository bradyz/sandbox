from queue import PriorityQueue
from collections import deque


number_jobs, queue_size = map(int, input().split())

ret = dict()
events = PriorityQueue()
jobs = deque()

for i in range(number_jobs):
    time, duration = map(int, input().split())
    events.put((time, 1, i, duration))

while not events.empty():
    data = events.get()

    if data[1] == 0:
        finish_time, job_number = data[0], data[2]
        ret[job_number] = finish_time
        jobs.popleft()

        if jobs:
            job, duration = jobs.popleft()
            jobs.appendleft((job, duration))
            events.put((finish_time + duration, 0, job))
    else:
        time, job_number, duration = data[0], data[2], data[3]

        if len(jobs) <= queue_size:
            if not jobs:
                events.put((time + duration, 0, job_number))
            jobs.append((job_number, duration))
        else:
            ret[job_number] = -1

print(" ".join(map(lambda x: str(ret[x]), sorted(ret))))
