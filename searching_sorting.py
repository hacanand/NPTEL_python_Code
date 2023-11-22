import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
def linear_search(n,x):
    elements = []
    for i in range(1,1001):
        elements.append(i)
    flag=0
    for i in elements:
        if(i==x):
            print("Element found!")
            flag=1
            break    
    if(flag==0):
        print("Element not found!")

linear_search(1000,400)
    
 