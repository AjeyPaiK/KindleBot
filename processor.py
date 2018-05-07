import email
def process_mailbox(M):
	rv, emails = M.search(None, "ALL")
	if rv != 'OK':
		print "No messages found!"

	# loop num over all emails in data.split()
	for num in emails[0].split():
		M.store(num,'+FLAGS','\\Deleted')
		rv, raw_mail = M.fetch(num, '(RFC822)')
		mail = email.message_from_string(raw_mail[0][1])
		if mail.is_multipart():
			for part in mail.walk():
				ctype = part.get_content_type()
				if ctype in ['application/pdf', 'application/x-pdf']:
					open('../Saved_PDFs/'+part.get_filename(), 'wb').write(part.get_payload(decode=True))

	M.expunge()
