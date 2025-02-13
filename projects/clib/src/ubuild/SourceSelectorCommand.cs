using System.Text.Json.Serialization;

namespace CLibrary.MicroBuild;

[JsonConverter(typeof(JsonStringEnumConverter<SourceSelectorCommand>))]
public enum SourceSelectorCommand
{
	[JsonStringEnumMemberName("set_cd")]
	SetCurrentDirectory,

	[JsonStringEnumMemberName("include")]
	IncludeFiles,

	[JsonStringEnumMemberName("exclude")]
	ExcludeFiles
}