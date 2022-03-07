class FIFOCache:    
    """
    FIFOCache is a Cache and does caching the Page requests according to First In First Out Technique.
    """
    def __init__(self):
        self.cache = []    

    def fifo(self, requestList):
        """
        FIFO tests wether the page is a hit or miss from the page Requests according to First In First Out Technique.
        """
        for pagenum in requestList:
            # if page request exist in cache it is a "Hit".
            if pagenum in self.cache:
                print("Hit")
            # if page request does not exist in the cache it it a "Miss".
            else:
                print("Miss")
                self.cache.append(pagenum)
                # if length of the cache exceeds 8 removes page request which has longest time since it was added. 
                if len(self.cache) == 9:
                    self.cache.pop(0)
        print("FIFO Cache:",self.cache)