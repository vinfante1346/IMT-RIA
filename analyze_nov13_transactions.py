#!/usr/bin/env python3
import csv
from collections import defaultdict
from datetime import datetime

# Read the CSV file
csv_file = '/Users/valinfante/Downloads/3846_20251114_transactions_v2-5.csv'

print("📊 Analyzing November 13, 2025 Transaction Data\n")
print("=" * 80)

transactions = []
with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        transactions.append(row)

print(f"Total Rows: {len(transactions)}\n")

# Analyze by status
status_counts = defaultdict(int)
status_volumes = defaultdict(float)

# Analyze by type
type_counts = defaultdict(int)
type_volumes = defaultdict(float)

# Fee analysis
total_tabapay_fees = 0.0
total_network_fees = 0.0
total_interchange = 0.0

# Volume tracking
completed_purchase_volume = 0.0
completed_disbursement_volume = 0.0
error_volume = 0.0

for txn in transactions:
    status = txn['Status']
    txn_type = txn['Type']
    amount = float(txn['Transaction Amount']) if txn['Transaction Amount'] else 0.0

    status_counts[status] += 1
    status_volumes[status] += amount

    type_counts[txn_type] += 1
    type_volumes[txn_type] += amount

    # Fees (only for completed transactions)
    if status == 'Complete':
        total_tabapay_fees += abs(float(txn['TabaPay Fee'])) if txn['TabaPay Fee'] else 0.0
        total_network_fees += abs(float(txn['Network Fee'])) if txn['Network Fee'] else 0.0
        total_interchange += abs(float(txn['Interchange'])) if txn['Interchange'] else 0.0

        if txn_type == 'Purchase':
            completed_purchase_volume += amount
        elif txn_type == 'Disbursement':
            completed_disbursement_volume += abs(amount)  # Disbursements are negative
    else:
        error_volume += amount

print("STATUS BREAKDOWN")
print("=" * 80)
for status in sorted(status_counts.keys()):
    count = status_counts[status]
    volume = status_volumes[status]
    pct = (count / len(transactions)) * 100
    print(f"{status:<15} {count:>6} txns ({pct:>5.1f}%)  ${volume:>12,.2f}")

print("\n" + "=" * 80)
print("TRANSACTION TYPE BREAKDOWN")
print("=" * 80)
for txn_type in sorted(type_counts.keys()):
    count = type_counts[txn_type]
    volume = type_volumes[txn_type]
    pct = (count / len(transactions)) * 100
    print(f"{txn_type:<20} {count:>6} txns ({pct:>5.1f}%)  ${volume:>12,.2f}")

# Calculate success metrics
completed_count = status_counts.get('Complete', 0)
error_count = status_counts.get('Error', 0)
success_rate = (completed_count / len(transactions)) * 100

print("\n" + "=" * 80)
print("KEY METRICS - NOVEMBER 13, 2025")
print("=" * 80)
print(f"\n📊 Total Transactions: {len(transactions):,}")
print(f"✅ Completed: {completed_count:,} ({success_rate:.1f}%)")
print(f"❌ Errors: {error_count:,} ({(error_count/len(transactions))*100:.1f}%)")

print(f"\n💰 VOLUME METRICS")
print(f"   Purchase Volume (Completed): ${completed_purchase_volume:,.2f}")
print(f"   Disbursement Volume (Completed): ${completed_disbursement_volume:,.2f}")
print(f"   Total Completed Volume: ${completed_purchase_volume + completed_disbursement_volume:,.2f}")
print(f"   Failed Transaction Attempts: ${error_volume:,.2f}")

print(f"\n💵 FEE ANALYSIS (Completed Transactions Only)")
print(f"   TabaPay Fees: ${total_tabapay_fees:,.2f}")
print(f"   Network Fees: ${total_network_fees:,.2f}")
print(f"   Interchange Fees: ${total_interchange:,.2f}")
print(f"   Total Fees: ${total_tabapay_fees + total_network_fees + total_interchange:,.2f}")

# Card brand breakdown
card_brands = defaultdict(int)
card_brand_volume = defaultdict(float)

for txn in transactions:
    if txn['Status'] == 'Complete':
        brand = txn['Card Brand']
        if brand:
            card_brands[brand] += 1
            amount = abs(float(txn['Transaction Amount'])) if txn['Transaction Amount'] else 0.0
            card_brand_volume[brand] += amount

print(f"\n💳 CARD BRAND BREAKDOWN (Completed)")
print("=" * 80)
for brand in sorted(card_brands.keys(), key=lambda x: card_brands[x], reverse=True):
    count = card_brands[brand]
    volume = card_brand_volume[brand]
    pct = (count / completed_count) * 100 if completed_count > 0 else 0
    print(f"{brand:<20} {count:>6} txns ({pct:>5.1f}%)  ${volume:>12,.2f}")

# Average transaction size
avg_purchase = completed_purchase_volume / type_counts['Purchase'] if type_counts['Purchase'] > 0 else 0
avg_disbursement = completed_disbursement_volume / type_counts['Disbursement'] if type_counts['Disbursement'] > 0 else 0

print(f"\n📈 AVERAGE TRANSACTION SIZE")
print(f"   Average Purchase: ${avg_purchase:.2f}")
print(f"   Average Disbursement: ${avg_disbursement:.2f}")

print("\n" + "=" * 80)
print("SUMMARY FOR PRESENTATION")
print("=" * 80)
print(f"""
November 13, 2025 Data:
- Total Transactions: {len(transactions):,}
- Success Rate: {success_rate:.1f}%
- Total Volume: ${completed_purchase_volume + completed_disbursement_volume:,.2f}
- Average Transaction: ${(completed_purchase_volume + completed_disbursement_volume)/completed_count:.2f}
- Primary Card Network: {max(card_brands.keys(), key=lambda x: card_brands[x])} ({(card_brands[max(card_brands.keys(), key=lambda x: card_brands[x])]/completed_count)*100:.1f}%)
""")
