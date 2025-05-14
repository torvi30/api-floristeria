import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_reset_email(to_email: str, reset_link: str):
    sender_email = "victortamayopine@gmail.com"
    sender_password = "bpjm frvg yoxw xlib"
    subject = "Recuperacion de password"
    body = f"Hola,\n\nHaz clic en el siguiente enlace para restablecer tu password:\n{reset_link}\n\nSi no solicitaste este cambio, ignora este correo."

    # Configurar el correo
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    # Enviar el correo
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())