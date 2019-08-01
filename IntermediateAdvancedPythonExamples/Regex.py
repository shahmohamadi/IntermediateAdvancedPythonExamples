# working with regex
import re
my_str = 'hi samane. Hi Shahab. hi everyone.'
result = re.search(r'hi', my_str)
print(result)
print(result.span())

my_input = 'samane.shahmohamadi@gmail.com'
print(re.search(r'.+@.+\..{2,3}', my_input))

my_input = 'samane.shahmohamadi@m'
if re.search(r'.+@.+\..{2,3}', my_input) is None:
    print('invalid email')

