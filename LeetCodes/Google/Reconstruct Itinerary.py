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
	def findItinerary(self, tickets):
		hmap = defaultdict(list)
		itinerary = []
		for t in tickets:
			heapq.heappush(hmap[t[0]], t[1])

		frontier = ["JFK"]
		while frontier:
			expand = frontier.pop()
			itinerary.append(expand)

			while expand in hmap and hmap[expand]:
				frontier.append(heapq.heappop(hmap[expand]))

		return list(reversed(itinerary[1:] + ["JFK"]))

class Solution2:
		def findItinerary(self, tickets):
			hmap = defaultdict(list)
			itinerary = []
			for t in tickets:
				heapq.heappush(hmap[t[0]], t[1])

			self.helper(itinerary, "JFK", hmap)
			return itinerary#[::-1]


		def helper(self, route, dep, hmap):
			route.append(dep)
			while dep in hmap and hmap[dep]:
				self.helper(route, heapq.heappop(hmap[dep]), hmap)


			return route


tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

#['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
#['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']

res = Solution2().findItinerary(tickets)
print(res)