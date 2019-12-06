# encoding: utf-8
# module win32security
# from C:\Python27\lib\site-packages\win32\win32security.pyd
# by generator 1.147
# no doc

# imports
from pywintypes import error


# Variables with simple values

ACCESS_ALLOWED_ACE_TYPE = 0

ACCESS_ALLOWED_OBJECT_ACE_TYPE = 5

ACCESS_DENIED_ACE_TYPE = 1

ACCESS_DENIED_OBJECT_ACE_TYPE = 6

ACL_REVISION = 2

ACL_REVISION_DS = 4

AuditCategoryAccountLogon = 8
AuditCategoryAccountManagement = 6
AuditCategoryDetailedTracking = 4
AuditCategoryDirectoryServiceAccess = 7
AuditCategoryLogon = 1
AuditCategoryObjectAccess = 2
AuditCategoryPolicyChange = 5
AuditCategoryPrivilegeUse = 3
AuditCategorySystem = 0

CONTAINER_INHERIT_ACE = 2

DACL_SECURITY_INFORMATION = 4

DENY_ACCESS = 3

DISABLE_MAX_PRIVILEGE = 1

DS_SPN_ADD_SPN_OP = 0

DS_SPN_DELETE_SPN_OP = 2

DS_SPN_DNS_HOST = 0

DS_SPN_DN_HOST = 1

DS_SPN_DOMAIN = 3

DS_SPN_NB_DOMAIN = 4
DS_SPN_NB_HOST = 2

DS_SPN_REPLACE_SPN_OP = 1

DS_SPN_SERVICE = 5

FAILED_ACCESS_ACE_FLAG = 128

GRANT_ACCESS = 1

GROUP_SECURITY_INFORMATION = 2

INHERITED_ACE = 16

INHERIT_ONLY_ACE = 8

LABEL_SECURITY_INFORMATION = 16

LOGON32_LOGON_BATCH = 4
LOGON32_LOGON_INTERACTIVE = 2
LOGON32_LOGON_NETWORK = 3

LOGON32_LOGON_NETWORK_CLEARTEXT = 8

LOGON32_LOGON_NEW_CREDENTIALS = 9

LOGON32_LOGON_SERVICE = 5
LOGON32_LOGON_UNLOCK = 7

LOGON32_PROVIDER_DEFAULT = 0
LOGON32_PROVIDER_WINNT35 = 1
LOGON32_PROVIDER_WINNT40 = 2
LOGON32_PROVIDER_WINNT50 = 3

MICROSOFT_KERBEROS_NAME_A = 'Kerberos'

MSV1_0_PACKAGE_NAME = 'MICROSOFT_AUTHENTICATION_PACKAGE_V1_0'

NOT_USED_ACCESS = 0

NO_INHERITANCE = 0

NO_PROPAGATE_INHERIT_ACE = 4

OBJECT_INHERIT_ACE = 1

OWNER_SECURITY_INFORMATION = 1

PolicyAccountDomainInformation = 5
PolicyAuditEventsInformation = 2
PolicyAuditFullQueryInformation = 11
PolicyAuditFullSetInformation = 10
PolicyAuditLogInformation = 1
PolicyDefaultQuotaInformation = 8
PolicyDnsDomainInformation = 12
PolicyLsaServerRoleInformation = 6
PolicyModificationInformation = 9
PolicyNotifyAccountDomainInformation = 2
PolicyNotifyAuditEventsInformation = 1
PolicyNotifyDnsDomainInformation = 4
PolicyNotifyDomainEfsInformation = 5
PolicyNotifyDomainKerberosTicketInformation = 6
PolicyNotifyMachineAccountPasswordInformation = 7
PolicyNotifyServerRoleInformation = 3
PolicyPdAccountInformation = 4
PolicyPrimaryDomainInformation = 3
PolicyReplicaSourceInformation = 7
PolicyServerDisabled = 3
PolicyServerEnabled = 2
PolicyServerRoleBackup = 2
PolicyServerRolePrimary = 3

POLICY_ALL_ACCESS = 987135

POLICY_AUDIT_EVENT_FAILURE = 2
POLICY_AUDIT_EVENT_NONE = 4
POLICY_AUDIT_EVENT_SUCCESS = 1
POLICY_AUDIT_EVENT_UNCHANGED = 0

POLICY_AUDIT_LOG_ADMIN = 512

