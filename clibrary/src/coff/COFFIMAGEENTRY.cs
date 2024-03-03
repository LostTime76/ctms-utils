using System.Runtime.InteropServices;

[StructLayout(LayoutKind.Explicit, Size = 24)]
unsafe internal struct COFFIMAGEENTRY
{
	[FieldOffset(0)]
	internal byte* Data;

	[FieldOffset(8)]
	internal int DataLen;

	[FieldOffset(12)]
	internal short TargetId;

	[FieldOffset(14)]
	internal short SectEnts;

	[FieldOffset(16)]
	internal int Entry;

	[FieldOffset(20)]
	internal int StrTabAddr;
}