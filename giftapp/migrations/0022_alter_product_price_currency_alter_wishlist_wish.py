# Generated by Django 4.0 on 2022-12-13 20:28

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0021_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_currency',
            field=models.CharField(choices=[('JOD', 'JOD'), ('BSD', 'BSD'), ('TPE', 'TPE'), ('MTP', 'MTP'), ('LTL', 'LTL'), ('SGD', 'SGD'), ('ZRN', 'ZRN'), ('NGN', 'NGN'), ('VEF', 'VEF'), ('ALK', 'ALK'), ('XPT', 'XPT'), ('AOK', 'AOK'), ('BEC', 'BEC'), ('PHP', 'PHP'), ('SLE', 'SLE'), ('ISJ', 'ISJ'), ('ROL', 'ROL'), ('IDR', 'IDR'), ('MNT', 'MNT'), ('LUL', 'LUL'), ('GRD', 'GRD'), ('GBP', 'GBP'), ('KGS', 'KGS'), ('MVP', 'MVP'), ('MUR', 'MUR'), ('UAH', 'UAH'), ('BGN', 'BGN'), ('MAD', 'MAD'), ('ILS', 'ILS'), ('BRB', 'BRB'), ('CRC', 'CRC'), ('KMF', 'KMF'), ('BAD', 'BAD'), ('SUR', 'SUR'), ('CYP', 'CYP'), ('SAR', 'SAR'), ('XEU', 'XEU'), ('GWE', 'GWE'), ('MAF', 'MAF'), ('BAN', 'BAN'), ('MLF', 'MLF'), ('UZS', 'UZS'), ('MWK', 'MWK'), ('MGF', 'MGF'), ('XFO', 'XFO'), ('USN', 'USN'), ('GTQ', 'GTQ'), ('BOP', 'BOP'), ('ITL', 'ITL'), ('CZK', 'CZK'), ('AMD', 'AMD'), ('XPD', 'XPD'), ('UYU', 'UYU'), ('NAD', 'NAD'), ('TND', 'TND'), ('BWP', 'BWP'), ('BRE', 'BRE'), ('GWP', 'GWP'), ('XCD', 'XCD'), ('BIF', 'BIF'), ('GYD', 'GYD'), ('ARL', 'ARL'), ('ETB', 'ETB'), ('RWF', 'RWF'), ('UYW', 'UYW'), ('DZD', 'DZD'), ('CNY', 'CNY'), ('BOV', 'BOV'), ('GHC', 'GHC'), ('TMT', 'TMT'), ('CLF', 'CLF'), ('ZWR', 'ZWR'), ('UGX', 'UGX'), ('BDT', 'BDT'), ('BGL', 'BGL'), ('YUM', 'YUM'), ('SYP', 'SYP'), ('RSD', 'RSD'), ('PEN', 'PEN'), ('LKR', 'LKR'), ('ERN', 'ERN'), ('ZRZ', 'ZRZ'), ('BGO', 'BGO'), ('ISK', 'ISK'), ('LRD', 'LRD'), ('LAK', 'LAK'), ('LSL', 'LSL'), ('TZS', 'TZS'), ('BOB', 'BOB'), ('VUV', 'VUV'), ('CSD', 'CSD'), ('UGS', 'UGS'), ('TTD', 'TTD'), ('PLN', 'PLN'), ('KRH', 'KRH'), ('LUF', 'LUF'), ('MXV', 'MXV'), ('AFN', 'AFN'), ('LVR', 'LVR'), ('STD', 'STD'), ('XBD', 'XBD'), ('NLG', 'NLG'), ('TJR', 'TJR'), ('JMD', 'JMD'), ('XBC', 'XBC'), ('YUR', 'YUR'), ('KHR', 'KHR'), ('INR', 'INR'), ('SRD', 'SRD'), ('AED', 'AED'), ('CNH', 'CNH'), ('MZM', 'MZM'), ('SHP', 'SHP'), ('ARA', 'ARA'), ('BUK', 'BUK'), ('RHD', 'RHD'), ('MTL', 'MTL'), ('MKN', 'MKN'), ('BRN', 'BRN'), ('VNN', 'VNN'), ('AUD', 'AUD'), ('BTN', 'BTN'), ('ARP', 'ARP'), ('XXX', 'XXX'), ('PKR', 'PKR'), ('BYB', 'BYB'), ('TRY', 'TRY'), ('XBA', 'XBA'), ('TJS', 'TJS'), ('XFU', 'XFU'), ('PEI', 'PEI'), ('RUR', 'RUR'), ('HRD', 'HRD'), ('MKD', 'MKD'), ('AOA', 'AOA'), ('ESA', 'ESA'), ('XDR', 'XDR'), ('RON', 'RON'), ('BOL', 'BOL'), ('BMD', 'BMD'), ('SBD', 'SBD'), ('SKK', 'SKK'), ('KRW', 'KRW'), ('FKP', 'FKP'), ('ANG', 'ANG'), ('CNX', 'CNX'), ('MYR', 'MYR'), ('AWG', 'AWG'), ('BND', 'BND'), ('BYN', 'BYN'), ('CHF', 'CHF'), ('CHW', 'CHW'), ('GMD', 'GMD'), ('HRK', 'HRK'), ('RUB', 'RUB'), ('USS', 'USS'), ('LVL', 'LVL'), ('MXP', 'MXP'), ('MMK', 'MMK'), ('FRF', 'FRF'), ('BRC', 'BRC'), ('EEK', 'EEK'), ('VED', 'VED'), ('PTE', 'PTE'), ('SVC', 'SVC'), ('BRR', 'BRR'), ('KYD', 'KYD'), ('SDD', 'SDD'), ('IRR', 'IRR'), ('HNL', 'HNL'), ('AON', 'AON'), ('GQE', 'GQE'), ('AZN', 'AZN'), ('CUC', 'CUC'), ('XPF', 'XPF'), ('TOP', 'TOP'), ('MOP', 'MOP'), ('OMR', 'OMR'), ('TMM', 'TMM'), ('THB', 'THB'), ('ILP', 'ILP'), ('ADP', 'ADP'), ('PAB', 'PAB'), ('MZN', 'MZN'), ('XSU', 'XSU'), ('ZMW', 'ZMW'), ('BEL', 'BEL'), ('HUF', 'HUF'), ('SCR', 'SCR'), ('MRU', 'MRU'), ('BAM', 'BAM'), ('BYR', 'BYR'), ('UYP', 'UYP'), ('BBD', 'BBD'), ('CUP', 'CUP'), ('CAD', 'CAD'), ('LUC', 'LUC'), ('TWD', 'TWD'), ('NOK', 'NOK'), ('BHD', 'BHD'), ('ZAR', 'ZAR'), ('GNF', 'GNF'), ('MVR', 'MVR'), ('WST', 'WST'), ('SIT', 'SIT'), ('ZAL', 'ZAL'), ('DEM', 'DEM'), ('BEF', 'BEF'), ('MDL', 'MDL'), ('DKK', 'DKK'), ('XAF', 'XAF'), ('GNS', 'GNS'), ('ILR', 'ILR'), ('BZD', 'BZD'), ('ZMK', 'ZMK'), ('XAG', 'XAG'), ('ARM', 'ARM'), ('YDD', 'YDD'), ('DJF', 'DJF'), ('SSP', 'SSP'), ('TRL', 'TRL'), ('ALL', 'ALL'), ('KPW', 'KPW'), ('CLP', 'CLP'), ('USD', 'USD'), ('XOF', 'XOF'), ('FIM', 'FIM'), ('KZT', 'KZT'), ('ECV', 'ECV'), ('MRO', 'MRO'), ('MGA', 'MGA'), ('JPY', 'JPY'), ('FJD', 'FJD'), ('VES', 'VES'), ('KES', 'KES'), ('SDP', 'SDP'), ('VND', 'VND'), ('SRG', 'SRG'), ('XBB', 'XBB'), ('GIP', 'GIP'), ('PYG', 'PYG'), ('MDC', 'MDC'), ('EGP', 'EGP'), ('LBP', 'LBP'), ('MZE', 'MZE'), ('IEP', 'IEP'), ('SDG', 'SDG'), ('IQD', 'IQD'), ('YER', 'YER'), ('UAK', 'UAK'), ('HKD', 'HKD'), ('BGM', 'BGM'), ('QAR', 'QAR'), ('XUA', 'XUA'), ('GEL', 'GEL'), ('SEK', 'SEK'), ('XTS', 'XTS'), ('VEB', 'VEB'), ('CDF', 'CDF'), ('LTT', 'LTT'), ('COP', 'COP'), ('KWD', 'KWD'), ('CSK', 'CSK'), ('EUR', 'EUR'), ('SOS', 'SOS'), ('ZWL', 'ZWL'), ('UYI', 'UYI'), ('ZWD', 'ZWD'), ('KRO', 'KRO'), ('XAU', 'XAU'), ('YUD', 'YUD'), ('CHE', 'CHE'), ('PGK', 'PGK'), ('GEK', 'GEK'), ('PES', 'PES'), ('YUN', 'YUN'), ('XRE', 'XRE'), ('DDM', 'DDM'), ('SZL', 'SZL'), ('ECS', 'ECS'), ('CLE', 'CLE'), ('NPR', 'NPR'), ('ESP', 'ESP'), ('DOP', 'DOP'), ('NIO', 'NIO'), ('NZD', 'NZD'), ('BRZ', 'BRZ'), ('MCF', 'MCF'), ('ESB', 'ESB'), ('ARS', 'ARS'), ('SLL', 'SLL'), ('COU', 'COU'), ('GHS', 'GHS'), ('LYD', 'LYD'), ('HTG', 'HTG'), ('NIC', 'NIC'), ('PLZ', 'PLZ'), ('CVE', 'CVE'), ('STN', 'STN'), ('AOR', 'AOR'), ('AZM', 'AZM'), ('AFA', 'AFA'), ('MXN', 'MXN'), ('ATS', 'ATS'), ('BRL', 'BRL')], default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='wish',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='category', chained_model_field='name', horizontal=True, to='giftapp.Product'),
        ),
    ]