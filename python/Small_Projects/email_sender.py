from typing import List, Optional
from email.message import EmailMessage
import smtplib
import ssl
import os
print("DEBUG USER:", os.getenv("EMAIL_USER"))
print("DEBUG PASS:", os.getenv("EMAIL_PASS"))


# Config from OS for safety
SMTP_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("EMAIL_PORT", "587"))
SMTP_USER = os.getenv("EMAIL_USER")
SMTP_PASS = os.getenv("EMAIL_PASS")

if not SMTP_USER or not SMTP_PASS:
    raise RuntimeError(
        "set EMAIL_USER and EMAIL_PASS environment variable before running!")

# Helper to build message


def build_message(
        subject: str,
        sender: str,
        recipients: List[str],
        body_text: str,
        body_html: Optional[str] = None,
        attachments: Optional[str] = None,
) -> EmailMessage:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)
    msg.set_content(body_text)

    if body_html:
        msg.add_alternative(body_html, subtype="html")

    # attach files

    if attachments:
        for path in attachments:
            try:
                with open(path, "rb") as f:
                    data = f.read()
                import mimetypes
                ctype, encoding = mimetypes.guess_type(path)
                if ctype is None:
                    ctype = "application/octect-stream"
                    maintype, subtype = ctype.split("/", 1)
                    filename = os.path.basename(path)
                    msg.add_attachment(data, maintype=maintype,
                                       subtype=subtype, filename=filename)
            except FileNotFoundError:
                print(f"Warning: attachement not found: {path}")
    return msg

# send files


def send_email(message: EmailMessage, host: str = SMTP_HOST, port: int = SMTP_PORT, user: str = SMTP_USER, password: str = SMTP_PASS):
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(host, port, timeout=30) as smtp:
            smtp.ehlo()
            if port == 587:
                smtp.starttls(context=context)
                smtp.ehlo()
            smtp.login(user, password)
            smtp.send_message(message)
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print("Failed to send email:", e)
        raise


# exmample usage
if __name__ == "__main__":
    # Example recipients:
    to_address = ["ramya.ravi.267@gmail.com"]
    plain = "Hello, \nThis is a test email send from python"
    html = """\
    <html>
      <body>
        <p>Hello,<br>
           This is a <b>test</b> email sent from Python.<br>
        </p>
      </body>
    </html>
    """

    msg = build_message(
        subject="Test email from python",
        sender=SMTP_USER,
        recipients=to_address,
        body_text=plain,
        body_html=html,
        attachments=None,
    )

    send_email(msg)
