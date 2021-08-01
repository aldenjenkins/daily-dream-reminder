# Daily Dream Reminder

-   Send out a daily email with a digest of your current life's dream in Markdown.

### Intuition

-   Being reminded of your 3 year dream is a fantastic tool for visualization.

### Usage


-   In a crontab:

```{bash}
THREE_YEAR_PAINTED_PICTURE=markdowntext SMTP_HOST=smtp.site.com SMTP_PASS=password EMAIL_FROM=from@test.com EMAIL_TO=to@test.com /thedir/send_email.py

```
