# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:59:57 2017

@author: localadmin
"""

import numpy as np
import Tkinter, tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw()
import os
from os.path import basename
import ntpath
import matplotlib.pyplot as plt


ntpath.basename("a/b/c")

file_path = tkFileDialog.askopenfilename()


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)
print path_leaf(file_path)

def loadarray():
    #reads coloumn1 from txt / skips first rows (3), 
    liste1=np.loadtxt(file_path, skiprows=(4), usecols=(0,))
    #reads coloumn2 from txt / skips first rows (3), 
    liste=np.loadtxt(file_path, skiprows=(4), usecols=(1,))
    #converts loaded coloumn1 to an numpy array:
    matrix1 = np.array((liste1))
    #converts loaded coloumn2 to an numpy array:
    aa = np.array((liste))
    #joins the arrays into a 2xN array 
    submatrix1= np.column_stack((matrix1, aa))
    submatrix1.view('i8,i8').sort(order=['f0'], axis=0)
    return submatrix1
    
def minimum_bin(array, increment):
    i=0
    N=len(array)
    minsize=increment
    while i<N-1:
        test=array[i+1,0]-array[i,0]
        if test >   1.5*increment:
            print "binsize too small"
            return test

        else:
            i=i+1

def distance_to_next_bin(delta_bin,increment) :
    j=0
    while j==0:
       case1=delta_bin
       
       if case1>increment:
           #print "over bin - case switch"
           return 0
       else:
          # print "shrink"
           return 1
    j=i+1
    
def extract_subarray(matrix,low,high):
    sub1x=low
    sub2x=high
    sub1y=low
    sub2y=high
    extracted=matrix[sub1x:sub2x,]
    return extracted

def sum_extracted(matrix):
    N=len(matrix)
    i=0
    while i<N-1:
        matrix[i,1]=matrix[i,1]+matrix[i+1,1]
        matrix[i,0]=matrix[i+1,0]
        matrix=np.delete(matrix,i+1, 0)  
        N=len(matrix)
        
    else:
        print matrix
        return matrix
        
def plot_xy(array,colour,name):
    x = array[:,0]
    y = array[:,1]
    plot=plt.scatter(x, y, color=colour,label=name)
    plt.legend(handles=[plot])
    plt.ylabel(name)
    plt.show()
    
def print_to_file(matrix,increment):
    print "now to file"
    np.savetxt("20150318_inco"+"_"+ repr(increment)+".txt", matrix[:], fmt='%.3E', delimiter='\t')
    return matrix
    
        
def shrink_subarray(matrix,i,increment):
    x = repr(increment)
    x=len(str(x).split(".")[1])
    first_element=matrix[0,0]
    matrix[0,0]=round(first_element,x)
#    print "first bin", matrix[0]
    i=1
    N=len(matrix)
    while i<=N:
        low=matrix[i-1,0]
        high = matrix[i,0]
        delta_bin=high-low
        #print "highlow", high, low
        print "delta_bin", delta_bin
        print "matrix elments", high,low
        case=distance_to_next_bin(delta_bin,increment)
        if case==0 and len(matrix)-i>=2:
            #how_often=delta_bin/increment
            #print "alt i+1", matrix[i+1]
            #print "alt i", matrix[i]            
            old= matrix[i,0]
            matrix[i,0]=matrix[i-1,0]+increment
            
            restx = old-matrix[i,0]
            rest2=(restx/increment)*matrix[i,1]
            #print "rest 2 x und y", restx, rest2
            #matrix[i,1]=(1-restx)*matrix[i,1]
            matrix[i,1]=matrix[i,1]-rest2
            matrix[i+1,1]=matrix[i+1,1]+rest2
            matrix[i+1,0]=matrix[i+1,0]+restx
            #print "corrected bin point i+1", matrix[i+1]
            #print "corrected bin point i", matrix[i]
            i=i+1

        elif case==1 and len(matrix)-i>=2:
                # macht weiter - tested am Anfang der whileschleife
                #wahlweise low=matrix[i-1,0]
       # arr2 = matrix[i]+matrix[i+1] - matrix[i,0]
            sum_value=matrix[i,1]+matrix[i+1,1]
           #print matrix[i,1],"+",matrix[i+1,1], "=",sum_value      
            matrix[i,1]=sum_value
            shrinked_y=matrix[i+1,0]
            matrix[i,0]=shrinked_y
           #print "deleted:", matrix[i+1,]
            matrix=np.delete(matrix,i+1, 0)   
            print "i", i
            
        else:
            print "stopp"
            print "letztes bin:", delta_bin
            rest=len(matrix)-i
            restmatrix=extract_subarray(matrix,i,N)
            #print "XXXXXXXXXXXXX restmatrix"
            #print restmatrix
            restmatrix=sum_extracted(restmatrix)
            endbin=len(matrix)-rest
            matrix=matrix[0:endbin,0:endbin]
            matrix=np.concatenate((matrix,restmatrix))
            print_to_file(matrix,increment)
            #print "size of new matrix", len(matrix)
            print matrix
            plot_xy(loadarray(),"y","input")
            plot_xy(matrix[0:],"c",increment)
            i=N
            return matrix


            

newmatrix=loadarray()
increment=0.5
 
newmatrix=shrink_subarray(loadarray(), 0, increment)

print minimum_bin(newmatrix,increment)  

