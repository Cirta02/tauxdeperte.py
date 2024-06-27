def extract_events(trace_file):
    events = []

    with open(trace_file, 'r') as file:
        for line in file:
            parts = line.strip().split(' ', 3)
            if len(parts) >= 4:
                event_symbol = parts[0]
                event_time = float(parts[1])
                event_type = parts[2]
                event_details = parts[3]
                events.append((event_symbol, event_time, event_type, event_details))

    return events

def calculate_packet_loss(events):
    total_sent = 0
    total_received = 0

    for event in events:
        event_symbol, event_time, event_type, event_details = event
        print(f"Event: {event_symbol} {event_time} {event_type} {event_details}")

        if event_symbol == '+' and "TxQueue/Enqueue" in event_type:
            total_sent += 1

        elif event_symbol == 'r' and "MacRx" in event_type:
            total_received += 1

    if total_sent > 0:
        loss_rate = ((total_sent - total_received) / total_sent) * 100
        print(f"Packet Loss Rate: {loss_rate:.2f}%")
    else:
        print("No valid packets found for calculating packet loss.")

def main():
    trace_file = "olsr-hna-csma.tr"
    events = extract_events(trace_file)
    print(f"Extracted {len(events)} events from trace file.")
    calculate_packet_loss(events)

if __name__ == "__main__":
    main()

