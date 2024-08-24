from django.shortcuts import render
from django.http import JsonResponse

def get_api_types(request):
	if request.method == 'GET':
		apidata = [
			{
				'thenCatchCards': [
					{
						'name': 'Fetch API',
						'subtitle': 'with then/catch',
						'image': 'src/assets/images/api_fetch_no_async.png',
						'description': 'Fetch API with then/catch handles Promises.'
					},
					{
						'name': 'Axios',
						'subtitle': 'with then/catch',
						'image': 'src/assets/images/api_axios_no_async.png',
						'description': 'Axios with then/catch handles Promises.'
					}
				],
				'categoryTitle': 'Api Requests with then/catch'
			},
			{
				'asyncAwaitCards': [
					{
						'name': 'Fetch API',
						'subtitle': 'with async/await',
						'image': 'src/assets/images/api_fetch_with_async.png',
						'description': 'Fetch API with async/await for cleaner code.'
					},
					{
						'name': 'Axios',
						'subtitle': 'with async/await',
						'image': 'src/assets/images/api_axios_with_async.png',
						'description': 'Axios with async/await for cleaner code.'
					}
				],
				'categoryTitle': 'Api Requests with async/await'
			},
			{
				'preEs6Cards': [
					{
						'name': '$.ajax (Pre-ES6)',
						'subtitle': 'with ajax/jQuery',
						'image': 'src/assets/images/api_pre_es6.png',
						'description': 'Pre-ES6 $.ajax method for API requests.'
					},
					{
						'name': 'XMLHttpRequest (Pre-ES6)',
						'subtitle': '',
						'image': 'src/assets/images/api_pre_es6.png',
						'description': 'Pre-ES6 XMLHttpRequest for API requests.'
					}
				],
				'categoryTitle': 'Pre-ES6 Methods'
			}
		]

		data = {
			'message': 'Hello, this is your GET endpoint for API JS Types!',
			'apidata': apidata
		}
		return JsonResponse(data)


def get_table_data(request):
	if request.method == 'GET':
		tabledata = [
	{
		"name": "John Doe",
		"email": "johndoe@gmail.com",
		"phone": "555-555-5555",
		"dob": "1990-01-01"
	},
	{
		"name": "Jane Smith",
		"email": "janesmith@yahoo.com",
		"phone": "555-555-1234",
		"dob": "1985-05-15"
	},
	{
		"name": "Bob Johnson",
		"email": "bob.johnson@hotmail.com",
		"phone": "555-555-2468",
		"dob": "1978-12-31"
	},
	{
		"name": "Emily Davis",
		"email": "emily.davis@outlook.com",
		"phone": "555-555-9876",
		"dob": "1995-07-22"
	},
	{
		"name": "Tom Lee",
		"email": "tom.lee@gmail.com",
		"phone": "555-555-3698",
		"dob": "1980-03-10"
	}
]

		data = {
			'message': 'Hello, this is your GET endpoint for Table data!',
			'tabledata': tabledata
		}
		return JsonResponse(data)