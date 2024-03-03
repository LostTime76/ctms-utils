using System.Runtime.InteropServices;

[StructLayout(LayoutKind.Explicit, Size = 50)]
internal struct COFFHEADERENTRY
{
	internal const int ValidMagic = 0x0108;
	
	[FieldOffset(2)]
	internal short SectEnts;

	[FieldOffset(8)]
	internal int SymTabAddr;

	[FieldOffset(12)]
	internal int SymEnts;

	[FieldOffset(20)]
	internal short TargetId;

	[FieldOffset(22)]
	internal short Magic;

	[FieldOffset(38)]
	internal int Entry;
}