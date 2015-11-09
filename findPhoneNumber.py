#! python3

# string are immutable

# to automate it in a batch file
#... @py c:\users\....\hello.py %*
# now you can save this in a batch file and run it.

import re, pprint
message  = '''this is my number 416-704-9142, 674-565-5465line = (157) 836-8167
This number is invalid because Area Codes cannot begin with a 1 or 0.
(298) 731-6185
This number is invalid because the NANP is not assigning area codes with 9 as the second digit.
(678) 035-7598
This number is invalid because Exchange Codes cannot begin with a 1 or 0.
(752) 811-1375
This number is invalid because Exchange Codes cannot end with two 1s. (265) 555-0128
This number is invalid because the Exchange Code is 555, and the Subscriber ID is within the range reserved for fictitious numbers.(800) 555-0199
This number is the only 800 number with a 555 Exchange Code which is reserved for use as a fictitious number."why people don't know what regex are? let me know asdfal2@als.com, alasdjfaksdfkas@kk.de " \
       "321dsasdsa@dasdassd-asasdsa.com.lo,asfasdfas.asdas-asasdsa@dasdsa.com'''

phoneNumber = re.compile(r'\(\d\d\d\) \d\d\d\-\d\d\d\d')
mo = phoneNumber.findall(message)
pprint.pprint(mo)

match = re.findall(r'[\w\.-]+@[\w\.-]+', message)
print(match)


