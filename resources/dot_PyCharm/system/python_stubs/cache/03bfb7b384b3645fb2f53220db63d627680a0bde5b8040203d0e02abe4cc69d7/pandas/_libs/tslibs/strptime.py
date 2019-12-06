# encoding: utf-8
# module pandas._libs.tslibs.strptime
# from C:\Python27\lib\site-packages\pandas\_libs\tslibs\strptime.pyd
# by generator 1.147
""" Strptime-related classes and functions. """

# imports
import locale as locale # C:\Python27\lib\locale.pyc
import calendar as calendar # C:\Python27\lib\calendar.pyc
import re as re # C:\Python27\lib\re.pyc
import numpy as np # C:\Python27\lib\site-packages\numpy\__init__.pyc
import __builtin__ as __builtins__ # <module '__builtin__' (built-in)>
import pytz as pytz # C:\Python27\lib\site-packages\pytz\__init__.pyc
import time as time # <module 'time' (built-in)>
from datetime import datetime_date

from thread import _thread_allocate_lock


# Variables with simple values

_CACHE_MAX_SIZE = 5

# functions

def array_strptime(*args, **kwargs): # real signature unknown
    """
    Calculates the datetime structs represented by the passed array of strings
    
        Parameters
        ----------
        values : ndarray of string-like objects
        fmt : string-like regex
        exact : matches must be exact if True, search if False
        errors : string specifying error handling, {'raise', 'ignore', 'coerce'}
    """
    pass

