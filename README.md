# Information-Retrieval-System
## COMS E6111 Advanced Database System - Project 1  
### a) Project 1 Group6
  Wanheng Li (wl2573)    
  Yibo Xu (yx2387)
### b) List of Files    
main.py   
wordExpansion.py     
stopwords.txt       
transcript.txt
### c) Instruction for Running the Program
**Installation:**         
pip install --upgrade google-api-python-client    
pip install beautifulsoup4     
pip install -U scikit-learn     

**Command:**    
Please run the program with following commond:    
[Directory]   [API Key] [Engine Key] [Query] [Precision]      
e.g. main.py AIzaSyAPbX4JVlc8waFre4Zve1v8zx1VSfhijIk 008083549322187859573:yubw3z65huy 0.9 per se
### d) Internal Design        
1. Input a list of words as user query and a target value as objective precision rate. The program will present all these inputs, including relevant key info as well.        
2. The program will call Google Custom Search API to retrieve top-10 results for current query words, present each result and recieve relevance judgement from user.        
3. Based on relevant and irrelevant results marked by user, the program appply Rocchio algorithm to query in this iteration. In each iteration, it derives at most two new words and reorder words in the new query. Detailed implementation of query-modification method will be discussed in part e. The feedback summary represents query, precision this round, and augmented word for next iteration. As long as the precision is lower than target value, repeat the step 2 and 3.
4. Terminate the programm if calculated precision is equal or larger than target value, which means the desired precision reached. The program will also stop given no relevant results, which means the query can no longer be augmented.        
### e) Query-modification Method
### f) Relevant Key
**Google Custom Search Engine API Key:**      
AIzaSyAPbX4JVlc8waFre4Zve1v8zx1VSfhijIk       
        
**Engine ID:**        
008083549322187859573:yubw3z65huy
### g) Reference

