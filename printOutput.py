
def sortAndPrintMatchings(residencyPairs):
	residencyPairs.sort(key = lambda tuple: tuple[0])
	print(residencyPairs)
