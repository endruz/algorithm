from typing import List
from collections import deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stations = dict()
        for route, stops in enumerate(routes):
            for stop in stops:
                stations.setdefault(stop, set()).add(route)

        routes = [set(route) for route in routes]
        token_routes, arrived_stations = set(), {source}

        queue = deque([(source, 0)])

        while queue:
            postion, cost = queue.popleft()
            if postion == target:
                return cost
            for route in stations[postion] - token_routes:
                token_routes.add(route)
                for station in routes[route] - arrived_stations:
                    arrived_stations.add(station)
                    queue.append((station, cost + 1))

        return -1
