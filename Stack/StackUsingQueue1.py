import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)  #append/push operation
a = stack.get() #pop operation 
print(a)
# if stack.get() is already empty but we are trying this operation agin then it takes a lot of time. for remove this we need to use "timeout" perameter for example:

stack2 = queue.LifoQueue(3)  #Defineing the limit
stack2.put(10)
stack2.put(20)
stack2.put(30)
stack2.put(40,timeout=1) #So it shows error after 1s 
stack2.get()
stack2.get()
stack2.get()
stack2.get(timeout=1)
print(stack2)


