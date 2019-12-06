# encoding: utf-8
# module win32cred
# from C:\Python27\lib\site-packages\win32\win32cred.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

CertCredential = 1

CREDUI_FLAGS_ALWAYS_SHOW_UI = 128

CREDUI_FLAGS_COMPLETE_USERNAME = 2048

CREDUI_FLAGS_DO_NOT_PERSIST = 2

CREDUI_FLAGS_EXCLUDE_CERTIFICATES = 8

CREDUI_FLAGS_EXPECT_CONFIRMATION = 131072

CREDUI_FLAGS_GENERIC_CREDENTIALS = 262144

CREDUI_FLAGS_INCORRECT_PASSWORD = 1

CREDUI_FLAGS_KEEP_USERNAME = 1048576

CREDUI_FLAGS_PASSWORD_ONLY_OK = 512

CREDUI_FLAGS_PERSIST = 4096

CREDUI_FLAGS_PROMPT_VALID = 1990623

CREDUI_FLAGS_REQUEST_ADMINISTRATOR = 4

CREDUI_FLAGS_REQUIRE_CERTIFICATE = 16
CREDUI_FLAGS_REQUIRE_SMARTCARD = 256

CREDUI_FLAGS_SERVER_CREDENTIAL = 16384

CREDUI_FLAGS_SHOW_SAVE_CHECK_BOX = 64

CREDUI_FLAGS_USERNAME_TARGET_CREDENTIALS = 524288

CREDUI_FLAGS_VALIDATE_USERNAME = 1024

CREDUI_MAX_CAPTION_LENGTH = 128

CREDUI_MAX_DOMAIN_TARGET_LENGTH = 337

CREDUI_MAX_GENERIC_TARGET_LENGTH = 32767

CREDUI_MAX_MESSAGE_LENGTH = 1024

CREDUI_MAX_PASSWORD_LENGTH = 256

CREDUI_MAX_USERNAME_LENGTH = 513

CRED_ALLOW_NAME_RESOLUTION = 1

CRED_CACHE_TARGET_INFORMATION = 1

CRED_FLAGS_OWF_CRED_BLOB = 8

CRED_FLAGS_PASSWORD_FOR_CERT = 1

CRED_FLAGS_PROMPT_NOW = 2

CRED_FLAGS_USERNAME_TARGET = 4

CRED_FLAGS_VALID_FLAGS = 61503

CRED_MAX_ATTRIBUTES = 64

CRED_MAX_DOMAIN_TARGET_NAME_LENGTH = 337

CRED_MAX_GENERIC_TARGET_NAME_LENGTH = 32767

CRED_MAX_STRING_LENGTH = 256

CRED_MAX_USERNAME_LENGTH = 513

CRED_MAX_VALUE_SIZE = 256

CRED_PERSIST_ENTERPRISE = 3

CRED_PERSIST_LOCAL_MACHINE = 2

CRED_PERSIST_NONE = 0
CRED_PERSIST_SESSION = 1

CRED_PRESERVE_CREDENTIAL_BLOB = 1

CRED_TI_CREATE_EXPLICIT_CRED = 16

CRED_TI_DOMAIN_FORMAT_UNKNOWN = 2

CRED_TI_ONLY_PASSWORD_REQUIRED = 4

CRED_TI_SERVER_FORMAT_UNKNOWN = 1

CRED_TI_USERNAME_TARGET = 8

CRED_TI_VALID_FLAGS = 61567

CRED_TI_WORKGROUP_MEMBER = 32

CRED_TYPE_DOMAIN_CERTIFICATE = 3
CRED_TYPE_DOMAIN_PASSWORD = 2

CRED_TYPE_DOMAIN_VISIBLE_PASSWORD = 4

CRED_TYPE_GENERIC = 1

UsernameTargetCredential = 2

# functions

def CredDelete(*args, **kwargs): # real signature unknown
    """ Deletes a stored credential """
    pass

def CredEnumerate(*args, **kwargs): # real signature unknown
    """ Lists stored credentials for current logon session """
    pass

def CredGetTargetInfo(*args, **kwargs): # real signature unknown
    """ Determines type and location of credential target """
    pass

def CredIsMarshaledCredential(*args, **kwargs): # real signature unknown
    """ Checks if a string matches the form of a marshaled credential """
    pass

def CredMarshalCredential(*args, **kwargs): # real signature unknown
    """ Marshals a credential into a unicode string """
    pass

def CredRead(*args, **kwargs): # real signature unknown
    """ Retrieves a stored credential """
    pass

def CredReadDomainCredentials(*args, **kwargs): # real signature unknown
    """ Retrieves a user's credentials for a domain or server """
    pass

def CredRename(*args, **kwargs): # real signature unknown
    """ Changes the target name of stored credentials """
    pass

def CredUICmdLinePromptForCredentials(*args, **kwargs): # real signature unknown
    """ Prompt for username/passwd from a console app """
    pass

def CredUIConfirmCredentials(*args, **kwargs): # real signature unknown
    """ Confirms whether credentials entered by user are valid or not """
    pass

def CredUIParseUserName(*args, **kwargs): # real signature unknown
    """ Parses a full username into domain and username """
    pass

def CredUIPromptForCredentials(*args, **kwargs): # real signature unknown
    """ Initiates dialog to request user credentials """
    pass

def CredUIReadSSOCredW(*args, **kwargs): # real signature unknown
    """ Retrieves single sign on username """
    pass

def CredUIStoreSSOCredW(*args, **kwargs): # real signature unknown
    """ Creates a single sign on credential """
    pass

def CredUnmarshalCredential(*args, **kwargs): # real signature unknown
    """ Unmarshals credentials formatted using <om win32cred.CredMarshalCredential> """
    pass

def CredWrite(*args, **kwargs): # real signature unknown
    """ Creates or updates a stored credential """
    pass

def CredWriteDomainCredentials(*args, **kwargs): # real signature unknown
    """ Creates or updates credential for a domain or server """
    pass

# no classes
