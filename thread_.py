import threading
from threading import Thread

def get_current_thread():
    return threading.current_thread()

def get_current_thread_name():
    return get_current_thread().getName()
    
def is_alive(t):
    return t.is_alive()
    
def create_and_start(name, target, daemon = True):
    t = Thread(target= target)
    t.daemon = True
    t.setName(name)
    t.start()
    return t

class ThreadPool(object):
    def __init__(self, capacity = 10):
        try:
            import threadpool
        except:
            print('threadpool is not install. Please run:')
            print('\t pip install threadpool --user')
        self.num_threads = capacity
        self.pool = threadpool.ThreadPool(10)
        
    def add(self, fn, args):
        import threadpool
        if type(args) == list:
            args = [(args, None)]
        elif type(args) == dict:
            args = [(None, args)]
        else:
            raise(ValueError, "Unsuported args,", type(args))
        request = threadpool.makeRequests(fn, args)[0]
        self.pool.putRequest(request, block = False)
        self.pool.poll()
    
    def join(self):
        self.pool.wait()
        
class ProcessPool(object):
    """
    Remember that function in function is not supported by multiprocessing.
    """
    def __init__(self, capacity = 8):
        from multiprocessing import Pool

        self.capacity = capacity
        self.pool = Pool(capacity)
    
    def add(self, fn, args):
        self.pool.apply_async(fn, args)
#         self.pool.poll()
#         self.pool.poll
        
    def join(self):
        self.pool.close()
        self.pool.join()


import multiprocessing as mlp
from multiprocessing import Pool

# # 任务数量
# num =
#
# # 子任务
# def task(s,e):
#     print('sub task')
#
# # 线程池
# p = Pool()
# n_cpu = mlp.cpu_count()
# split = num // n_cpu
#
# for i in range(n_cpu):
#     a = split * i
#     if i == n_cpu - 1:
#         b = num
#     else:
#         b = split * (i + 1)
#     p.apply_async(task, args=(s,e))
#
# p.close()
# p.join()

def multitask(task,num):
    p = Pool()
    n_cpu = mlp.cpu_count()
    split = num // n_cpu

    for i in range(n_cpu):
        s = split * i
        if i == n_cpu - 1:
            e = num
        else:
            e = split * (i + 1)
        p.apply_async(task, args=(s, e))

    p.close()
    p.join()