POLICY_CREATE_ACCOUNT = 16
POLICY_CREATE_PRIVILEGE = 64
POLICY_CREATE_SECRET = 32

POLICY_EXECUTE = 133121

POLICY_GET_PRIVATE_INFORMATION = 4

POLICY_LOOKUP_NAMES = 2048

POLICY_NOTIFICATION = 4096
POLICY_READ = 131078

POLICY_SERVER_ADMIN = 1024

POLICY_SET_AUDIT_REQUIREMENTS = 256

POLICY_SET_DEFAULT_QUOTA_LIMITS = 128

POLICY_TRUST_ADMIN = 8

POLICY_VIEW_AUDIT_INFORMATION = 2

POLICY_VIEW_LOCAL_INFORMATION = 1

POLICY_WRITE = 133112

PROTECTED_DACL_SECURITY_INFORMATION = -2147483648

PROTECTED_SACL_SECURITY_INFORMATION = 1073741824

REVOKE_ACCESS = 4

SACL_SECURITY_INFORMATION = 8

SANDBOX_INERT = 2

SDDL_REVISION_1 = 1

SECPKG_CRED_BOTH = 3
SECPKG_CRED_INBOUND = 1
SECPKG_CRED_OUTBOUND = 2

SECPKG_FLAG_ACCEPT_WIN32_NAME = 512

SECPKG_FLAG_CLIENT_ONLY = 64

SECPKG_FLAG_CONNECTION = 16
SECPKG_FLAG_DATAGRAM = 8

SECPKG_FLAG_EXTENDED_ERROR = 128

SECPKG_FLAG_IMPERSONATION = 256
SECPKG_FLAG_INTEGRITY = 1

SECPKG_FLAG_MULTI_REQUIRED = 32

SECPKG_FLAG_PRIVACY = 2
SECPKG_FLAG_STREAM = 1024

SECPKG_FLAG_TOKEN_ONLY = 4

SecurityAnonymous = 0
SecurityDelegation = 3
SecurityIdentification = 1
SecurityImpersonation = 2

SECURITY_CREATOR_SID_AUTHORITY = 3

SECURITY_LOCAL_SID_AUTHORITY = 2

SECURITY_NON_UNIQUE_AUTHORITY = 4

SECURITY_NT_AUTHORITY = 5

SECURITY_NULL_SID_AUTHORITY = 0

SECURITY_RESOURCE_MANAGER_AUTHORITY = 9

SECURITY_WORLD_SID_AUTHORITY = 1

SET_ACCESS = 2

SET_AUDIT_FAILURE = 6
SET_AUDIT_SUCCESS = 5

SE_ASSIGNPRIMARYTOKEN_NAME = u'SeAssignPrimaryTokenPrivilege'

SE_AUDIT_NAME = u'SeAuditPrivilege'

SE_BACKUP_NAME = u'SeBackupPrivilege'

SE_BATCH_LOGON_NAME = u'SeBatchLogonRight'

SE_CHANGE_NOTIFY_NAME = u'SeChangeNotifyPrivilege'

SE_CREATE_GLOBAL_NAME = u'SeCreateGlobalPrivilege'

SE_CREATE_PAGEFILE_NAME = u'SeCreatePagefilePrivilege'

SE_CREATE_PERMANENT_NAME = u'SeCreatePermanentPrivilege'

SE_CREATE_SYMBOLIC_LINK_NAME = u'SeCreateSymbolicLinkPrivilege'

SE_CREATE_TOKEN_NAME = u'SeCreateTokenPrivilege'

SE_DACL_AUTO_INHERITED = 1024

SE_DACL_DEFAULTED = 8
SE_DACL_PRESENT = 4
SE_DACL_PROTECTED = 4096

SE_DEBUG_NAME = u'SeDebugPrivilege'

SE_DENY_BATCH_LOGON_NAME = u'SeDenyBatchLogonRight'

SE_DENY_INTERACTIVE_LOGON_NAME = u'SeDenyInteractiveLogonRight'

SE_DENY_NETWORK_LOGON_NAME = u'SeDenyNetworkLogonRight'

SE_DENY_REMOTE_INTERACTIVE_LOGON_NAME = u'SeDenyRemoteInteractiveLogonRight'

SE_DENY_SERVICE_LOGON_NAME = u'SeDenyServiceLogonRight'

SE_DS_OBJECT = 8

SE_DS_OBJECT_ALL = 9

