# Generated by Django 4.0 on 2022-12-16 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0048_alter_product_price_currency_alter_wishlist_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('KPW', 'KPW'), ('PES', 'PES'), ('FIM', 'FIM'), ('XAF', 'XAF'), ('GEK', 'GEK'), ('MLF', 'MLF'), ('HNL', 'HNL'), ('XEU', 'XEU'), ('MDL', 'MDL'), ('ERN', 'ERN'), ('LBP', 'LBP'), ('CHF', 'CHF'), ('TJS', 'TJS'), ('BZD', 'BZD'), ('ZRZ', 'ZRZ'), ('ISJ', 'ISJ'), ('OMR', 'OMR'), ('XPF', 'XPF'), ('EUR', 'EUR'), ('KRH', 'KRH'), ('MVR', 'MVR'), ('GNF', 'GNF'), ('DKK', 'DKK'), ('XAG', 'XAG'), ('FRF', 'FRF'), ('EEK', 'EEK'), ('MVP', 'MVP'), ('FKP', 'FKP'), ('ZRN', 'ZRN'), ('NAD', 'NAD'), ('ESB', 'ESB'), ('AOA', 'AOA'), ('MKN', 'MKN'), ('XRE', 'XRE'), ('BUK', 'BUK'), ('BYN', 'BYN'), ('ILR', 'ILR'), ('STD', 'STD'), ('GHS', 'GHS'), ('LVR', 'LVR'), ('BAD', 'BAD'), ('CNY', 'CNY'), ('KES', 'KES'), ('XPT', 'XPT'), ('RUR', 'RUR'), ('HUF', 'HUF'), ('MOP', 'MOP'), ('CYP', 'CYP'), ('GQE', 'GQE'), ('UAH', 'UAH'), ('XFU', 'XFU'), ('XUA', 'XUA'), ('VND', 'VND'), ('BOL', 'BOL'), ('PKR', 'PKR'), ('VNN', 'VNN'), ('KRO', 'KRO'), ('LTL', 'LTL'), ('ESP', 'ESP'), ('BTN', 'BTN'), ('SDP', 'SDP'), ('RUB', 'RUB'), ('AOR', 'AOR'), ('BOB', 'BOB'), ('DEM', 'DEM'), ('UYP', 'UYP'), ('ZAR', 'ZAR'), ('ROL', 'ROL'), ('XTS', 'XTS'), ('ZAL', 'ZAL'), ('XCD', 'XCD'), ('BRB', 'BRB'), ('CHW', 'CHW'), ('VED', 'VED'), ('LAK', 'LAK'), ('GIP', 'GIP'), ('CAD', 'CAD'), ('ETB', 'ETB'), ('AOK', 'AOK'), ('SSP', 'SSP'), ('IDR', 'IDR'), ('KMF', 'KMF'), ('CLF', 'CLF'), ('XBA', 'XBA'), ('LUC', 'LUC'), ('BYB', 'BYB'), ('MTL', 'MTL'), ('KRW', 'KRW'), ('UAK', 'UAK'), ('BYR', 'BYR'), ('GYD', 'GYD'), ('HTG', 'HTG'), ('XSU', 'XSU'), ('YDD', 'YDD'), ('PEI', 'PEI'), ('MXN', 'MXN'), ('XBC', 'XBC'), ('NIC', 'NIC'), ('LTT', 'LTT'), ('ZWD', 'ZWD'), ('YER', 'YER'), ('XBB', 'XBB'), ('NIO', 'NIO'), ('SRD', 'SRD'), ('USS', 'USS'), ('KHR', 'KHR'), ('GHC', 'GHC'), ('PAB', 'PAB'), ('HRK', 'HRK'), ('CZK', 'CZK'), ('UZS', 'UZS'), ('BRL', 'BRL'), ('BRR', 'BRR'), ('SUR', 'SUR'), ('AZN', 'AZN'), ('TWD', 'TWD'), ('HKD', 'HKD'), ('TPE', 'TPE'), ('EGP', 'EGP'), ('UYI', 'UYI'), ('YUM', 'YUM'), ('CUP', 'CUP'), ('GNS', 'GNS'), ('UGX', 'UGX'), ('DJF', 'DJF'), ('TRY', 'TRY'), ('BRZ', 'BRZ'), ('LRD', 'LRD'), ('LYD', 'LYD'), ('FJD', 'FJD'), ('ARS', 'ARS'), ('YUN', 'YUN'), ('ZWR', 'ZWR'), ('BGN', 'BGN'), ('ITL', 'ITL'), ('MCF', 'MCF'), ('LKR', 'LKR'), ('XAU', 'XAU'), ('SBD', 'SBD'), ('MAD', 'MAD'), ('BGM', 'BGM'), ('LUL', 'LUL'), ('BDT', 'BDT'), ('MAF', 'MAF'), ('ATS', 'ATS'), ('BEC', 'BEC'), ('BRE', 'BRE'), ('SDG', 'SDG'), ('JPY', 'JPY'), ('MMK', 'MMK'), ('RON', 'RON'), ('BND', 'BND'), ('BSD', 'BSD'), ('ILS', 'ILS'), ('LVL', 'LVL'), ('VEB', 'VEB'), ('AFN', 'AFN'), ('DDM', 'DDM'), ('ZMW', 'ZMW'), ('CRC', 'CRC'), ('LSL', 'LSL'), ('AED', 'AED'), ('AUD', 'AUD'), ('GBP', 'GBP'), ('RWF', 'RWF'), ('SCR', 'SCR'), ('TRL', 'TRL'), ('SLL', 'SLL'), ('CUC', 'CUC'), ('SAR', 'SAR'), ('MZM', 'MZM'), ('MZE', 'MZE'), ('CVE', 'CVE'), ('GWE', 'GWE'), ('IQD', 'IQD'), ('USN', 'USN'), ('MRO', 'MRO'), ('BGO', 'BGO'), ('TTD', 'TTD'), ('AMD', 'AMD'), ('ESA', 'ESA'), ('LUF', 'LUF'), ('TZS', 'TZS'), ('ANG', 'ANG'), ('MGF', 'MGF'), ('SEK', 'SEK'), ('MWK', 'MWK'), ('QAR', 'QAR'), ('UGS', 'UGS'), ('BGL', 'BGL'), ('ECV', 'ECV'), ('ILP', 'ILP'), ('SOS', 'SOS'), ('BMD', 'BMD'), ('ARL', 'ARL'), ('MXV', 'MXV'), ('ECS', 'ECS'), ('TOP', 'TOP'), ('AWG', 'AWG'), ('XDR', 'XDR'), ('VUV', 'VUV'), ('XPD', 'XPD'), ('THB', 'THB'), ('KYD', 'KYD'), ('TND', 'TND'), ('UYW', 'UYW'), ('NOK', 'NOK'), ('BWP', 'BWP'), ('BIF', 'BIF'), ('CSD', 'CSD'), ('IEP', 'IEP'), ('ZWL', 'ZWL'), ('RHD', 'RHD'), ('NLG', 'NLG'), ('GRD', 'GRD'), ('ZMK', 'ZMK'), ('BEL', 'BEL'), ('ISK', 'ISK'), ('BRN', 'BRN'), ('GMD', 'GMD'), ('RSD', 'RSD'), ('NZD', 'NZD'), ('XFO', 'XFO'), ('CHE', 'CHE'), ('MXP', 'MXP'), ('PGK', 'PGK'), ('GWP', 'GWP'), ('DZD', 'DZD'), ('MRU', 'MRU'), ('SZL', 'SZL'), ('HRD', 'HRD'), ('VEF', 'VEF'), ('STN', 'STN'), ('PHP', 'PHP'), ('CDF', 'CDF'), ('COP', 'COP'), ('PLZ', 'PLZ'), ('XBD', 'XBD'), ('JMD', 'JMD'), ('TJR', 'TJR'), ('XXX', 'XXX'), ('CNH', 'CNH'), ('CSK', 'CSK'), ('COU', 'COU'), ('CNX', 'CNX'), ('PYG', 'PYG'), ('AFA', 'AFA'), ('PLN', 'PLN'), ('MKD', 'MKD'), ('YUD', 'YUD'), ('KZT', 'KZT'), ('ARP', 'ARP'), ('KGS', 'KGS'), ('SYP', 'SYP'), ('MDC', 'MDC'), ('MUR', 'MUR'), ('ARA', 'ARA'), ('USD', 'USD'), ('WST', 'WST'), ('BOV', 'BOV'), ('SIT', 'SIT'), ('BEF', 'BEF'), ('PTE', 'PTE'), ('ALL', 'ALL'), ('YUR', 'YUR'), ('MZN', 'MZN'), ('PEN', 'PEN'), ('VES', 'VES'), ('BAN', 'BAN'), ('SRG', 'SRG'), ('ADP', 'ADP'), ('MNT', 'MNT'), ('MYR', 'MYR'), ('SVC', 'SVC'), ('MGA', 'MGA'), ('GEL', 'GEL'), ('XOF', 'XOF'), ('UYU', 'UYU'), ('ARM', 'ARM'), ('NGN', 'NGN'), ('SHP', 'SHP'), ('KWD', 'KWD'), ('AZM', 'AZM'), ('CLE', 'CLE'), ('BAM', 'BAM'), ('CLP', 'CLP'), ('DOP', 'DOP'), ('INR', 'INR'), ('NPR', 'NPR'), ('TMM', 'TMM'), ('IRR', 'IRR'), ('ALK', 'ALK'), ('MTP', 'MTP'), ('SLE', 'SLE'), ('SGD', 'SGD'), ('BHD', 'BHD'), ('SKK', 'SKK'), ('BBD', 'BBD'), ('BRC', 'BRC'), ('JOD', 'JOD'), ('TMT', 'TMT'), ('SDD', 'SDD'), ('BOP', 'BOP'), ('GTQ', 'GTQ'), ('AON', 'AON')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='giftapp.productcategory'),
        ),
    ]
