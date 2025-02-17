using Library.MicroBuild.Data;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace Library;

[JsonSourceGenerationOptions(
	WriteIndented = true,
	RespectNullableAnnotations = true,
	AllowTrailingCommas = true,
	ReadCommentHandling = JsonCommentHandling.Skip)]
[JsonSerializable(typeof(BuildConfigData))]
[JsonSerializable(typeof(BuildResultData))]
internal partial class JsonDataContext : JsonSerializerContext { }