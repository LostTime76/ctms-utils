using System.Diagnostics.CodeAnalysis;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Text.Json.Serialization.Metadata;

namespace CLibrary.MicroBuild;

public class CompilerJsonConfig
{
	[JsonPropertyName("exe_path")]
	public required string Executable { get; init; }

	[JsonPropertyName("obj_fmt")]
	public required string ObjectFormat { get; init; }

	[JsonPropertyName("obj_ext")]
	public required string ObjectFileExt { get; init; }

	[JsonPropertyName("src_fmt")]
	public required string SourceFormat { get; init; }

	[JsonPropertyName("rsp_fmt")]
	public string? ResponseFormat { get; init; }

	[JsonPropertyName("rsp_ext")]
	public string? ResponseFileExt { get; init; }

	[JsonPropertyName("deps_fmt")]
	public string? DependsFormat { get; init; }

	[JsonPropertyName("deps_ext")]
	public string? DependsFileExt { get; init; }

	[JsonPropertyName("inc_fmt")]
	public string? IncludeFormat { get; init; }

	[JsonPropertyName("def_fmt")]
	public string? DefineFormat { get; init; }

	[JsonPropertyName("includes")]
	public string[]? Includes { get; init; }

	[JsonPropertyName("defines")]
	public string[]? Defines { get; init; }

	[JsonPropertyName("src_exts")]
	public string[]? SourceFileExts { get; init; }
}

public class LinkerJsonConfig
{
	[JsonPropertyName("exe_path")]
	public required string Executable { get; init; }

	[JsonPropertyName("obj_fmt")]
	public required string ObjectFormat { get; init; }

	[JsonPropertyName("rsp_fmt")]
	public string? ResponseFormat { get; init; }

	[JsonPropertyName("rsp_ext")]
	public string? ResponseFileExt { get; init; }

	[JsonPropertyName("lib_fmt")]
	public string? LibraryFormat { get; init; }

	[JsonPropertyName("in_fmts")]
	public string[]? InputFormats { get; init; }

	[JsonPropertyName("out_fmts")]
	public string[]? OutputFormats { get; init; }

	[JsonPropertyName("libs")]
	public string[]? Libraries { get; init; }

	[JsonPropertyName("inputs")]
	public string[]? Inputs { get; init; }

	[JsonPropertyName("outputs")]
	public string[]? Outputs { get; init; }
}

public class SourceSelectorJsonConfig
{
	[JsonPropertyName("cmd")]
	public SourceSelectorCommand Command { get; init; }

	[JsonPropertyName("recurse")]
	public int Recursion { get; init; }

	[JsonPropertyName("dir")]
	public string? Directory { get; init; }

	[JsonPropertyName("pattern")]
	public string? Pattern { get; init; }

	[JsonPropertyName("files")]
	public string[]? Files { get; init; }
}

public class MicroBuildJsonConfig
{
	private static readonly JsonTypeInfo<MicroBuildJsonConfig> JsonType =
		MicroBuildJsonContext.Default.MicroBuildJsonConfig;

	public static string Serialize(MicroBuildJsonConfig config)
	{
		return JsonSerializer.Serialize(config, JsonType);
	}

	unsafe public static MicroBuildJsonConfig Deserialize(byte* json, int length)
	{
		return Deserialize((json != null) && (length >= 0) ? new (json, length) : default);
	}

	public static MicroBuildJsonConfig Deserialize(ReadOnlySpan<byte> json)
	{
		MicroBuildJsonConfig? config = JsonSerializer.Deserialize(json, JsonType);

		if (config == null)
		{
			ThrowInvalidJson();
		}

		return config;
	}

	[DoesNotReturn]
	private static void ThrowInvalidJson()
	{
		throw new JsonException("The json is not valid.");
	}

	[JsonPropertyName("max_threads")]
	public int MaxThreads { get; init; }

	[JsonPropertyName("out_dir")]
	public string? OutputDirectory { get; init; }

	[JsonPropertyName("cc")]
	public required CompilerJsonConfig Compiler { get; init; }

	[JsonPropertyName("ld")]
	public required LinkerJsonConfig Linker { get; init; }

	[JsonPropertyName("sources")]
	public SourceSelectorJsonConfig[]? Sources { get; init; }
}

[JsonSourceGenerationOptions(
	WriteIndented = true,
	IndentCharacter = '\t',
	IndentSize = 1,
	RespectNullableAnnotations = true)]
[JsonSerializable(typeof(MicroBuildJsonConfig))]
public partial class MicroBuildJsonContext : JsonSerializerContext { }