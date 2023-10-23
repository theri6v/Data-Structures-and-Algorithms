from queue import Queue 
from typing import List


class KnapsackNode: 
	def __init__(self, items: List[int], value: int, weight: int): 
		self.items = items 
		self.value = value 
		self.weight = weight 


class Item: 
	def __init__(self, value: int, weight: int): 
		self.value = value 
		self.weight = weight 
		self.ratio = value / weight 


class Knapsack: 
	def __init__(self, maxWeight: int, items: List[Item]): 
		self.maxWeight = maxWeight 
		self.items = items 

	def solve(self) -> int: 
		self.items.sort(key=lambda x: x.ratio, reverse=True) 
		bestValue = 0
		queue = [KnapsackNode([], 0, 0)] 

		while queue: 
			node = queue.pop(0) 
			i = len(node.items) 

			if i == len(self.items): 
				bestValue = max(bestValue, node.value) 
			else: 
				item = self.items[i] 
				withItem = KnapsackNode( 
					node.items + [i], 
					node.value + item.value, 
					node.weight + item.weight 
				) 
				if self.isPromising(withItem, self.maxWeight, bestValue): 
					queue.append(withItem) 
				withoutItem = KnapsackNode( 
					node.items, 
					node.value, 
					node.weight 
				) 
				if self.isPromising(withoutItem, self.maxWeight, bestValue): 
					queue.append(withoutItem) 

		return bestValue 

	def isPromising(self, node: KnapsackNode, maxWeight: int, bestValue: int) -> bool: 
		return node.weight <= maxWeight and node.value + self.getBound(node) > bestValue 

	def getBound(self, node: KnapsackNode) -> float: 
		remainingWeight = self.maxWeight - node.weight 
		bound = node.value 

		for i in range(len(node.items), len(self.items)): 
			item = self.items[i] 

			if remainingWeight >= item.weight: 
				bound += item.value 
				remainingWeight -= item.weight 
			else: 
				bound += remainingWeight * item.ratio 
				break

		return bound 


'''------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


items = [ 
	Item(60, 10), 
	Item(100, 20), 
	Item(120, 30) 
] 
knapsack = Knapsack(50, items) 
bestValue = knapsack.solve() 
print("Best value: " + str(bestValue))