SE_ENABLE_DELEGATION_NAME = u'SeEnableDelegationPrivilege'

SE_FILE_OBJECT = 1

SE_GROUP_DEFAULTED = 2
SE_GROUP_ENABLED = 4

SE_GROUP_ENABLED_BY_DEFAULT = 2

SE_GROUP_INTEGRITY = 32

SE_GROUP_INTEGRITY_ENABLED = 64

SE_GROUP_LOGON_ID = -1073741824

SE_GROUP_MANDATORY = 1
SE_GROUP_OWNER = 8
SE_GROUP_RESOURCE = 536870912

SE_GROUP_USE_FOR_DENY_ONLY = 16

SE_IMPERSONATE_NAME = u'SeImpersonatePrivilege'

SE_INCREASE_QUOTA_NAME = u'SeIncreaseQuotaPrivilege'

SE_INC_BASE_PRIORITY_NAME = u'SeIncreaseBasePriorityPrivilege'

SE_INC_WORKING_SET_NAME = u'SeIncreaseWorkingSetPrivilege'

SE_INTERACTIVE_LOGON_NAME = u'SeInteractiveLogonRight'

SE_KERNEL_OBJECT = 6

SE_LMSHARE = 5

SE_LOAD_DRIVER_NAME = u'SeLoadDriverPrivilege'

SE_LOCK_MEMORY_NAME = u'SeLockMemoryPrivilege'

SE_MACHINE_ACCOUNT_NAME = u'SeMachineAccountPrivilege'

SE_MANAGE_VOLUME_NAME = u'SeManageVolumePrivilege'

SE_NETWORK_LOGON_NAME = u'SeNetworkLogonRight'

SE_OWNER_DEFAULTED = 1

SE_PRINTER = 3

SE_PRIVILEGE_ENABLED = 2

SE_PRIVILEGE_ENABLED_BY_DEFAULT = 1

SE_PRIVILEGE_REMOVED = 4

SE_PRIVILEGE_USED_FOR_ACCESS = -2147483648

SE_PROF_SINGLE_PROCESS_NAME = u'SeProfileSingleProcessPrivilege'

SE_PROVIDER_DEFINED_OBJECT = 10

SE_REGISTRY_KEY = 4

SE_REGISTRY_WOW64_32KEY = 12

SE_RELABEL_NAME = u'SeRelabelPrivilege'

SE_REMOTE_INTERACTIVE_LOGON_NAME = u'SeRemoteInteractiveLogonRight'

SE_REMOTE_SHUTDOWN_NAME = u'SeRemoteShutdownPrivilege'

SE_RESTORE_NAME = u'SeRestorePrivilege'

SE_SACL_AUTO_INHERITED = 2048

SE_SACL_DEFAULTED = 32
SE_SACL_PRESENT = 16
SE_SACL_PROTECTED = 8192

SE_SECURITY_NAME = u'SeSecurityPrivilege'

SE_SELF_RELATIVE = 32768

SE_SERVICE = 2

SE_SERVICE_LOGON_NAME = u'SeServiceLogonRight'

SE_SHUTDOWN_NAME = u'SeShutdownPrivilege'

SE_SYNC_AGENT_NAME = u'SeSyncAgentPrivilege'

SE_SYSTEMTIME_NAME = u'SeSystemtimePrivilege'

SE_SYSTEM_ENVIRONMENT_NAME = u'SeSystemEnvironmentPrivilege'

SE_SYSTEM_PROFILE_NAME = u'SeSystemProfilePrivilege'

SE_TAKE_OWNERSHIP_NAME = u'SeTakeOwnershipPrivilege'

SE_TCB_NAME = u'SeTcbPrivilege'

SE_TIME_ZONE_NAME = u'SeTimeZonePrivilege'

SE_TRUSTED_CREDMAN_ACCESS_NAME = u'SeTrustedCredManAccessPrivilege'

SE_UNDOCK_NAME = u'SeUndockPrivilege'

SE_UNKNOWN_OBJECT_TYPE = 0

SE_UNSOLICITED_INPUT_NAME = u'SeUnsolicitedInputPrivilege'

SE_WINDOW_OBJECT = 7

SE_WMIGUID_OBJECT = 11

SidTypeAlias = 4
SidTypeComputer = 9
SidTypeDeletedAccount = 6
SidTypeDomain = 3
SidTypeGroup = 2
SidTypeInvalid = 7
SidTypeUnknown = 8
SidTypeUser = 1
SidTypeWellKnownGroup = 5

