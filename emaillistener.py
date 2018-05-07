import imaplib
import email
import processor
PASSWORD = #KINDLEBOT PASSWORD
EMAIL_ACCOUNT = #KINDLEBOT EMAIL ID
M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    rv, data = M.login(EMAIL_ACCOUNT, PASSWORD)
    print "Logged into ",EMAIL_ACCOUNT
except imaplib.IMAP4.error:
    print "LOGIN FAILED!!! "
    sys.exit(1)

rv, mailboxes = M.list()
#if rv == 'OK':
#    print "Mailboxes:"
#    print mailboxes

rv, emails_count = M.select('INBOX')
if rv == 'OK':
    print "Processing mailbox...\n"
    processor.process_mailbox(M)
    M.close()
