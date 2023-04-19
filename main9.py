from time import sleep, perf_counter
from threading import Thread


def task(number):
    counter = 10
    print(f'Starting a thread #{number}')
    while counter > 0:
        sleep(1)
        print(f'thread #{number} - {counter}')
        counter -= 1

    print('done')


start_time = perf_counter()

# create two new threads
t1 = Thread(target=task, args=(1,))
t2 = Thread(target=task, args=(2,))

# start the threads
t1.start()
t2.start()

# wait for the threads to complete
t2.join()

end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')






