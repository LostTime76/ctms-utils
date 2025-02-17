using CeetemSoft.Native;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Text.Json.Serialization.Metadata;

namespace Library.MicroBuild.Data;

public readonly struct BuildResultData
{
	private static readonly JsonTypeInfo<BuildResultData> JsonType =
		JsonDataContext.Default.BuildResultData;

	public string Serialize()
	{
		return JsonSerializer.Serialize(this, JsonType);
	}

	unsafe public byte* SerializeToNative()
	{
		return NativeUtf8.Alloc(Serialize());
	}

	unsafe public static BuildResultData Deserialize(byte* json)
	{
		return Deserialize(new ReadOnlySpan<byte>(json, NativeUtf8.GetLength(json)));
	}

	unsafe public static BuildResultData Deserialize(ReadOnlySpan<byte> json)
	{
		return JsonSerializer.Deserialize(json, JsonType);
	}

	[JsonPropertyName("linked")]
	public bool Linked { get; init; }

	[JsonPropertyName("success")]
	public bool Success { get; init; }

	[JsonPropertyName("msg")]
	public string? Message { get; init; }
}