# Almanecar los datos en una base de datos. (Asegurar el almacenamiento con el tipo de dato apropiado)

import sqlite3
import pandas as pd

data = pd.read_csv("candidates.csv")
conn = sqlite3.connect("candidates.db")
data.to_sql("candidates_data", conn, index=False, if_exists="replace")
conn.close()


# A partir de la lectura de los datos deberá generar un procesamiento reporte.

conn = sqlite3.connect("candidates.db")
query_avg_experience = "SELECT AVG([Yoe (years of experience)]) FROM candidates_data"
query_avg_score = "SELECT AVG([Code Challenge Score]) FROM candidates_data"

avg_experience = conn.execute(query_avg_experience).fetchone()[0]
avg_score = conn.execute(query_avg_score).fetchone()[0]
conn.close()

report = f"Informe de candidatos:\nPromedio de años de experiencia: {avg_experience}\nPromedio de puntaje del desafío de código: {avg_score}"

print(report)


# Realizar un código de envio de correos integrado en su solución.
import smtplib
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "tu_correo@gmail.com"
smtp_password = "tu_contraseña"
sender_email = "tu_correo@gmail.com"
receiver_email = "correo_destino@example.com"
subject = "Informe de candidatos"
message = report  

msg = MIMEText(message)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Correo electrónico enviado exitosamente.")
except Exception as e:
    print(f"Error al enviar el correo electrónico: {str(e)}")

