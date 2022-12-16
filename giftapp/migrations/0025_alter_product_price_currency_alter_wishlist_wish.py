# Generated by Django 4.0 on 2022-12-13 21:49

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0024_alter_product_price_currency_alter_wishlist_wish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('AON', 'AON'), ('LUF', 'LUF'), ('ZMK', 'ZMK'), ('BEL', 'BEL'), ('GWP', 'GWP'), ('ECV', 'ECV'), ('IEP', 'IEP'), ('LUC', 'LUC'), ('KRW', 'KRW'), ('CNX', 'CNX'), ('CUP', 'CUP'), ('LVR', 'LVR'), ('BRE', 'BRE'), ('HRK', 'HRK'), ('CDF', 'CDF'), ('MXN', 'MXN'), ('MTL', 'MTL'), ('CUC', 'CUC'), ('ALL', 'ALL'), ('BSD', 'BSD'), ('XAF', 'XAF'), ('GIP', 'GIP'), ('ILS', 'ILS'), ('SAR', 'SAR'), ('GYD', 'GYD'), ('MNT', 'MNT'), ('UYW', 'UYW'), ('AFN', 'AFN'), ('BRZ', 'BRZ'), ('XRE', 'XRE'), ('BAM', 'BAM'), ('CHF', 'CHF'), ('TWD', 'TWD'), ('ZMW', 'ZMW'), ('XBA', 'XBA'), ('BZD', 'BZD'), ('SDP', 'SDP'), ('BRC', 'BRC'), ('RHD', 'RHD'), ('BRR', 'BRR'), ('TRY', 'TRY'), ('YDD', 'YDD'), ('BOP', 'BOP'), ('CAD', 'CAD'), ('MKD', 'MKD'), ('SCR', 'SCR'), ('MRU', 'MRU'), ('NAD', 'NAD'), ('PES', 'PES'), ('KRO', 'KRO'), ('ITL', 'ITL'), ('LVL', 'LVL'), ('SSP', 'SSP'), ('MYR', 'MYR'), ('AOR', 'AOR'), ('COP', 'COP'), ('MXV', 'MXV'), ('SRD', 'SRD'), ('ARL', 'ARL'), ('SZL', 'SZL'), ('XEU', 'XEU'), ('BRN', 'BRN'), ('MTP', 'MTP'), ('EUR', 'EUR'), ('MOP', 'MOP'), ('WST', 'WST'), ('CSD', 'CSD'), ('MZE', 'MZE'), ('USD', 'USD'), ('MDL', 'MDL'), ('ARA', 'ARA'), ('GRD', 'GRD'), ('MGF', 'MGF'), ('UYI', 'UYI'), ('LUL', 'LUL'), ('XUA', 'XUA'), ('IRR', 'IRR'), ('STN', 'STN'), ('AZN', 'AZN'), ('PEN', 'PEN'), ('MMK', 'MMK'), ('VES', 'VES'), ('ESP', 'ESP'), ('SIT', 'SIT'), ('ILP', 'ILP'), ('JMD', 'JMD'), ('KES', 'KES'), ('HUF', 'HUF'), ('BGN', 'BGN'), ('CYP', 'CYP'), ('NIC', 'NIC'), ('USS', 'USS'), ('SLE', 'SLE'), ('AMD', 'AMD'), ('ARP', 'ARP'), ('RSD', 'RSD'), ('BGL', 'BGL'), ('RUB', 'RUB'), ('TZS', 'TZS'), ('FKP', 'FKP'), ('ZRZ', 'ZRZ'), ('KPW', 'KPW'), ('NPR', 'NPR'), ('DDM', 'DDM'), ('EGP', 'EGP'), ('PLN', 'PLN'), ('LTL', 'LTL'), ('SVC', 'SVC'), ('MUR', 'MUR'), ('PTE', 'PTE'), ('UAK', 'UAK'), ('XXX', 'XXX'), ('ARM', 'ARM'), ('BOB', 'BOB'), ('TMM', 'TMM'), ('ZRN', 'ZRN'), ('PEI', 'PEI'), ('XFU', 'XFU'), ('XAU', 'XAU'), ('DJF', 'DJF'), ('ECS', 'ECS'), ('DKK', 'DKK'), ('XOF', 'XOF'), ('OMR', 'OMR'), ('RUR', 'RUR'), ('MVP', 'MVP'), ('NLG', 'NLG'), ('ESA', 'ESA'), ('BOL', 'BOL'), ('BOV', 'BOV'), ('ZWR', 'ZWR'), ('TJR', 'TJR'), ('AOK', 'AOK'), ('BTN', 'BTN'), ('MZN', 'MZN'), ('ANG', 'ANG'), ('BEC', 'BEC'), ('ISK', 'ISK'), ('ZWL', 'ZWL'), ('SRG', 'SRG'), ('SHP', 'SHP'), ('BDT', 'BDT'), ('CHE', 'CHE'), ('ROL', 'ROL'), ('HRD', 'HRD'), ('VUV', 'VUV'), ('DOP', 'DOP'), ('LBP', 'LBP'), ('YUR', 'YUR'), ('BYB', 'BYB'), ('VND', 'VND'), ('CLP', 'CLP'), ('PKR', 'PKR'), ('TTD', 'TTD'), ('XFO', 'XFO'), ('AWG', 'AWG'), ('BRB', 'BRB'), ('NOK', 'NOK'), ('ETB', 'ETB'), ('BHD', 'BHD'), ('NIO', 'NIO'), ('GEK', 'GEK'), ('VED', 'VED'), ('JOD', 'JOD'), ('BND', 'BND'), ('STD', 'STD'), ('KRH', 'KRH'), ('VEB', 'VEB'), ('CSK', 'CSK'), ('MAD', 'MAD'), ('PHP', 'PHP'), ('VEF', 'VEF'), ('CLE', 'CLE'), ('PYG', 'PYG'), ('UZS', 'UZS'), ('MCF', 'MCF'), ('BEF', 'BEF'), ('SUR', 'SUR'), ('LAK', 'LAK'), ('GNF', 'GNF'), ('BYR', 'BYR'), ('SEK', 'SEK'), ('UYP', 'UYP'), ('TRL', 'TRL'), ('SDG', 'SDG'), ('ESB', 'ESB'), ('SGD', 'SGD'), ('GQE', 'GQE'), ('PLZ', 'PLZ'), ('GMD', 'GMD'), ('YUN', 'YUN'), ('DZD', 'DZD'), ('IQD', 'IQD'), ('CZK', 'CZK'), ('MAF', 'MAF'), ('MGA', 'MGA'), ('MWK', 'MWK'), ('XAG', 'XAG'), ('ZWD', 'ZWD'), ('KWD', 'KWD'), ('THB', 'THB'), ('ZAR', 'ZAR'), ('AUD', 'AUD'), ('CNH', 'CNH'), ('SLL', 'SLL'), ('BMD', 'BMD'), ('RWF', 'RWF'), ('BIF', 'BIF'), ('BUK', 'BUK'), ('SDD', 'SDD'), ('RON', 'RON'), ('UYU', 'UYU'), ('IDR', 'IDR'), ('TND', 'TND'), ('GNS', 'GNS'), ('TJS', 'TJS'), ('HTG', 'HTG'), ('YUM', 'YUM'), ('USN', 'USN'), ('EEK', 'EEK'), ('GTQ', 'GTQ'), ('GEL', 'GEL'), ('LTT', 'LTT'), ('XDR', 'XDR'), ('AZM', 'AZM'), ('CHW', 'CHW'), ('BWP', 'BWP'), ('GBP', 'GBP'), ('XSU', 'XSU'), ('MDC', 'MDC'), ('UGX', 'UGX'), ('MRO', 'MRO'), ('YER', 'YER'), ('MKN', 'MKN'), ('HKD', 'HKD'), ('COU', 'COU'), ('BBD', 'BBD'), ('BGO', 'BGO'), ('FRF', 'FRF'), ('CLF', 'CLF'), ('MLF', 'MLF'), ('MVR', 'MVR'), ('SYP', 'SYP'), ('XBD', 'XBD'), ('XTS', 'XTS'), ('KZT', 'KZT'), ('ERN', 'ERN'), ('AFA', 'AFA'), ('BAD', 'BAD'), ('JPY', 'JPY'), ('MZM', 'MZM'), ('ARS', 'ARS'), ('LKR', 'LKR'), ('LYD', 'LYD'), ('INR', 'INR'), ('GHC', 'GHC'), ('NGN', 'NGN'), ('XPT', 'XPT'), ('CNY', 'CNY'), ('VNN', 'VNN'), ('SKK', 'SKK'), ('MXP', 'MXP'), ('XPF', 'XPF'), ('LSL', 'LSL'), ('ADP', 'ADP'), ('SOS', 'SOS'), ('UAH', 'UAH'), ('XBB', 'XBB'), ('CRC', 'CRC'), ('ISJ', 'ISJ'), ('ZAL', 'ZAL'), ('TMT', 'TMT'), ('YUD', 'YUD'), ('FIM', 'FIM'), ('AED', 'AED'), ('NZD', 'NZD'), ('FJD', 'FJD'), ('UGS', 'UGS'), ('BGM', 'BGM'), ('HNL', 'HNL'), ('KMF', 'KMF'), ('PAB', 'PAB'), ('TOP', 'TOP'), ('CVE', 'CVE'), ('LRD', 'LRD'), ('BAN', 'BAN'), ('DEM', 'DEM'), ('QAR', 'QAR'), ('XBC', 'XBC'), ('KGS', 'KGS'), ('XPD', 'XPD'), ('AOA', 'AOA'), ('BRL', 'BRL'), ('TPE', 'TPE'), ('KYD', 'KYD'), ('BYN', 'BYN'), ('ATS', 'ATS'), ('ILR', 'ILR'), ('ALK', 'ALK'), ('GHS', 'GHS'), ('GWE', 'GWE'), ('SBD', 'SBD'), ('PGK', 'PGK'), ('KHR', 'KHR'), ('XCD', 'XCD')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='name', default='1', on_delete=django.db.models.deletion.CASCADE, to='giftapp.product'),
        ),
    ]