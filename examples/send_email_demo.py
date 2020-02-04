from lightutils import send_email_notification

to = "iamlightsmile@qq.com"
subject = "just a test"
contents = ["the test of lightUtils's send_email_notification function"]
result = send_email_notification(to, subject, contents)
if result:
    print("发送成功！")
else:
    print("发送失败！")
