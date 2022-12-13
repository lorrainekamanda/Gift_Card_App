# Generated by Django 4.1.4 on 2022-12-12 10:12

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0008_alter_product_price_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('MWK', 'MWK'), ('WST', 'WST'), ('USS', 'USS'), ('VED', 'VED'), ('SGD', 'SGD'), ('GTQ', 'GTQ'), ('KGS', 'KGS'), ('ARP', 'ARP'), ('GQE', 'GQE'), ('ILP', 'ILP'), ('KYD', 'KYD'), ('BAN', 'BAN'), ('MUR', 'MUR'), ('ESP', 'ESP'), ('KZT', 'KZT'), ('ADP', 'ADP'), ('DZD', 'DZD'), ('HKD', 'HKD'), ('MZM', 'MZM'), ('SDG', 'SDG'), ('ARS', 'ARS'), ('YER', 'YER'), ('XSU', 'XSU'), ('COP', 'COP'), ('BOB', 'BOB'), ('EUR', 'EUR'), ('KES', 'KES'), ('MCF', 'MCF'), ('BRN', 'BRN'), ('BYB', 'BYB'), ('XBB', 'XBB'), ('BUK', 'BUK'), ('PLZ', 'PLZ'), ('VEB', 'VEB'), ('SLE', 'SLE'), ('BYN', 'BYN'), ('BOP', 'BOP'), ('MTL', 'MTL'), ('MAD', 'MAD'), ('ILR', 'ILR'), ('GNS', 'GNS'), ('QAR', 'QAR'), ('AFA', 'AFA'), ('BGM', 'BGM'), ('ALL', 'ALL'), ('BRB', 'BRB'), ('CNH', 'CNH'), ('DKK', 'DKK'), ('MMK', 'MMK'), ('AZM', 'AZM'), ('IQD', 'IQD'), ('PES', 'PES'), ('UAH', 'UAH'), ('AON', 'AON'), ('AUD', 'AUD'), ('BRC', 'BRC'), ('INR', 'INR'), ('ESA', 'ESA'), ('PAB', 'PAB'), ('BRR', 'BRR'), ('LTT', 'LTT'), ('VND', 'VND'), ('BAD', 'BAD'), ('FKP', 'FKP'), ('BGO', 'BGO'), ('SCR', 'SCR'), ('RWF', 'RWF'), ('YUR', 'YUR'), ('XAU', 'XAU'), ('BWP', 'BWP'), ('GEL', 'GEL'), ('SYP', 'SYP'), ('AOA', 'AOA'), ('ZRZ', 'ZRZ'), ('ITL', 'ITL'), ('ZAL', 'ZAL'), ('JMD', 'JMD'), ('ILS', 'ILS'), ('LBP', 'LBP'), ('VUV', 'VUV'), ('GWP', 'GWP'), ('LSL', 'LSL'), ('IEP', 'IEP'), ('KRO', 'KRO'), ('MRO', 'MRO'), ('NGN', 'NGN'), ('BMD', 'BMD'), ('AZN', 'AZN'), ('BIF', 'BIF'), ('PKR', 'PKR'), ('CLP', 'CLP'), ('XBD', 'XBD'), ('NOK', 'NOK'), ('TMT', 'TMT'), ('XAG', 'XAG'), ('MDC', 'MDC'), ('RSD', 'RSD'), ('ZAR', 'ZAR'), ('TOP', 'TOP'), ('TPE', 'TPE'), ('VEF', 'VEF'), ('NIO', 'NIO'), ('LUC', 'LUC'), ('ROL', 'ROL'), ('RUB', 'RUB'), ('XOF', 'XOF'), ('CUC', 'CUC'), ('CYP', 'CYP'), ('GYD', 'GYD'), ('MNT', 'MNT'), ('BRL', 'BRL'), ('UYU', 'UYU'), ('YUD', 'YUD'), ('HRK', 'HRK'), ('DDM', 'DDM'), ('CAD', 'CAD'), ('ZMW', 'ZMW'), ('GRD', 'GRD'), ('PLN', 'PLN'), ('YDD', 'YDD'), ('KWD', 'KWD'), ('USD', 'USD'), ('UGS', 'UGS'), ('CZK', 'CZK'), ('SEK', 'SEK'), ('SVC', 'SVC'), ('CDF', 'CDF'), ('UAK', 'UAK'), ('GEK', 'GEK'), ('KRH', 'KRH'), ('MGA', 'MGA'), ('ZWL', 'ZWL'), ('TMM', 'TMM'), ('AWG', 'AWG'), ('BHD', 'BHD'), ('UYW', 'UYW'), ('GHC', 'GHC'), ('NLG', 'NLG'), ('XRE', 'XRE'), ('RHD', 'RHD'), ('PTE', 'PTE'), ('BYR', 'BYR'), ('USN', 'USN'), ('UZS', 'UZS'), ('GWE', 'GWE'), ('CUP', 'CUP'), ('KPW', 'KPW'), ('NIC', 'NIC'), ('BAM', 'BAM'), ('CHF', 'CHF'), ('ZWD', 'ZWD'), ('ATS', 'ATS'), ('SZL', 'SZL'), ('BND', 'BND'), ('TND', 'TND'), ('BSD', 'BSD'), ('SIT', 'SIT'), ('CHW', 'CHW'), ('ECV', 'ECV'), ('BGN', 'BGN'), ('LKR', 'LKR'), ('TJS', 'TJS'), ('COU', 'COU'), ('MGF', 'MGF'), ('BOV', 'BOV'), ('BEC', 'BEC'), ('BRZ', 'BRZ'), ('AOK', 'AOK'), ('OMR', 'OMR'), ('IRR', 'IRR'), ('XUA', 'XUA'), ('SOS', 'SOS'), ('XXX', 'XXX'), ('BZD', 'BZD'), ('GMD', 'GMD'), ('TJR', 'TJR'), ('BEL', 'BEL'), ('DJF', 'DJF'), ('SLL', 'SLL'), ('AOR', 'AOR'), ('TTD', 'TTD'), ('HRD', 'HRD'), ('AFN', 'AFN'), ('FIM', 'FIM'), ('BBD', 'BBD'), ('BDT', 'BDT'), ('CVE', 'CVE'), ('YUN', 'YUN'), ('SHP', 'SHP'), ('LUF', 'LUF'), ('XPF', 'XPF'), ('AED', 'AED'), ('CLF', 'CLF'), ('XPD', 'XPD'), ('GIP', 'GIP'), ('KHR', 'KHR'), ('STD', 'STD'), ('ARL', 'ARL'), ('MYR', 'MYR'), ('BOL', 'BOL'), ('SRG', 'SRG'), ('ISJ', 'ISJ'), ('XBC', 'XBC'), ('SUR', 'SUR'), ('XAF', 'XAF'), ('HUF', 'HUF'), ('MDL', 'MDL'), ('MOP', 'MOP'), ('XTS', 'XTS'), ('DOP', 'DOP'), ('MZN', 'MZN'), ('XFO', 'XFO'), ('CSK', 'CSK'), ('AMD', 'AMD'), ('TWD', 'TWD'), ('ZRN', 'ZRN'), ('JOD', 'JOD'), ('LUL', 'LUL'), ('FJD', 'FJD'), ('MLF', 'MLF'), ('TZS', 'TZS'), ('UYP', 'UYP'), ('ESB', 'ESB'), ('LVR', 'LVR'), ('MRU', 'MRU'), ('RON', 'RON'), ('EEK', 'EEK'), ('ARM', 'ARM'), ('XDR', 'XDR'), ('MXN', 'MXN'), ('GNF', 'GNF'), ('KMF', 'KMF'), ('LTL', 'LTL'), ('SKK', 'SKK'), ('STN', 'STN'), ('BTN', 'BTN'), ('GBP', 'GBP'), ('MTP', 'MTP'), ('ZMK', 'ZMK'), ('BGL', 'BGL'), ('ISK', 'ISK'), ('LRD', 'LRD'), ('KRW', 'KRW'), ('PYG', 'PYG'), ('GHS', 'GHS'), ('MVR', 'MVR'), ('XFU', 'XFU'), ('EGP', 'EGP'), ('CRC', 'CRC'), ('HTG', 'HTG'), ('VNN', 'VNN'), ('MAF', 'MAF'), ('MKD', 'MKD'), ('PGK', 'PGK'), ('CNY', 'CNY'), ('BEF', 'BEF'), ('MXV', 'MXV'), ('MVP', 'MVP'), ('TRY', 'TRY'), ('CHE', 'CHE'), ('PHP', 'PHP'), ('XPT', 'XPT'), ('CLE', 'CLE'), ('MZE', 'MZE'), ('XBA', 'XBA'), ('BRE', 'BRE'), ('ECS', 'ECS'), ('CSD', 'CSD'), ('NAD', 'NAD'), ('TRL', 'TRL'), ('SRD', 'SRD'), ('LAK', 'LAK'), ('SBD', 'SBD'), ('NPR', 'NPR'), ('SDD', 'SDD'), ('SSP', 'SSP'), ('RUR', 'RUR'), ('PEN', 'PEN'), ('ERN', 'ERN'), ('JPY', 'JPY'), ('SAR', 'SAR'), ('ETB', 'ETB'), ('MXP', 'MXP'), ('MKN', 'MKN'), ('ALK', 'ALK'), ('HNL', 'HNL'), ('LYD', 'LYD'), ('ZWR', 'ZWR'), ('ARA', 'ARA'), ('CNX', 'CNX'), ('UGX', 'UGX'), ('UYI', 'UYI'), ('FRF', 'FRF'), ('ANG', 'ANG'), ('VES', 'VES'), ('PEI', 'PEI'), ('XEU', 'XEU'), ('NZD', 'NZD'), ('IDR', 'IDR'), ('XCD', 'XCD'), ('DEM', 'DEM'), ('SDP', 'SDP'), ('YUM', 'YUM'), ('LVL', 'LVL'), ('THB', 'THB')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='giftapp.product'),
        ),
    ]
