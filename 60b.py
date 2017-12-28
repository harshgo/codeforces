def get_cube(k, n, m):
  result = []
  for i in range(k):
    input()
    result.append([])
    for j in range(n):
      line = input()
      result[i].append([True if i == '.' else False for i in line])
  return result

def solution(cube, tapX, tapY):
  stack = [(0, tapX, tapY)]
  x = [1,-1,0,0,0,0]
  y = [0,0,1,-1,0,0]
  z = [0,0,0,0,-1,1]
  mins = 0
  visited = set()
  while stack:
    currx, curry, currz = stack.pop()
    if currx < 0 or currx >= len(cube):
      continue
    if curry < 0 or curry >= len(cube[0]):
      continue
    if currz < 0 or currz >= len(cube[0][0]):
      continue
    if (currx, curry, currz) in visited or not cube[currx][curry][currz]:
      continue
    mins += 1
    for dx, dy, dz in zip(x,y,z):
      stack.append((currx+dx, curry+dy, currz+dz))
    visited.add((currx, curry, currz))
  return mins

    

k,n,m = [int(i) for i in input().split()]
cube = get_cube(k,n,m)
input()
tapX, tapY = [int(i) for i in input().split()]
print(solution(cube, tapX-1, tapY-1))
