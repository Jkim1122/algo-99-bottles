def bottle_song():
	bottles = 99
	while bottles > 2:
		print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down pass it around {bottles - 1} bottles of beer on the wall.')
		bottles -= 1
	while bottles > 1:
		print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down pass it around {bottles - 1} bottle of beer on the wall.')
		bottles -= 1
	while bottles > 0:
		print(f'{bottles} bottle of beer on the wall, {bottles} bottle of beer. Take one down pass it around no more bottles of beer on the wall.')
		bottles -= 1
	print('No more bottles of beer on the wall, no more bottles of beer. Go to the store & buy some more, 99 bottles of beer on the wall.')

bottle_song()