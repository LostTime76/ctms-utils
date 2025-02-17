using System.Text.Json.Serialization;

namespace Library.MicroBuild.Data;

public readonly struct SpecFragmentData
{
	[JsonPropertyName("type")]
	public required SpecFragmentType Type { get; init; }

	[JsonPropertyName("cont")]
	public bool Continue { get; init; }

	[JsonPropertyName("str")]
	public object? String { get; init; }

	[JsonPropertyName("fmt")]
	public string? Format { get; init; }

	[JsonPropertyName("fext")]
	public string? FileExt { get; init; }

	[JsonPropertyName("key")]
	public string? Key { get; init; }
}