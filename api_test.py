# -*- coding utf-8 -*-
import requests
import json

if __name__ == '__main__':
    api_url = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
    response = requests.get(api_url)
    for question in response.json()['items']:
        if question['answer_count']:
            print(f"{question['owner']['display_name']}: {question['title']}")
            print(f"Answers: {question['answer_count']}")
            print(question['link'])
            print()
        else:
            print('skipped')
        print()
