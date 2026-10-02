"""
Generates continuous streams of synthetic JSON event logs using Faker.
Includes intentional, controlled schema errors for testing data validation pipelines.
"""
import json
import random
import time
from datetime import datetime
from pathlib import Path

import click
from faker import Faker

# Define acceptable schema values
VALID_EVENT_NAME = "user.signup"
VALID_PLANS = ["free", "pro", "enterprise"]

# Define corrupted values to simulate data drift and legacy payload errors
INVALID_PLANS = ["premium"]

# Initialize Faker instance globally to avoid re-instantiation per batch
fake = Faker()


def generate_events(num_records: int = 50, error_rate: float = 0.05) -> None:
    """
    Generates a batch of synthetic JSON events and writes them to a local file.
    
    Args:
        num_records (int): Number of event records to generate in this batch.
        error_rate (float): Probability (0.0 to 1.0) of a record containing malformed data.
    """
    events = []

    for _ in range(num_records):
        # Determine if this specific record will be corrupted based on the error rate
        is_error = random.random() < error_rate

        event = {
            "event_id": fake.uuid4(),
            "event_name": VALID_EVENT_NAME,
            
            # Generate an ISO-8601 formatted timestamp within the last 30 days
            "timestamp": fake.date_time_between(start_date="-30d", end_date="now").isoformat() + "Z",
            
            # Type Validation Error: 50% chance to inject a string username instead of an integer ID
            "user_id": fake.user_name() if is_error and random.random() < 0.5 else fake.random_int(min=1000, max=99999),
            
            # Schema Validation Error: 50% chance to inject an invalid plan type
            "plan_type": random.choice(INVALID_PLANS) if is_error and random.random() < 0.5 else random.choice(VALID_PLANS),
            
            # Sparse Data Simulation: 30% of records have no referral source (tests Optional fields)
            "referral_source": None if random.random() < 0.3 else fake.url()

            # Error breakdown:
            # - 50% user_id or plan_type
            # - 25% user_id and plan_type
            # - 25% will pass cleanly
        }
        events.append(event)

    # Ensure the output directory exists using pathlib for cross-platform reliability
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    # Generate a unique timestamped filename for the batch
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = data_dir / f"raw_events_{current_time}.json"

    # Write the batch of events to disk as formatted JSON
    with output_path.open("w") as f:
        json.dump(events, f, indent=2)

    # Calculate approximate errors for logging and print color-coded terminal output
    approx_errors = int(num_records * error_rate)
    click.secho(f"Generated {num_records} events in {output_path} ", fg="green", nl=False)
    click.secho(f"(Approx. {approx_errors} intentional errors)", fg="yellow")


@click.command()
@click.option('--batch-size', default=50, help='Number of records to generate per batch.')
@click.option('--error-rate', default=0.05, help='Probability of generating a malformed record.')
@click.option('--interval', default=5, help='Seconds to wait between generating batches.')
def main(batch_size: int, error_rate: float, interval: int) -> None:
    """
    CLI entry point that runs an infinite loop generating JSON event streams.
    Press Ctrl+C to safely interrupt and stop the script.
    """
    click.secho(f"Starting data generation: batch size={batch_size}, error rate={error_rate}, interval={interval}s", fg="blue", bold=True)
    try:
        # Continuously generate data batches until manually stopped
        while True:
            generate_events(num_records=batch_size, error_rate=error_rate)
            time.sleep(interval)
    except KeyboardInterrupt:
        # Handle user exit gracefully without throwing traceback errors
        click.secho("\nData generation interrupted by user.", fg="red", bold=True)


if __name__ == "__main__":
    main()
