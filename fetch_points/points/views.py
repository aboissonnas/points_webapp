from datetime import datetime

from django.shortcuts import render

from .forms import AddForm, SpendForm
from .models import PointsRecord
from . import utils


def index(request):
    return render(request, 'points/index.html')


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            # Get data from form
            payer = form.cleaned_data['payer']
            points = form.cleaned_data['points']
            time_stamp = form.cleaned_data['timestamp']

            # Create row in database
            PointsRecord.objects.create(payer=payer, value=points, timestamp=time_stamp)
    else:
        form = AddForm()

    return render(request, 'points/add.html', {'form': form})


def spend(request):
    if request.method == 'POST':
        form = SpendForm(request.POST)
        if form.is_valid():
            spend_val = form.cleaned_data['points']
            points_records = PointsRecord.objects.filter(is_spent=False).order_by('timestamp')
            points_list = points_records.values_list('payer', 'value', 'id')

            # Spending negative points isn't a thing. Ensure spend_val is positive
            if spend_val < 0:
                spend_val = spend_val * -1

            # Spend points
            spend_transactions, all_points_spent, spend_val = utils.spend_points(points_list, spend_val)

            # Total spend transactions per payer
            total_spent = utils.total_points(spend_transactions)

            # Create new records for spend transactions
            for payer in total_spent.keys():
                PointsRecord.objects.create(payer=payer, value=total_spent[payer], timestamp=datetime.now(), is_spent=True)

            # Find the last transaction
            last_transaction_id = spend_transactions[len(spend_transactions) - 1][2]
            last_transaction_record = points_records.get(id=last_transaction_id)

            # If the last transaction didn't use up all the points in the record that will be labeled "spent",
            # create a new, backdated record with the remainder            
            if spend_val < 0:
                payer = last_transaction_record.payer
                timestamp = last_transaction_record.timestamp
                PointsRecord.objects.create(payer=payer, value=spend_val * -1, timestamp=timestamp)

            # Label all spent points "spent"
            for spend_record in spend_transactions:
                db_record = points_records.get(id=spend_record[2])
                db_record.is_spent = True
                db_record.save()

            context = {
                'total_spent': total_spent,
                'all_points_spent': all_points_spent,
                'spend_val': spend_val,
            }

            return render(request, 'points/spend_return.html', context)

    else:
        form = SpendForm()

    return render(request, 'points/spend.html', {'form': form})


def balance(request):
    # Find and total all unspent points
    all_points_records = PointsRecord.objects.filter(is_spent=False).order_by('timestamp').values_list('payer', 'value')
    points_by_payer = utils.total_points(all_points_records)

    # Check for any payers with balance 0 and add them to the list
    unique_payers = PointsRecord.objects.all().values_list('payer', flat=True).distinct()
    for payer in unique_payers:
        if payer not in points_by_payer.keys():
            points_by_payer[payer] = 0

    return render(request, 'points/balance.html', {'points_by_payer': points_by_payer})