STYPE_DEVICE = 2
STYPE_DISKTREE = 0
STYPE_IPC = 3
STYPE_PRINTQ = 1
STYPE_SPECIAL = -2147483648
STYPE_TEMPORARY = 1073741824

SUB_CONTAINERS_AND_OBJECTS_INHERIT = 3

SUB_CONTAINERS_ONLY_INHERIT = 2

SUB_OBJECTS_ONLY_INHERIT = 1

SUCCESSFUL_ACCESS_ACE_FLAG = 64

SYSTEM_AUDIT_ACE_TYPE = 2

SYSTEM_AUDIT_OBJECT_ACE_TYPE = 7

SYSTEM_MANDATORY_LABEL_NO_EXECUTE_UP = 4

SYSTEM_MANDATORY_LABEL_NO_READ_UP = 2

SYSTEM_MANDATORY_LABEL_NO_WRITE_UP = 1

SYSTEM_MANDATORY_LABEL_VALID_MASK = 7

TokenAccessInformation = 22
TokenAuditPolicy = 16
TokenDefaultDacl = 6
TokenElevation = 20
TokenElevationType = 18
TokenElevationTypeDefault = 1
TokenElevationTypeFull = 2
TokenElevationTypeLimited = 3
TokenGroups = 2
TokenGroupsAndPrivileges = 13
TokenHasRestrictions = 21
TokenImpersonation = 2
TokenImpersonationLevel = 9
TokenIntegrityLevel = 25
TokenLinkedToken = 19
TokenLogonSid = 28
TokenMandatoryPolicy = 27
TokenOrigin = 17
TokenOwner = 4
TokenPrimary = 1
TokenPrimaryGroup = 5
TokenPrivileges = 3
TokenRestrictedSids = 11
TokenSandBoxInert = 15
TokenSessionId = 12
TokenSessionReference = 14
TokenSource = 7
TokenStatistics = 10
TokenType = 8
TokenUIAccess = 26
TokenUser = 1
TokenVirtualizationAllowed = 23
TokenVirtualizationEnabled = 24

TOKEN_ADJUST_DEFAULT = 128
TOKEN_ADJUST_GROUPS = 64
TOKEN_ADJUST_PRIVILEGES = 32

TOKEN_ALL_ACCESS = 983551

TOKEN_ASSIGN_PRIMARY = 1

TOKEN_DUPLICATE = 2
TOKEN_EXECUTE = 131072
TOKEN_IMPERSONATE = 4

TOKEN_MANDATORY_POLICY_NEW_PROCESS_MIN = 2

TOKEN_MANDATORY_POLICY_NO_WRITE_UP = 1

TOKEN_MANDATORY_POLICY_OFF = 0

TOKEN_MANDATORY_POLICY_VALID_MASK = 3

TOKEN_QUERY = 8

TOKEN_QUERY_SOURCE = 16

TOKEN_READ = 131080
TOKEN_WRITE = 131296

TrustedControllersInformation = 2
TrustedDomainAuthInformation = 7
TrustedDomainAuthInformationInternal = 9
TrustedDomainFullInformation = 8
TrustedDomainFullInformation2Internal = 12
TrustedDomainFullInformationInternal = 10
TrustedDomainInformationBasic = 5
TrustedDomainInformationEx = 6
TrustedDomainInformationEx2Internal = 11
TrustedDomainNameInformation = 1
TrustedPasswordInformation = 4
TrustedPosixOffsetInformation = 3

TRUSTEE_BAD_FORM = 2

TRUSTEE_IS_ALIAS = 4
TRUSTEE_IS_COMPUTER = 8
TRUSTEE_IS_DELETED = 6
TRUSTEE_IS_DOMAIN = 3
TRUSTEE_IS_GROUP = 2
TRUSTEE_IS_INVALID = 7
TRUSTEE_IS_NAME = 1

TRUSTEE_IS_OBJECTS_AND_NAME = 4
TRUSTEE_IS_OBJECTS_AND_SID = 3

TRUSTEE_IS_SID = 0
TRUSTEE_IS_UNKNOWN = 0
TRUSTEE_IS_USER = 1

TRUSTEE_IS_WELL_KNOWN_GROUP = 5

UNICODE = 1

UNPROTECTED_DACL_SECURITY_INFORMATION = 536870912

