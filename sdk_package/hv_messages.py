from enum import Enum

class MessageID(Enum):
    DEFAULT = 0x0000
    ERR_AddSNM2StorageDevice = 0xA003
    ERR_AddRAIDStorageDevice = 0xA004
    ERR_Createlu = 0xA005
    ERR_Presentlu = 0xA006
    ERR_CreateHG = 0xA008
    ERR_getHG = 0xA009
    ERR_getLu = 0xA00A
    ERR_DeleteLu = 0xA00B
    ERR_DeleteHg = 0xA00C
    ERR_CreateSnapshot = 0xA00D
    ERR_DeleteSnapshot = 0xA00E
    ERR_GetSnapshot = 0xA00F
    ERR_SplitSnapshot = 0xA010
    ERR_ResyncSnapshot = 0xA011
    ERR_RestoreSnapshot = 0xA012
    ERR_AddWWNToHg = 0xA014
    ERR_CreateFS = 0xA015
    ERR_UpdateFS = 0xA016
    ERR_SetFSSysLock = 0xA017
    ERR_GetFS = 0xA018
    ERR_CreateFSSnapshot = 0xA019
    ERR_CreateNFSExport = 0xA01A
    ERR_IncreaseNFSSize = 0xA01B
    ERR_GetNFS = 0xA01D
    ERR_DeleteNFS = 0xA01E
    ERR_CreateHUR = 0xA021
    ERR_CreateVVol = 0xA022
    ERR_GetShadowImagePairList = 0xA024
    ERR_CreateShadowImagePair = 0xA025
    ERR_DeleteShadowImagePair = 0xA026
    ERR_SplitShadowImagePair = 0xA027
    ERR_ResyncShadowImagePair = 0xA028
    ERR_RestoreShadowImagePair = 0xA029
    ERR_RemoveWWNFromHg = 0xA02A
    ERR_RemoveInitiatorFromISCSITarget = 0xA030
    ERR_AddLogicalUnitToISCSITarget = 0xA031
    ERR_RemoveLogicalUnitFromISCSITarget = 0xA032
    ERR_SplitReplicationPairGroup = 0xA035
    ERR_ResyncReplicationPairGroup = 0xA036
    ERR_RestoreReplicationPairGroup = 0xA037
    ERR_DeleteReplicationPairGroup = 0xA038
    ERR_CreateSnapshotPair = 0xA03A
    ERR_CreateVVolAutoLunID = 0xA03F
    ERR_GetFreeRemoteCTG = 0xA048
    ERR_CreateTrueCopy = 0xA049
    ERR_SplitTrueCopy = 0xA04A
    ERR_ResyncTrueCopy = 0xA04B
    ERR_DeleteTrueCopy = 0xA04C
    ERR_ExpandLU = 0xA04E
    ERR_GetTrueCopyList = 0xA050
    ERR_ExpandDynamicPool = 0xA054
    ERR_GetFSS = 0xA05B
    ERR_CreateFileClone = 0xA060
    ERR_CreateCommandDevice = 0xA076
    ERR_CreateCommandDeviceParityGroup = 0xA080
    ERR_GetFreeUniversalReplicatorConsistencyGroup_1 = 0xA08A
    ERR_MapVirtualLogicalUnitID = 0xA08C
    ERR_UnmapVLUR = 0xA08D
    ERR_ShutdownHorcmInstance_1 = 0xA091
    ERR_CreateMultiSiteTrueCopyPair = 0xA04A
    ERR_CreateMultiSiteUniversalReplicatorPair = 0xA04B
    ERR_StartSecondaryHorcmInstance = 0xA04C
    ERR_GetFreeLun = 0xA014
    ERR_GetFSSnapshots = 0xA05E
    ERR_DeleteFSSnapshot = 0xA067
    ERR_SETHOSTMODE = 0xA06E
    ERR_GetISCSITargetList = 0xA074
    ERR_CreateISCSITarget = 0xA075
    ERR_DeleteISCSITarget = 0xA076
    ERR_AddInitiatorToISCSITarget = 0xA077
    ERR_EXPAND_DYNAMICPOOL = 0xA080
    ERR_SHRINK_DYNAMICPOOL = 0xA081
    ERR_DELETE_DYNAMICPOOL = 0xA082
    ERR_CREATE_DYNAMICPOOL = 0xA088
    ERR_UNMAPSNAPSHOTVOLUME = 0xA12A
    ERR_MAPSNAPSHOTVOLUME = 0xA12B
    ERR_FailToSetLogicalUnitQuorumDisk_1 = 0xA17A
    ERR_Remove_HOSTGROUP_LU = 0xA194
    ERR_AddHNASStorageDevice = 0xA19B
    ERR_CreateLuWithCSV = 0xA1BA
    ERR_GetFreeLunList = 0xA1C2
    ERR_ReclaimLUZeroPages_2 = 0xA1C3
    ERR_FormatFS = 0xA1CF
    ERR_CREATE_GAD_PAIR = 0xA1D4
    ERR_GetFreeLocalCTG = 0xA1D5
    ERR_DeleteFS = 0xA1D7
    ERR_MountFS = 0xA1D8
    ERR_UnmountFS = 0xA1D9
    ERR_AddRootHostsToNFSExport = 0xA1DC
    ERR_AddRWHostsToNFSExport = 0xA1DD
    ERR_CloseConnections = 0xA1DE
    ERR_CreateHUSSnapshotPair = 0xA1DF
    ERR_CreateMetaResourceLun = 0xA1E0
    ERR_DeleteInstance = 0xA1E1
    ERR_GetLoginWWNs = 0xA1E2
    ERR_GetLuList = 0xA1E3
    ERR_GetPorts = 0xA1E4
    ERR_GetSnapshotList = 0xA1E5
    ERR_GetStoragePools = 0xA1E6
    ERR_RemoveRootHostsFromNFSExport = 0xA1E7
    ERR_RemoveRWHostsFromNFSExport = 0xA1E8
    ERR_SplitShadowImageGroup = 0xA1E9
    ERR_GetRAIDStorageInfo = 0xA1EA
    ERR_GetFileServerInfo = 0xA1EB
    ERR_CloneLun = 0xA1EC    
    ERR_GET_SUPPORT_LOGS = 0xA1ED
    ERR_GET_NAS_FILE_SERVER_INFO = 0xA1EE
    ERR_GET_NAS_EVS_INFO = 0xA1EF
    ERR_GET_NAS_EXPORTS = 0xA1F0 
    ERR_OPERATION_HOSTGROUP = 0xA1F1
    ERR_OPERATION_LUN = 0xA1F2
    ERR_OPERATION_REPLICATIONS = 0xA1F3
    ERR_OPERATION_VSM = 0xA1F4
    ERR_OPERATION_HNAS = 0xA1F5
    