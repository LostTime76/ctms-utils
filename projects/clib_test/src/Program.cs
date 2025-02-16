
using System.Text.RegularExpressions;
using CeetemSoft.Io;

namespace Test;

unsafe public static partial class Program
{
	private const string BuildFilename      = "build.json";
	private const string OutputDirectoryKey = "out_dir";
	private const string SourceDirectoryKey = "src_dir";

	private static readonly string ProjectDirectory =
		Path.GetFullPath(Path.Combine(PathUtils.GetCurrentSourceDirectory(), "../../test"));

	private static readonly string OutputDirectory =
		Path.Combine(ProjectDirectory, "artifacts");

	private static readonly string SourceDirectory =
		Path.Combine(ProjectDirectory, "src");

	private static readonly Regex JsonPattern = GetJsonPattern();

	public static void Main()
	{
		string json = GetBuildJson();
	}

	private static string GetBuildJson()
	{
		return JsonPattern.Replace(File.ReadAllText(BuildFilename), ReplaceJsonPlaceholder);
	}

	private static string ReplaceJsonPlaceholder(Match match)
	{
		switch(match.Groups[1].Value)
		{
			case OutputDirectoryKey:
				return PathUtils.NormalizePath(OutputDirectory);
			case SourceDirectoryKey:
				return PathUtils.NormalizePath(SourceDirectory);
			default:
				return string.Empty;
		}
	}

	[GeneratedRegex("\\${([^}]*)}")]
	private static partial Regex GetJsonPattern();
}