UNPROTECTED_SACL_SECURITY_INFORMATION = 268435456

WinAccountAdministratorSid = 38
WinAccountCertAdminsSid = 46
WinAccountComputersSid = 44
WinAccountControllersSid = 45
WinAccountDomainAdminsSid = 41
WinAccountDomainGuestsSid = 43
WinAccountDomainUsersSid = 42
WinAccountEnterpriseAdminsSid = 48
WinAccountGuestSid = 39
WinAccountKrbtgtSid = 40
WinAccountPolicyAdminsSid = 49
WinAccountRasAndIasServersSid = 50
WinAccountReadonlyControllersSid = 75
WinAccountSchemaAdminsSid = 47
WinAnonymousSid = 13
WinAuthenticatedUserSid = 17
WinBatchSid = 10
WinBuiltinAccountOperatorsSid = 30
WinBuiltinAdministratorsSid = 26
WinBuiltinAuthorizationAccessSid = 59
WinBuiltinBackupOperatorsSid = 33
WinBuiltinCryptoOperatorsSid = 64
WinBuiltinDCOMUsersSid = 61
WinBuiltinDomainSid = 25
WinBuiltinEventLogReadersGroup = 76
WinBuiltinGuestsSid = 28
WinBuiltinIncomingForestTrustBuildersSid = 56
WinBuiltinIUsersSid = 62
WinBuiltinNetworkConfigurationOperatorsSid = 37
WinBuiltinPerfLoggingUsersSid = 58
WinBuiltinPerfMonitoringUsersSid = 57
WinBuiltinPowerUsersSid = 29
WinBuiltinPreWindows2000CompatibleAccessSid = 35
WinBuiltinPrintOperatorsSid = 32
WinBuiltinRemoteDesktopUsersSid = 36
WinBuiltinReplicatorSid = 34
WinBuiltinSystemOperatorsSid = 31
WinBuiltinTerminalServerLicenseServersSid = 60
WinBuiltinUsersSid = 27
WinCacheablePrincipalsGroupSid = 72
WinCreatorGroupServerSid = 6
WinCreatorGroupSid = 4
WinCreatorOwnerRightsSid = 71
WinCreatorOwnerServerSid = 5
WinCreatorOwnerSid = 3
WinDialupSid = 8
WinDigestAuthenticationSid = 52
WinEnterpriseControllersSid = 15
WinEnterpriseReadonlyControllersSid = 74
WinHighLabelSid = 68
WinInteractiveSid = 11
WinIUserSid = 63
WinLocalServiceSid = 23
WinLocalSid = 2
WinLocalSystemSid = 22
WinLogonIdsSid = 21
WinLowLabelSid = 66
WinMediumLabelSid = 67
WinNetworkServiceSid = 24
WinNetworkSid = 9
WinNonCacheablePrincipalsGroupSid = 73
WinNtAuthoritySid = 7
WinNTLMAuthenticationSid = 51
WinNullSid = 0
WinOtherOrganizationSid = 55
WinProxySid = 14
WinRemoteLogonIdSid = 20
WinRestrictedCodeSid = 18
WinSChannelAuthenticationSid = 53
WinSelfSid = 16
WinServiceSid = 12
WinSystemLabelSid = 69
WinTerminalServerSid = 19
WinThisOrganizationSid = 54
WinUntrustedLabelSid = 65
WinWorldSid = 1
WinWriteRestrictedCodeSid = 70

# functions

def AcceptSecurityContext(*args, **kwargs): # real signature unknown
    pass

def ACL(*args, **kwargs): # real signature unknown
    pass

def AcquireCredentialsHandle(*args, **kwargs): # real signature unknown
    pass

def AdjustTokenGroups(*args, **kwargs): # real signature unknown
    pass

def AdjustTokenPrivileges(*args, **kwargs): # real signature unknown
    pass

def AllocateLocallyUniqueId(*args, **kwargs): # real signature unknown
    pass

def CheckTokenMembership(*args, **kwargs): # real signature unknown
    pass

def ConvertSecurityDescriptorToStringSecurityDescriptor(*args, **kwargs): # real signature unknown
    pass

def ConvertSidToStringSid(*args, **kwargs): # real signature unknown
    pass

def ConvertStringSecurityDescriptorToSecurityDescriptor(*args, **kwargs): # real signature unknown
    pass

def ConvertStringSidToSid(*args, **kwargs): # real signature unknown
    pass

