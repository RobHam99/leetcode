from collections import deque


def print_all_nodes(root):
    queue = deque([root])
    while queue:
        nodes_in_current_level = len(queue)
        
        for _ in range(nodes_in_current_level):
            node = queue.popleft()
            print(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)