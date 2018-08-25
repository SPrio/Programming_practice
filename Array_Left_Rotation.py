#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:24:13 2018

@author: sprio
"""

a=list()
a = [int(x) for x in input('Enter the list ').split()]#print(a)
n=int(input('How many times you want to do left rotation '))


'''int actualRotations = k % n;
		int newArray[]      = new int[n];
		int currentIndex    = 0;

		for (int i = actualRotations ; i < n ; i++ ) {
			newArray[currentIndex] = a[i];
			currentIndex++;
		}

		for (int i = 0; i < actualRotations; i++ ) {
			newArray[currentIndex] = a[i];
			currentIndex++;
		}

for i in range(1,n1+1):
    for j in range(len(a)-1):
        a[j],a[j+1]=a[j+1],a[j]
        '''
        
n1=n%len(a)
n2=len(a)
a1=a.copy()
currentIndex=0

for i in range( n1,n2) :
		a1[currentIndex] = a[i]
		currentIndex+=1
		

for i in range( 0, n1) :
		a1[currentIndex] = a[i]
		currentIndex+=1
		
print(a1)
        
    