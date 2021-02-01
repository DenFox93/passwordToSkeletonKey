# passwordToSkeletonKey
The Skeleton key by default is “mimikatz” that converted to NT hash is “60BA4FCADC466C7A033C178194C03DF6”. This password will work for any account in the domain. 

The skeleton key is defined two times first in the function “kuhl_misc_skeleton_rc4_init” and then in “kuhl_misc_skeleton_rc4_init_decryp”

• New versions of mimikatz →  in the source code file kuhl_m_misc.c(lines:607,634)as the parameter:
    
    DWORD kiwiKey[] = {0xca4fba60, 0x7a6c46dc, 0x81173c03, 0xf63dc094};”
    
• Old versions of mimikatz → in the source code file kuhl_m_misc.c(lines:672,700)
    
    BYTE kiwiKey[] = {0x60, 0xba, 0x4f, 0xca, 0xdc, 0x46, 0x6c, 0x7a, 0x03, 0x3c, 0x17, 0x81, 0x94, 0xc0, 0x3d, 0xf6};

We can run it also by directly using wget: 

    wget -qO - https://raw.githubusercontent.com/DenFox93/passwordToSkeletonKey/main/converter.py | python -- - <PASSWORD>

