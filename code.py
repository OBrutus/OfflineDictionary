#!/bin/python3
from difflib import get_close_matches
import json

path_to_json='$HOME/.Dictionary_AV/'
data = json.load(open(path_to_json))
list_of_cmd=[\
	'refresh',\
	'insert',\
	'exit'\
]

def search(word):
    if word in data: 
        result= data[word]
        if len(result)>0:
            if len(result)==1:
                return result
            else:
                for i in range(0,len(result)-1):
                    print (result[i], "/n")
                return (result[i+1])
    elif len(get_close_matches(word,data.keys())) > 0:
        print ("Did you mean: " , get_close_matches(word,data.keys())[0])
        decision = input("Enter y if yes, n if no: ")
        decision=str.lower(decision)
        if decision == "y":
            result = data[get_close_matches(word,data.keys())[0]]
            if len(result)>0:
                if len(result)==1:
                    return result
                else:
                    for i in range(0,len(result)-1):
                        print (result[i], "/n")
                    return (result[i+1])
        elif decision == "n":
            return ("Sorry, I'm unable to find the word that you were searchning for")
    else:
        return ("Sorry, I'm unable to find the word that you were searchning for")

def banner():
	import os
	print('Developed by Aniket ')
	print('visit : https://github.com/OBrutus ')
	os.system('figlet "  Dictionary"')


def exec_cmd(cmd):
	if cmd=='refresh':
		print('json refreshing ...')
		data = json.load(open(path_to_json))
	elif cmd=='add':
		word=input('Enter the word : '  )
		meaning=[]
		x='AV';
		while x!='':
			x=input("Enter the meaning [hit enter when done] : ")
			meaning.append(x)
		data[word]=meaning
		print('writing ... ')
		json.dump(data, open(path_to_json, 'w'))
		exec_cmd('refresh')
	elif cmd=='exit':
		print('For any query / suggestion do visit : https://github.com/OBrutus ')
		print('Thank You !')
		exit()
	else:
		print('Invalid cmd, here are list of commands')
		for cmd in list_of_cmd:
			print('\t'+cmd)

if __name__=='__main__':
	banner()
	try:
		while(True):
			print('*'*10)
			word=input("Enter the word to search: ")
			word = str.lower(word)
			if(word[0]=='/'):
				exec_cmd(word[1:])
				continue
			print(search(word))
	except(KeyboardInterrupt):
		print("Byee ... ! ");
