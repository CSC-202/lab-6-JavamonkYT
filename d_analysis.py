# d_analysis.py
## author - Gregory L.

# IMPORTS
import time
import math
import matplotlib.pyplot as plt

import a_iterative_list as List_iter
import a_recursive_list as List_rec

import b_iterative_stack as Stack_iter
import b_recursive_stack as Stack_rec

import c_iterative_queue as Queue_iter
import c_recursive_queue as Queue_rec


# CONSTANTS
N_TRIALS = 100  # TODO run on 20 trials
N_ELEMENTS = 512  # TODO run on 100 elements per trial

# DEFINITIONS
def experiment_list_iter_front(n_trials, n_elements):
    results = []
    def test_list_front(n):
        # initialize the data structure
        list = List_iter.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            list = List_iter.addToFront(list, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_list_front(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_list_iter_back(n_trials, n_elements):
    results = []
    def test_list_back(n):
        # initialize the data structure
        list = List_iter.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            list = List_iter.addToBack(list, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_list_back(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_list_rec_front(n_trials, n_elements):
    results = []
    def test_list_front(n):
        # initialize the data structure
        list = List_rec.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            list = List_rec.addToFront(list, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_list_front(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_list_rec_back(n_trials, n_elements):
    results = []
    def test_list_back(n):
        # initialize the data structure
        list = List_rec.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            list = List_rec.addToBack(list, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_list_back(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time



def experiment_stack_iter_push(n_trials, n_elements):
    results = []
    def test_stack_push(n):
        # initialize the data structure
        stack = Stack_iter.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            stack = Stack_iter.push(stack, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_stack_push(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_stack_iter_pop(n_trials, n_elements):
    results = []
    def test_stack_pop(n):
        # initialize the data structure
        stack = Stack_iter.initialize()
        for i in range(n):
            stack = Stack_iter.push(stack, i)

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            (_, stack) = Stack_iter.pop(stack)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_stack_pop(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_stack_rec_push(n_trials, n_elements):
    results = []
    def test_stack_push(n):
        # initialize the data structure
        stack = Stack_rec.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            stack = Stack_rec.push(stack, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_stack_push(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_stack_rec_pop(n_trials, n_elements):
    results = []
    def test_stack_pop(n):
        # initialize the data structure
        stack = Stack_rec.initialize()
        for i in range(n):
            stack = Stack_rec.push(stack, i)

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            (_, stack) = Stack_rec.pop(stack)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_stack_pop(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time



def experiment_queue_iter_enqueue(n_trials, n_elements):
    results = []
    def test_queue_enqueue(n):
        # initialize the data structure
        queue = Queue_iter.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            queue = Queue_iter.enqueue(queue, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_queue_enqueue(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_queue_iter_dequeue(n_trials, n_elements):
    results = []
    def test_queue_dequeue(n):
        # initialize the data structure
        queue = Queue_iter.initialize()
        for i in range(n):
            queue = Queue_iter.enqueue(queue, i)

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            (_, queue) = Queue_iter.dequeue(queue)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_queue_dequeue(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_queue_rec_enqueue(n_trials, n_elements):
    results = []
    def test_queue_enqueue(n):
        # initialize the data structure
        queue = Queue_rec.initialize()

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            queue = Queue_rec.enqueue(queue, i)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_queue_enqueue(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time


def experiment_queue_rec_dequeue(n_trials, n_elements):
    results = []
    def test_queue_dequeue(n):
        # initialize the data structure
        queue = Queue_rec.initialize()
        for i in range(n):
            queue = Queue_rec.enqueue(queue, i)

        # time the test
        t_0 = time.perf_counter_ns()
        for i in range(n):
            (_, queue) = Queue_rec.dequeue(queue)
        t_1 = time.perf_counter_ns()
        return t_1 - t_0

    for _ in range(n_trials):
        delta_t = test_queue_dequeue(n_elements)
        results.append(delta_t)

    average_time = sum(results) / n_trials
    return average_time



# RUN THE EXPERIMENTS
RESULTS = {
    # list
    'back  (i)': experiment_list_iter_back(N_TRIALS, N_ELEMENTS),
    'front (i)': experiment_list_iter_front(N_TRIALS, N_ELEMENTS),
    'back  (r)': experiment_list_rec_back(N_TRIALS, N_ELEMENTS),
    'front (r)': experiment_list_rec_front(N_TRIALS, N_ELEMENTS),
    # stack
    'push  (i)': experiment_stack_iter_push(N_TRIALS, N_ELEMENTS),
    'pop   (i)': experiment_stack_iter_pop(N_TRIALS, N_ELEMENTS),
    'push  (r)': experiment_stack_rec_push(N_TRIALS, N_ELEMENTS),
    'pop   (r)': experiment_stack_rec_pop(N_TRIALS, N_ELEMENTS),
    # queue
    'enq   (i)': experiment_queue_iter_enqueue(N_TRIALS, N_ELEMENTS),
    'deq   (i)': experiment_queue_iter_dequeue(N_TRIALS, N_ELEMENTS),
    'enq   (r)': experiment_queue_rec_enqueue(N_TRIALS, N_ELEMENTS),
    'deq   (r)': experiment_queue_rec_dequeue(N_TRIALS, N_ELEMENTS)
}

# NORMALIZE THE RESULTS
values = list(RESULTS.values())
squares = [ v*v for v in values ]
norm = math.sqrt(sum(squares))
for experiment in RESULTS:
    RESULTS[experiment] = RESULTS[experiment] / norm

# YOUR CODE GOES BELOW

x = [0,1]
numbers = list(RESULTS.values())
names = list(RESULTS.keys())
figure, axes = plt.subplots(1,3)
plt.suptitle("Leathrum - Lab 6 Analysis")
for plots in range(3):
    axes[plots].set_yticks(ticks=[])
    axes[plots].set_xticks(ticks=[])
structures = ["List", "Stack", "Queue"]


##All the graphs at once
for structure in range(3):
    axes[structure].bar(0, numbers[4*(structure)+2], width=0.8) #Recursive back/push/enq
    axes[structure].bar(1, numbers[4*(structure)+3], width=0.8) #Recursive front/pop/deq
    axes[structure].bar(0, numbers[4*(structure)], width=0.5) #Iterative back/push/enq
    axes[structure].bar(1, numbers[4*(structure)+1], width=0.5) #Iterative front/pop/deq
    axes[structure].legend([names[4*(structure) + 2], names[4*(structure) + 3], names[4*(structure)], names[4*(structure) + 1]])
    axes[structure].set_xlabel(structures[structure])

#RESULTS.keys gets all the names!





## SAVE FIGURE
plt.savefig('C:/Users/grego/Desktop/CalPoly_Senior/CS202/lab-6-nhstaple/figs/leathrum_lab6_analysis.png')
