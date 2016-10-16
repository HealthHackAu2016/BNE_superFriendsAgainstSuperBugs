# -*- coding: utf-8 -*-
from django.db import models

GENDER_CHOICES = (('1', 'Male',), ('2', 'Female',))
AGE_CHOICES = (
    ('1', '0-5',), ('2', '6-10',), ('3', '11-15',), ('4', '16-20',), ('5', '21-25',), ('6', '26-30',), ('7', '31-35',),
    ('8', '36-40',), ('9', '41-45',), ('10', '46-50',), ('11', '51-55',), ('12', '56-60',), ('13', '61-65',),
    ('14', '66-70',), ('15', '71-75',), ('16', '76-80',), ('17', '80+',))
AB_OPTIONS = (
    ('Aminocoumarin', 'Aminocoumarin'), ('Aminoglycoside', 'Aminoglycoside'), ('Beta_lactamase', 'Beta_lactamase'),
    ('Beta_lactamase_class_A', 'Beta_lactamase_class_A'), ('Beta_lactamase_class_B', 'Beta_lactamase_class_B'),
    ('Beta_lactamase_class_C', 'Beta_lactamase_class_C'), ('Beta_lactamase_class_D', 'Beta_lactamase_class_D'),
    ('Bleomycin', 'Bleomycin'), ('Chloramphenicol', 'Chloramphenicol'), ('Cycloserine', 'Cycloserine'),
    ('Aminoglycoside_daptomycin', 'Aminoglycoside_daptomycin'), ('Elfamycin', 'Elfamycin'),
    ('Ethambutol', 'Ethambutol'), ('Fluoroquinolone', 'Fluoroquinolone'), ('Fosfomycin', 'Fosfomycin'),
    ('FusidicAcid', 'FusidicAcid'), ('Lincosamide', 'Lincosamide'), ('Macrolide', 'Macrolide'),
    ('Penicillin', 'Penicillin'), ('Polymyxin', 'Polymyxin'), ('Rifampin', 'Rifampin'), ('Rifamycin', 'Rifamycin'),
    ('Streptothricin', 'Streptothricin'), ('Sulfonamide', 'Sulfonamide'), ('Tetracycline', 'Tetracycline'),
    ('Trimethoprim', 'Trimethoprim'), ('Tunicamycin', 'Tunicamycin'),
    ('Aminoglycoside_vancomycin', 'Aminoglycoside_vancomycin'), ('Viomycin', 'Viomycin'))
