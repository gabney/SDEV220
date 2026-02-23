import multiprocessing
import random
import time


def rand_wait(i):
    """
    Waits a random amount of time between 0 and 1 seconds, then returns the current time.
    """
    # generates a random wait time
    wait_time = random.random()
    print(f"Process {i} will wait for {wait_time} seconds.")
    # waits
    time.sleep(wait_time)
    # saves current time
    now = time.time()
    print(f"Time's up! Process {i}'s current time: {now}")

    


# runs only if the program is the main program
if __name__ == "__main__":
    # creates three processes to run the rand_wait function
    for i in range(3): 
        p = multiprocessing.Process(target = rand_wait, args = (i+1,))
        p.start()