def _getlang(*args, **kwargs): # real signature unknown
    """ Figure out what language is being used for the locale """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class LocaleTime(object):
    """
    Stores and handles locale-specific information related to time.
    
        ATTRIBUTES:
            f_weekday -- full weekday names (7-item list)
            a_weekday -- abbreviated weekday names (7-item list)
            f_month -- full month names (13-item list; dummy value in [0], which
                        is added by code)
            a_month -- abbreviated month names (13-item list, dummy value in
                        [0], which is added by code)
            am_pm -- AM/PM representation (2-item list)
            LC_date_time -- format string for date/time representation (string)
            LC_date -- format string for date representation (string)
            LC_time -- format string for time representation (string)
            timezone -- daylight- and non-daylight-savings timezone representation
                        (2-item list of sets)
            lang -- Language used by instance (2-item tuple)
    """
    def _LocaleTime__calc_am_pm(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_date_time(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_month(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_timezone(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__calc_weekday(self, *args, **kwargs): # real signature unknown
        pass

    def _LocaleTime__pad(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Set all attributes.
        
                Order of methods called matters for dependency reasons.
        
                The locale language is set at the offset and then checked again before
                exiting.  This is to make sure that the attributes were not set with a
                mix of information from more than one locale.  This would most likely
                happen when using threads where one thread calls a locale-dependent
                function while another thread changes the locale while the function in
                the other thread is still running.  Proper coding would call for
                locks to prevent changing the locale while locale-dependent code is
                running.  The check here is done in case someone does not think about
                doing this.
        
                Only other possible issue is if someone changed the timezone and did
                not call tz.tzset .  That is an issue for the programmer, though,
                since changing the timezone is worthless without that call.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "dict_proxy({'_LocaleTime__calc_am_pm': <cyfunction LocaleTime.__calc_am_pm at 0x00000000036FB048>, '__module__': 'pandas._libs.tslibs.strptime', '_LocaleTime__calc_weekday': <cyfunction LocaleTime.__calc_weekday at 0x00000000036F4E88>, '_LocaleTime__calc_date_time': <cyfunction LocaleTime.__calc_date_time at 0x00000000036FB108>, '__qualname__': 'LocaleTime', '_LocaleTime__pad': <cyfunction LocaleTime.__pad at 0x00000000036F4DC8>, '__dict__': <attribute '__dict__' of 'LocaleTime' objects>, '_LocaleTime__calc_timezone': <cyfunction LocaleTime.__calc_timezone at 0x00000000036FB1C8>, '_LocaleTime__calc_month': <cyfunction LocaleTime.__calc_month at 0x00000000036F4F48>, '__weakref__': <attribute '__weakref__' of 'LocaleTime' objects>, '__doc__': 'Stores and handles locale-specific information related to time.\\n\\n    ATTRIBUTES:\\n        f_weekday -- full weekday names (7-item list)\\n        a_weekday -- abbreviated weekday names (7-item list)\\n        f_month -- full month names (13-item list; dummy value in [0], which\\n                    is added by code)\\n        a_month -- abbreviated month names (13-item list, dummy value in\\n                    [0], which is added by code)\\n        am_pm -- AM/PM representation (2-item list)\\n        LC_date_time -- format string for date/time representation (string)\\n        LC_date -- format string for date representation (string)\\n        LC_time -- format string for time representation (string)\\n        timezone -- daylight- and non-daylight-savings timezone representation\\n                    (2-item list of sets)\\n        lang -- Language used by instance (2-item tuple)\\n    ', '__init__': <cyfunction LocaleTime.__init__ at 0x00000000036F4D08>})"
    __qualname__ = 'LocaleTime'


class TimeRE(dict):
    """
    Handle conversion from format directives to regexes.
    
        Creates regexes for pattern matching a string of text containing
        time information
    """
    def compile(self, *args, **kwargs): # real signature unknown
        """ Return a compiled re object for the format string. """
        pass

    def pattern(self, *args, **kwargs): # real signature unknown
        """
        Return regex pattern for the format string.
        
                Need to make sure that any characters that might be interpreted as
                regex syntax are escaped.
        """
        pass

    def _TimeRE__seqToRE(self, *args, **kwargs): # real signature unknown
        """
        Convert a list to a regex string for matching a directive.
        
                Want possible matching values to be from longest to shortest.  This
                prevents the possibility of a match occurring for a value that also
                a substring of a larger value that should have matched (e.g., 'abc'
                matching when 'abcdef' should have been the match).
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        """
        Create keys/values.
        
                Order of execution is important for dependency reasons.
        """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "dict_proxy({'compile': <cyfunction TimeRE.compile at 0x00000000036FB4C8>, '__qualname__': 'TimeRE', '__module__': 'pandas._libs.tslibs.strptime', '__dict__': <attribute '__dict__' of 'TimeRE' objects>, 'pattern': <cyfunction TimeRE.pattern at 0x00000000036FB408>, '_TimeRE__seqToRE': <cyfunction TimeRE.__seqToRE at 0x00000000036FB348>, '__weakref__': <attribute '__weakref__' of 'TimeRE' objects>, '__doc__': '\\n    Handle conversion from format directives to regexes.\\n\\n    Creates regexes for pattern matching a string of text containing\\n    time information\\n    ', '__init__': <cyfunction TimeRE.__init__ at 0x00000000036FB288>})"
    __qualname__ = 'TimeRE'


# variables with complex values

nat_strings = None # (!) real value is "set(['nat', 'NaT', 'NAN', 'nan', 'NaN', 'NAT'])"

_cache_lock = None # (!) real value is '<thread.lock object at 0x00000000025FB8B0>'

_regex_cache = {}

_TimeRE_cache = {
    '%': '%',
    'A': '(?P<A>wednesday|thursday|saturday|tuesday|monday|friday|sunday)',
    'B': '(?P<B>september|february|november|december|january|october|august|march|april|june|july|may)',
    'H': '(?P<H>2[0-3]|[0-1]\\d|\\d)',
    'I': '(?P<I>1[0-2]|0[1-9]|[1-9])',
    'M': '(?P<M>[0-5]\\d|\\d)',
    'S': '(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'U': '(?P<U>5[0-3]|[0-4]\\d|\\d)',
    'W': '(?P<W>5[0-3]|[0-4]\\d|\\d)',
    'X': '(?P<H>2[0-3]|[0-1]\\d|\\d):(?P<M>[0-5]\\d|\\d):(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'Y': '(?P<Y>\\d\\d\\d\\d)',
    'Z': '(?P<Z>America\\/Argentina\\/ComodRivadavia|America\\/Argentina\\/Buenos\\_Aires|America\\/Argentina\\/Rio\\_Gallegos|America\\/North\\_Dakota\\/New\\_Salem|America\\/Indiana\\/Indianapolis|America\\/Argentina\\/Catamarca|America\\/Kentucky\\/Louisville|America\\/Kentucky\\/Monticello|America\\/North\\_Dakota\\/Beulah|America\\/North\\_Dakota\\/Center|America\\/Argentina\\/La\\_Rioja|America\\/Argentina\\/San\\_Juan|America\\/Argentina\\/San\\_Luis|America\\/Indiana\\/Petersburg|America\\/Argentina\\/Cordoba|America\\/Argentina\\/Mendoza|America\\/Argentina\\/Tucuman|America\\/Argentina\\/Ushuaia|America\\/Indiana\\/Tell\\_City|America\\/Indiana\\/Vincennes|Antarctica\\/DumontDUrville|America\\/Argentina\\/Jujuy|America\\/Argentina\\/Salta|America\\/Indiana\\/Marengo|America\\/Indiana\\/Winamac|America\\/Bahia\\_Banderas|America\\/Port\\-au\\-Prince|Atlantic\\/South\\_Georgia|America\\/Cambridge\\_Bay|America\\/Coral\\_Harbour|America\\/Indiana\\/Vevay|America\\/Lower\\_Princes|America\\/Port\\_of\\_Spain|America\\/Santo\\_Domingo|America\\/St\\_Barthelemy|America\\/Swift\\_Current|Antarctica\\/South\\_Pole|Australia\\/Broken\\_Hill|Africa\\/Dar\\_es\\_Salaam|America\\/Blanc\\-Sablon|America\\/Buenos\\_Aires|America\\/Campo\\_Grande|America\\/Danmarkshavn|America\\/Dawson\\_Creek|America\\/Indiana\\/Knox|America\\/Indianapolis|America\\/Punta\\_Arenas|America\\/Rankin\\_Inlet|America\\/Santa\\_Isabel|America\\/Scoresbysund|Antarctica\\/Macquarie|Australia\\/Queensland|Australia\\/Yancowinna|Pacific\\/Bougainville|Pacific\\/Port\\_Moresby|Africa\\/Johannesburg|America\\/El\\_Salvador|America\\/Fort\\_Nelson|America\\/Los\\_Angeles|America\\/Mexico\\_City|America\\/Pangnirtung|America\\/Porto\\_Velho|America\\/Puerto\\_Rico|America\\/Rainy\\_River|America\\/Tegucigalpa|America\\/Thunder\\_Bay|America\\/Yellowknife|Arctic\\/Longyearbyen|Atlantic\\/Cape\\_Verde|Australia\\/Lord\\_Howe|Australia\\/Melbourne|Canada\\/Newfoundland|Canada\\/Saskatchewan|Indian\\/Antananarivo|Pacific\\/Guadalcanal|Africa\\/Addis\\_Ababa|Africa\\/Brazzaville|Africa\\/Ouagadougou|America\\/Costa\\_Rica|America\\/Fort\\_Wayne|America\\/Grand\\_Turk|America\\/Guadeloupe|America\\/Hermosillo|America\\/Kralendijk|America\\/Louisville|America\\/Martinique|America\\/Metlakatla|America\\/Montevideo|America\\/Montserrat|America\\/Paramaribo|America\\/Porto\\_Acre|America\\/Rio\\_Branco|America\\/St\\_Vincent|America\\/Whitehorse|Antarctica\\/McMurdo|Antarctica\\/Rothera|Asia\\/Srednekolymsk|Asia\\/Ujung\\_Pandang|Asia\\/Yekaterinburg|Atlantic\\/Jan\\_Mayen|Atlantic\\/Reykjavik|Atlantic\\/St\\_Helena|Australia\\/Adelaide|Australia\\/Brisbane|Australia\\/Canberra|Australia\\/Lindeman|Australia\\/Tasmania|Australia\\/Victoria|Chile\\/EasterIsland|Europe\\/Isle\\_of\\_Man|Europe\\/Kaliningrad|Pacific\\/Kiritimati|Africa\\/Casablanca|Africa\\/Libreville|Africa\\/Lubumbashi|Africa\\/Nouakchott|Africa\\/Porto\\-Novo|America\\/Anchorage|America\\/Araguaina|America\\/Boa\\_Vista|America\\/Catamarca|America\\/Chihuahua|America\\/Fortaleza|America\\/Glace\\_Bay|America\\/Goose\\_Bay|America\\/Guatemala|America\\/Guayaquil|America\\/Matamoros|America\\/Menominee|America\\/Monterrey|America\\/Sao\\_Paulo|America\\/St\\_Thomas|America\\/Vancouver|Antarctica\\/Mawson|Antarctica\\/Palmer|Antarctica\\/Vostok|Asia\\/Kuala\\_Lumpur|Asia\\/Novokuznetsk|Chile\\/Continental|Europe\\/Bratislava|Europe\\/Copenhagen|Europe\\/Luxembourg|Europe\\/San\\_Marino|Europe\\/Simferopol|Europe\\/Zaporozhye|Pacific\\/Enderbury|Pacific\\/Galapagos|Pacific\\/Kwajalein|Pacific\\/Marquesas|Pacific\\/Pago\\_Pago|Pacific\\/Rarotonga|Pacific\\/Tongatapu|US\\/Indiana\\-Starke|Africa\\/Bujumbura|Africa\\/Mogadishu|America\\/Anguilla|America\\/Asuncion|America\\/Atikokan|America\\/Barbados|America\\/Dominica|America\\/Edmonton|America\\/Eirunepe|America\\/Ensenada|America\\/Mazatlan|America\\/Miquelon|America\\/Montreal|America\\/New\\_York|America\\/Resolute|America\\/Santarem|America\\/Santiago|America\\/Shiprock|America\\/St\\_Johns|America\\/St\\_Kitts|America\\/St\\_Lucia|America\\/Winnipeg|Antarctica\\/Casey|Antarctica\\/Davis|Antarctica\\/Syowa|Antarctica\\/Troll|Asia\\/Ho\\_Chi\\_Minh|Asia\\/Krasnoyarsk|Asia\\/Novosibirsk|Asia\\/Ulaanbaatar|Asia\\/Vladivostok|Atlantic\\/Bermuda|Atlantic\\/Madeira|Atlantic\\/Stanley|Australia\\/Currie|Australia\\/Darwin|Australia\\/Hobart|Australia\\/Sydney|Brazil\\/DeNoronha|Europe\\/Amsterdam|Europe\\/Astrakhan|Europe\\/Bucharest|Europe\\/Gibraltar|Europe\\/Ljubljana|Europe\\/Mariehamn|Europe\\/Podgorica|Europe\\/Stockholm|Europe\\/Ulyanovsk|Europe\\/Volgograd|Indian\\/Christmas|Indian\\/Kerguelen|Indian\\/Mauritius|Mexico\\/BajaNorte|Pacific\\/Auckland|Pacific\\/Funafuti|Pacific\\/Honolulu|Pacific\\/Johnston|Pacific\\/Pitcairn|Africa\\/Blantyre|Africa\\/Djibouti|Africa\\/El\\_Aaiun|Africa\\/Freetown|Africa\\/Gaborone|Africa\\/Khartoum|Africa\\/Kinshasa|Africa\\/Monrovia|Africa\\/Ndjamena|Africa\\/Sao\\_Tome|Africa\\/Timbuktu|Africa\\/Windhoek|America\\/Antigua|America\\/Caracas|America\\/Cayenne|America\\/Chicago|America\\/Cordoba|America\\/Creston|America\\/Curacao|America\\/Detroit|America\\/Godthab|America\\/Grenada|America\\/Halifax|America\\/Iqaluit|America\\/Jamaica|America\\/Knox\\_IN|America\\/Managua|America\\/Marigot|America\\/Mendoza|America\\/Moncton|America\\/Nipigon|America\\/Noronha|America\\/Ojinaga|America\\/Phoenix|America\\/Rosario|America\\/Tijuana|America\\/Toronto|America\\/Tortola|America\\/Yakutat|Asia\\/Choibalsan|Asia\\/Phnom\\_Penh|Asia\\/Ulan\\_Bator|Atlantic\\/Azores|Atlantic\\/Canary|Atlantic\\/Faeroe|Australia\\/Eucla|Australia\\/North|Australia\\/Perth|Australia\\/South|Canada\\/Atlantic|Canada\\/Mountain|Europe\\/Belgrade|Europe\\/Brussels|Europe\\/Budapest|Europe\\/Busingen|Europe\\/Chisinau|Europe\\/Guernsey|Europe\\/Helsinki|Europe\\/Istanbul|Europe\\/Sarajevo|Europe\\/Tiraspol|Europe\\/Uzhgorod|Indian\\/Maldives|Pacific\\/Chatham|Pacific\\/Fakaofo|Pacific\\/Gambier|Pacific\\/Norfolk|Pacific\\/Pohnpei|US\\/East\\-Indiana|Africa\\/Abidjan|Africa\\/Algiers|Africa\\/Conakry|Africa\\/Kampala|Africa\\/Mbabane|Africa\\/Nairobi|Africa\\/Tripoli|America\\/Belize|America\\/Bogota|America\\/Cancun|America\\/Cayman|America\\/Cuiaba|America\\/Dawson|America\\/Denver|America\\/Guyana|America\\/Havana|America\\/Inuvik|America\\/Juneau|America\\/La\\_Paz|America\\/Maceio|America\\/Manaus|America\\/Merida|America\\/Nassau|America\\/Panama|America\\/Recife|America\\/Regina|America\\/Virgin|Asia\\/Ashkhabad|Asia\\/Chongqing|Asia\\/Chungking|Asia\\/Famagusta|Asia\\/Hong\\_Kong|Asia\\/Jerusalem|Asia\\/Kamchatka|Asia\\/Kathmandu|Asia\\/Pontianak|Asia\\/Pyongyang|Asia\\/Qyzylorda|Asia\\/Samarkand|Asia\\/Singapore|Asia\\/Vientiane|Atlantic\\/Faroe|Australia\\/West|Canada\\/Central|Canada\\/Eastern|Canada\\/Pacific|Europe\\/Andorra|Europe\\/Belfast|Europe\\/Nicosia|Europe\\/Saratov|Europe\\/Tallinn|Europe\\/Vatican|Europe\\/Vilnius|Indian\\/Mayotte|Indian\\/Reunion|Mexico\\/BajaSur|Mexico\\/General|Pacific\\/Easter|Pacific\\/Kosrae|Pacific\\/Majuro|Pacific\\/Midway|Pacific\\/Noumea|Pacific\\/Ponape|Pacific\\/Saipan|Pacific\\/Tahiti|Pacific\\/Tarawa|Pacific\\/Wallis|Africa\\/Asmara|Africa\\/Asmera|Africa\\/Bamako|Africa\\/Bangui|Africa\\/Banjul|Africa\\/Bissau|Africa\\/Douala|Africa\\/Harare|Africa\\/Kigali|Africa\\/Luanda|Africa\\/Lusaka|Africa\\/Malabo|Africa\\/Maputo|Africa\\/Maseru|Africa\\/Niamey|America\\/Aruba|America\\/Bahia|America\\/Belem|America\\/Boise|America\\/Jujuy|America\\/Sitka|America\\/Thule|Asia\\/Ashgabat|Asia\\/Calcutta|Asia\\/Damascus|Asia\\/Dushanbe|Asia\\/Istanbul|Asia\\/Jayapura|Asia\\/Katmandu|Asia\\/Khandyga|Asia\\/Makassar|Asia\\/Qostanay|Asia\\/Sakhalin|Asia\\/Shanghai|Asia\\/Tashkent|Asia\\/Tel\\_Aviv|Asia\\/Ust\\-Nera|Australia\\/ACT|Australia\\/LHI|Australia\\/NSW|Etc\\/Greenwich|Etc\\/Universal|Europe\\/Athens|Europe\\/Berlin|Europe\\/Dublin|Europe\\/Jersey|Europe\\/Lisbon|Europe\\/London|Europe\\/Madrid|Europe\\/Monaco|Europe\\/Moscow|Europe\\/Prague|Europe\\/Samara|Europe\\/Skopje|Europe\\/Tirane|Europe\\/Vienna|Europe\\/Warsaw|Europe\\/Zagreb|Europe\\/Zurich|Indian\\/Chagos|Indian\\/Comoro|Pacific\\/Chuuk|Pacific\\/Efate|Pacific\\/Nauru|Pacific\\/Palau|Pacific\\/Samoa|Africa\\/Accra|Africa\\/Cairo|Africa\\/Ceuta|Africa\\/Dakar|Africa\\/Lagos|Africa\\/Tunis|America\\/Adak|America\\/Atka|America\\/Lima|America\\/Nome|Asia\\/Baghdad|Asia\\/Bahrain|Asia\\/Bangkok|Asia\\/Barnaul|Asia\\/Bishkek|Asia\\/Colombo|Asia\\/Irkutsk|Asia\\/Jakarta|Asia\\/Karachi|Asia\\/Kashgar|Asia\\/Kolkata|Asia\\/Kuching|Asia\\/Magadan|Asia\\/Nicosia|Asia\\/Rangoon|Asia\\/Tbilisi|Asia\\/Thimphu|Asia\\/Yakutsk|Asia\\/Yerevan|Canada\\/Yukon|Europe\\/Kirov|Europe\\/Malta|Europe\\/Minsk|Europe\\/Paris|Europe\\/Sofia|Europe\\/Vaduz|Indian\\/Cocos|Pacific\\/Apia|Pacific\\/Fiji|Pacific\\/Guam|Pacific\\/Niue|Pacific\\/Truk|Pacific\\/Wake|Africa\\/Juba|Africa\\/Lome|Asia\\/Almaty|Asia\\/Anadyr|Asia\\/Aqtobe|Asia\\/Atyrau|Asia\\/Beirut|Asia\\/Brunei|Asia\\/Harbin|Asia\\/Hebron|Asia\\/Kuwait|Asia\\/Manila|Asia\\/Muscat|Asia\\/Riyadh|Asia\\/Saigon|Asia\\/Taipei|Asia\\/Tehran|Asia\\/Thimbu|Asia\\/Urumqi|Asia\\/Yangon|Brazil\\/Acre|Brazil\\/East|Brazil\\/West|Europe\\/Kiev|Europe\\/Oslo|Europe\\/Riga|Europe\\/Rome|Indian\\/Mahe|Pacific\\/Yap|US\\/Aleutian|US\\/Michigan|US\\/Mountain|Asia\\/Amman|Asia\\/Aqtau|Asia\\/Chita|Asia\\/Dacca|Asia\\/Dhaka|Asia\\/Dubai|Asia\\/Kabul|Asia\\/Macao|Asia\\/Macau|Asia\\/Qatar|Asia\\/Seoul|Asia\\/Tokyo|Asia\\/Tomsk|Etc\\/GMT\\+10|Etc\\/GMT\\+11|Etc\\/GMT\\+12|Etc\\/GMT\\-10|Etc\\/GMT\\-11|Etc\\/GMT\\-12|Etc\\/GMT\\-13|Etc\\/GMT\\-14|US\\/Arizona|US\\/Central|US\\/Eastern|US\\/Pacific|Asia\\/Aden|Asia\\/Baku|Asia\\/Dili|Asia\\/Gaza|Asia\\/Hovd|Asia\\/Omsk|Asia\\/Oral|Etc\\/GMT\\+0|Etc\\/GMT\\+1|Etc\\/GMT\\+2|Etc\\/GMT\\+3|Etc\\/GMT\\+4|Etc\\/GMT\\+5|Etc\\/GMT\\+6|Etc\\/GMT\\+7|Etc\\/GMT\\+8|Etc\\/GMT\\+9|Etc\\/GMT\\-0|Etc\\/GMT\\-1|Etc\\/GMT\\-2|Etc\\/GMT\\-3|Etc\\/GMT\\-4|Etc\\/GMT\\-5|Etc\\/GMT\\-6|Etc\\/GMT\\-7|Etc\\/GMT\\-8|Etc\\/GMT\\-9|Greenwich|Kwajalein|Singapore|US\\/Alaska|US\\/Hawaii|Universal|Etc\\/GMT0|Etc\\/Zulu|Hongkong|Portugal|US\\/Samoa|CST6CDT|EST5EDT|Etc\\/GMT|Etc\\/UCT|Etc\\/UTC|GB\\-Eire|Iceland|Jamaica|MST7MDT|NZ\\-CHAT|PST8PDT|Israel|Navajo|Poland|Turkey|Egypt|GMT\\+0|GMT\\-0|Japan|Libya|Cuba|Eire|GMT0|Iran|W\\-SU|Zulu|CET|EET|EST|GMT|HST|MET|MST|PRC|ROC|ROK|UCT|UTC|WET|GB|NZ)',
    'a': '(?P<a>mon|tue|wed|thu|fri|sat|sun)',
    'b': '(?P<b>jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)',
    'c': '(?P<m>1[0-2]|0[1-9]|[1-9])/(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])/(?P<y>\\d\\d)\\s+(?P<H>2[0-3]|[0-1]\\d|\\d):(?P<M>[0-5]\\d|\\d):(?P<S>6[0-1]|[0-5]\\d|\\d)',
    'd': '(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])',
    'f': '(?P<f>[0-9]{1,9})',
    'j': '(?P<j>36[0-6]|3[0-5]\\d|[1-2]\\d\\d|0[1-9]\\d|00[1-9]|[1-9]\\d|0[1-9]|[1-9])',
    'm': '(?P<m>1[0-2]|0[1-9]|[1-9])',
    'p': '(?P<p>am|pm)',
    'w': '(?P<w>[0-6])',
    'x': '(?P<m>1[0-2]|0[1-9]|[1-9])/(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])/(?P<y>\\d\\d)',
    'y': '(?P<y>\\d\\d)',
    'z': '(?P<z>[+-]\\d\\d:?[0-5]\\d(:?[0-5]\\d(\\.\\d{1,6})?)?|Z)',
}

__test__ = {}

