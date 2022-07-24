def get_top_k_orders_hourly(records, k):
	import heapq
	from collections import defaultdict
	n = len(records)
	hourly = defaultdict(defaultdict)
	for record in records:
		re_id, item, time = record
		if item not in hourly[time]:
			hourly[time][item] = 0
		hourly[time][item] += 1

	topK_order = []
	for time, orders in hourly.items():

		top_k_hourly = []
		for order, cnt in orders.items():
			heapq.heappush(top_k_hourly, (cnt, order))
		top_k_order_hourly = [x[1] for x in heapq.nlargest(k, top_k_hourly)]
		if not top_k_order_hourly:
			topK_order.append(['no order at time:{}'.format(time)])
		else:
			topK_order.append(top_k_order_hourly)
	return topK_order

records = [(0, 'banana', 21), (1, 'noodle', 19), (2, 'rice', 12), (3, 'yogurt', 15), (4, 'banana', 21)]
res = get_top_k_orders_hourly(records, 2)
print(res)