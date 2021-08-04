import unittest
from unittest.mock import patch
from employee.employee import Employee



class TestRequestExample(unittest.TestCase):
	
	# def test_get_valid_url(self):
	# 	url = 'www.google.com'
	# 	re = RequestExample(url)
	# 	example_content = re.get()
	# 	self.assertIsNotNone(example_content)
	# 	self.assertEqual(example_content, "Tiago Melo")

	def test_get_id(self):
		em = Employee()

		with patch('employee.employee.Employee.get_from_url') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text='Success'

			schedule=em.get_from_url(2)
			mocked_get.assert_called_with(2)
			print(f'schedule={schedule}')
			self.assertEqual(schedule.text,'Success')

		# pass