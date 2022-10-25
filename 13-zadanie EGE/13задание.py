G = {
'А': "ЗВ", 'Б': 'АГ', 'В': 'БЕКЗ','Г': 'А','Д': 'АГ','Е': 'Б','Ж': 'И','З': 'ИЖК','И': 'Д','К': 'ЕЖ',
}
count = 0
def findPath( path, target ):
   global count
   lastTown = path[-1]
   if lastTown == target and len(path) > 1:
      count += 1
      print( path )
      return
   for town in G[lastTown]:
      if not town in path or town == target:
        findPath( path+town, target )

findPath( 'А', 'А' )
print( count )
