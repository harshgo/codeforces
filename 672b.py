from collections import defaultdict

num_chars = input()
in_str = input()
if len(in_str) > 26:
  print(-1)
else:
  frequencies = defaultdict(lambda: -1)
  for c in in_str:
    frequencies[c] += 1

  print(sum([frequencies[key] for key in frequencies.keys()]))