def CreateRestrictedToken(*args, **kwargs): # real signature unknown
    pass

def CreateWellKnownSid(*args, **kwargs): # real signature unknown
    pass

def CryptEnumProviders(*args, **kwargs): # real signature unknown
    pass

def DsBind(*args, **kwargs): # real signature unknown
    pass

def DsCrackNames(*args, **kwargs): # real signature unknown
    pass

def DsGetDcName(*args, **kwargs): # real signature unknown
    pass

def DsGetSpn(*args, **kwargs): # real signature unknown
    pass

def DsListDomainsInSite(*args, **kwargs): # real signature unknown
    pass

def DsListInfoForServer(*args, **kwargs): # real signature unknown
    pass

def DsListRoles(*args, **kwargs): # real signature unknown
    pass

def DsListServersForDomainInSite(*args, **kwargs): # real signature unknown
    pass

def DsListServersInSite(*args, **kwargs): # real signature unknown
    pass

def DsListSites(*args, **kwargs): # real signature unknown
    pass

def DsUnBind(*args, **kwargs): # real signature unknown
    pass

def DsWriteAccountSpn(*args, **kwargs): # real signature unknown
    pass

def DuplicateToken(*args, **kwargs): # real signature unknown
    pass

def DuplicateTokenEx(*args, **kwargs): # real signature unknown
    pass

def EnumerateSecurityPackages(*args, **kwargs): # real signature unknown
    pass

def GetBinarySid(*args, **kwargs): # real signature unknown
    pass

def GetFileSecurity(*args, **kwargs): # real signature unknown
    pass

def GetKernelObjectSecurity(*args, **kwargs): # real signature unknown
    pass

def GetNamedSecurityInfo(*args, **kwargs): # real signature unknown
    pass

def GetPolicyHandle(*args, **kwargs): # real signature unknown
    pass

def GetSecurityInfo(*args, **kwargs): # real signature unknown
    pass

def GetTokenInformation(*args, **kwargs): # real signature unknown
    pass

def GetUserObjectSecurity(*args, **kwargs): # real signature unknown
    pass

def ImpersonateAnonymousToken(*args, **kwargs): # real signature unknown
    pass

def ImpersonateLoggedOnUser(*args, **kwargs): # real signature unknown
    pass

def ImpersonateNamedPipeClient(*args, **kwargs): # real signature unknown
    pass

def ImpersonateSelf(*args, **kwargs): # real signature unknown
    pass

def InitializeSecurityContext(*args, **kwargs): # real signature unknown
    pass

def IsTokenRestricted(*args, **kwargs): # real signature unknown
    pass

def LogonUser(*args, **kwargs): # real signature unknown
    pass

def LogonUserEx(*args, **kwargs): # real signature unknown
    pass

def LookupAccountName(*args, **kwargs): # real signature unknown
    pass

def LookupAccountSid(*args, **kwargs): # real signature unknown
    pass

def LookupPrivilegeDisplayName(*args, **kwargs): # real signature unknown
    pass

def LookupPrivilegeName(*args, **kwargs): # real signature unknown
    pass

def LookupPrivilegeValue(*args, **kwargs): # real signature unknown
    pass

def LsaAddAccountRights(*args, **kwargs): # real signature unknown
    pass

def LsaCallAuthenticationPackage(*args, **kwargs): # real signature unknown
    pass

def LsaClose(*args, **kwargs): # real signature unknown
    pass

def LsaConnectUntrusted(*args, **kwargs): # real signature unknown
    pass

def LsaDeregisterLogonProcess(*args, **kwargs): # real signature unknown
    pass

def LsaEnumerateAccountRights(*args, **kwargs): # real signature unknown
    pass

def LsaEnumerateAccountsWithUserRight(*args, **kwargs): # real signature unknown
    pass

def LsaEnumerateLogonSessions(*args, **kwargs): # real signature unknown
    pass

def LsaGetLogonSessionData(*args, **kwargs): # real signature unknown
    pass

def LsaLookupAuthenticationPackage(*args, **kwargs): # real signature unknown
    pass

def LsaOpenPolicy(*args, **kwargs): # real signature unknown
    pass

def LsaQueryInformationPolicy(*args, **kwargs): # real signature unknown
    pass

def LsaRegisterLogonProcess(*args, **kwargs): # real signature unknown
    pass

