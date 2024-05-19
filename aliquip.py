from collections import deque

def return_path(graph, start, end):
    """Returns a list of nodes in the shortest path from start to end in a graph.

    Args:
        graph: A dictionary representing the graph, where the keys are the nodes and the values are lists of the nodes that are connected to them.
        start: The starting node.
        end: The ending node.

    Returns:
        A list of nodes in the shortest path from start to end, or None if no path exists.
    """
    # Use a deque for efficient popleft operations.
    queue = deque([start])

    # Store the previous node for each visited node.
    previous = {start: None}

    # Visit nodes until the queue is empty.
    while queue:
        # Get the next node from the queue.
        current = queue.popleft()

        # Return the path if the end node is reached.
        if current == end:
            path = []
            while current:
                path.append(current)
                current = previous[current]
            path.reverse()
            return path

        # Visit each neighbor that hasn't been visited yet.
        for neighbor in graph[current]:
            if neighbor not in previous:
                previous[neighbor] = current
                queue.append(neighbor)

    # If the end node was not reached, return None.
    return None
