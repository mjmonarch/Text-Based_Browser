import os.path

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# ------------------------------------------------STAGE 1------------------------------------------------
# available_sites = {'nytimes.com': nytimes_com, 'bloomberg.com': bloomberg_com}
#
#
# while True:
#     inp = input()
#     if inp == 'exit':
#         break
#     if inp in available_sites.keys():
#         print(available_sites[inp])

# ------------------------------------------------STAGE 2------------------------------------------------
# import sys
#
#
# def check_url(cmd):
#     if cmd == 'exit':
#         sys.exit()
#     if cmd in available_sites.keys():
#         print(available_sites[cmd])
#         file_name = cmd.rpartition('.')[0]
#         with open(os.path.join(directory, file_name), 'w', encoding='utf-8') as writer:
#             writer.write(available_sites[cmd])
#     else:
#         print("Error: Invalid http address")
#
#
# def check_file(cmd):
#     if cmd == 'exit':
#         sys.exit()
#     if os.path.isfile(os.path.join(directory, cmd)):
#         with open(os.path.join(directory, cmd), 'r', encoding='utf-8') as reader:
#             res = reader.read()
#         print(res)
#     else:
#         check_url(cmd)
#
#
# available_sites = {'nytimes.com': nytimes_com, 'bloomberg.com': bloomberg_com}
#
# args = sys.argv
# if len(args) == 1:
#     directory = '.'
# else:
#     dir_name = args[1]
#     if not os.path.isdir(dir_name):
#         os.mkdir(dir_name)
#     directory = f'./{dir_name}'
#
# # print(directory)
#
# inp1 = input()
# check_url(inp1)
#
# inp2 = input()
# check_file(inp2)

# ------------------------------------------------STAGE 3------------------------------------------------
# import sys
#
#
# def check_url(cmd):
#     if cmd in available_sites.keys():
#         print(available_sites[cmd])
#         file_name = cmd.rpartition('.')[0]
#         with open(os.path.join(directory, file_name), 'w', encoding='utf-8') as writer:
#             writer.write(available_sites[cmd])
#         stack.append(file_name)
#     else:
#         print("Error: Invalid http address")
#
#
# def check_file(cmd):
#     if os.path.isfile(os.path.join(directory, cmd)):
#         with open(os.path.join(directory, cmd), 'r', encoding='utf-8') as reader:
#             res = reader.read()
#         print(res)
#     else:
#         check_url(cmd)
#
#
# available_sites = {'nytimes.com': nytimes_com, 'bloomberg.com': bloomberg_com}
# stack = []
# last_file = ""
#
# args = sys.argv
# if len(args) == 1:
#     directory = '.'
# else:
#     dir_name = args[1]
#     if not os.path.isdir(dir_name):
#         os.mkdir(dir_name)
#     directory = f'./{dir_name}'
#
# inp = input()
# if inp == "exit":
#     sys.exit()
# check_url(inp)
# inp = input()
# while inp != "exit":
#     if inp == "back":
#         try:
#             stack.pop()
#             file = stack[-1]
#             with open(os.path.join(directory, file), 'r', encoding='utf-8') as reader:
#                 res = reader.read()
#             print(res)
#         except IndexError:
#             pass
#     else:
#         check_file(inp)
#     inp = input()

# ------------------------------------------------STAGE 4------------------------------------------------
# import sys
# import requests
#
#
# def check_url(url):
#     if url[:8] != "https://":
#         url = "https://" + url
#     r = requests.get(url)
#     print(r.text)
#     file_name = url.rpartition('.')[0]
#     with open(os.path.join(directory, file_name[8:]), 'w', encoding='utf-8') as writer:
#         writer.write(r.text)
#     stack.append(file_name[8:])
#
#
# def check_file(cmd):
#     if os.path.isfile(os.path.join(directory, cmd)):
#         with open(os.path.join(directory, cmd), 'r', encoding='utf-8') as reader:
#             res = reader.read()
#         print(res)
#     else:
#         check_url(cmd)
#
#
# stack = []
# last_file = ""
#
# args = sys.argv
# if len(args) == 1:
#     directory = '.'
# else:
#     dir_name = args[1]
#     if not os.path.isdir(dir_name):
#         os.mkdir(dir_name)
#     directory = f'./{dir_name}'
#
# inp = input()
# if inp == "exit":
#     sys.exit()
# check_url(inp)
# inp = input()
# while inp != "exit":
#     if inp == "back":
#         try:
#             stack.pop()
#             file = stack[-1]
#             with open(os.path.join(directory, file), 'r', encoding='utf-8') as reader:
#                 res = reader.read()
#             print(res)
#         except IndexError:
#             pass
#     else:
#         check_file(inp)
#     inp = input()

# ------------------------------------------------STAGE 5------------------------------------------------
import sys
import requests
from bs4 import BeautifulSoup


def check_url(url):
    if url[:8] != "https://":
        url = "https://" + url
    try:
        r = requests.get(url)
        if r.status_code != 200:
            print("Incorrect URL")
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            print(soup.getText())
            file_name = url.rpartition('.')[0]
            with open(os.path.join(directory, file_name[8:]), 'w', encoding='utf-8') as writer:
                writer.write(soup.getText())
            stack.append(file_name[8:])
    except requests.exceptions.ConnectionError:
        print("Incorrect URL")


def check_file(cmd):
    if os.path.isfile(os.path.join(directory, cmd)):
        with open(os.path.join(directory, cmd), 'r', encoding='utf-8') as reader:
            res = reader.read()
        print(res)
    else:
        check_url(cmd)


stack = []
last_file = ""

args = sys.argv
if len(args) == 1:
    directory = '.'
else:
    dir_name = args[1]
    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)
    directory = f'./{dir_name}'

inp = input()
if inp == "exit":
    sys.exit()
check_url(inp)
inp = input()
while inp != "exit":
    if inp == "back":
        try:
            stack.pop()
            file = stack[-1]
            with open(os.path.join(directory, file), 'r', encoding='utf-8') as reader:
                res = reader.read()
            print(res)
        except IndexError:
            pass
    else:
        check_file(inp)
    inp = input()