import requests

class ClassWithRequest():
	
	def get_from_url(self, id):
		url=f'http://company.com/{id}'
		x=requests.get(url)
		if x.ok:
			return 'Success'
		else:
			return 'Bad Response'
