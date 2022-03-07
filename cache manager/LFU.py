class LFUCache:
    """
    LFUCache is a Cache and does caching the page Requests according to Least Frequently Used Technique.
    """
    def __init__ (self):
        """
        empty LFU cache dictionary
        """
        self.cache = {}
    
    def lfu(self, requestlist):
        """
        Function to run the LFU cache management on page requests.
        """
        global pageFreq
        for pagenum in requestlist:
            # if page request exist in cache it is a "Hit".
            if pagenum in self.cache:
                print("Hit")
                new_freq = self.cache[pagenum] + 1
                self.cache.update({pagenum:new_freq})
            # if page request does not exist in the cache it it a "Miss".
            else:
                print("Miss")
                pageFreq = 1
                # if length of the cache exceeds 8 removes page request which has fewest hits since it was added.
                if(len(self.cache) == 8 ):
                    minFreq = min(self.cache.values())
                    minFreqPages = [k for k, v in self.cache.items() if v == minFreq]
                    leastPage = min(minFreqPages)
                    self.cache.pop(leastPage)
                self.cache.update({pagenum:pageFreq})
        print("LFU Cache:", self.cache)
