using CeetemSoft.Io;
using CeetemSoft.Runtime;
using CeetemSoft.Text;
using CLibrary;
using CLibrary.MicroBuild;
using System.Text;

namespace Test;

unsafe public static class Program
{
	private static readonly string ProjectDirectory =
		Path.GetFullPath(Path.Combine(PathUtils.GetCurrentSourceDirectory(), "../../test"));

	private static readonly string OutputDirectory =
		Path.Combine(ProjectDirectory, "artifacts");

	private static readonly string SourceDirectory =
		Path.Combine(ProjectDirectory, "src");

	public static int Main()
	{
		// Compiler settings
		CompilerJsonConfig compiler = new()
		{
			Executable    = "clang",
			ObjectFormat  = "-o {0}",
			ObjectFileExt = ".o",
			SourceFormat  = "{0}"
		};

		// Linker settings
		LinkerJsonConfig linker = new()
		{
			Executable   = "ld.lld",
			ObjectFormat = "{0}"
		};

		// Select sources
		SourceSelectorJsonConfig[] sources = [

			// Set base directory for selection
			new() {
				Command   = SourceSelectorCommand.SetCurrentDirectory,
				Directory = SourceDirectory
			},

			// Include all of the possibles sources
			new() {
				Command   = SourceSelectorCommand.IncludeFiles,
				Recursion = int.MaxValue
			}
		];

		// Serialize the test config
		string json = MicroBuildJsonConfig.Serialize(new()
		{
			MaxThreads      = 1,
			OutputDirectory = OutputDirectory,
			Compiler        = compiler,
			Linker          = linker,
			Sources         = sources
		});

		// Convert the config into byte data
		ReadOnlySpan<byte> jdata = Encoding.UTF8.GetBytes(json);

		// Run the test build
		byte* error = NativeFunctions.BuildEntry(jdata.AsPointer(), jdata.Length);

		// Print any error
		ConsoleExtensions.WriteLineIfNotEmpty(NativeUtf8.GetString(error));

		// Free any error memory
		NativeFunctions.FreeMemory(error);

		// Exit the process
		return error != null ? 1 : 0;
	}
}