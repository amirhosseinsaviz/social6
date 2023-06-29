import networkx as nx
import matplotlib.pyplot as plt
import random

# تولید یک گراف تصادفی Erdős-Rényi
n = 100  # تعداد گره‌ها
m = 300  # تعداد یال‌ها
graph1 = nx.gnm_random_graph(n, m)

# رسم گراف
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(graph1)
nx.draw(graph1, pos, node_size=10, node_color='skyblue', edge_color='gray', alpha=0.7, with_labels=True)
plt.title("گراف تصادفی Erdős-Rényi (n=100، m=300)")
plt.show()

