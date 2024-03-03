using System.Runtime.CompilerServices;

internal readonly struct COFFTARGET
{
	private const int ByteAddressableFlag = 1 << 17;
	private const int IdMask              = 0xFFFF;

	internal static readonly COFFTARGET TMS470       = new(ByteAddressableFlag | 0x97);
	internal static readonly COFFTARGET TMS320C5400  = new(0x98);
	internal static readonly COFFTARGET TMS320C6000  = new(ByteAddressableFlag | 0x99);
	internal static readonly COFFTARGET TMS320C5500  = new(ByteAddressableFlag | 0x9C);
	internal static readonly COFFTARGET TMS320C2800  = new(0x9D);
	internal static readonly COFFTARGET MSP430       = new(ByteAddressableFlag | 0xA0);
	internal static readonly COFFTARGET None         = new();
	internal static readonly COFFTARGET TMS320C5500P = new(ByteAddressableFlag | 0xA1);

	private static readonly Dictionary<int, COFFTARGET> _targets = new() {
		{ TMS470.Id, TMS470 },
		{ TMS320C5400.Id, TMS320C5400 },
		{ TMS320C6000.Id, TMS320C6000 },
		{ TMS320C5500.Id, TMS320C5500 },
		{ TMS320C2800.Id, TMS320C2800 },
		{ MSP430.Id, MSP430 },
		{ TMS320C5500P.Id, TMS320C5500P }
	};

	private readonly int _data;

	private COFFTARGET(int data)
	{
		_data = data;
	}

	public override bool Equals(object? target)
	{
		return target != null && ((COFFTARGET)target) == this;
	}

	public override int GetHashCode()
	{
		return _data.GetHashCode();
	}

	[MethodImpl(MethodImplOptions.AggressiveInlining | MethodImplOptions.AggressiveOptimization)]
	public static COFFTARGET GetTargetFromId(int id)
	{
		return _targets.TryGetValue(id, out COFFTARGET target) ? target : None;
	}

	public static bool operator ==(COFFTARGET a, COFFTARGET b)
	{
		return a._data == b._data;
	}

	public static bool operator !=(COFFTARGET a, COFFTARGET b)
	{
		return a._data == b._data;
	}

	internal bool IsByteAddressable => (_data & ByteAddressableFlag) != 0;

	internal short Id => (short)(_data & IdMask);
}