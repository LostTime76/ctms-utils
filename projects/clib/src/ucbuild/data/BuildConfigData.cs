using CeetemSoft.Native;
using System.Diagnostics.CodeAnalysis;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Text.Json.Serialization.Metadata;

namespace Library.MicroBuild.Data;

public class BuildConfigData
{
	private static readonly JsonTypeInfo<BuildConfigData> JsonType =
		JsonDataContext.Default.BuildConfigData;

	unsafe internal static BuildConfigData Deserialize(byte* json)
	{
		return Deserialize(new ReadOnlySpan<byte>(json, NativeUtf8.GetLength(json)));
	}

	internal static BuildConfigData Deserialize(ReadOnlySpan<byte> json)
	{
		BuildConfigData? config = JsonSerializer.Deserialize(json, JsonType);

		if (config == null)
		{
			ThrowInvalidConfig();
		}

		return config;
	}

	[DoesNotReturn]
	private static void ThrowInvalidConfig()
	{
		throw new ArgumentNullException("The build configuration is not valid.");
	}

	[JsonPropertyName("max_threads")]
	public int MaxThreads { get; init; }

	[JsonPropertyName("incs")]
	public string[]? Includes { get; init; }

	[JsonPropertyName("defs")]
	public string[]? Defines { get; init; }

	[JsonPropertyName("libs")]
	public string[]? Libraries { get; init; }

	[JsonPropertyName("cc_spec")]
	public CompilerSpecData? Compiler { get; init; }

	[JsonPropertyName("ld_spec")]
	public LinkerSpecData? Linker { get; init; }

	[JsonPropertyName("sources")]
	public SourceSelectorData[]? Sources { get; init; }
}