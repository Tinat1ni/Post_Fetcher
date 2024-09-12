Post Fetcher

This project is a Python script that fetches posts from a public API (jsonplaceholder.typicode.com) using threading. The results are stored in a JSON file.

Features

Multithreading: The script uses Python's ThreadPoolExecutor to fetch posts concurrently, speeding up the process.
Thread Safety: A Lock is used to ensure thread-safe access to shared resources (the results list).
JSON Output: All fetched posts are saved in a formatted data.json file.

Requirements

Python 3.x
requests library (for making HTTP requests)