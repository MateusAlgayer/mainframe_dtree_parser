import random

graph_content = ""
for i in range(1, 100):
    graph_content += f"    A{i} --> A{random.randint(1, i+1)}\n"
    graph_content += f"    A{random.randint(1, i+1)} --> B{random.randint(1, i+1)}\n"
    graph_content += f"    A{random.randint(1, i+1)} --> B{random.randint(1, i+1)}\n"

mermaid_code = f"""```mermaid
graph TD
    {graph_content}
```
"""

# Assuming mermaid_code is defined as above

with open("my_diagram.md", "w") as f:
    f.write(mermaid_code)
