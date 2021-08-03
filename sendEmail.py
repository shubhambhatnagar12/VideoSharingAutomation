import smtplib as email

obj=email.SMTP("smtp.gmail.com",587)

obj.starttls()

obj.login("shubhamlogintest1234@gmail.com","aws@TEST1234")


subject="test subject for python"
body="this mail is from python"

message="Subject:{}\n\n{}".format(subject,body)

listofrecepients=["500069818@stu.upes.ac.in","bhatnagarshubham1234@gmail.com"]

obj.sendmail("shubhamlogintest1234",listofrecepients,message)

print("sent")
obj.quit()