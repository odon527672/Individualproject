from flask import Flask, render_template
import win32evtlog

app = Flask(__name__)

# Route to display Windows system errors
@app.route('/system-errors')
def system_errors():
    try:
        events = []

        # Open the System event log
        hand = win32evtlog.OpenEventLog(None, "System")
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        total_records = win32evtlog.GetNumberOfEventLogRecords(hand)

        events_read = 0
        while events_read < total_records:
            records = win32evtlog.ReadEventLog(hand, flags, 0)
            if not records:
                break
            for record in records:
                event_info = {
                    'TimeGenerated': record.TimeGenerated.Format(),
                    'SourceName': record.SourceName,
                    'EventID': record.EventID & 0xFFFF,  # Get lower 16 bits of EventID
                    'EventType': record.EventType,
                    'StringInserts': record.StringInserts
                }
                events.append(event_info)
                events_read += 1

        # Close the event log
        win32evtlog.CloseEventLog(hand)

        return render_template('test.html', events=events)
    except Exception as e:
        return f"Error retrieving system errors: {e}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
