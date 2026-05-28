import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import serial
import time
import warnings
import re
import smtplib
from email.mime.text import MIMEText

warnings.filterwarnings("ignore")

# ================== EMAIL CONFIG ==================
EMAIL_SENDER = "franciest2004@gmail.com"
EMAIL_PASSWORD = "qgpn ruyu kxip iqhy"
EMAIL_RECEIVER = "vinayprasath7@gmail.com"

def send_email_alert(message):
    try:
        msg = MIMEText(message)
        msg["Subject"] = "⚠️ Machine Abnormal Alert"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print("📧 Email Alert Sent ✅\n")

    except Exception as e:
        print("❌ Email Error:", e)


# ================== LOAD MODEL ==================
data = pd.read_csv("Machine.csv")

X = data[["Tilt","Temperature","Sound","Current","Voltage"]]
y = data["Output"]

model = DecisionTreeClassifier()
model.fit(X, y)

print("✅ Model trained successfully")

# ================== SERIAL ==================
ser = serial.Serial('COM7', 9600, timeout=1)
time.sleep(2)

print("✅ Connected to COM7")
print("⏳ Waiting for machine data...\n")

buffer = ""
last_alert_time = 0

# ================== MAIN LOOP ==================
while True:
    try:
        raw = ser.read(100).decode('utf-8', errors='ignore')

        if not raw:
            continue

        buffer += raw

        matches = re.findall(r'X(\d+)T(\d+)S(\d+)C(\d+)V(\d+)', buffer)

        for match in matches:
            tilt, temp, sound, current, voltage = map(int, match)

            print("===================================")
            print(f"📥 Incoming Data:")
            print(f"   Tilt        : {tilt}")
            print(f"   Temperature : {temp}")
            print(f"   Sound       : {sound}")
            print(f"   Current     : {current}")
            print(f"   Voltage     : {voltage}")

            values = [tilt, temp, sound, current, voltage]

            prediction = model.predict([values])[0]

            # ✅ NORMAL
            if prediction == 0:
                print("🟢 STATUS: NORMAL")
                print("✔ Machine working properly\n")
                ser.write(b'0')

            # ⚠️ ABNORMAL
            else:
                print("🔴 STATUS: ABNORMAL")
                print("⚠️ Issue detected in machine\n")
                ser.write(b'1')

                # ⏱ Send email once per 60 sec
                if time.time() - last_alert_time > 60:
                    message = f"""
⚠️ MACHINE ABNORMAL ALERT ⚠️

Tilt        : {tilt}
Temperature : {temp}
Sound       : {sound}
Current     : {current}
Voltage     : {voltage}

Status: ABNORMAL

Immediate attention required!
"""
                    send_email_alert(message)
                    last_alert_time = time.time()

        # Clean buffer
        if len(buffer) > 200:
            buffer = buffer[-100:]

        time.sleep(0.2)

    except KeyboardInterrupt:
        print("🔴 Stopped")
        break

    except Exception as e:
        print("⚠️ Error:", e)
