import smtplib as sms


def sendIt(title: str, body: str | None = None):
    server = sms.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login("pythondeveloper441@gmail.com", "$enterpassword$")
    message = f"Title: \n{title}\n\nBody:\n{body}"
    server.sendmail("pythondeveloper441@gmail.com", "$enterpassword$", message)
    server.quit()


sendIt("Assalomu alaykum hurmatli lox!!!",
       "Man oddiy pythonda 12 qator kod orqali sani mailingga sms jo'natyamman!!!, Yeganing shu busin")
