#!/usr/bin/python
from random import shuffle 

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def add_secret_santa(self, secret_santa):
        self.secret_santa = secret_santa
   

def create_list(filename):
    '''
    input: filename with a list of names and corresponding emails (eg. test1 test1@gmail.com)
    output: list of person objects
    '''
    fh = open(filename)
    #list of person objects, everyone in he secret santa
    people_list = []
    for line in fh:
        line = line.split()
        people_list.append(Person(line[0], line[1]))
    return people_list


def match(p_list):
    '''
    input: list of person objects in the order they are written in the text file 
    output: list of person objects with assigned secret santa 
    '''
    #shuffle the original list 
    #this is where the random pick comes from
    shuffle(p_list)
  
    #go through shuffle list and the person before in the list is the current person's secret santa
    #ie person 2's secret santa is person 1 etc. where 1,2 are locations in the list
    #first person in list gets last person
    p_list[0].add_secret_santa(p_list[-1])
    for i in range(1, len(p_list)):
        p_list[i].add_secret_santa(p_list[i-1])
    return p_list


def print_list(people_list):
    for p in people_list:
        print p.name, p.email
        if p.secret_santa:
            print 'is the secret santa of.. %s'%(p.secret_santa.name)


def main():
    p_list = create_list('test.txt')
    p_list = match(p_list)    
    print_list(p_list)


if __name__ == "__main__":
    main()
