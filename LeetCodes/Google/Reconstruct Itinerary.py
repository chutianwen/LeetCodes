'''
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''
import heapq
from collections import defaultdict

class Solution:
	'''
	Finding Eulerian tours is quite like DFS, with a little change :
	First keep going forward until you get stuck. That's a good main path already. Remaining tickets form cycles which are found on the way back and
	get merged into that main path. By writing down the path backwards when retreating from recursion, merging the cycles into the main path is easy -
	the end part of the path has already been written, the start part of the path hasn't been written yet, so just write down the cycle now and then
	keep backwards-writing the path.

	Example:

	enter image description here

	From JFK we first visit JFK -> A -> C -> D -> A. There we're stuck, so we write down A as the end of the route and retreat back to D. There we see
	the unused ticket to B and follow it: D -> B -> C -> JFK -> D. Then we're stuck again, retreat and write down the airports while doing so: Write
	down D before the already written A, then JFK before the D, etc. When we're back from our cycle at D, the written route is D -> B -> C -> JFK -> D -> A.
	 Then we retreat further along the original path, prepending C, A and finally JFK to the route, ending up with the route JFK -> A -> C -> D -> B -> C -> JFK -> D -> A.

	'''
	def findItinerary(self, tickets):
		hmap = defaultdict(list)
		itinerary = []
		for t in tickets:
			heapq.heappush(hmap[t[0]], t[1])

		frontier = ["JFK"]
		while frontier:
			expand = frontier[-1]
			if len(hmap[expand]) == 0:
				itinerary.append(expand)
				frontier.pop()

			elif expand in hmap:
				frontier.append(heapq.heappop(hmap[expand]))

		return itinerary[::-1]

class Solution2:
	def findItinerary(self, tickets):
		hmap = defaultdict(list)
		itinerary = []
		for t in tickets:
			heapq.heappush(hmap[t[0]], t[1])

		self.helper(itinerary, "JFK", hmap)
		return itinerary[::-1]


	def helper(self, route, dep, hmap):
		while dep in hmap and hmap[dep]:
			self.helper(route, heapq.heappop(hmap[dep]), hmap)
		route.append(dep)



tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

#['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
#['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']

res = Solution().findItinerary(tickets)
print(res)