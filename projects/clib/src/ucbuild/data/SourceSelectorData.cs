using System.Text.Json.Serialization;

namespace Library.MicroBuild.Data;

public readonly struct SourceSelectorData
{
	[JsonPropertyName("cmd")]
	public required SourceSelectorCommand Command { get; init; }

	[JsonPropertyName("recurse")]
	public bool Recurse { get; init; }

	[JsonPropertyName("dir")]
	public string? Directory { get; init; }

	[JsonPropertyName("pattern")]
	public string? Pattern { get; init; }

	[JsonPropertyName("files")]
	public string[]? Files { get; init; }
}