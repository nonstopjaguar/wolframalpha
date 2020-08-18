import wolframalpha

client = wolframalpha.Client('wolframalpha client ID')

while True:
	query = str(input('Query:'))
	res = client.query(query)
	output = next(res.results).text
	print(output)
