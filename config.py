detf = open('details.txt','w+')

EMAIL_ACCOUNT = raw_input('Enter the Email ID for the KindleBot to be use: ')
PASSWORD = raw_input('Enter the password: ')
SEND_EMAIL = raw_input('Enter the Email ID registered to the Kindle: ')

detf.write(EMAIL_ACCOUNT)
detf.write("\n")
detf.write(PASSWORD)
detf.write("\n")
detf.write(SEND_EMAIL)
detf.write("\n")

print("Details Recorded!")

detf.close()
