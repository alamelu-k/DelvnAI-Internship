PART - A

1.Explain the difference between a process and a thread, in your own words, with one real-life example.

A process is an independent program running on a computer with its own memory and resources. A thread is a smaller unit of a process that shares the same memory with other threads in that process.

Example: A school is a process, and the teachers are threads. The school is one organization, while the teachers perform different tasks at the same time, sharing the same school resources.

2.What is the difference between a LEFT JOIN and an INNER JOIN in SQL? Give a tiny example where they return different results.

An INNER JOIN returns only the rows that have matching values in both tables. A LEFT JOIN returns all rows from the left table and the matching rows from the right table. If there is no match, it returns NULL for the right table.

Example:

Students

ID  Name

1   Asha

2   Ravi

3   Meena


   
Marks

ID  Marks

1   90

2   85

INNER JOIN: Asha, Ravi

LEFT JOIN: Asha, Ravi, Meena (NULL)

3.What does it mean for code to be in version control? Explain what a commit and a pull request are, as
if to a friend who has never coded.

Version control is a system that keeps track of changes made to code, making it easy to restore older versions and work with others.
A commit is a saved snapshot of the code with a message describing the changes.
A pull request is a request to review and merge your changes into the main project after they are approved.

4.You call an API and it is sometimes slow. Name two things that could cause that, and how you would
investigate each

1. Server overload:
If many users send requests at the same time, the server may become slow. I would investigate by checking the server logs and CPU or memory usage.

2. Slow database queries:
If the database takes too long to return data, the API response will be delayed. I would investigate by checking the database logs and query execution time.

PART-B


Description

This program reads transaction data from a CSV file, calculates the total amount for each category, sorts the totals from highest to lowest, and displays the results.

Files

main.py - Python program
transactions.csv - Sample transaction data

How to Run

1. Make sure Python is installed.
2. Keep main.py and transactions.csv in the same folder.
3. Open a terminal in that folder.
4. Run:
   python main.py
   
Sample Output

Software: 2999
Travel: 2000
Food: 750

Error Handling

If a transaction has a missing field or an invalid amount, the program skips that row instead of crashing.

Future Improvement

If I had more time, I would learn more about working with JSON files and update the program to support both CSV and JSON formats. I would also allow users to choose which type of file they want the program to read.

PART - C

While working on Part B, I was not sure how error handling worked in Python. I learned the difference between "ValueError" and "KeyError" and how to use "try" and "except" to handle errors without crashing the program. I also found the sorting part challenging because I was only familiar with basic ascending and descending sorting. I learned how the "sorted()" function can sort dictionary data using a key. 
