F = open( "24-200.txt" )

def valid( s ):
  s = s.strip()
  mask = "195.2?.1?5.14"
  for c1, c2 in zip(s, mask):
    if c2 != '?' and c1 != c2:
      return False
  return len(s) == len(mask)

ips = set()
for s in F.readlines():
  if valid(s):
    ips.add( s )

print( len(ips) )

F.close()