# Reddit API Project

This project consists of Python scripts for interacting with the Reddit API to retrieve information about subreddits, including the number of subscribers, hot articles, and keyword counts in hot articles.

## Project Structure

- **0-subs.py:** Python script to get the number of subscribers for a given subreddit.
- **2-recurse.py:** Recursive Python script to fetch titles of all hot articles for a given subreddit.
- **100-count.py:** Recursive Python script to count and print the occurrences of specified keywords in hot articles.

## How to Use

### 0-subs.py

```bash
$ python3 0-main.py programming
756024
$ python3 0-main.py this_is_a_fake_subreddit
0
2-recurse.py
bash
Copy code
$ python3 2-main.py programming
932
$ python3 2-main.py this_is_a_fake_subreddit

$ python3 100-main.py programming 'react python java javascript scala no_results_for_this_one'
java: 27
javascript: 20
python: 17
react: 17
scala: 4
Requirements
Python 3
requests library (pip install requests)
Important Notes
Ensure you set a custom User-Agent to avoid Too Many Requests errors.
Invalid subreddits may return a redirect to search results. This project avoids following redirects.
Acknowledgements
This project is part of the ALX School System Engineering & DevOps curriculum.

vbnet
Copy code

Make sure to replace the example commands and descriptions with the actual commands a