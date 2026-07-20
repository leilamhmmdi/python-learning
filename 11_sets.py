# Empty set
s = set()
print(s)
print(type(s))

# Create set
s = {1, 2, 3, 4}
print(s)

# Mixed data types
s = {'h1', 2, 3, 4, 'a'}
print(s)

# Add and remove
s.add(5)
s.remove(3)
print(s)

# Different data types
s = {'h1', 2, 3, 4, 'a', 2.5, (1, 2, 3)}
print(s)

# Union & Intersection
p = {1, 2, 5, 4, 7, 9}
q = {4, 7, 9, 3, 8, 6}

print(p.union(q))
print(p.intersection(q))
print(p ^ q)
print(p.symmetric_difference(q))

# Subset & Superset
A = {10, 20, 30, 40, 50, 60}
B = {10, 30, 60}

print(A.issubset(B))
print(A.issuperset(B))