def LsaRegisterPolicyChangeNotification(*args, **kwargs): # real signature unknown
    pass

def LsaRemoveAccountRights(*args, **kwargs): # real signature unknown
    pass

def LsaRetrievePrivateData(*args, **kwargs): # real signature unknown
    pass

def LsaSetInformationPolicy(*args, **kwargs): # real signature unknown
    pass

def LsaStorePrivateData(*args, **kwargs): # real signature unknown
    pass

def LsaUnregisterPolicyChangeNotification(*args, **kwargs): # real signature unknown
    pass

def MapGenericMask(*args, **kwargs): # real signature unknown
    pass

def OpenProcessToken(*args, **kwargs): # real signature unknown
    pass

def OpenThreadToken(*args, **kwargs): # real signature unknown
    pass

def QuerySecurityPackageInfo(*args, **kwargs): # real signature unknown
    pass

def RevertToSelf(*args, **kwargs): # real signature unknown
    pass

def SECURITY_ATTRIBUTES(*args, **kwargs): # real signature unknown
    pass

def SECURITY_DESCRIPTOR(*args, **kwargs): # real signature unknown
    pass

def SetFileSecurity(*args, **kwargs): # real signature unknown
    pass

def SetKernelObjectSecurity(*args, **kwargs): # real signature unknown
    pass

def SetNamedSecurityInfo(*args, **kwargs): # real signature unknown
    pass

def SetSecurityInfo(*args, **kwargs): # real signature unknown
    pass

def SetThreadToken(*args, **kwargs): # real signature unknown
    pass

def SetTokenInformation(*args, **kwargs): # real signature unknown
    pass

def SetUserObjectSecurity(*args, **kwargs): # real signature unknown
    pass

def SID(*args, **kwargs): # real signature unknown
    pass

def TranslateName(*args, **kwargs): # real signature unknown
    pass

# classes

class PyCredHandleType(object):
    # no doc
    def Detach(self, *args, **kwargs): # real signature unknown
        pass

    def FreeCredentialsHandle(self, *args, **kwargs): # real signature unknown
        pass

    def QueryCredentialsAttributes(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CredHandleType = PyCredHandleType


class PyCtxtHandleType(object):
    # no doc
    def CompleteAuthToken(self, *args, **kwargs): # real signature unknown
        pass

    def DecryptMessage(self, *args, **kwargs): # real signature unknown
        pass

    def DeleteSecurityContext(self, *args, **kwargs): # real signature unknown
        pass

    def Detach(self, *args, **kwargs): # real signature unknown
        pass

    def EncryptMessage(self, *args, **kwargs): # real signature unknown
        pass

    def ImpersonateSecurityContext(self, *args, **kwargs): # real signature unknown
        pass

    def MakeSignature(self, *args, **kwargs): # real signature unknown
        pass

    def QueryContextAttributes(self, *args, **kwargs): # real signature unknown
        pass

    def QuerySecurityContextToken(self, *args, **kwargs): # real signature unknown
        pass

    def RevertSecurityContext(self, *args, **kwargs): # real signature unknown
        pass

    def VerifySignature(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass


CtxtHandleType = PyCtxtHandleType


class SecBufferDescType(object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __delitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__delitem__(y) <==> del x[y] """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __getitem__(self, y): # real signature unknown; restored from __doc__
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self): # real signature unknown; restored from __doc__
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    def __setitem__(self, i, y): # real signature unknown; restored from __doc__
        """ x.__setitem__(i, y) <==> x[i]=y """
        pass

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Currently should always be SECBUFFER_VERSION"""



PySecBufferDescType = SecBufferDescType


class SecBufferType(object):
    # no doc
    def Clear(self, *args, **kwargs): # real signature unknown
        pass

    def __delattr__(self, name): # real signature unknown; restored from __doc__
        """ x.__delattr__('name') <==> del x.name """
        pass

    def __getattribute__(self, name): # real signature unknown; restored from __doc__
        """ x.__getattribute__('name') <==> x.name """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    def __setattr__(self, name, value): # real signature unknown; restored from __doc__
        """ x.__setattr__('name', value) <==> x.name = value """
        pass

    Buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Encoded data buffer"""

    BufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Current size of data in buffer"""

    BufferType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type of buffer, one of the SECBUFFER_* constants -  can also be combined with SECBUFFER_READONLY"""

    MaxBufferSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum size of data buffer"""



PySecBufferType = SecBufferType


