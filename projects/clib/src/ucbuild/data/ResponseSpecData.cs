using System.Text.Json.Serialization;

namespace Library.MicroBuild.Data;

public class ResponseSpecData
{
	[JsonPropertyName("fmt")]
	public required string Format { get; init; }

	[JsonPropertyName("fext")]
	public string? FileExt { get; init; }

	[JsonPropertyName("fname")]
	public string? Filename { get; init; }
}