# Generated by Django 4.0 on 2022-12-16 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0050_remove_wishlist_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('XXX', 'XXX'), ('INR', 'INR'), ('VES', 'VES'), ('XTS', 'XTS'), ('PEI', 'PEI'), ('KRO', 'KRO'), ('ZMW', 'ZMW'), ('CNH', 'CNH'), ('JOD', 'JOD'), ('SAR', 'SAR'), ('XEU', 'XEU'), ('RUB', 'RUB'), ('VND', 'VND'), ('IQD', 'IQD'), ('GHC', 'GHC'), ('SBD', 'SBD'), ('LUF', 'LUF'), ('WST', 'WST'), ('CRC', 'CRC'), ('GHS', 'GHS'), ('GWE', 'GWE'), ('UZS', 'UZS'), ('KES', 'KES'), ('BRB', 'BRB'), ('PTE', 'PTE'), ('ALK', 'ALK'), ('AFN', 'AFN'), ('BOV', 'BOV'), ('KRH', 'KRH'), ('MWK', 'MWK'), ('MGF', 'MGF'), ('XAG', 'XAG'), ('XBA', 'XBA'), ('LTL', 'LTL'), ('XOF', 'XOF'), ('SDP', 'SDP'), ('ARA', 'ARA'), ('GNS', 'GNS'), ('AMD', 'AMD'), ('LKR', 'LKR'), ('MVR', 'MVR'), ('SVC', 'SVC'), ('RON', 'RON'), ('BOL', 'BOL'), ('PYG', 'PYG'), ('RSD', 'RSD'), ('BTN', 'BTN'), ('AFA', 'AFA'), ('PLZ', 'PLZ'), ('SGD', 'SGD'), ('SRG', 'SRG'), ('LVR', 'LVR'), ('VUV', 'VUV'), ('UYI', 'UYI'), ('NLG', 'NLG'), ('USN', 'USN'), ('MZM', 'MZM'), ('XBD', 'XBD'), ('HUF', 'HUF'), ('OMR', 'OMR'), ('KPW', 'KPW'), ('LSL', 'LSL'), ('MTP', 'MTP'), ('HRD', 'HRD'), ('CHW', 'CHW'), ('SIT', 'SIT'), ('PEN', 'PEN'), ('XDR', 'XDR'), ('BEF', 'BEF'), ('MCF', 'MCF'), ('TOP', 'TOP'), ('HTG', 'HTG'), ('NGN', 'NGN'), ('BGO', 'BGO'), ('MGA', 'MGA'), ('SDD', 'SDD'), ('MRU', 'MRU'), ('ETB', 'ETB'), ('PAB', 'PAB'), ('EGP', 'EGP'), ('ARL', 'ARL'), ('CUC', 'CUC'), ('LRD', 'LRD'), ('MMK', 'MMK'), ('JMD', 'JMD'), ('FRF', 'FRF'), ('VEF', 'VEF'), ('SLE', 'SLE'), ('TMM', 'TMM'), ('DKK', 'DKK'), ('MZE', 'MZE'), ('CAD', 'CAD'), ('AED', 'AED'), ('BRL', 'BRL'), ('ISJ', 'ISJ'), ('BGM', 'BGM'), ('GIP', 'GIP'), ('UGS', 'UGS'), ('LTT', 'LTT'), ('BGL', 'BGL'), ('KWD', 'KWD'), ('ZRZ', 'ZRZ'), ('ERN', 'ERN'), ('DEM', 'DEM'), ('AON', 'AON'), ('ILS', 'ILS'), ('MLF', 'MLF'), ('BYB', 'BYB'), ('BEC', 'BEC'), ('PLN', 'PLN'), ('AZM', 'AZM'), ('XUA', 'XUA'), ('BEL', 'BEL'), ('HRK', 'HRK'), ('MZN', 'MZN'), ('AOR', 'AOR'), ('YUN', 'YUN'), ('BIF', 'BIF'), ('TWD', 'TWD'), ('ADP', 'ADP'), ('UAK', 'UAK'), ('MNT', 'MNT'), ('TRL', 'TRL'), ('USD', 'USD'), ('SKK', 'SKK'), ('SCR', 'SCR'), ('USS', 'USS'), ('SRD', 'SRD'), ('GMD', 'GMD'), ('MDC', 'MDC'), ('CSK', 'CSK'), ('XSU', 'XSU'), ('ARS', 'ARS'), ('XCD', 'XCD'), ('CUP', 'CUP'), ('MTL', 'MTL'), ('TZS', 'TZS'), ('BRC', 'BRC'), ('GTQ', 'GTQ'), ('YER', 'YER'), ('AZN', 'AZN'), ('ARP', 'ARP'), ('MXP', 'MXP'), ('BZD', 'BZD'), ('SUR', 'SUR'), ('CNY', 'CNY'), ('MAF', 'MAF'), ('RWF', 'RWF'), ('XPD', 'XPD'), ('RUR', 'RUR'), ('VNN', 'VNN'), ('CLE', 'CLE'), ('SDG', 'SDG'), ('LUL', 'LUL'), ('BRE', 'BRE'), ('KZT', 'KZT'), ('BRN', 'BRN'), ('BHD', 'BHD'), ('NAD', 'NAD'), ('SOS', 'SOS'), ('YDD', 'YDD'), ('XRE', 'XRE'), ('CZK', 'CZK'), ('XBC', 'XBC'), ('KRW', 'KRW'), ('SLL', 'SLL'), ('ROL', 'ROL'), ('YUM', 'YUM'), ('DOP', 'DOP'), ('HKD', 'HKD'), ('BRR', 'BRR'), ('STN', 'STN'), ('COP', 'COP'), ('SSP', 'SSP'), ('MXN', 'MXN'), ('MKN', 'MKN'), ('SEK', 'SEK'), ('ITL', 'ITL'), ('THB', 'THB'), ('EEK', 'EEK'), ('EUR', 'EUR'), ('ILP', 'ILP'), ('NPR', 'NPR'), ('CLP', 'CLP'), ('ZAR', 'ZAR'), ('TND', 'TND'), ('MOP', 'MOP'), ('ISK', 'ISK'), ('TRY', 'TRY'), ('BWP', 'BWP'), ('BUK', 'BUK'), ('GEK', 'GEK'), ('ZAL', 'ZAL'), ('GNF', 'GNF'), ('SZL', 'SZL'), ('NOK', 'NOK'), ('UYP', 'UYP'), ('MYR', 'MYR'), ('CVE', 'CVE'), ('TTD', 'TTD'), ('XAF', 'XAF'), ('CHE', 'CHE'), ('CNX', 'CNX'), ('ECS', 'ECS'), ('ECV', 'ECV'), ('BAN', 'BAN'), ('IDR', 'IDR'), ('PGK', 'PGK'), ('TMT', 'TMT'), ('BMD', 'BMD'), ('UAH', 'UAH'), ('BBD', 'BBD'), ('ANG', 'ANG'), ('ZMK', 'ZMK'), ('RHD', 'RHD'), ('ARM', 'ARM'), ('TPE', 'TPE'), ('AWG', 'AWG'), ('IRR', 'IRR'), ('STD', 'STD'), ('DJF', 'DJF'), ('YUD', 'YUD'), ('LVL', 'LVL'), ('CDF', 'CDF'), ('UYU', 'UYU'), ('ESA', 'ESA'), ('ZRN', 'ZRN'), ('PKR', 'PKR'), ('ZWR', 'ZWR'), ('KGS', 'KGS'), ('BOB', 'BOB'), ('NZD', 'NZD'), ('XFU', 'XFU'), ('XBB', 'XBB'), ('PES', 'PES'), ('MRO', 'MRO'), ('GYD', 'GYD'), ('NIO', 'NIO'), ('SHP', 'SHP'), ('GWP', 'GWP'), ('IEP', 'IEP'), ('QAR', 'QAR'), ('AOK', 'AOK'), ('PHP', 'PHP'), ('MKD', 'MKD'), ('MAD', 'MAD'), ('LBP', 'LBP'), ('TJS', 'TJS'), ('GQE', 'GQE'), ('BYR', 'BYR'), ('ZWL', 'ZWL'), ('COU', 'COU'), ('CYP', 'CYP'), ('MXV', 'MXV'), ('BAM', 'BAM'), ('DDM', 'DDM'), ('UGX', 'UGX'), ('ESB', 'ESB'), ('AUD', 'AUD'), ('CLF', 'CLF'), ('XPT', 'XPT'), ('UYW', 'UYW'), ('BAD', 'BAD'), ('BRZ', 'BRZ'), ('XFO', 'XFO'), ('BSD', 'BSD'), ('LYD', 'LYD'), ('FIM', 'FIM'), ('VED', 'VED'), ('DZD', 'DZD'), ('ATS', 'ATS'), ('BDT', 'BDT'), ('LUC', 'LUC'), ('FKP', 'FKP'), ('LAK', 'LAK'), ('HNL', 'HNL'), ('ZWD', 'ZWD'), ('BYN', 'BYN'), ('KMF', 'KMF'), ('ILR', 'ILR'), ('NIC', 'NIC'), ('CHF', 'CHF'), ('SYP', 'SYP'), ('VEB', 'VEB'), ('YUR', 'YUR'), ('JPY', 'JPY'), ('MUR', 'MUR'), ('MVP', 'MVP'), ('XPF', 'XPF'), ('ALL', 'ALL'), ('ESP', 'ESP'), ('GEL', 'GEL'), ('AOA', 'AOA'), ('GRD', 'GRD'), ('FJD', 'FJD'), ('KYD', 'KYD'), ('TJR', 'TJR'), ('XAU', 'XAU'), ('BND', 'BND'), ('CSD', 'CSD'), ('BGN', 'BGN'), ('MDL', 'MDL'), ('GBP', 'GBP'), ('BOP', 'BOP'), ('KHR', 'KHR')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='giftapp.product'),
        ),
    ]