#!/usr/bin/python3
import requests
import json
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
        else:
            print("Error print")


def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        structured_posts = []
        for post in posts:
            structured_posts.append = ({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })
        
        with open('posts.csv','w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_posts)
        
        print(f"Status Code: {response.status_code}")
    
    else:
        print("Error save")