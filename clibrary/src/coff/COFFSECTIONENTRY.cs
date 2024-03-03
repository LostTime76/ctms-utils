using System.Runtime.InteropServices;

[StructLayout(LayoutKind.Explicit, Size = 48)]
internal struct COFFSECTIONENTRY
{
	[FieldOffset(0)]
	internal COFFNAMEENTRY Name;

	[FieldOffset(8)]
	internal int PhysAddr;

	[FieldOffset(12)]
	internal int VirtAddr;

	[FieldOffset(16)]
	internal int DataLen;

	[FieldOffset(20)]
	internal int DataAddr;

	[FieldOffset(40)]
	internal COFFSECTIONFLAGS Flags;
}