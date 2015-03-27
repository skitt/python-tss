from interface import tss_lib

TSS_NV_DEFINED = tss_lib.TSS_NV_DEFINED
TPM_NV_INDEX_LOCK = tss_lib.TPM_NV_INDEX_LOCK
TPM_NV_INDEX0 = tss_lib.TPM_NV_INDEX0
TPM_NV_INDEX_DIR = tss_lib.TPM_NV_INDEX_DIR
TPM_NV_INDEX_EKCert = tss_lib.TPM_NV_INDEX_EKCert
TPM_NV_INDEX_TPM_CC = tss_lib.TPM_NV_INDEX_TPM_CC
TPM_NV_INDEX_PlatformCert = tss_lib.TPM_NV_INDEX_PlatformCert
TPM_NV_INDEX_Platform_CC = tss_lib.TPM_NV_INDEX_Platform_CC
TPM_NV_INDEX_TSS_BASE = tss_lib.TPM_NV_INDEX_TSS_BASE
TPM_NV_INDEX_PC_BASE = tss_lib.TPM_NV_INDEX_PC_BASE
TPM_NV_INDEX_SERVER_BASE = tss_lib.TPM_NV_INDEX_SERVER_BASE
TPM_NV_INDEX_MOBILE_BASE = tss_lib.TPM_NV_INDEX_MOBILE_BASE
TPM_NV_INDEX_PERIPHERAL_BASE = tss_lib.TPM_NV_INDEX_PERIPHERAL_BASE
TPM_NV_INDEX_GROUP_RESV_BASE = tss_lib.TPM_NV_INDEX_GROUP_RESV_BASE

TSS_POLICY_USAGE = tss_lib.TSS_POLICY_USAGE
TSS_POLICY_MIGRATION = tss_lib.TSS_POLICY_MIGRATION
TSS_POLICY_OPERATOR = tss_lib.TSS_POLICY_OPERATOR

TSS_SECRET_LIFETIME_ALWAYS = tss_lib.TSS_SECRET_LIFETIME_ALWAYS
TSS_SECRET_LIFETIME_COUNTER = tss_lib.TSS_SECRET_LIFETIME_COUNTER
TSS_SECRET_LIFETIME_TIMER = tss_lib.TSS_SECRET_LIFETIME_TIMER
TSS_SECRET_MODE_NONE = tss_lib.TSS_SECRET_MODE_NONE
TSS_SECRET_MODE_SHA1 = tss_lib.TSS_SECRET_MODE_SHA1
TSS_SECRET_MODE_PLAIN = tss_lib.TSS_SECRET_MODE_PLAIN
TSS_SECRET_MODE_POPUP = tss_lib.TSS_SECRET_MODE_POPUP
TSS_SECRET_MODE_CALLBACK = tss_lib.TSS_SECRET_MODE_CALLBACK

TSS_PS_TYPE_USER = tss_lib.TSS_PS_TYPE_USER
TSS_PS_TYPE_SYSTEM = tss_lib.TSS_PS_TYPE_SYSTEM

