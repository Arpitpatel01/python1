class node:
    def __init__(self,item=None,next=None,prev=None):
        self.item=item
        self.next=next
        self.prev=prev

class dsll:
    def __init__(self,start=None):
        self.start=start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n=node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=None
        self.start=n

    def insert_at_last(self,data):
        temp=self.start
        if self.start !=None:
            while temp.next !=None:
                temp=temp.next
                n=node(None,data,temp)

        

        
        