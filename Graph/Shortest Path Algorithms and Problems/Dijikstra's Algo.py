import heapq
from typing import List, Tuple

class Solution:
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        min_heap = []
        distance = [float("inf")] * len(adj)
        
        distance[src] = 0
        heapq.heappush(min_heap, (0, src)) 
        
        while min_heap:
            d, element = heapq.heappop(min_heap)
            
            for element_1, d_2 in adj[element]:
                if d + d_2 < distance[element_1]:
                    distance[element_1] = d + d_2
                    heapq.heappush(min_heap, (distance[element_1], element_1))
                    
        return distance


adj = [
    [(1, 4), (2, 8)],
    [(0, 4), (2, 2)],
    [(0, 8), (1, 2), (3, 7)],
    [(2, 7)] 
]

sol = Solution()
src = 0
print(sol.dijkstra(adj, src)) 



