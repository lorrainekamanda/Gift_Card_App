# Generated by Django 4.0 on 2022-12-16 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0052_alter_product_price_currency_alter_wishlist_wish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('DOP', 'DOP'), ('UZS', 'UZS'), ('KHR', 'KHR'), ('ERN', 'ERN'), ('MGF', 'MGF'), ('GRD', 'GRD'), ('DZD', 'DZD'), ('MUR', 'MUR'), ('TOP', 'TOP'), ('HRD', 'HRD'), ('ISJ', 'ISJ'), ('FIM', 'FIM'), ('MWK', 'MWK'), ('HTG', 'HTG'), ('MZE', 'MZE'), ('XBA', 'XBA'), ('MRO', 'MRO'), ('BAD', 'BAD'), ('RWF', 'RWF'), ('USN', 'USN'), ('MRU', 'MRU'), ('UYP', 'UYP'), ('VES', 'VES'), ('UAK', 'UAK'), ('LKR', 'LKR'), ('SAR', 'SAR'), ('SUR', 'SUR'), ('RSD', 'RSD'), ('GYD', 'GYD'), ('BTN', 'BTN'), ('UGX', 'UGX'), ('AON', 'AON'), ('ROL', 'ROL'), ('QAR', 'QAR'), ('EGP', 'EGP'), ('FRF', 'FRF'), ('XBB', 'XBB'), ('TZS', 'TZS'), ('BIF', 'BIF'), ('BSD', 'BSD'), ('BRB', 'BRB'), ('CNH', 'CNH'), ('GHC', 'GHC'), ('XOF', 'XOF'), ('STN', 'STN'), ('BRE', 'BRE'), ('SOS', 'SOS'), ('MTL', 'MTL'), ('EUR', 'EUR'), ('SGD', 'SGD'), ('NGN', 'NGN'), ('SSP', 'SSP'), ('PKR', 'PKR'), ('BOP', 'BOP'), ('FJD', 'FJD'), ('GWE', 'GWE'), ('BOV', 'BOV'), ('KGS', 'KGS'), ('ARS', 'ARS'), ('AWG', 'AWG'), ('MXN', 'MXN'), ('CVE', 'CVE'), ('USS', 'USS'), ('PHP', 'PHP'), ('BRC', 'BRC'), ('XEU', 'XEU'), ('GBP', 'GBP'), ('CLE', 'CLE'), ('KYD', 'KYD'), ('MXP', 'MXP'), ('LSL', 'LSL'), ('ARL', 'ARL'), ('XUA', 'XUA'), ('RUR', 'RUR'), ('WST', 'WST'), ('XXX', 'XXX'), ('HUF', 'HUF'), ('SBD', 'SBD'), ('XPF', 'XPF'), ('DDM', 'DDM'), ('LVR', 'LVR'), ('LBP', 'LBP'), ('ITL', 'ITL'), ('ZRZ', 'ZRZ'), ('BRN', 'BRN'), ('XDR', 'XDR'), ('VEB', 'VEB'), ('BAM', 'BAM'), ('ZWD', 'ZWD'), ('ADP', 'ADP'), ('BEC', 'BEC'), ('UYW', 'UYW'), ('HNL', 'HNL'), ('MVR', 'MVR'), ('CSD', 'CSD'), ('BOB', 'BOB'), ('ILS', 'ILS'), ('CNX', 'CNX'), ('LTL', 'LTL'), ('TJR', 'TJR'), ('LYD', 'LYD'), ('AFN', 'AFN'), ('GIP', 'GIP'), ('CZK', 'CZK'), ('GWP', 'GWP'), ('ISK', 'ISK'), ('ILP', 'ILP'), ('SHP', 'SHP'), ('DKK', 'DKK'), ('MMK', 'MMK'), ('LTT', 'LTT'), ('ZMK', 'ZMK'), ('MKN', 'MKN'), ('SZL', 'SZL'), ('PGK', 'PGK'), ('BND', 'BND'), ('PYG', 'PYG'), ('TTD', 'TTD'), ('XRE', 'XRE'), ('XBC', 'XBC'), ('BAN', 'BAN'), ('MGA', 'MGA'), ('NPR', 'NPR'), ('YDD', 'YDD'), ('BRZ', 'BRZ'), ('NIC', 'NIC'), ('AOR', 'AOR'), ('USD', 'USD'), ('MDL', 'MDL'), ('ALK', 'ALK'), ('SKK', 'SKK'), ('TMT', 'TMT'), ('VNN', 'VNN'), ('BRL', 'BRL'), ('SEK', 'SEK'), ('ATS', 'ATS'), ('SLL', 'SLL'), ('XAG', 'XAG'), ('XCD', 'XCD'), ('RHD', 'RHD'), ('BDT', 'BDT'), ('BMD', 'BMD'), ('JMD', 'JMD'), ('TRY', 'TRY'), ('CLF', 'CLF'), ('KRW', 'KRW'), ('YUR', 'YUR'), ('BBD', 'BBD'), ('KRH', 'KRH'), ('ALL', 'ALL'), ('BEF', 'BEF'), ('VED', 'VED'), ('GHS', 'GHS'), ('PES', 'PES'), ('GMD', 'GMD'), ('MLF', 'MLF'), ('PTE', 'PTE'), ('ARM', 'ARM'), ('MXV', 'MXV'), ('CNY', 'CNY'), ('BZD', 'BZD'), ('UYI', 'UYI'), ('KPW', 'KPW'), ('BGN', 'BGN'), ('UGS', 'UGS'), ('VEF', 'VEF'), ('MCF', 'MCF'), ('CSK', 'CSK'), ('KRO', 'KRO'), ('BHD', 'BHD'), ('ESA', 'ESA'), ('YUN', 'YUN'), ('CHE', 'CHE'), ('NOK', 'NOK'), ('BEL', 'BEL'), ('BGO', 'BGO'), ('ANG', 'ANG'), ('COP', 'COP'), ('ILR', 'ILR'), ('TWD', 'TWD'), ('XPD', 'XPD'), ('AUD', 'AUD'), ('XBD', 'XBD'), ('CDF', 'CDF'), ('AED', 'AED'), ('BGM', 'BGM'), ('YUD', 'YUD'), ('MTP', 'MTP'), ('MZN', 'MZN'), ('PAB', 'PAB'), ('MAD', 'MAD'), ('MKD', 'MKD'), ('SDD', 'SDD'), ('OMR', 'OMR'), ('MVP', 'MVP'), ('MDC', 'MDC'), ('MYR', 'MYR'), ('KES', 'KES'), ('PEI', 'PEI'), ('PLZ', 'PLZ'), ('SVC', 'SVC'), ('CUC', 'CUC'), ('ZAL', 'ZAL'), ('NAD', 'NAD'), ('CHF', 'CHF'), ('ECV', 'ECV'), ('UYU', 'UYU'), ('AOA', 'AOA'), ('AZM', 'AZM'), ('TPE', 'TPE'), ('ZMW', 'ZMW'), ('BGL', 'BGL'), ('ETB', 'ETB'), ('IDR', 'IDR'), ('ARA', 'ARA'), ('RON', 'RON'), ('UAH', 'UAH'), ('IRR', 'IRR'), ('SRG', 'SRG'), ('XPT', 'XPT'), ('GQE', 'GQE'), ('JPY', 'JPY'), ('ECS', 'ECS'), ('THB', 'THB'), ('NIO', 'NIO'), ('TMM', 'TMM'), ('TRL', 'TRL'), ('XAU', 'XAU'), ('AFA', 'AFA'), ('AZN', 'AZN'), ('ESP', 'ESP'), ('BWP', 'BWP'), ('LRD', 'LRD'), ('SIT', 'SIT'), ('RUB', 'RUB'), ('JOD', 'JOD'), ('KWD', 'KWD'), ('DEM', 'DEM'), ('ZWR', 'ZWR'), ('SDG', 'SDG'), ('GTQ', 'GTQ'), ('LVL', 'LVL'), ('BRR', 'BRR'), ('ZRN', 'ZRN'), ('BYB', 'BYB'), ('ZWL', 'ZWL'), ('SRD', 'SRD'), ('BYN', 'BYN'), ('MNT', 'MNT'), ('BOL', 'BOL'), ('VND', 'VND'), ('KZT', 'KZT'), ('TJS', 'TJS'), ('XAF', 'XAF'), ('IQD', 'IQD'), ('INR', 'INR'), ('CAD', 'CAD'), ('YUM', 'YUM'), ('CUP', 'CUP'), ('PLN', 'PLN'), ('TND', 'TND'), ('EEK', 'EEK'), ('GEK', 'GEK'), ('ARP', 'ARP'), ('XSU', 'XSU'), ('LUC', 'LUC'), ('CHW', 'CHW'), ('VUV', 'VUV'), ('MZM', 'MZM'), ('LUL', 'LUL'), ('FKP', 'FKP'), ('IEP', 'IEP'), ('HKD', 'HKD'), ('LUF', 'LUF'), ('KMF', 'KMF'), ('HRK', 'HRK'), ('LAK', 'LAK'), ('MOP', 'MOP'), ('XTS', 'XTS'), ('NZD', 'NZD'), ('PEN', 'PEN'), ('MAF', 'MAF'), ('STD', 'STD'), ('NLG', 'NLG'), ('BYR', 'BYR'), ('CRC', 'CRC'), ('CLP', 'CLP'), ('SLE', 'SLE'), ('AOK', 'AOK'), ('SCR', 'SCR'), ('SDP', 'SDP'), ('GNF', 'GNF'), ('DJF', 'DJF'), ('GEL', 'GEL'), ('YER', 'YER'), ('CYP', 'CYP'), ('GNS', 'GNS'), ('AMD', 'AMD'), ('XFO', 'XFO'), ('ZAR', 'ZAR'), ('SYP', 'SYP'), ('ESB', 'ESB'), ('COU', 'COU'), ('BUK', 'BUK'), ('XFU', 'XFU')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftapp.product'),
        ),
    ]