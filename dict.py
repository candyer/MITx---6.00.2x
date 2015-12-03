class D():
    def __init__(self, size=7):
        self.size = size
        self.elements = 0
        self.values = [[] for _ in range(self.size)] 


    def put(self, key, val):
        '''
        insert the key and val inside the dictionary, double the size if the elements grow until half of the original size 
        '''
        h = hash(key)
        index = h % self.size #decide the element will be in which bucket
        size_before = len(self.values[index]) # this size means the number of elements in a perticular bucket
        #make sure there is no same key
        self.values[index] = [(k, v) for k, v in self.values[index] if k != key]
        bucket = self.values[index]
        bucket.append((key, val))
        size_after = len(self.values[index]) #same as size_before
        self.elements += size_after - size_before #count how many elements in total
        if self.elements * 2 > self.size:
            self.resize()


    def get(self, key):
        '''
        get the value of a key. if the key doesnt exist, raise the Error,return the counter as well
        '''
        h = hash(key)
        index = h % self.size
        bucket = self.values[index]
        cpt = 0
        for k, v in bucket:
            cpt += 1
            if k == key:
                print 'searched {} elements'.format(cpt)
                return v
        raise KeyError('key {} doesn\'t exist!'.format(key))


    def delete(self,key):
        '''
        take one key as argument, delete the corresponding key value 
        from the dictionary, raise a KeyError exception if ket doesnt exist
        '''
        bucket = self.values[hash(key) % self.size]
        for k, v in bucket:
            if k == key:
                bucket.remove((k,v))
                return self.values
        raise KeyError('key {} doesn\'t exist!'.format(key))


    def resize(self):
        """
        resize the dictionary,buckets stay pretty empty, so the search stay fast
        """
        new_d = D(self.size * 2)
        for bucket in self.values:
            for k, v in bucket:
                new_d.put(k, v)
                print new_d
        # we replace the current dictionary with the new one by changing the arguments
        self.size = new_d.size
        self.values = new_d.values
        self.elements = new_d.elements


    def __repr__(self):
        return '{}'.format(self.values)


    def info(self):
        print 'number of buckets: {}'.format(self.size)
        print 'number of elements: {}'.format(self.elements)
        print [len(bucket) for bucket in self.values]


    def info2(self):
        print 'number of buckets: {}'.format(self.size)
        print 'number of elements: {}'.format(self.elements)
        
d = D()
d.put(10, 'abc')
d.put(17, 'def')
d.put(2445, 'hello')
d.put(2445, 'world')
d.put('cat', 'dog')
print d   #[[], [], [], [(17, 'def')], [], [], [], [], [], [(2445, 'world'), ('cat', 'dog')], [(10, 'abc')], [], [], []]
print d.get(10)  #searched 1 elements  'abc'
print d.get('cat')  #searched 2 elements   'dog'
print d.delete(17)  #[[], [], [], [], [], [], [], [], [], [(2445, 'world'), ('cat', 'dog')], [(10, 'abc')], [], [], []]
print d.delete(10)  #[[], [], [], [], [], [], [], [], [], [(2445, 'world'), ('cat', 'dog')], [], [], [], []]
print d.delete(2445)  #[[], [], [], [], [], [], [], [], [], [('cat', 'dog')], [], [], [], []]
print d.delete('car')  #KeyError: "key car doesn't exist!"