COUNTRY_OPTION = (
    ('-', '- select -'), ('AF', 'Afghanistan'), ('AX', 'Åland Islands'), ('AL', 'Albania'), ('DZ', 'Algeria'),
    ('AS', 'American Samoa'), ('AD', 'Andorra'), ('AO', 'Angola'), ('AI', 'Anguilla'), ('AQ', 'Antarctica'),
    ('AG', 'Antigua and Barbuda'), ('AR', 'Argentina'), ('AM', 'Armenia'), ('AW', 'Aruba'), ('AU', 'Australia'),
    ('AT', 'Austria'), ('AZ', 'Azerbaijan'), ('BS', 'Bahamas'), ('BH', 'Bahrain'), ('BD', 'Bangladesh'),
    ('BB', 'Barbados'), ('BY', 'Belarus'), ('BE', 'Belgium'), ('BZ', 'Belize'), ('BJ', 'Benin'), ('BM', 'Bermuda'),
    ('BT', 'Bhutan'), ('BO', 'Bolivia'), ('BQ', 'Bonaire, Sint Eustatius and Saba'), ('BA', 'Bosnia and Herzegovina'),
    ('BW', 'Botswana'), ('BV', 'Bouvet Island'), ('BR', 'Brazil'), ('IO', 'British Indian Ocean Territory'),
    ('BN', 'Brunei'), ('BG', 'Bulgaria'), ('BF', 'Burkina Faso'), ('BI', 'Burundi'), ('CV', 'Cabo Verde'),
    ('KH', 'Cambodia'), ('CM', 'Cameroon'), ('CA', 'Canada'), ('KY', 'Cayman Islands'),
    ('CF', 'Central African Republic'), ('TD', 'Chad'), ('CL', 'Chile'), ('CN', 'China'), ('CX', 'Christmas Island'),
    ('CC', 'Cocos (Keeling) Islands'), ('CO', 'Colombia'), ('KM', 'Comoros'), ('CG', 'Congo'),
    ('CD', 'Congo (the Democratic Republic of the)'), ('CK', 'Cook Islands'), ('CR', 'Costa Rica'),
    ('CI', 'Côte d&#39;Ivoire'), ('HR', 'Croatia'), ('CU', 'Cuba'), ('CW', 'Curaçao'), ('CY', 'Cyprus'),
    ('CZ', 'Czech Republic'), ('DK', 'Denmark'), ('DJ', 'Djibouti'), ('DM', 'Dominica'), ('DO', 'Dominican Republic'),
    ('EC', 'Ecuador'), ('EG', 'Egypt'), ('SV', 'El Salvador'), ('GQ', 'Equatorial Guinea'), ('ER', 'Eritrea'),
    ('EE', 'Estonia'), ('ET', 'Ethiopia'), ('FK', 'Falkland Islands [Malvinas]'), ('FO', 'Faroe Islands'),
    ('FJ', 'Fiji'), ('FI', 'Finland'), ('FR', 'France'), ('GF', 'French Guiana'), ('PF', 'French Polynesia'),
    ('TF', 'French Southern Territories'), ('GA', 'Gabon'), ('GM', 'Gambia'), ('GE', 'Georgia'), ('DE', 'Germany'),
    ('GH', 'Ghana'), ('GI', 'Gibraltar'), ('GR', 'Greece'), ('GL', 'Greenland'), ('GD', 'Grenada'),
    ('GP', 'Guadeloupe'), ('GU', 'Guam'), ('GT', 'Guatemala'), ('GG', 'Guernsey'), ('GN', 'Guinea'),
    ('GW', 'Guinea-Bissau'), ('GY', 'Guyana'), ('HT', 'Haiti'), ('HM', 'Heard Island and McDonald Islands'),
    ('VA', 'Holy See'), ('HN', 'Honduras'), ('HK', 'Hong Kong'), ('HU', 'Hungary'), ('IS', 'Iceland'), ('IN', 'India'),
    ('ID', 'Indonesia'), ('IR', 'Iran'), ('IQ', 'Iraq'), ('IE', 'Ireland'), ('IM', 'Isle of Man'), ('IL', 'Israel'),
    ('IT', 'Italy'), ('JM', 'Jamaica'), ('JP', 'Japan'), ('JE', 'Jersey'), ('JO', 'Jordan'), ('KZ', 'Kazakhstan'),
    ('KE', 'Kenya'), ('KI', 'Kiribati'), ('KW', 'Kuwait'), ('KG', 'Kyrgyzstan'), ('LA', 'Laos'), ('LV', 'Latvia'),
    ('LB', 'Lebanon'), ('LS', 'Lesotho'), ('LR', 'Liberia'), ('LY', 'Libya'), ('LI', 'Liechtenstein'),
    ('LT', 'Lithuania'), ('LU', 'Luxembourg'), ('MO', 'Macao'), ('MK', 'Macedonia'), ('MG', 'Madagascar'),
    ('MW', 'Malawi'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('ML', 'Mali'), ('MT', 'Malta'),
    ('MH', 'Marshall Islands'), ('MQ', 'Martinique'), ('MR', 'Mauritania'), ('MU', 'Mauritius'), ('YT', 'Mayotte'),
    ('MX', 'Mexico'), ('FM', 'Micronesia (Federated States of)'), ('MD', 'Moldova'), ('MC', 'Monaco'),
    ('MN', 'Mongolia'), ('ME', 'Montenegro'), ('MS', 'Montserrat'), ('MA', 'Morocco'), ('MZ', 'Mozambique'),
    ('MM', 'Myanmar'), ('NA', 'Namibia'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NL', 'Netherlands'),
    ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('NI', 'Nicaragua'), ('NE', 'Niger'), ('NG', 'Nigeria'),
    ('NU', 'Niue'), ('NF', 'Norfolk Island'), ('KP', 'North Korea'), ('MP', 'Northern Mariana Islands'),
    ('NO', 'Norway'), ('OM', 'Oman'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PS', 'Palestine, State of'),
    ('PA', 'Panama'), ('PG', 'Papua New Guinea'), ('PY', 'Paraguay'), ('PE', 'Peru'), ('PH', 'Philippines'),
    ('PN', 'Pitcairn'), ('PL', 'Poland'), ('PT', 'Portugal'), ('PR', 'Puerto Rico'), ('QA', 'Qatar'), ('RE', 'Réunion'),
    ('RO', 'Romania'), ('RU', 'Russia'), ('RW', 'Rwanda'), ('BL', 'Saint Barthélemy'),
    ('SH', 'Saint Helena, Ascension and Tristan da Cunha'), ('KN', 'Saint Kitts and Nevis'), ('LC', 'Saint Lucia'),
    ('MF', 'Saint Martin (French part)'), ('PM', 'Saint Pierre and Miquelon'),
    ('VC', 'Saint Vincent and the Grenadines'), ('WS', 'Samoa'), ('SM', 'San Marino'), ('ST', 'Sao Tome and Principe'),
    ('SA', 'Saudi Arabia'), ('SN', 'Senegal'), ('RS', 'Serbia'), ('SC', 'Seychelles'), ('SL', 'Sierra Leone'),
    ('SG', 'Singapore'), ('SX', 'Sint Maarten (Dutch part)'), ('SK', 'Slovakia'), ('SI', 'Slovenia'),
    ('SB', 'Solomon Islands'), ('SO', 'Somalia'), ('ZA', 'South Africa'),
    ('GS', 'South Georgia and the South Sandwich Islands'), ('KR', 'South Korea'), ('SS', 'South Sudan'),
    ('ES', 'Spain'), ('LK', 'Sri Lanka'), ('SD', 'Sudan'), ('SR', 'Suriname'), ('SJ', 'Svalbard and Jan Mayen'),
    ('SZ', 'Swaziland'), ('SE', 'Sweden'), ('CH', 'Switzerland'), ('SY', 'Syria'), ('TW', 'Taiwan'),
    ('TJ', 'Tajikistan'), ('TZ', 'Tanzania'), ('TH', 'Thailand'), ('TL', 'Timor-Leste'), ('TG', 'Togo'),
    ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TT', 'Trinidad and Tobago'), ('TN', 'Tunisia'), ('TR', 'Turkey'),
    ('TM', 'Turkmenistan'), ('TC', 'Turks and Caicos Islands'), ('TV', 'Tuvalu'), ('UG', 'Uganda'), ('UA', 'Ukraine'),
    ('AE', 'United Arab Emirates'), ('GB', 'United Kingdom'), ('UM', 'United States Minor Outlying Islands'),
    ('US', 'United States of America'), ('UY', 'Uruguay'), ('UZ', 'Uzbekistan'), ('VU', 'Vanuatu'), ('VE', 'Venezuela'),
    ('VN', 'Vietnam'), ('VG', 'Virgin Islands (British)'), ('VI', 'Virgin Islands (U.S.)'), ('WF', 'Wallis and Futuna'),
    ('EH', 'Western Sahara'), ('YE', 'Yemen'), ('ZM', 'Zambia'), ('ZW', 'Zimbabwe'))


class Sample(models.Model):
    date = models.DateField()
    hospital = models.CharField(max_length=15)
    ward = models.CharField(max_length=10)
    doctor = models.CharField(max_length=25)
    gender = models.IntegerField()
    age_group = models.IntegerField()
    postcode = models.IntegerField()
    country = models.CharField(max_length=3)
    travel_last_6_m = models.CharField(max_length=3)
    condition = models.TextField()
    allergies_ab = models.TextField()
    current_ab = models.TextField()
    specie = models.TextField()
    strain = models.TextField()
    resistances = models.TextField()