TSS_KEY_NO_AUTHORIZATION = tss_lib.TSS_KEY_NO_AUTHORIZATION
TSS_KEY_AUTHORIZATION = tss_lib.TSS_KEY_AUTHORIZATION
TSS_KEY_AUTHORIZATION_PRIV_USE_ONLY = tss_lib.TSS_KEY_AUTHORIZATION_PRIV_USE_ONLY
TSS_KEY_NON_VOLATILE = tss_lib.TSS_KEY_NON_VOLATILE
TSS_KEY_VOLATILE = tss_lib.TSS_KEY_VOLATILE
TSS_KEY_NOT_MIGRATABLE = tss_lib.TSS_KEY_NOT_MIGRATABLE
TSS_KEY_MIGRATABLE = tss_lib.TSS_KEY_MIGRATABLE
TSS_KEY_TYPE_DEFAULT = tss_lib.TSS_KEY_TYPE_DEFAULT
TSS_KEY_TYPE_SIGNING = tss_lib.TSS_KEY_TYPE_SIGNING
TSS_KEY_TYPE_STORAGE = tss_lib.TSS_KEY_TYPE_STORAGE
TSS_KEY_TYPE_IDENTITY = tss_lib.TSS_KEY_TYPE_IDENTITY
TSS_KEY_TYPE_AUTHCHANGE = tss_lib.TSS_KEY_TYPE_AUTHCHANGE
TSS_KEY_TYPE_BIND = tss_lib.TSS_KEY_TYPE_BIND
TSS_KEY_TYPE_LEGACY = tss_lib.TSS_KEY_TYPE_LEGACY
TSS_KEY_TYPE_MIGRATE = tss_lib.TSS_KEY_TYPE_MIGRATE
TSS_KEY_TYPE_BITMASK = tss_lib.TSS_KEY_TYPE_BITMASK
TSS_KEY_SIZE_DEFAULT = tss_lib.TSS_KEY_SIZE_DEFAULT
TSS_KEY_SIZE_512 = tss_lib.TSS_KEY_SIZE_512
TSS_KEY_SIZE_1024 = tss_lib.TSS_KEY_SIZE_1024
TSS_KEY_SIZE_2048 = tss_lib.TSS_KEY_SIZE_2048
TSS_KEY_SIZE_4096 = tss_lib.TSS_KEY_SIZE_4096
TSS_KEY_SIZE_8192 = tss_lib.TSS_KEY_SIZE_8192
TSS_KEY_SIZE_16384 = tss_lib.TSS_KEY_SIZE_16384
TSS_KEY_SIZE_BITMASK = tss_lib.TSS_KEY_SIZE_BITMASK
TSS_KEY_NOT_CERTIFIED_MIGRATABLE = tss_lib.TSS_KEY_NOT_CERTIFIED_MIGRATABLE
TSS_KEY_CERTIFIED_MIGRATABLE = tss_lib.TSS_KEY_CERTIFIED_MIGRATABLE
TSS_KEY_STRUCT_DEFAULT = tss_lib.TSS_KEY_STRUCT_DEFAULT
TSS_KEY_STRUCT_KEY = tss_lib.TSS_KEY_STRUCT_KEY
TSS_KEY_STRUCT_KEY12 = tss_lib.TSS_KEY_STRUCT_KEY12
TSS_KEY_STRUCT_BITMASK = tss_lib.TSS_KEY_STRUCT_BITMASK
TSS_KEY_EMPTY_KEY = tss_lib.TSS_KEY_EMPTY_KEY
TSS_KEY_TSP_SRK = tss_lib.TSS_KEY_TSP_SRK
TSS_KEY_TEMPLATE_BITMASK = tss_lib.TSS_KEY_TEMPLATE_BITMASK
TSS_KEY_SIZEVAL_512BIT = tss_lib.TSS_KEY_SIZEVAL_512BIT
TSS_KEY_SIZEVAL_1024BIT = tss_lib.TSS_KEY_SIZEVAL_1024BIT
TSS_KEY_SIZEVAL_2048BIT = tss_lib.TSS_KEY_SIZEVAL_2048BIT
TSS_KEY_SIZEVAL_4096BIT = tss_lib.TSS_KEY_SIZEVAL_4096BIT
TSS_KEY_SIZEVAL_8192BIT = tss_lib.TSS_KEY_SIZEVAL_8192BIT
TSS_KEY_SIZEVAL_16384BIT = tss_lib.TSS_KEY_SIZEVAL_16384BIT

