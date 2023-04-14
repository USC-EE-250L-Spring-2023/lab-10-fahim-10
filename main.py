import time
import numpy as np
from typing import List, Optional

import threading
import pandas as pd
import requests
import plotly.express as px

def generate_data() -> List[int]:
    """Generate some random data."""
    return np.random.randint(100, 10000, 1000).tolist()

def process1(data: List[int]) -> List[int]:
    """
    Summary: Calculates the next largest prime number for each elements
    of a list of ints 

    Inputs:
        data: list of ints 
    
    Returns:
        A list that contains the next prime number for each element in the supplied
        input array.    
    """

    def foo(x):
        """Find the next largest prime number."""
        while True:
            x += 1
            if all(x % i for i in range(2, x)):
                return x
    return [foo(x) for x in data]

def process2(data: List[int]) -> List[int]:
    """
    Summary: Calculates the next largest perfect square for each element of
    a list of ints

    Inputs: 
        data: a list of ints

    Returns:
        a list that contains the next largest square for each element of the input array    
    """

    def foo(x):
        """Return the next largest perfect square."""
        while True:
            x += 1
            if int(np.sqrt(x)) ** 2 == x:
                return x
    return [foo(x) for x in data]

def final_process(data1: List[int], data2: List[int]) -> List[int]:
    """
    Summary: Calculates the average of a list that contains the subtraction of each element
    from list 2 from each element of list 1

    Inputs:
        data1: a list of ints
        data2: a list of ints

    Returns:
        Returns the average of a new list that contains the subtraction of each element
        from data2 from data1
    """

    return np.mean([x - y for x, y in zip(data1, data2)])

offload_url = 'http://127.0.0.1:5000' # TODO: Change this to the IP address of your server
offload_url_p1 = offload_url + "/process1"
offload_url_p2 = offload_url + "/process2"

def run(offload: Optional[str] = None) -> float:
    """Run the program, offloading the specified function(s) to the server.
    
    Args:
        offload: Which function(s) to offload to the server. Can be None, 'process1', 'process2', or 'both'.

    Returns:
        float: the final result of the program.
    """
    data = generate_data()
    if offload is None: # in this case, we run the program locally
        data1 = process1(data)
        data2 = process2(data)
    elif offload == 'process1':
        data1 = None
        def offload_process1(data):
            nonlocal data1
            res = requests.post(offload_url_p1, json={"data": data})
            data1 = res.json()

        thread = threading.Thread(target=offload_process1, args=(data,))
        thread.start()
        data2 = process2(data)
        thread.join()
        # Question 2: Why do we need to join the thread here?
        # Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?
        #   See this article: https://oxylabs.io/blog/concurrency-vs-parallelism
        #   ChatGPT is also good at explaining the difference between parallel and concurrent execution!
        #   Make sure to cite any sources you use to answer this question.
    elif offload == 'process2':
        data2 = None
        def offload_process2(data):
            nonlocal data2
            res = requests.post(offload_url_p2, json={"data": data})
            data2 = res.json()
            
        thread = threading.Thread(target=offload_process2, args=(data,))
        thread.start()
        data1 = process1(data)
        thread.join()

    elif offload == 'both':
        data1 = requests.post(offload_url_p1, json={"data": data})
        data1 = data1.json()
        data2 = requests.post(offload_url_p2, json={"data": data})
        data2 = data2.json()


    ans = final_process(data1, data2)
    return ans 

def main():
    # TODO: Run the program 5 times for each offloading mode, and record the total execution time
    #   Compute the mean and standard deviation of the execution times
    #   Hint: store the results in a pandas DataFrame, use previous labs as a reference
    options = [None, 'process1', 'process2', 'both']
    times = []

    for option in options:
        for i in range(0, 5):  
            start = time.process_time()
            result = run(option)
            end = time.process_time()

            delta = end - start
            times.append(delta)

    d = {"none": times[0:5], "process1": times[5:10], "process2": times[10:15], "both": times[15:]}
    df = pd.DataFrame(data=d)

    dfAvgs = df.aggregate(func='mean', axis='index')
    dfStds = df.aggregate(func='std', axis='index')

    # TODO: Plot makespans (total execution time) as a bar chart with error bars
    # Make sure to include a title and x and y labels
    fig = px.bar(dfAvgs, title="Makespan for Different Offloading Methods",  labels={"index": "Offloading Methods", "value": "Makespan (s)"}, error_y=dfStds)
    fig.update_layout(showlegend=False)
    # fig.show()


    # TODO: save plot to "makespan.png"
    fig.write_image("makespan.png")

    # Question 4: What is the best offloading mode? Why do you think that is?
    # Question 5: What is the worst offloading mode? Why do you think that is?
    # Question 6: The processing functions in the example aren't very likely to be used in a real-world application. 
    #   What kind of processing functions would be more likely to be used in a real-world application?
    #   When would you want to offload these functions to a server?
    
    
if __name__ == '__main__':
    main()