using System.Runtime.InteropServices;
using CeetemSoft.Utils.Text;

unsafe internal static class Library
{
	[ThreadStatic]
	private static string? _errMsg;

	[UnmanagedCallersOnly(EntryPoint = "free_mem")]
	internal static void Free(void* memory)
	{
		NativeMemory.Free(memory);
	}

	[UnmanagedCallersOnly(EntryPoint = "get_errmsg")]
	internal static byte* GetErrorMessage()
	{
		// If the error message is null, a null pointer is returned
		byte* msg = Utf8Utils.Alloc(_errMsg);

		// Clear the error indicator
		_errMsg = null;

		// Return the message
		return msg;
	}

	internal static void SetErrorMessage(string message)
	{
		_errMsg = message;
	}
}