TSS_TSPATTRIB_CONTEXT_SILENT_MODE = tss_lib.TSS_TSPATTRIB_CONTEXT_SILENT_MODE
TSS_TSPATTRIB_CONTEXT_MACHINE_NAME = tss_lib.TSS_TSPATTRIB_CONTEXT_MACHINE_NAME
TSS_TSPATTRIB_CONTEXT_VERSION_MODE = tss_lib.TSS_TSPATTRIB_CONTEXT_VERSION_MODE
TSS_TSPATTRIB_CONTEXT_TRANSPORT = tss_lib.TSS_TSPATTRIB_CONTEXT_TRANSPORT
TSS_TSPATTRIB_CONTEXT_CONNECTION_VERSION = tss_lib.TSS_TSPATTRIB_CONTEXT_CONNECTION_VERSION
TSS_TSPATTRIB_SECRET_HASH_MODE = tss_lib.TSS_TSPATTRIB_SECRET_HASH_MODE
TSS_TSPATTRIB_CONTEXTTRANS_CONTROL = tss_lib.TSS_TSPATTRIB_CONTEXTTRANS_CONTROL
TSS_TSPATTRIB_CONTEXTTRANS_MODE = tss_lib.TSS_TSPATTRIB_CONTEXTTRANS_MODE
TSS_TSPATTRIB_CONTEXT_NOT_SILENT = tss_lib.TSS_TSPATTRIB_CONTEXT_NOT_SILENT
TSS_TSPATTRIB_CONTEXT_SILENT = tss_lib.TSS_TSPATTRIB_CONTEXT_SILENT
TSS_TSPATTRIB_CONTEXT_VERSION_AUTO = tss_lib.TSS_TSPATTRIB_CONTEXT_VERSION_AUTO
TSS_TSPATTRIB_CONTEXT_VERSION_V1_1 = tss_lib.TSS_TSPATTRIB_CONTEXT_VERSION_V1_1
TSS_TSPATTRIB_CONTEXT_VERSION_V1_2 = tss_lib.TSS_TSPATTRIB_CONTEXT_VERSION_V1_2
TSS_TSPATTRIB_DISABLE_TRANSPORT = tss_lib.TSS_TSPATTRIB_DISABLE_TRANSPORT
TSS_TSPATTRIB_ENABLE_TRANSPORT = tss_lib.TSS_TSPATTRIB_ENABLE_TRANSPORT
TSS_TSPATTRIB_TRANSPORT_NO_DEFAULT_ENCRYPTION = tss_lib.TSS_TSPATTRIB_TRANSPORT_NO_DEFAULT_ENCRYPTION
TSS_TSPATTRIB_TRANSPORT_DEFAULT_ENCRYPTION = tss_lib.TSS_TSPATTRIB_TRANSPORT_DEFAULT_ENCRYPTION
TSS_TSPATTRIB_TRANSPORT_AUTHENTIC_CHANNEL = tss_lib.TSS_TSPATTRIB_TRANSPORT_AUTHENTIC_CHANNEL
TSS_TSPATTRIB_TRANSPORT_EXCLUSIVE = tss_lib.TSS_TSPATTRIB_TRANSPORT_EXCLUSIVE
TSS_TSPATTRIB_TRANSPORT_STATIC_AUTH = tss_lib.TSS_TSPATTRIB_TRANSPORT_STATIC_AUTH
TSS_TSPATTRIB_SECRET_HASH_MODE_POPUP = tss_lib.TSS_TSPATTRIB_SECRET_HASH_MODE_POPUP
TSS_TSPATTRIB_HASH_MODE_NOT_NULL = tss_lib.TSS_TSPATTRIB_HASH_MODE_NOT_NULL
TSS_TSPATTRIB_HASH_MODE_NULL = tss_lib.TSS_TSPATTRIB_HASH_MODE_NULL
TSS_TSPATTRIB_TPM_CALLBACK_COLLATEIDENTITY = tss_lib.TSS_TSPATTRIB_TPM_CALLBACK_COLLATEIDENTITY
TSS_TSPATTRIB_TPM_CALLBACK_ACTIVATEIDENTITY = tss_lib.TSS_TSPATTRIB_TPM_CALLBACK_ACTIVATEIDENTITY
TSS_TSPATTRIB_TPM_ORDINAL_AUDIT_STATUS = tss_lib.TSS_TSPATTRIB_TPM_ORDINAL_AUDIT_STATUS
TSS_TSPATTRIB_TPM_CREDENTIAL = tss_lib.TSS_TSPATTRIB_TPM_CREDENTIAL
TSS_TSPATTRIB_POLICY_CALLBACK_HMAC = tss_lib.TSS_TSPATTRIB_POLICY_CALLBACK_HMAC
TSS_TSPATTRIB_POLICY_CALLBACK_XOR_ENC = tss_lib.TSS_TSPATTRIB_POLICY_CALLBACK_XOR_ENC
TSS_TSPATTRIB_POLICY_CALLBACK_TAKEOWNERSHIP = tss_lib.TSS_TSPATTRIB_POLICY_CALLBACK_TAKEOWNERSHIP
TSS_TSPATTRIB_POLICY_CALLBACK_CHANGEAUTHASYM = tss_lib.TSS_TSPATTRIB_POLICY_CALLBACK_CHANGEAUTHASYM
TSS_TSPATTRIB_POLICY_SECRET_LIFETIME = tss_lib.TSS_TSPATTRIB_POLICY_SECRET_LIFETIME
TSS_TSPATTRIB_POLICY_POPUPSTRING = tss_lib.TSS_TSPATTRIB_POLICY_POPUPSTRING
TSS_TSPATTRIB_POLICY_CALLBACK_SEALX_MASK = tss_lib.TSS_TSPATTRIB_POLICY_CALLBACK_SEALX_MASK
TSS_TSPATTRIB_SECRET_HASH_MODE = tss_lib.TSS_TSPATTRIB_SECRET_HASH_MODE
TSS_TSPATTRIB_POLICY_DELEGATION_INFO = tss_lib.TSS_TSPATTRIB_POLICY_DELEGATION_INFO
TSS_TSPATTRIB_POLICY_DELEGATION_PCR = tss_lib.TSS_TSPATTRIB_POLICY_DELEGATION_PCR
TSS_TSPATTRIB_POLSECRET_LIFETIME_ALWAYS = tss_lib.TSS_TSPATTRIB_POLSECRET_LIFETIME_ALWAYS
TSS_TSPATTRIB_POLSECRET_LIFETIME_COUNTER = tss_lib.TSS_TSPATTRIB_POLSECRET_LIFETIME_COUNTER
TSS_TSPATTRIB_POLSECRET_LIFETIME_TIMER = tss_lib.TSS_TSPATTRIB_POLSECRET_LIFETIME_TIMER
TSS_TSPATTRIB_POLICYSECRET_LIFETIME_ALWAYS = tss_lib.TSS_TSPATTRIB_POLICYSECRET_LIFETIME_ALWAYS
TSS_TSPATTRIB_POLICYSECRET_LIFETIME_COUNTER = tss_lib.TSS_TSPATTRIB_POLICYSECRET_LIFETIME_COUNTER
TSS_TSPATTRIB_POLICYSECRET_LIFETIME_TIMER = tss_lib.TSS_TSPATTRIB_POLICYSECRET_LIFETIME_TIMER
TSS_TSPATTRIB_POLDEL_TYPE = tss_lib.TSS_TSPATTRIB_POLDEL_TYPE
TSS_TSPATTRIB_POLDEL_INDEX = tss_lib.TSS_TSPATTRIB_POLDEL_INDEX
TSS_TSPATTRIB_POLDEL_PER1 = tss_lib.TSS_TSPATTRIB_POLDEL_PER1
TSS_TSPATTRIB_POLDEL_PER2 = tss_lib.TSS_TSPATTRIB_POLDEL_PER2
TSS_TSPATTRIB_POLDEL_LABEL = tss_lib.TSS_TSPATTRIB_POLDEL_LABEL
TSS_TSPATTRIB_POLDEL_FAMILYID = tss_lib.TSS_TSPATTRIB_POLDEL_FAMILYID
TSS_TSPATTRIB_POLDEL_VERCOUNT = tss_lib.TSS_TSPATTRIB_POLDEL_VERCOUNT
TSS_TSPATTRIB_POLDEL_OWNERBLOB = tss_lib.TSS_TSPATTRIB_POLDEL_OWNERBLOB
TSS_TSPATTRIB_POLDEL_KEYBLOB = tss_lib.TSS_TSPATTRIB_POLDEL_KEYBLOB
TSS_TSPATTRIB_POLDELPCR_LOCALITY = tss_lib.TSS_TSPATTRIB_POLDELPCR_LOCALITY
TSS_TSPATTRIB_POLDELPCR_DIGESTATRELEASE = tss_lib.TSS_TSPATTRIB_POLDELPCR_DIGESTATRELEASE
TSS_TSPATTRIB_POLDELPCR_SELECTION = tss_lib.TSS_TSPATTRIB_POLDELPCR_SELECTION
TSS_TSPATTRIB_ENCDATA_BLOB = tss_lib.TSS_TSPATTRIB_ENCDATA_BLOB
TSS_TSPATTRIB_ENCDATA_PCR = tss_lib.TSS_TSPATTRIB_ENCDATA_PCR
TSS_TSPATTRIB_ENCDATA_PCR_LONG = tss_lib.TSS_TSPATTRIB_ENCDATA_PCR_LONG
TSS_TSPATTRIB_ENCDATA_SEAL = tss_lib.TSS_TSPATTRIB_ENCDATA_SEAL
TSS_TSPATTRIB_ENCDATABLOB_BLOB = tss_lib.TSS_TSPATTRIB_ENCDATABLOB_BLOB
TSS_TSPATTRIB_ENCDATAPCR_DIGEST_ATCREATION = tss_lib.TSS_TSPATTRIB_ENCDATAPCR_DIGEST_ATCREATION
TSS_TSPATTRIB_ENCDATAPCR_DIGEST_ATRELEASE = tss_lib.TSS_TSPATTRIB_ENCDATAPCR_DIGEST_ATRELEASE
TSS_TSPATTRIB_ENCDATAPCR_SELECTION = tss_lib.TSS_TSPATTRIB_ENCDATAPCR_SELECTION
TSS_TSPATTRIB_ENCDATAPCR_DIGEST_RELEASE = tss_lib.TSS_TSPATTRIB_ENCDATAPCR_DIGEST_RELEASE
TSS_TSPATTRIB_ENCDATAPCRLONG_LOCALITY_ATCREATION = tss_lib.TSS_TSPATTRIB_ENCDATAPCRLONG_LOCALITY_ATCREATION
TSS_TSPATTRIB_ENCDATAPCRLONG_LOCALITY_ATRELEASE = tss_lib.TSS_TSPATTRIB_ENCDATAPCRLONG_LOCALITY_ATRELEASE
TSS_TSPATTRIB_ENCDATAPCRLONG_CREATION_SELECTION = tss_lib.TSS_TSPATTRIB_ENCDATAPCRLONG_CREATION_SELECTION
TSS_TSPATTRIB_ENCDATAPCRLONG_RELEASE_SELECTION = tss_lib.TSS_TSPATTRIB_ENCDATAPCRLONG_RELEASE_SELECTION
TSS_TSPATTRIB_ENCDATAPCRLONG_DIGEST_ATCREATION = tss_lib.TSS_TSPATTRIB_ENCDATAPCRLONG_DIGEST_ATCREATION
TSS_TSPATTRIB_ENCDATAPCRLONG_DIGEST_ATRELEASE = tss_lib.TSS_TSPATTRIB_ENCDATAPCRLONG_DIGEST_ATRELEASE
TSS_TSPATTRIB_ENCDATASEAL_PROTECT_MODE = tss_lib.TSS_TSPATTRIB_ENCDATASEAL_PROTECT_MODE
TSS_TSPATTRIB_ENCDATASEAL_NOPROTECT = tss_lib.TSS_TSPATTRIB_ENCDATASEAL_NOPROTECT
TSS_TSPATTRIB_ENCDATASEAL_PROTECT = tss_lib.TSS_TSPATTRIB_ENCDATASEAL_PROTECT
TSS_TSPATTRIB_ENCDATASEAL_NO_PROTECT = tss_lib.TSS_TSPATTRIB_ENCDATASEAL_NO_PROTECT
TSS_TSPATTRIB_NV_INDEX = tss_lib.TSS_TSPATTRIB_NV_INDEX
TSS_TSPATTRIB_NV_PERMISSIONS = tss_lib.TSS_TSPATTRIB_NV_PERMISSIONS
TSS_TSPATTRIB_NV_STATE = tss_lib.TSS_TSPATTRIB_NV_STATE
TSS_TSPATTRIB_NV_DATASIZE = tss_lib.TSS_TSPATTRIB_NV_DATASIZE
TSS_TSPATTRIB_NV_PCR = tss_lib.TSS_TSPATTRIB_NV_PCR
TSS_TSPATTRIB_NVSTATE_READSTCLEAR = tss_lib.TSS_TSPATTRIB_NVSTATE_READSTCLEAR
TSS_TSPATTRIB_NVSTATE_WRITESTCLEAR = tss_lib.TSS_TSPATTRIB_NVSTATE_WRITESTCLEAR
TSS_TSPATTRIB_NVSTATE_WRITEDEFINE = tss_lib.TSS_TSPATTRIB_NVSTATE_WRITEDEFINE
TSS_TSPATTRIB_NVPCR_READPCRSELECTION = tss_lib.TSS_TSPATTRIB_NVPCR_READPCRSELECTION
TSS_TSPATTRIB_NVPCR_READDIGESTATRELEASE = tss_lib.TSS_TSPATTRIB_NVPCR_READDIGESTATRELEASE
TSS_TSPATTRIB_NVPCR_READLOCALITYATRELEASE = tss_lib.TSS_TSPATTRIB_NVPCR_READLOCALITYATRELEASE
TSS_TSPATTRIB_NVPCR_WRITEPCRSELECTION = tss_lib.TSS_TSPATTRIB_NVPCR_WRITEPCRSELECTION
TSS_TSPATTRIB_NVPCR_WRITEDIGESTATRELEASE = tss_lib.TSS_TSPATTRIB_NVPCR_WRITEDIGESTATRELEASE
TSS_TSPATTRIB_NVPCR_WRITELOCALITYATRELEASE = tss_lib.TSS_TSPATTRIB_NVPCR_WRITELOCALITYATRELEASE
TSS_TSPATTRIB_HASH_IDENTIFIER = tss_lib.TSS_TSPATTRIB_HASH_IDENTIFIER
TSS_TSPATTRIB_ALG_IDENTIFIER = tss_lib.TSS_TSPATTRIB_ALG_IDENTIFIER
TSS_TSPATTRIB_PCRS_INFO = tss_lib.TSS_TSPATTRIB_PCRS_INFO
TSS_TSPATTRIB_PCRSINFO_PCRSTRUCT = tss_lib.TSS_TSPATTRIB_PCRSINFO_PCRSTRUCT
TSS_TSPATTRIB_DELFAMILY_STATE = tss_lib.TSS_TSPATTRIB_DELFAMILY_STATE
TSS_TSPATTRIB_DELFAMILY_INFO = tss_lib.TSS_TSPATTRIB_DELFAMILY_INFO
TSS_TSPATTRIB_DELFAMILYSTATE_LOCKED = tss_lib.TSS_TSPATTRIB_DELFAMILYSTATE_LOCKED
TSS_TSPATTRIB_DELFAMILYSTATE_ENABLED = tss_lib.TSS_TSPATTRIB_DELFAMILYSTATE_ENABLED
TSS_TSPATTRIB_DELFAMILYINFO_LABEL = tss_lib.TSS_TSPATTRIB_DELFAMILYINFO_LABEL
TSS_TSPATTRIB_DELFAMILYINFO_VERCOUNT = tss_lib.TSS_TSPATTRIB_DELFAMILYINFO_VERCOUNT
TSS_TSPATTRIB_DELFAMILYINFO_FAMILYID = tss_lib.TSS_TSPATTRIB_DELFAMILYINFO_FAMILYID
TSS_TSPATTRIB_DAACRED_COMMIT = tss_lib.TSS_TSPATTRIB_DAACRED_COMMIT
TSS_TSPATTRIB_DAACRED_ATTRIB_GAMMAS = tss_lib.TSS_TSPATTRIB_DAACRED_ATTRIB_GAMMAS
TSS_TSPATTRIB_DAACRED_CREDENTIAL_BLOB = tss_lib.TSS_TSPATTRIB_DAACRED_CREDENTIAL_BLOB
TSS_TSPATTRIB_DAACRED_CALLBACK_SIGN = tss_lib.TSS_TSPATTRIB_DAACRED_CALLBACK_SIGN
TSS_TSPATTRIB_DAACRED_CALLBACK_VERIFYSIGNATURE = tss_lib.TSS_TSPATTRIB_DAACRED_CALLBACK_VERIFYSIGNATURE
TSS_TSPATTRIB_DAACOMMIT_NUMBER = tss_lib.TSS_TSPATTRIB_DAACOMMIT_NUMBER
TSS_TSPATTRIB_DAACOMMIT_SELECTION = tss_lib.TSS_TSPATTRIB_DAACOMMIT_SELECTION
TSS_TSPATTRIB_DAACOMMIT_COMMITMENTS = tss_lib.TSS_TSPATTRIB_DAACOMMIT_COMMITMENTS
TSS_TSPATTRIB_DAAATTRIBGAMMAS_BLOB = tss_lib.TSS_TSPATTRIB_DAAATTRIBGAMMAS_BLOB
TSS_TSPATTRIB_DAAISSUERKEY_BLOB = tss_lib.TSS_TSPATTRIB_DAAISSUERKEY_BLOB
TSS_TSPATTRIB_DAAISSUERKEY_PUBKEY = tss_lib.TSS_TSPATTRIB_DAAISSUERKEY_PUBKEY
TSS_TSPATTRIB_DAAISSUERKEYBLOB_PUBLIC_KEY = tss_lib.TSS_TSPATTRIB_DAAISSUERKEYBLOB_PUBLIC_KEY
TSS_TSPATTRIB_DAAISSUERKEYBLOB_SECRET_KEY = tss_lib.TSS_TSPATTRIB_DAAISSUERKEYBLOB_SECRET_KEY
TSS_TSPATTRIB_DAAISSUERKEYBLOB_KEYBLOB = tss_lib.TSS_TSPATTRIB_DAAISSUERKEYBLOB_KEYBLOB
TSS_TSPATTRIB_DAAISSUERKEYBLOB_PROOF = tss_lib.TSS_TSPATTRIB_DAAISSUERKEYBLOB_PROOF
TSS_TSPATTRIB_DAAISSUERKEYPUBKEY_NUM_ATTRIBS = tss_lib.TSS_TSPATTRIB_DAAISSUERKEYPUBKEY_NUM_ATTRIBS
TSS_TSPATTRIB_DAAISSUERKEYPUBKEY_NUM_PLATFORM_ATTRIBS = tss_lib.TSS_TSPATTRIB_DAAISSUERKEYPUBKEY_NUM_PLATFORM_ATTRIBS
TSS_TSPATTRIB_DAAISSUERKEYPUBKEY_NUM_ISSUER_ATTRIBS = tss_lib.TSS_TSPATTRIB_DAAISSUERKEYPUBKEY_NUM_ISSUER_ATTRIBS
TSS_TSPATTRIB_DAAARAKEY_BLOB = tss_lib.TSS_TSPATTRIB_DAAARAKEY_BLOB
TSS_TSPATTRIB_DAAARAKEYBLOB_PUBLIC_KEY = tss_lib.TSS_TSPATTRIB_DAAARAKEYBLOB_PUBLIC_KEY
TSS_TSPATTRIB_DAAARAKEYBLOB_SECRET_KEY = tss_lib.TSS_TSPATTRIB_DAAARAKEYBLOB_SECRET_KEY
TSS_TSPATTRIB_DAAARAKEYBLOB_KEYBLOB = tss_lib.TSS_TSPATTRIB_DAAARAKEYBLOB_KEYBLOB
TSS_TSPATTRIB_KEY_BLOB = tss_lib.TSS_TSPATTRIB_KEY_BLOB
TSS_TSPATTRIB_KEY_INFO = tss_lib.TSS_TSPATTRIB_KEY_INFO
TSS_TSPATTRIB_KEY_UUID = tss_lib.TSS_TSPATTRIB_KEY_UUID
TSS_TSPATTRIB_KEY_PCR = tss_lib.TSS_TSPATTRIB_KEY_PCR
TSS_TSPATTRIB_RSAKEY_INFO = tss_lib.TSS_TSPATTRIB_RSAKEY_INFO
TSS_TSPATTRIB_KEY_REGISTER = tss_lib.TSS_TSPATTRIB_KEY_REGISTER
TSS_TSPATTRIB_KEY_PCR_LONG = tss_lib.TSS_TSPATTRIB_KEY_PCR_LONG
TSS_TSPATTRIB_KEY_CONTROLBIT = tss_lib.TSS_TSPATTRIB_KEY_CONTROLBIT
TSS_TSPATTRIB_KEY_CMKINFO = tss_lib.TSS_TSPATTRIB_KEY_CMKINFO
TSS_TSPATTRIB_KEYBLOB_BLOB = tss_lib.TSS_TSPATTRIB_KEYBLOB_BLOB
TSS_TSPATTRIB_KEYBLOB_PUBLIC_KEY = tss_lib.TSS_TSPATTRIB_KEYBLOB_PUBLIC_KEY
TSS_TSPATTRIB_KEYBLOB_PRIVATE_KEY = tss_lib.TSS_TSPATTRIB_KEYBLOB_PRIVATE_KEY
TSS_TSPATTRIB_KEYINFO_SIZE = tss_lib.TSS_TSPATTRIB_KEYINFO_SIZE
TSS_TSPATTRIB_KEYINFO_USAGE = tss_lib.TSS_TSPATTRIB_KEYINFO_USAGE
TSS_TSPATTRIB_KEYINFO_KEYFLAGS = tss_lib.TSS_TSPATTRIB_KEYINFO_KEYFLAGS
TSS_TSPATTRIB_KEYINFO_AUTHUSAGE = tss_lib.TSS_TSPATTRIB_KEYINFO_AUTHUSAGE
TSS_TSPATTRIB_KEYINFO_ALGORITHM = tss_lib.TSS_TSPATTRIB_KEYINFO_ALGORITHM
TSS_TSPATTRIB_KEYINFO_SIGSCHEME = tss_lib.TSS_TSPATTRIB_KEYINFO_SIGSCHEME
TSS_TSPATTRIB_KEYINFO_ENCSCHEME = tss_lib.TSS_TSPATTRIB_KEYINFO_ENCSCHEME
TSS_TSPATTRIB_KEYINFO_MIGRATABLE = tss_lib.TSS_TSPATTRIB_KEYINFO_MIGRATABLE
TSS_TSPATTRIB_KEYINFO_REDIRECTED = tss_lib.TSS_TSPATTRIB_KEYINFO_REDIRECTED
TSS_TSPATTRIB_KEYINFO_VOLATILE = tss_lib.TSS_TSPATTRIB_KEYINFO_VOLATILE
TSS_TSPATTRIB_KEYINFO_AUTHDATAUSAGE = tss_lib.TSS_TSPATTRIB_KEYINFO_AUTHDATAUSAGE
TSS_TSPATTRIB_KEYINFO_VERSION = tss_lib.TSS_TSPATTRIB_KEYINFO_VERSION
TSS_TSPATTRIB_KEYINFO_CMK = tss_lib.TSS_TSPATTRIB_KEYINFO_CMK
TSS_TSPATTRIB_KEYINFO_KEYSTRUCT = tss_lib.TSS_TSPATTRIB_KEYINFO_KEYSTRUCT
TSS_TSPATTRIB_KEYCONTROL_OWNEREVICT = tss_lib.TSS_TSPATTRIB_KEYCONTROL_OWNEREVICT
TSS_TSPATTRIB_KEYINFO_RSA_EXPONENT = tss_lib.TSS_TSPATTRIB_KEYINFO_RSA_EXPONENT
TSS_TSPATTRIB_KEYINFO_RSA_MODULUS = tss_lib.TSS_TSPATTRIB_KEYINFO_RSA_MODULUS
TSS_TSPATTRIB_KEYINFO_RSA_KEYSIZE = tss_lib.TSS_TSPATTRIB_KEYINFO_RSA_KEYSIZE
TSS_TSPATTRIB_KEYINFO_RSA_PRIMES = tss_lib.TSS_TSPATTRIB_KEYINFO_RSA_PRIMES
TSS_TSPATTRIB_KEYPCR_DIGEST_ATCREATION = tss_lib.TSS_TSPATTRIB_KEYPCR_DIGEST_ATCREATION
TSS_TSPATTRIB_KEYPCR_DIGEST_ATRELEASE = tss_lib.TSS_TSPATTRIB_KEYPCR_DIGEST_ATRELEASE
TSS_TSPATTRIB_KEYPCR_SELECTION = tss_lib.TSS_TSPATTRIB_KEYPCR_SELECTION
TSS_TSPATTRIB_KEYREGISTER_USER = tss_lib.TSS_TSPATTRIB_KEYREGISTER_USER
TSS_TSPATTRIB_KEYREGISTER_SYSTEM = tss_lib.TSS_TSPATTRIB_KEYREGISTER_SYSTEM
TSS_TSPATTRIB_KEYREGISTER_NO = tss_lib.TSS_TSPATTRIB_KEYREGISTER_NO
TSS_TSPATTRIB_KEYPCRLONG_LOCALITY_ATCREATION = tss_lib.TSS_TSPATTRIB_KEYPCRLONG_LOCALITY_ATCREATION
TSS_TSPATTRIB_KEYPCRLONG_LOCALITY_ATRELEASE = tss_lib.TSS_TSPATTRIB_KEYPCRLONG_LOCALITY_ATRELEASE
TSS_TSPATTRIB_KEYPCRLONG_CREATION_SELECTION = tss_lib.TSS_TSPATTRIB_KEYPCRLONG_CREATION_SELECTION
TSS_TSPATTRIB_KEYPCRLONG_RELEASE_SELECTION = tss_lib.TSS_TSPATTRIB_KEYPCRLONG_RELEASE_SELECTION
TSS_TSPATTRIB_KEYPCRLONG_DIGEST_ATCREATION = tss_lib.TSS_TSPATTRIB_KEYPCRLONG_DIGEST_ATCREATION
TSS_TSPATTRIB_KEYPCRLONG_DIGEST_ATRELEASE = tss_lib.TSS_TSPATTRIB_KEYPCRLONG_DIGEST_ATRELEASE
TSS_TSPATTRIB_KEYINFO_CMK_MA_APPROVAL = tss_lib.TSS_TSPATTRIB_KEYINFO_CMK_MA_APPROVAL
TSS_TSPATTRIB_KEYINFO_CMK_MA_DIGEST = tss_lib.TSS_TSPATTRIB_KEYINFO_CMK_MA_DIGEST

