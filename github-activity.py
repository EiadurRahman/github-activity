import requests
import json
import argparse

def fetch_github_user_data(username):
    base_url = f'https://api.github.com/users/{username}/events'

    response = requests.get(base_url)

    if response.status_code == 200:
        json_response = json.dumps(response.json(),indent=4)
        return json_response
    else:
        print('status code : ',response.status_code)
        return None


if __name__ == "__main__":

    # argument parser

    parser = argparse.ArgumentParser(
        description='GitHub User Activity. \nUse GitHub API to fetch user activity and display it in the terminal.',
        epilog='This tool was made as a project challenge from roadmap.sh/python/projects')
    
    parser.add_argument('username',help='github account username')
    args = parser.parse_args()


    data = fetch_github_user_data(args.username)
    print(data)