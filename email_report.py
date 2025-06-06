import smtplib
from email.message import EmailMessage
from generate_summary import generate_summary

def send_email():
    summary = generate_summary()

    msg = EmailMessage()
    msg["Subject"] = f"Teaka Trading – Daily Summary Report ({summary['date']})"
    msg["From"] = "gee@teaka.trading"
    msg["To"] = "gee@teaka.trading"

    text = f"""
🔥 DAILY TRADE SUMMARY – {summary['date']}

📈 Total Trades: {summary['total_trades']}
💰 Win Rate: {summary['win_rate']}%
📊 P&L: +${summary['pnl_usd']} ({summary['pnl_percent']}%)
🏆 Top Symbol: {summary['top_symbol']} (+${summary['top_pnl']})
💣 Worst Symbol: {summary['worst_symbol']} (${summary['worst_pnl']})

📍 Signal Forecast:
"""
    for symbol, bias in summary["forecast"].items():
        text += f"{symbol} → {bias.upper()}\n"

    text += f"\n{summary['notes']}\n\n— Teaka Swarm Core"

    msg.set_content(text)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login("gee@teaka.trading", "Success-25")  # ⚠️ Replace with App Password if needed
        smtp.send_message(msg)
