# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Fahim Kamal

## Lab Question Answers

Question 1: Under what circumstances do you think it will be worthwhile to offload one or both
of the processing tasks to your PC? And conversely, under what circumstances will it not be
worthwhile?
It will be worthwhile to offload some of the processing tasks to the PC if the time it takes
the PC to execute the code is faster than that of the RPI. This is especially true if are computation is on 
a large input of data. As seen in the makespan.png, the time it takes to do both tasks on the RPI is about
1.6 seconds. Offloading both processes to the computer takes less than 0.1 seconds. As the input sizes to these functions grows, the differences between the time it takes on the RPI vs the computer will also grow. Thus, it is shown that it is worthwhile to offload both processing tasks. 

Question 2: Why do we need to join the thread here?
We need to join the thread to prevent the code from executing further until we have received the computation from the server. After the thread is joined, we can use both data1 and data2 in our final_process. We could not have executed further without having both of these arguments so it was important to join the thread.

Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?The processing functions are executing concurrently because threads execute concurrently.This means that the CPU is able to start and stop these processes very quickly, and is able to switch between them. This results in a speed up of our computation. Executing in parallel would mean that the processes would run on seperate cores or processors where they would actually be occuring at the same time. 

Question 4: What is the best offloading mode? Why do you think that is?
The best offloading mode is 'both' because it has the fastest time of execution. I believe this is because my local machine has a better processor/more ram so it is more quickly able to execute instructions.

Question 5: What is the worst offloading mode? Why do you think that is?
The worst offloading mode is 'none' because it has the slowest time of execution. I believe this is because the RPI is less computationally powerful than a laptop because of the CPU/ram decisions they had to make for the RPI to be modular. 

Question 6: The processing functions in the example aren't very likely to be used in a real-world application. What kind of processing functions would be more likely to be used in a real-world application? When would you want to offload these functions to a server?
I think processing functions that require a lot of computational power or are memory intensive are likely to be used in a real-world application. Some examples may be a database or a machine learning model. Instead of hosting these applications on a embedded device with limited resources, it would be better to do the computation/querying on a server and let the embedded devicee access these resources by making HTTP requests.

