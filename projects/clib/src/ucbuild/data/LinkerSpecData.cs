using System.Text.Json.Serialization;

namespace Library.MicroBuild.Data;

public class LinkerSpecData
{
	[JsonPropertyName("exe")]
	public required string Executable { get; init; }

	[JsonPropertyName("rsp")]
	public ResponseSpecData? Response { get; init; }

	[JsonPropertyName("frags")]
	public SpecFragmentData[]? Fragments { get; init; }
}