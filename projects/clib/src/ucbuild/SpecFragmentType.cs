using System.Text.Json.Serialization;

namespace Library.MicroBuild;

[JsonConverter(typeof(JsonStringEnumConverter<SpecFragmentType>))]
public enum SpecFragmentType
{
	[JsonStringEnumMemberName("str")]
	String,

	[JsonStringEnumMemberName("opts")]
	Options,

	[JsonStringEnumMemberName("src")]
	Source,

	[JsonStringEnumMemberName("incs")]
	Includes,

	[JsonStringEnumMemberName("defs")]
	Defines,

	[JsonStringEnumMemberName("deps")]
	Depends,

	[JsonStringEnumMemberName("libs")]
	Libraries,

	[JsonStringEnumMemberName("objs")]
	Objects,

	[JsonStringEnumMemberName("ins")]
	InputString,

	[JsonStringEnumMemberName("inf")]
	InputFile,

	[JsonStringEnumMemberName("outf")]
	OutputFile
}