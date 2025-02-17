using System.Text.Json.Serialization;

namespace Library.MicroBuild;

[JsonConverter(typeof(JsonStringEnumConverter<SourceSelectorCommand>))]
public enum SourceSelectorCommand
{
	[JsonStringEnumMemberName("set_dir")]
	SetDirectory,

	[JsonStringEnumMemberName("include")]
	Include,

	[JsonStringEnumMemberName("exclude")]
	Exclude
}