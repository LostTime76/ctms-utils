using CeetemSoft.Utils;
using System.Runtime.InteropServices;

unsafe internal static class BitOperations
{
	[UnmanagedCallersOnly(EntryPoint = "rev16")]
	internal static void Rev16(byte* data, int dlen)
	{
		BitUtils.Rev16(new Span<byte>(data, dlen));
	}

	[UnmanagedCallersOnly(EntryPoint = "crc32")]
	internal static int Crc32(byte* data, int dlen)
	{
		return (int)System.IO.Hashing.Crc32.HashToUInt32(new ReadOnlySpan<byte>(data, dlen));
	}
}