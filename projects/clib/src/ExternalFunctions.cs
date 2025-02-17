using Library.MicroBuild;
using Library.MicroBuild.Data;
using System.Runtime.InteropServices;

namespace Library;

unsafe public static class ExternalFunctions
{
	public static readonly delegate* unmanaged<byte*, byte*> BuildEntry = &ubuild_entry;

	[UnmanagedCallersOnly(EntryPoint = "mem_free")]
	internal static void mem_free(void* memory)
	{
		NativeMemory.Free(memory);
	}

	[UnmanagedCallersOnly(EntryPoint = nameof(ubuild_entry))]
	internal static byte* ubuild_entry(byte* json)
	{
		if (json == null)
		{
			return null;
		}

		try
		{
			var data   = BuildConfigData.Deserialize(json);
			var config = new BuildConfig(data);
			var engine = new BuildEngine(config);

			return new BuildResultData() {
				Success = engine.Run(),
				Linked  = engine.Linked
			}.SerializeToNative();
		}
		catch(Exception e)
		{
			return new BuildResultData() {
				Message = e.Message
			}.SerializeToNative();
		}
	}
}