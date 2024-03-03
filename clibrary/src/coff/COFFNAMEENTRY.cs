using System.Runtime.InteropServices;

[StructLayout(LayoutKind.Explicit, Size = 8)]
internal struct COFFNAMEENTRY
{
	[FieldOffset(0)]
	internal int StrTabFlag;

	[FieldOffset(0)]
	internal int NameAddr;

	[FieldOffset(4)]
	internal int StrTabOffset;

	[FieldOffset(4)]
	internal int NameLen;
}