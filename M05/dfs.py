def dfs(graph, start, visited=None):            #fungsi rekursi untuk DFS
    if visited is None:                         #jika diawal belum ada node yang dikunjungi
        visited = set()                         #maka buat penampung untuk node yang dikunjungi
    visited.add(start)                          #dan tambahkan node yang pertama kali dikunjungi
    
    print(start,end='')                         #cetak start untuk menandakan sudah dikunjungi
    
    for next in set(graph[start]) - visited:    #untuk setiap tetangga dari node yabg dikunjungi
        dfs(graph, next, visited)               #panggil fungi DFS dengan node tetangga yang akan dikunjungi
                                                #beserta penampung node yang sudah dikunjungi
    
    return visited      #kembalikan node yang sudah dikunjungi setiap fungsi ini dipanggil                      

graph = {
    'a':['b','c'],
    'b':['d','e'],
    'c':['f','g'],
    'd':[],
    'e':[],
    'f':[],
    'g':[]
}    

dfs(graph, 'a')
