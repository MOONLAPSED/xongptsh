import os

import requests


def upload_file(file_path, upload_url):
    with open(file_path, 'rb') as file:
        response = requests.post(upload_url, files={'file': file})
    return response

def download_file(download_url, save_path):
    response = requests.get(download_url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    return save_path

def display_file_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
