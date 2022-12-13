# Generated by Django 4.1.4 on 2022-12-12 20:03

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0016_alter_product_price_currency_alter_wishlist_wish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('VEB', 'VEB'), ('ZWR', 'ZWR'), ('AON', 'AON'), ('BRC', 'BRC'), ('BYN', 'BYN'), ('TWD', 'TWD'), ('NGN', 'NGN'), ('ZWL', 'ZWL'), ('GEL', 'GEL'), ('SCR', 'SCR'), ('XXX', 'XXX'), ('GBP', 'GBP'), ('GNS', 'GNS'), ('AMD', 'AMD'), ('BUK', 'BUK'), ('KPW', 'KPW'), ('BAM', 'BAM'), ('KGS', 'KGS'), ('SEK', 'SEK'), ('VNN', 'VNN'), ('LKR', 'LKR'), ('WST', 'WST'), ('TPE', 'TPE'), ('LVL', 'LVL'), ('PLZ', 'PLZ'), ('XTS', 'XTS'), ('SBD', 'SBD'), ('UZS', 'UZS'), ('USN', 'USN'), ('NIC', 'NIC'), ('THB', 'THB'), ('UYP', 'UYP'), ('LUF', 'LUF'), ('NOK', 'NOK'), ('USD', 'USD'), ('TND', 'TND'), ('ALL', 'ALL'), ('UAH', 'UAH'), ('KRH', 'KRH'), ('GHS', 'GHS'), ('BRZ', 'BRZ'), ('UYW', 'UYW'), ('YUM', 'YUM'), ('KRO', 'KRO'), ('COP', 'COP'), ('ATS', 'ATS'), ('UGS', 'UGS'), ('BEC', 'BEC'), ('BND', 'BND'), ('KRW', 'KRW'), ('YUN', 'YUN'), ('BEF', 'BEF'), ('QAR', 'QAR'), ('AOK', 'AOK'), ('SDD', 'SDD'), ('FRF', 'FRF'), ('CHW', 'CHW'), ('XOF', 'XOF'), ('PGK', 'PGK'), ('ESP', 'ESP'), ('JOD', 'JOD'), ('AOR', 'AOR'), ('DZD', 'DZD'), ('HUF', 'HUF'), ('SHP', 'SHP'), ('AFA', 'AFA'), ('UAK', 'UAK'), ('LBP', 'LBP'), ('MTL', 'MTL'), ('ROL', 'ROL'), ('IQD', 'IQD'), ('SDP', 'SDP'), ('ARM', 'ARM'), ('ESA', 'ESA'), ('AED', 'AED'), ('RHD', 'RHD'), ('XBB', 'XBB'), ('CDF', 'CDF'), ('RSD', 'RSD'), ('MKN', 'MKN'), ('MOP', 'MOP'), ('MZN', 'MZN'), ('NPR', 'NPR'), ('DOP', 'DOP'), ('ARP', 'ARP'), ('SRD', 'SRD'), ('XAF', 'XAF'), ('MAF', 'MAF'), ('BOL', 'BOL'), ('TRL', 'TRL'), ('PLN', 'PLN'), ('MUR', 'MUR'), ('SRG', 'SRG'), ('AZM', 'AZM'), ('MAD', 'MAD'), ('KZT', 'KZT'), ('CSK', 'CSK'), ('ZAR', 'ZAR'), ('MXN', 'MXN'), ('ISJ', 'ISJ'), ('KES', 'KES'), ('SVC', 'SVC'), ('MKD', 'MKD'), ('PAB', 'PAB'), ('ILP', 'ILP'), ('EUR', 'EUR'), ('BOB', 'BOB'), ('ILR', 'ILR'), ('CAD', 'CAD'), ('GEK', 'GEK'), ('SAR', 'SAR'), ('RUR', 'RUR'), ('TMM', 'TMM'), ('PES', 'PES'), ('SUR', 'SUR'), ('UGX', 'UGX'), ('TRY', 'TRY'), ('GHC', 'GHC'), ('SKK', 'SKK'), ('XBA', 'XBA'), ('KMF', 'KMF'), ('VEF', 'VEF'), ('XEU', 'XEU'), ('BGL', 'BGL'), ('MZE', 'MZE'), ('ZRZ', 'ZRZ'), ('AZN', 'AZN'), ('TJS', 'TJS'), ('MGF', 'MGF'), ('MMK', 'MMK'), ('HRD', 'HRD'), ('IRR', 'IRR'), ('CUP', 'CUP'), ('HKD', 'HKD'), ('IDR', 'IDR'), ('XRE', 'XRE'), ('LAK', 'LAK'), ('BTN', 'BTN'), ('BOP', 'BOP'), ('LTL', 'LTL'), ('LUL', 'LUL'), ('PTE', 'PTE'), ('ECS', 'ECS'), ('USS', 'USS'), ('BRL', 'BRL'), ('XAU', 'XAU'), ('SIT', 'SIT'), ('PHP', 'PHP'), ('BGO', 'BGO'), ('GWP', 'GWP'), ('BMD', 'BMD'), ('ANG', 'ANG'), ('JMD', 'JMD'), ('RWF', 'RWF'), ('MDC', 'MDC'), ('MTP', 'MTP'), ('XCD', 'XCD'), ('DJF', 'DJF'), ('AWG', 'AWG'), ('KHR', 'KHR'), ('BWP', 'BWP'), ('MCF', 'MCF'), ('BIF', 'BIF'), ('ISK', 'ISK'), ('NAD', 'NAD'), ('XPT', 'XPT'), ('JPY', 'JPY'), ('PEI', 'PEI'), ('UYU', 'UYU'), ('ALK', 'ALK'), ('BYB', 'BYB'), ('MRO', 'MRO'), ('AFN', 'AFN'), ('GQE', 'GQE'), ('BBD', 'BBD'), ('BDT', 'BDT'), ('CYP', 'CYP'), ('BHD', 'BHD'), ('MWK', 'MWK'), ('SLE', 'SLE'), ('CNY', 'CNY'), ('LUC', 'LUC'), ('GRD', 'GRD'), ('XBC', 'XBC'), ('ZMW', 'ZMW'), ('GYD', 'GYD'), ('MVR', 'MVR'), ('INR', 'INR'), ('XDR', 'XDR'), ('KWD', 'KWD'), ('LTT', 'LTT'), ('IEP', 'IEP'), ('VED', 'VED'), ('BSD', 'BSD'), ('MLF', 'MLF'), ('PEN', 'PEN'), ('SLL', 'SLL'), ('EGP', 'EGP'), ('BRN', 'BRN'), ('CLP', 'CLP'), ('OMR', 'OMR'), ('FJD', 'FJD'), ('NLG', 'NLG'), ('XSU', 'XSU'), ('AUD', 'AUD'), ('ZMK', 'ZMK'), ('ITL', 'ITL'), ('ZRN', 'ZRN'), ('PKR', 'PKR'), ('SGD', 'SGD'), ('MZM', 'MZM'), ('LYD', 'LYD'), ('XPF', 'XPF'), ('BRE', 'BRE'), ('TOP', 'TOP'), ('GMD', 'GMD'), ('GWE', 'GWE'), ('ECV', 'ECV'), ('CHE', 'CHE'), ('ARL', 'ARL'), ('ARS', 'ARS'), ('CNH', 'CNH'), ('YUR', 'YUR'), ('CLF', 'CLF'), ('VND', 'VND'), ('CHF', 'CHF'), ('TMT', 'TMT'), ('BZD', 'BZD'), ('MVP', 'MVP'), ('SSP', 'SSP'), ('BOV', 'BOV'), ('RUB', 'RUB'), ('YUD', 'YUD'), ('SYP', 'SYP'), ('HRK', 'HRK'), ('BYR', 'BYR'), ('LRD', 'LRD'), ('TJR', 'TJR'), ('XPD', 'XPD'), ('BGN', 'BGN'), ('FKP', 'FKP'), ('PYG', 'PYG'), ('XBD', 'XBD'), ('XUA', 'XUA'), ('MGA', 'MGA'), ('HNL', 'HNL'), ('STD', 'STD'), ('XFO', 'XFO'), ('KYD', 'KYD'), ('CNX', 'CNX'), ('CRC', 'CRC'), ('SDG', 'SDG'), ('YDD', 'YDD'), ('ETB', 'ETB'), ('DEM', 'DEM'), ('FIM', 'FIM'), ('TZS', 'TZS'), ('DDM', 'DDM'), ('BRR', 'BRR'), ('SOS', 'SOS'), ('GTQ', 'GTQ'), ('RON', 'RON'), ('MNT', 'MNT'), ('BAD', 'BAD'), ('MDL', 'MDL'), ('AOA', 'AOA'), ('LVR', 'LVR'), ('DKK', 'DKK'), ('STN', 'STN'), ('ZWD', 'ZWD'), ('NZD', 'NZD'), ('BAN', 'BAN'), ('ARA', 'ARA'), ('CSD', 'CSD'), ('BGM', 'BGM'), ('ADP', 'ADP'), ('BEL', 'BEL'), ('CUC', 'CUC'), ('SZL', 'SZL'), ('VES', 'VES'), ('VUV', 'VUV'), ('LSL', 'LSL'), ('TTD', 'TTD'), ('XFU', 'XFU'), ('MYR', 'MYR'), ('ZAL', 'ZAL'), ('CVE', 'CVE'), ('ERN', 'ERN'), ('YER', 'YER'), ('MRU', 'MRU'), ('MXV', 'MXV'), ('NIO', 'NIO'), ('CZK', 'CZK'), ('EEK', 'EEK'), ('HTG', 'HTG'), ('ILS', 'ILS'), ('CLE', 'CLE'), ('UYI', 'UYI'), ('BRB', 'BRB'), ('GNF', 'GNF'), ('COU', 'COU'), ('MXP', 'MXP'), ('ESB', 'ESB'), ('GIP', 'GIP'), ('XAG', 'XAG')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='name', on_delete=django.db.models.deletion.CASCADE, to='giftapp.product'),
        ),
    ]
