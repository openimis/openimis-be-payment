# Generated by Django 3.2.18 on 2023-05-16 13:12
from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_set_managed_to_true'),
    ]

    operations = [
        migrations.RunSQL(sql="""
            alter table "tblPayment" add column if not exists "TransferFee" numeric(18,2);
            alter table "tblPayment" add column if not exists "SpReconcReqId" character varying(30) NULL;
            alter table "tblPayment" add column if not exists "ReconciliationDate" timestamp NULL;
            alter table "tblPayment" add column if not exists "PayerPhoneNumber" character varying(50) NULL;
            alter table "tblPayment" add column if not exists "SmsRequired" bit NULL;
        """, reverse_sql=""),
    ] if settings.MSSQL else [
    ]
