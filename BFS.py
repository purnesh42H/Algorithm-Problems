class Graph:
    
    def __init__(self, n):
        self.nodes = n
        self.edges = {}
        
    def connect (self, n1, n2):
        if n1 not in self.edges:
            self.edges[n1] = [n2]
        else:
            if n2 not in self.edges[n1]:
                self.edges[n1].append(n2)
        if n2 not in self.edges:
            self.edges[n2] = [n1]
        else:
            if n1 not in self.edges[n2]:
                self.edges[n2].append(n1)
        
    def find_all_distances(self, s):
        links = []
        if s in self.edges:
            links = self.edges[s]
        d = {}
        for link in links:
            if link not in d:
                d[link] = 6
            
        depth = 12
        i = 0
        nextDepth = len(links)
        fetched = 0
        while len(links) > 0:
            if fetched == nextDepth:
                depth += 6
                nextDepth = len(links)
                fetched = 0
            node = links[0]
            links = links[1:]
            fetched += 1
            if node in self.edges:
                children = self.edges[node]
                if len(children) > 0:
                    for link in children:
                        if link not in d and link != s:
                            d[link] = depth
                            links.append(link)
            
                    
        return d
                
t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1)
    s = input()
    d = graph.find_all_distances(s-1)
    answer = ''
    node = 0
    while node < graph.nodes:
        if (node+1) != s:
            if node in d:
                answer += '%d '% d[node]
            else:
                answer += '-1 '
        node += 1
        
    print answer[:-1]
