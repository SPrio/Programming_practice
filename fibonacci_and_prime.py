#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:53:24 2018

@author: sprio
"""


def fibo(n):
    #print("hello")
    a=0;b=1;c=1;
    for i in range(0,n-1):
        c=a+b
        a=b
        b=c
    return c

def isprime(x):
    #traditional method
    '''
    count=0
    for i in range(1,x+1):
        if(x%i == 0):
            count+=1
    if count==2:
        return 1
    else:
        return 0
    '''
    #new method
    flag = True
    for i in range(2,int(x/2)+1):
        if(x%i==0):
            flag=False
            break
    return flag
        
    
def prime_value(n):
    i=0;j=2;
    while(True):
        if(isprime(j)):
            if(i==n):
                return j
                #break
            i+=1
        j+=1;
            
       
def index_operation(inx):
    if(inx%2==0):
        #print('its even')
        even=1
    else:
        #print('its odd')
        even=0
    if even==1:
        index=int(inx/2)-1
        #print('index is ',index)
        return prime_value(index)
    else:
        index=int(((inx-1)/2)+1)
        #print('index is ',index)
        return fibo(index)

        
if __name__ == '__main__':
    #print (fibo(4),'\n')
    #print(isprime(3))
    #print(isprime(18))
    #print (prime_value(0))
    #print (prime_value(1))
    #print (prime_value(2))
    #print (prime_value(3))
    
    
    print (index_operation(11))
    