TPM_ALG_RSA = tss_lib.TPM_ALG_RSA
TPM_ALG_DES = tss_lib.TPM_ALG_DES
TPM_ALG_3DES = tss_lib.TPM_ALG_3DES
TPM_ALG_SHA = tss_lib.TPM_ALG_SHA
TPM_ALG_HMAC = tss_lib.TPM_ALG_HMAC
TPM_ALG_AES = tss_lib.TPM_ALG_AES
TPM_ALG_AES128 = tss_lib.TPM_ALG_AES128
TPM_ALG_MGF1 = tss_lib.TPM_ALG_MGF1
TPM_ALG_AES192 = tss_lib.TPM_ALG_AES192
TPM_ALG_AES256 = tss_lib.TPM_ALG_AES256
TPM_ALG_XOR = tss_lib.TPM_ALG_XOR

TPM_ES_NONE = tss_lib.TPM_ES_NONE
TPM_ES_RSAESPKCSv15 = tss_lib.TPM_ES_RSAESPKCSv15
TPM_ES_RSAESOAEP_SHA1_MGF1 = tss_lib.TPM_ES_RSAESOAEP_SHA1_MGF1
TPM_ES_SYM_CNT = tss_lib.TPM_ES_SYM_CNT
TPM_ES_SYM_CTR = tss_lib.TPM_ES_SYM_CTR
TPM_ES_SYM_OFB = tss_lib.TPM_ES_SYM_OFB
TPM_ES_SYM_CBC_PKCS5PAD = tss_lib.TPM_ES_SYM_CBC_PKCS5PAD

TPM_SS_NONE = tss_lib.TPM_SS_NONE
TPM_SS_RSASSAPKCS1v15_SHA1 = tss_lib.TPM_SS_RSASSAPKCS1v15_SHA1
TPM_SS_RSASSAPKCS1v15_DER = tss_lib.TPM_SS_RSASSAPKCS1v15_DER
TPM_SS_RSASSAPKCS1v15_INFO = tss_lib.TPM_SS_RSASSAPKCS1v15_INFO

TSS_PCRS_STRUCT_DEFAULT = tss_lib.TSS_PCRS_STRUCT_DEFAULT
TSS_PCRS_STRUCT_INFO = tss_lib.TSS_PCRS_STRUCT_INFO
TSS_PCRS_STRUCT_INFO_LONG = tss_lib.TSS_PCRS_STRUCT_INFO_LONG
TSS_PCRS_STRUCT_INFO_SHORT = tss_lib.TSS_PCRS_STRUCT_INFO_SHORT
TSS_PCRS_DIRECTION_CREATION = tss_lib.TSS_PCRS_DIRECTION_CREATION
TSS_PCRS_DIRECTION_RELEASE = tss_lib.TSS_PCRS_DIRECTION_RELEASE