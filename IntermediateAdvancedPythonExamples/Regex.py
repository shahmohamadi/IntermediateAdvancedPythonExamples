# working with regex
import re


# example 1
my_str = 'hi samane. Hi Shahab. hi everyone.'
result = re.search(r'hi', my_str)
print(result)
print(result.span())

# example 2
my_input = 'samane.shahmohamadi@gmail.com'
print(re.search(r'.+@.+\..{2,3}', my_input))

my_input = 'samane.shahmohamadi@m'
if re.search(r'.+@.+\..{2,3}', my_input) is None:
    print('invalid email')

# example 3
web_string = 'the price of oil is 67$ per each 1barrel'
result = re.findall(r'the price of oil is (\d+)\$ per each (\d+)barrel', web_string)
print(result)
result[0]
price, barrel = result[0]
print(price)
print(barrel)

web_string = 'the price of oil is 67$ per each 1barrel in 7AM\nthe price of oil is 69$ per each 1barrel in 12PM\nthe ' \
             'price of oil is 65$ per each 1barrel in 5PM'
print(web_string)
result = re.findall(r'the price of oil is (\d+)\$ per each (\d+)barrel in (.*)', web_string)
print(result)
for price, barrel, time in result:
    print(price, barrel, time)

# example 4
my_str = 'hi samane. Hi Shahab. hi everyone.'
result = re.sub(r'hi', 'hello', my_str)
print(result)
result = re.sub(r'[hH]i', 'hello', my_str)
print(result)
result = re.sub(r'[hH]i \w+\.', 'hello', my_str)
print(result)
print(my_str)
result = re.sub(r'[hH]i (\w+)\.', 'hello \g<1>', my_str)
print(result)
result = re.sub(r'[hH]i (\w+)\.', 'hello \g<0>', my_str)
print(result)

# example 5
web_string = 'the price of oil is 67$ per each 1barrel in 7AM\nthe price of oil is 69$ per each 1barrel in 12PM\nthe ' \
             'price of oil is 65$ per each 1barrel in 5PM'
result = re.sub(r'the price of oil is (\d+)\$ per each (\d+)barrel in (.*)', '\g<3>, \g<2>, \g<1>', web_string)
print(result)
