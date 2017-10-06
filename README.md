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
e.g. python main.py AIzaSyAPbX4JVlc8waFre4Zve1v8zx1VSfhijIk 008083549322187859573:yubw3z65huy 0.9 per se
### d) Internal Design        
1. Input a list of words as user query and a target value as objective precision rate. The program will present all these inputs, including relevant key info as well.        
2. The program calls Google Custom Search API to retrieve top-10 results with current query words, present each result and recieve relevance judgement from user.        
3. Based on relevant and irrelevant results marked by user, the program appply Rocchio algorithm to query in this iteration. In each iteration, it derives at most two new words and reorder words in the new query. Detailed implementation of query-modification method will be discussed in part e. The feedback summary represents query, precision this round, and augmented word for next iteration. As long as the precision is lower than target value, repeat the step 2 and 3.
4. Terminate the programm if calculated precision is equal or larger than target value, which means the desired precision reached. The program will also terminate given no relevant results, which means the query can no longer be augmented.        
### e) Query-modification Method        
1. Preprocess the retrieved top-10 results by removing stop words. If the user query contains certain stop words, remove corresponding words from the stop word list.       
2. Vectorize retrieved results using tf-idf term weighting and initialize the query vector.      
3. Update the query vector using Rocchio algorithm. The equation for updating the query vector is as follows:      
q' = alpha * q + beta / |R_doc| * sum(vector R_doc) - gamma / |NR_doc| * sum(vector NR_doc).       
The parameter alpha, beta and gamma constants are set empirically, and we set alpha = 1, beta = 0.75, gamma = 0.15.
When there is negative term weight in query vector, we set it two be zero.
4. For new query in next iteration, we increase the number of words in query by two, and sort new words by decreasing order of word query scores.
To prevent deletion of query words from original query, we will replace the missing original words from the end of new word list. Derive the augmenting word generated in this iteration and return new query word list.
### f) Relevant Key
**Google Custom Search Engine API Key:**      
AIzaSyAPbX4JVlc8waFre4Zve1v8zx1VSfhijIk       
        
**Engine ID:**        
008083549322187859573:yubw3z65huy
### g) Reference        
1. Modern Information Retrieval: A Brief Overview
2. Introduction to Information Retrieval: Relevance Feedback & Query Expansion

