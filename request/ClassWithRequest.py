import requests

class ClassWithRequest():
	
	def get_from_url(self, id):
		
		if id is None:
			return 'Bad Request'
			
		url=f'http://company.com/{id}'
		x=requests.get(url)
		if x.ok:
			return 'Success'
		else:
			return 'Bad Response'
