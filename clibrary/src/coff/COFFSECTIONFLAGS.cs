using System.Runtime.CompilerServices;

internal readonly struct COFFSECTIONFLAGS
{
	private const int TEXT_FLAG = 0x20;
	private const int DATA_FLAG = 0x40;
	private const int BSS_FLAG  = 0x80;

	private readonly int _data;

	public COFFSECTIONFLAGS(int data)
	{
		_data = data;
	}

	[MethodImpl(MethodImplOptions.AggressiveInlining | MethodImplOptions.AggressiveOptimization)]
	public static implicit operator int (COFFSECTIONFLAGS flags)
	{
		return flags._data;
	}

	[MethodImpl(MethodImplOptions.AggressiveInlining | MethodImplOptions.AggressiveOptimization)]
	public static implicit operator COFFSECTIONFLAGS (int data)
	{
		return new(data);
	}

	public bool Allocated => (_data & (TEXT_FLAG | DATA_FLAG | BSS_FLAG)) != 0;
}