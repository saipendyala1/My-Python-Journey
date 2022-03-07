def cachemanager():
    """
    Cache manager is a function To Manage the page requests according to the user Requested technique.
    """
    requests =[]
    while True:
        number = int(input("Enter a Page Number / 0 to exit the page requests:\n"))
        if number != 0:
            requests.append(number)
        else:
            # end of page requests if '0' is entered.
            print("End of Page Requests!")
            break
    # user choice: press '1' for fifo, or '2' for lfu. 'q' to exit.
    print("===============")
    choice = input("Enter '1' for FIFO \nEnter'2' for LFU \nEnter'q' to quit\n ")
    print("===============")
    # choice '1' for the FIFO technique.
    if choice == '1':
        from FIFO import FIFOCache
        FIFOObj = FIFOCache()
        FIFOObj.fifo(requests)
    # choice '2' for the LFU technique.
    elif choice == '2':
        from LFU import LFUCache
        LFUObj = LFUCache()
        LFUObj.lfu(requests)    
    # choice 'q' to exit.
    elif choice == 'q':
        quit
    else:
        print("enter the valid input")
    # to return to the main menu again 
    cachemanager()
cachemanager()

