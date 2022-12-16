# Generated by Django 4.0 on 2022-12-13 23:55

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0034_alter_product_price_currency_alter_wishlist_wish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('BWP', 'BWP'), ('UAH', 'UAH'), ('XBB', 'XBB'), ('MDC', 'MDC'), ('NIC', 'NIC'), ('ZAR', 'ZAR'), ('BGN', 'BGN'), ('MCF', 'MCF'), ('BAD', 'BAD'), ('BYR', 'BYR'), ('SGD', 'SGD'), ('SRD', 'SRD'), ('TMT', 'TMT'), ('FIM', 'FIM'), ('EUR', 'EUR'), ('BGO', 'BGO'), ('VES', 'VES'), ('YDD', 'YDD'), ('KRO', 'KRO'), ('GIP', 'GIP'), ('BND', 'BND'), ('BOL', 'BOL'), ('ECS', 'ECS'), ('AZN', 'AZN'), ('NGN', 'NGN'), ('ADP', 'ADP'), ('TPE', 'TPE'), ('CAD', 'CAD'), ('ECV', 'ECV'), ('AUD', 'AUD'), ('IEP', 'IEP'), ('YUD', 'YUD'), ('VUV', 'VUV'), ('DDM', 'DDM'), ('KGS', 'KGS'), ('ZWD', 'ZWD'), ('ALK', 'ALK'), ('ZRZ', 'ZRZ'), ('BHD', 'BHD'), ('MKN', 'MKN'), ('JMD', 'JMD'), ('NIO', 'NIO'), ('OMR', 'OMR'), ('KWD', 'KWD'), ('NPR', 'NPR'), ('PES', 'PES'), ('BAN', 'BAN'), ('CHW', 'CHW'), ('MZE', 'MZE'), ('NAD', 'NAD'), ('FKP', 'FKP'), ('ILP', 'ILP'), ('TOP', 'TOP'), ('DOP', 'DOP'), ('UZS', 'UZS'), ('PGK', 'PGK'), ('LTL', 'LTL'), ('ERN', 'ERN'), ('UYU', 'UYU'), ('XPT', 'XPT'), ('MOP', 'MOP'), ('XFU', 'XFU'), ('MGF', 'MGF'), ('GQE', 'GQE'), ('SYP', 'SYP'), ('TJS', 'TJS'), ('UYP', 'UYP'), ('XBD', 'XBD'), ('NOK', 'NOK'), ('CHF', 'CHF'), ('CRC', 'CRC'), ('MUR', 'MUR'), ('HRK', 'HRK'), ('LVL', 'LVL'), ('ZRN', 'ZRN'), ('ISK', 'ISK'), ('HNL', 'HNL'), ('ESB', 'ESB'), ('GHS', 'GHS'), ('GWE', 'GWE'), ('ZWL', 'ZWL'), ('JOD', 'JOD'), ('RUR', 'RUR'), ('AON', 'AON'), ('GYD', 'GYD'), ('SZL', 'SZL'), ('SOS', 'SOS'), ('CNH', 'CNH'), ('AZM', 'AZM'), ('XXX', 'XXX'), ('XAF', 'XAF'), ('LUC', 'LUC'), ('MGA', 'MGA'), ('GTQ', 'GTQ'), ('TND', 'TND'), ('BEF', 'BEF'), ('BYN', 'BYN'), ('EEK', 'EEK'), ('QAR', 'QAR'), ('MRO', 'MRO'), ('SSP', 'SSP'), ('AOA', 'AOA'), ('MLF', 'MLF'), ('TWD', 'TWD'), ('MXP', 'MXP'), ('XBC', 'XBC'), ('VEB', 'VEB'), ('BUK', 'BUK'), ('CUC', 'CUC'), ('PAB', 'PAB'), ('MNT', 'MNT'), ('BBD', 'BBD'), ('BRR', 'BRR'), ('ZMW', 'ZMW'), ('XDR', 'XDR'), ('XAG', 'XAG'), ('SEK', 'SEK'), ('MZN', 'MZN'), ('XUA', 'XUA'), ('ISJ', 'ISJ'), ('DZD', 'DZD'), ('DJF', 'DJF'), ('THB', 'THB'), ('CLE', 'CLE'), ('HKD', 'HKD'), ('TZS', 'TZS'), ('ARS', 'ARS'), ('XCD', 'XCD'), ('HUF', 'HUF'), ('LBP', 'LBP'), ('XTS', 'XTS'), ('MZM', 'MZM'), ('GWP', 'GWP'), ('MRU', 'MRU'), ('NZD', 'NZD'), ('SLE', 'SLE'), ('ZAL', 'ZAL'), ('LSL', 'LSL'), ('ROL', 'ROL'), ('ARM', 'ARM'), ('NLG', 'NLG'), ('COP', 'COP'), ('INR', 'INR'), ('PEN', 'PEN'), ('ESA', 'ESA'), ('BRL', 'BRL'), ('GBP', 'GBP'), ('VED', 'VED'), ('XBA', 'XBA'), ('XPD', 'XPD'), ('YUN', 'YUN'), ('BMD', 'BMD'), ('XSU', 'XSU'), ('BSD', 'BSD'), ('UYI', 'UYI'), ('ANG', 'ANG'), ('KYD', 'KYD'), ('JPY', 'JPY'), ('SDP', 'SDP'), ('AOR', 'AOR'), ('BRB', 'BRB'), ('MXV', 'MXV'), ('FJD', 'FJD'), ('LRD', 'LRD'), ('KMF', 'KMF'), ('COU', 'COU'), ('STD', 'STD'), ('PLN', 'PLN'), ('PYG', 'PYG'), ('CNX', 'CNX'), ('BEL', 'BEL'), ('EGP', 'EGP'), ('MAF', 'MAF'), ('FRF', 'FRF'), ('ARP', 'ARP'), ('SBD', 'SBD'), ('XOF', 'XOF'), ('SUR', 'SUR'), ('BRC', 'BRC'), ('HTG', 'HTG'), ('XPF', 'XPF'), ('SHP', 'SHP'), ('SVC', 'SVC'), ('ITL', 'ITL'), ('PHP', 'PHP'), ('BRZ', 'BRZ'), ('AFA', 'AFA'), ('BGL', 'BGL'), ('KPW', 'KPW'), ('MXN', 'MXN'), ('ILR', 'ILR'), ('AFN', 'AFN'), ('CVE', 'CVE'), ('ARL', 'ARL'), ('BTN', 'BTN'), ('SRG', 'SRG'), ('BZD', 'BZD'), ('BRN', 'BRN'), ('LVR', 'LVR'), ('GNS', 'GNS'), ('PEI', 'PEI'), ('SLL', 'SLL'), ('WST', 'WST'), ('GHC', 'GHC'), ('TJR', 'TJR'), ('MDL', 'MDL'), ('GRD', 'GRD'), ('CZK', 'CZK'), ('BOB', 'BOB'), ('LUF', 'LUF'), ('TTD', 'TTD'), ('YUM', 'YUM'), ('HRD', 'HRD'), ('RUB', 'RUB'), ('VND', 'VND'), ('RON', 'RON'), ('LTT', 'LTT'), ('YUR', 'YUR'), ('BIF', 'BIF'), ('GNF', 'GNF'), ('SDG', 'SDG'), ('TMM', 'TMM'), ('USN', 'USN'), ('UGS', 'UGS'), ('ATS', 'ATS'), ('CYP', 'CYP'), ('AWG', 'AWG'), ('KZT', 'KZT'), ('XEU', 'XEU'), ('MYR', 'MYR'), ('MKD', 'MKD'), ('BOV', 'BOV'), ('RSD', 'RSD'), ('ESP', 'ESP'), ('ZWR', 'ZWR'), ('XRE', 'XRE'), ('AOK', 'AOK'), ('BAM', 'BAM'), ('GMD', 'GMD'), ('UAK', 'UAK'), ('RHD', 'RHD'), ('VEF', 'VEF'), ('IDR', 'IDR'), ('GEK', 'GEK'), ('CLF', 'CLF'), ('ALL', 'ALL'), ('ZMK', 'ZMK'), ('LUL', 'LUL'), ('USS', 'USS'), ('BRE', 'BRE'), ('BDT', 'BDT'), ('IRR', 'IRR'), ('UYW', 'UYW'), ('AMD', 'AMD'), ('XAU', 'XAU'), ('LKR', 'LKR'), ('SAR', 'SAR'), ('BYB', 'BYB'), ('SDD', 'SDD'), ('CUP', 'CUP'), ('DKK', 'DKK'), ('BGM', 'BGM'), ('CLP', 'CLP'), ('VNN', 'VNN'), ('SIT', 'SIT'), ('MMK', 'MMK'), ('DEM', 'DEM'), ('RWF', 'RWF'), ('MVP', 'MVP'), ('CSK', 'CSK'), ('GEL', 'GEL'), ('SKK', 'SKK'), ('IQD', 'IQD'), ('CNY', 'CNY'), ('PLZ', 'PLZ'), ('BEC', 'BEC'), ('XFO', 'XFO'), ('TRY', 'TRY'), ('BOP', 'BOP'), ('MTP', 'MTP'), ('SCR', 'SCR'), ('STN', 'STN'), ('CDF', 'CDF'), ('MVR', 'MVR'), ('MWK', 'MWK'), ('PTE', 'PTE'), ('ARA', 'ARA'), ('KRW', 'KRW'), ('UGX', 'UGX'), ('YER', 'YER'), ('PKR', 'PKR'), ('LYD', 'LYD'), ('ETB', 'ETB'), ('TRL', 'TRL'), ('MAD', 'MAD'), ('USD', 'USD'), ('ILS', 'ILS'), ('KRH', 'KRH'), ('LAK', 'LAK'), ('CSD', 'CSD'), ('KES', 'KES'), ('KHR', 'KHR'), ('AED', 'AED'), ('MTL', 'MTL'), ('CHE', 'CHE')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='name', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='giftapp.product'),
        ),
    ]