def spend_points(points_records, spend_val):
    record_index = 0
    spend_transactions = []
    all_points_spent = True

    # Spend points
    while spend_val > 0:
        # If there are no more points available to spend, stop
        if record_index >= len(points_records):
            all_points_spent = False
            break

        # Find how many points are left to spend
        payer = points_records[record_index][0]
        points = points_records[record_index][1]
        id = points_records[record_index][2]
        new_val = spend_val - points

        if new_val < 0:
            # All requested points have been spent
            spend_transactions.append((payer, spend_val * -1, id))
        else:
            spend_transactions.append((payer, points * -1, id))

        spend_val = new_val
        record_index += 1

    return spend_transactions, all_points_spent, spend_val


def total_points(points_records):
    points_by_payer = {}

    for record in points_records:
        payer = record[0]
        points = record[1]

        if payer in points_by_payer.keys():
            points_by_payer[payer] += points
        else:
            points_by_payer[payer] = points

    return points_by_payer