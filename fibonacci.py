def fibonacci(n):
    fib_sequance = []
    a, b = 0, 1
    while a <= n:
        fib_sequance.append(a)
        a, b = b, a + b
    return fib_sequance

print(fibonacci(1000))

TASK_KEY = 'task'  
COMPLETED_KEY = 'completed' 

def display_tasks(tasks):  
    if not tasks:  
        print("Your task list is empty.")  
    else:  
        print("\nYour Tasks:")  
        for index, task in enumerate(tasks):  
            print(f"{index + 1}. {task[TASK_KEY]} [{'X' if task[COMPLETED_KEY] else ' '}]")  
    print("")  