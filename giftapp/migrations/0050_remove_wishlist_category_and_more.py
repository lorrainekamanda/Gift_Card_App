# Generated by Django 4.0 on 2022-12-16 11:51

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0049_alter_product_price_currency_alter_wishlist_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('GWE', 'GWE'), ('MAF', 'MAF'), ('MUR', 'MUR'), ('MZM', 'MZM'), ('SLE', 'SLE'), ('ARL', 'ARL'), ('XBA', 'XBA'), ('PES', 'PES'), ('PEN', 'PEN'), ('STN', 'STN'), ('ARS', 'ARS'), ('RON', 'RON'), ('AOK', 'AOK'), ('PGK', 'PGK'), ('MKN', 'MKN'), ('NGN', 'NGN'), ('XPT', 'XPT'), ('TTD', 'TTD'), ('ZAR', 'ZAR'), ('BGM', 'BGM'), ('DKK', 'DKK'), ('CVE', 'CVE'), ('BRL', 'BRL'), ('SEK', 'SEK'), ('AMD', 'AMD'), ('EEK', 'EEK'), ('XAG', 'XAG'), ('IQD', 'IQD'), ('STD', 'STD'), ('BGO', 'BGO'), ('HKD', 'HKD'), ('SRD', 'SRD'), ('MDC', 'MDC'), ('BRC', 'BRC'), ('GRD', 'GRD'), ('PAB', 'PAB'), ('TPE', 'TPE'), ('ESP', 'ESP'), ('ZAL', 'ZAL'), ('BAN', 'BAN'), ('SVC', 'SVC'), ('NIC', 'NIC'), ('IEP', 'IEP'), ('GNF', 'GNF'), ('XFO', 'XFO'), ('LVL', 'LVL'), ('ALK', 'ALK'), ('BIF', 'BIF'), ('XXX', 'XXX'), ('BYN', 'BYN'), ('USD', 'USD'), ('HTG', 'HTG'), ('ISJ', 'ISJ'), ('AZM', 'AZM'), ('ILR', 'ILR'), ('YUD', 'YUD'), ('BMD', 'BMD'), ('MYR', 'MYR'), ('BYR', 'BYR'), ('JOD', 'JOD'), ('KRW', 'KRW'), ('PLN', 'PLN'), ('SZL', 'SZL'), ('MLF', 'MLF'), ('BYB', 'BYB'), ('VND', 'VND'), ('USS', 'USS'), ('SYP', 'SYP'), ('SRG', 'SRG'), ('ZWL', 'ZWL'), ('ERN', 'ERN'), ('KPW', 'KPW'), ('BDT', 'BDT'), ('ETB', 'ETB'), ('LUF', 'LUF'), ('EGP', 'EGP'), ('GQE', 'GQE'), ('TJR', 'TJR'), ('SDD', 'SDD'), ('ZMW', 'ZMW'), ('XFU', 'XFU'), ('MWK', 'MWK'), ('GTQ', 'GTQ'), ('TND', 'TND'), ('MOP', 'MOP'), ('TMT', 'TMT'), ('TJS', 'TJS'), ('CSK', 'CSK'), ('BTN', 'BTN'), ('CYP', 'CYP'), ('PHP', 'PHP'), ('FKP', 'FKP'), ('AOR', 'AOR'), ('XAF', 'XAF'), ('KES', 'KES'), ('XBC', 'XBC'), ('CHW', 'CHW'), ('XTS', 'XTS'), ('SLL', 'SLL'), ('MDL', 'MDL'), ('MZE', 'MZE'), ('COP', 'COP'), ('SKK', 'SKK'), ('CLF', 'CLF'), ('GHS', 'GHS'), ('CDF', 'CDF'), ('XOF', 'XOF'), ('LSL', 'LSL'), ('AFN', 'AFN'), ('OMR', 'OMR'), ('XDR', 'XDR'), ('UAK', 'UAK'), ('QAR', 'QAR'), ('RHD', 'RHD'), ('MCF', 'MCF'), ('COU', 'COU'), ('CAD', 'CAD'), ('THB', 'THB'), ('KHR', 'KHR'), ('LVR', 'LVR'), ('ZWR', 'ZWR'), ('VEB', 'VEB'), ('VED', 'VED'), ('LUC', 'LUC'), ('VNN', 'VNN'), ('WST', 'WST'), ('XUA', 'XUA'), ('BZD', 'BZD'), ('IDR', 'IDR'), ('MTL', 'MTL'), ('MXV', 'MXV'), ('MZN', 'MZN'), ('UYP', 'UYP'), ('HUF', 'HUF'), ('LRD', 'LRD'), ('BEF', 'BEF'), ('ZRZ', 'ZRZ'), ('CRC', 'CRC'), ('JMD', 'JMD'), ('MXP', 'MXP'), ('LTT', 'LTT'), ('VEF', 'VEF'), ('YDD', 'YDD'), ('XSU', 'XSU'), ('SOS', 'SOS'), ('TOP', 'TOP'), ('BRE', 'BRE'), ('FRF', 'FRF'), ('GHC', 'GHC'), ('JPY', 'JPY'), ('CHE', 'CHE'), ('UAH', 'UAH'), ('UYU', 'UYU'), ('SGD', 'SGD'), ('XEU', 'XEU'), ('KRO', 'KRO'), ('XBD', 'XBD'), ('DDM', 'DDM'), ('PLZ', 'PLZ'), ('DEM', 'DEM'), ('SCR', 'SCR'), ('KGS', 'KGS'), ('LYD', 'LYD'), ('RUB', 'RUB'), ('GEK', 'GEK'), ('MVP', 'MVP'), ('LKR', 'LKR'), ('YUR', 'YUR'), ('XCD', 'XCD'), ('RSD', 'RSD'), ('TRY', 'TRY'), ('BEL', 'BEL'), ('BOP', 'BOP'), ('BRN', 'BRN'), ('ZWD', 'ZWD'), ('ZRN', 'ZRN'), ('CSD', 'CSD'), ('YUN', 'YUN'), ('CLP', 'CLP'), ('UGS', 'UGS'), ('AED', 'AED'), ('BUK', 'BUK'), ('LBP', 'LBP'), ('ALL', 'ALL'), ('UZS', 'UZS'), ('MGF', 'MGF'), ('BAM', 'BAM'), ('AON', 'AON'), ('SUR', 'SUR'), ('NZD', 'NZD'), ('ESA', 'ESA'), ('HNL', 'HNL'), ('XPD', 'XPD'), ('FIM', 'FIM'), ('GYD', 'GYD'), ('NAD', 'NAD'), ('GWP', 'GWP'), ('HRD', 'HRD'), ('MVR', 'MVR'), ('ROL', 'ROL'), ('CLE', 'CLE'), ('AZN', 'AZN'), ('MXN', 'MXN'), ('VES', 'VES'), ('ZMK', 'ZMK'), ('DJF', 'DJF'), ('NPR', 'NPR'), ('ATS', 'ATS'), ('YUM', 'YUM'), ('BBD', 'BBD'), ('AWG', 'AWG'), ('MTP', 'MTP'), ('BHD', 'BHD'), ('CUC', 'CUC'), ('CNX', 'CNX'), ('CZK', 'CZK'), ('NOK', 'NOK'), ('YER', 'YER'), ('TMM', 'TMM'), ('PTE', 'PTE'), ('KRH', 'KRH'), ('BND', 'BND'), ('BRZ', 'BRZ'), ('BRR', 'BRR'), ('AOA', 'AOA'), ('ARA', 'ARA'), ('EUR', 'EUR'), ('CNY', 'CNY'), ('ISK', 'ISK'), ('CUP', 'CUP'), ('MGA', 'MGA'), ('TRL', 'TRL'), ('GNS', 'GNS'), ('BEC', 'BEC'), ('FJD', 'FJD'), ('DZD', 'DZD'), ('ARP', 'ARP'), ('AFA', 'AFA'), ('BOV', 'BOV'), ('ILP', 'ILP'), ('ANG', 'ANG'), ('KWD', 'KWD'), ('BWP', 'BWP'), ('ADP', 'ADP'), ('LTL', 'LTL'), ('KMF', 'KMF'), ('PYG', 'PYG'), ('ARM', 'ARM'), ('HRK', 'HRK'), ('XBB', 'XBB'), ('XRE', 'XRE'), ('MNT', 'MNT'), ('BOL', 'BOL'), ('BOB', 'BOB'), ('MMK', 'MMK'), ('ECV', 'ECV'), ('UGX', 'UGX'), ('VUV', 'VUV'), ('XPF', 'XPF'), ('USN', 'USN'), ('SAR', 'SAR'), ('LAK', 'LAK'), ('SBD', 'SBD'), ('PEI', 'PEI'), ('SHP', 'SHP'), ('PKR', 'PKR'), ('GEL', 'GEL'), ('TWD', 'TWD'), ('TZS', 'TZS'), ('LUL', 'LUL'), ('MAD', 'MAD'), ('UYW', 'UYW'), ('GBP', 'GBP'), ('NIO', 'NIO'), ('KZT', 'KZT'), ('XAU', 'XAU'), ('BSD', 'BSD'), ('BGL', 'BGL'), ('SDP', 'SDP'), ('NLG', 'NLG'), ('INR', 'INR'), ('BGN', 'BGN'), ('GMD', 'GMD'), ('CHF', 'CHF'), ('ILS', 'ILS'), ('MKD', 'MKD'), ('IRR', 'IRR'), ('BRB', 'BRB'), ('GIP', 'GIP'), ('UYI', 'UYI'), ('MRO', 'MRO'), ('SIT', 'SIT'), ('RUR', 'RUR'), ('CNH', 'CNH'), ('ECS', 'ECS'), ('RWF', 'RWF'), ('SSP', 'SSP'), ('BAD', 'BAD'), ('DOP', 'DOP'), ('ESB', 'ESB'), ('ITL', 'ITL'), ('SDG', 'SDG'), ('MRU', 'MRU'), ('KYD', 'KYD'), ('AUD', 'AUD')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=smart_selects.db_fields.ChainedForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='giftapp.product'),
        ),
    ]
