using System.Runtime.InteropServices;

[StructLayout(LayoutKind.Explicit, Size = 18)]
internal struct COFFSYMBOLENTRY
{
	[FieldOffset(0)]
	internal COFFNAMEENTRY Name;
}