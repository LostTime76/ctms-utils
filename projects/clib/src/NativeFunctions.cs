using CeetemSoft.Text;
using CLibrary.MicroBuild;
using System.Runtime.InteropServices;

namespace CLibrary;

unsafe public static class NativeFunctions
{
	public static readonly delegate* unmanaged<void*, void> FreeMemory = &mem_free;

	public static readonly delegate* unmanaged<byte*, int, byte*> BuildEntry = &ubuild_entry;

	[UnmanagedCallersOnly(EntryPoint = nameof(mem_free))]
	public static void mem_free(void* memory)
	{
		NativeMemory.Free(memory);
	}

	[UnmanagedCallersOnly(EntryPoint = nameof(ubuild_entry))]
	public static byte* ubuild_entry(byte* json, int length)
	{
		try
		{
			BuildEngine.Run(MicroBuildJsonConfig.Deserialize(json, length));
		}
		catch(Exception e)
		{
			return NativeUtf8.Alloc(e.Message);
		}

		return null;
	}
}