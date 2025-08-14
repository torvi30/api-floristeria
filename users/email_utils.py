import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_reset_email(to_email: str, reset_link: str):
    sender_email = "victortamayopine@gmail.com"
    sender_password = "bpjm frvg yoxw xlib"
    subject = "Recuperación de contraseña - Floristería"
    body = f"""
    <html>
      <body style="font-family: Arial, sans-serif; background-color: #fff8f0; color: #333;">
        <div style="max-width: 500px; margin: auto; border-radius: 10px; border: 1px solid #e0b7b7; background: #fff; box-shadow: 0 2px 8px #f3d6d6;">
          <div style="padding: 24px 32px;">
            <h2 style="color: #b94e4e; text-align: center;">🌸 Floristería Bella Flor 🌸</h2>
            <p>¡Hola!</p>
            <p>Recibimos una solicitud para restablecer tu contraseña.</p>
            <p>
              <a href="{reset_link}" style="display: inline-block; padding: 12px 24px; background-color: #b94e4e; color: #fff; border-radius: 5px; text-decoration: none; font-weight: bold;">
                Restablecer contraseña
              </a>
            </p>
            <p>Si no solicitaste este cambio, puedes ignorar este correo.</p>
            <hr style="border: none; border-top: 1px solid #f3d6d6;">
            <p style="font-size: 13px; color: #b94e4e; text-align: center;">Gracias por confiar en Floristería Bella Flor 🌷</p>
          </div>
        </div>
      </body>
    </html>
    """

    # Configurar el correo
    msg = MIMEMultipart("alternative")
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    # Enviar el correo
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())