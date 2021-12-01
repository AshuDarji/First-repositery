import smtplib , getpass , re ,os 
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
def Login():
    try:
        password = getpass.getpass("Enter your password : ")
        server.login(os.environ.get('MyEmail'), password)
        print("Login successful")
    except smtplib.SMTPAuthenticationError:
        print("Login Error, Type valid Email/Password ")
        Login()
def check_email(email):
    """To validate the email Address"""
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    checking = re.fullmatch(regex,email) 
    if checking :
        return True
    else:
        print("Wrong email , Enter valid email address")
        return False
try:
    Login()
    ToEmail = input("Enter receiver's email: ") 
    while not check_email(ToEmail):
        ToEmail = (input("Email To : "))
    else:       
        subject = input("Enter subject: ")
        content = input("Enter content: ")
        body = "Subject: " + subject + '\n' + content
        server.sendmail(os.environ.get('MyEmail'),ToEmail , body)
        print(f'Email has been sent to :{ToEmail}')
except smtplib.SMTPException:
    print('Something went wrong,Please contact ISC')



