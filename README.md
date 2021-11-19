# Search Algorithms
BSF, iterative deepening and A* algorithms implementation

Input should be a text file with the following contents:

- Each line in the file should be either a comment, vertex or an edge.
- A line that starts with # is a comment line and should be skipped
- A vertex consists of a node label followed by two ints: an x and y coordinate.
- An edge (always undirected) is simply two node labels.

Note: A node label should be any string with alphanumeric characters
Note: there is no guaranteed order. Edges might reference vertices not yet defined, and that is fine as long as they appear somewhere in the file.

The length of any edge is computed from the 2 vertices (x,y) coordinates using standard Euclidean distance for p, q of = sqrt((p_x - q_x)^2 + (p_y - q_y)^2).




About running the code:

Run the code for each algorithm with the following command in the terminal, 

- python A*.py (for A* algorithm)
- python Iterative_deepening.py (for Iterative deepening algorithm)
- python BFS.py for (BFS algorithm)

After executing any one of these 3 command, terminal will prompt for an input. Here, give the name of the input txt file with extension.
