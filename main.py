import os
from dotenv import load_dotenv

from github import Github

import re

load_dotenv()

# Login to github
# g = Github('username','password')

g = Github(os.getenv('TOKEN'))
print('--> Logged in')

user = g.get_user()
print('--> Loaded username from token')

repos = [
    # "Fondamentaux-Python",
    # "Web_Interface_API",
    # "SQL-Postgre-Cloud",
    # "Deep-Learning-Neural-Networks",
    "Deep-Learning-CNN",
    # "Machine-Learning",
    # "Hadoop-Elements",
    # "ETL-Kafka",
    # "ETL-NiFi",
    # "Elastic-Stack",
    # "Data-Visualisation",
    # "Data-Preparation",
    # "NoSQL-MongoDB-Prem",
    # "Web-Scraping",
    # "SQL-Postgre-Prem",
    # "Data-Statistics-Python"
]


def get_repos_contents(repo):
    print("kplr-training/{}".format(repo))
    repo = g.get_repo("kplr-training/{}".format(repo))
    contents = repo.get_contents("")
    count = 0
    while len(contents) > 1:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            if file_content.path[-6:] == ".ipynb":
                convert_base64(repo.get_contents(file_content.path).decoded_content)
    return count


counter = 0


def convert_base64(content):
    global counter
    # print("Content",content)
    found = ""
    try:
        found = re.search('(data:image\/[^;]+;base64[^\"]+)', str(content)).group(1)
        found = found.split(",")[1].split(")")[0]
        print(found)
        from base64topng import convert
        convert(found, "{}.png".format(counter))
        counter += 1
    except AttributeError:
        # AAA, ZZZ not found in the original string
        found = ''  # apply your error handling
    # return str(content).count("(data:image/png;base64,")


count = 0
for repo in repos:
    count += get_repos_contents(repo)

print(count)
