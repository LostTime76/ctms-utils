using CeetemSoft.Utils;
using CeetemSoft.Utils.Text;
using System.Runtime.InteropServices;

unsafe internal static class CoffUtils
{
	[UnmanagedCallersOnly(EntryPoint = "coff_load")]
	internal static bool Load(byte* data, int dlen, COFFIMAGEENTRY* coff)
	{
		if (dlen < sizeof(COFFHEADERENTRY))
		{
			Library.SetErrorMessage("The data does not comprise a valid coff image.");
			return false;
		}

		var   header     = (COFFHEADERENTRY*)data;
		var   target     = COFFTARGET.GetTargetFromId(BitUtils.ReadLe(header->TargetId));
		short magic      = BitUtils.ReadLe(header->Magic);
		short sectEnts   = BitUtils.ReadLe(header->SectEnts);
		int   secTabEnd  = sizeof(COFFHEADERENTRY) + sizeof(COFFSECTIONENTRY) * sectEnts;
		int   symTabAddr = BitUtils.ReadLe(header->SymTabAddr);
		int   symEnts    = BitUtils.ReadLe(header->SymEnts);
		int   strTabAddr = symTabAddr + sizeof(COFFSYMBOLENTRY) * symEnts;
		int   strTabLen  = dlen - strTabAddr;
		int   strTabEnd  = strTabAddr + strTabLen;
		int   entry      = BitUtils.ReadLe(header->Entry);

		if (magic != COFFHEADERENTRY.ValidMagic)
		{
			Library.SetErrorMessage($"Expected a magic value of {COFFHEADERENTRY.ValidMagic} " +
				$"within the image, but read {magic}.");
			return false;
		}
		else if (target == COFFTARGET.None)
		{
			Library.SetErrorMessage("The target chipset for the image is not valid.");
			return false;
		}
		else if ((ulong)secTabEnd > (ulong)dlen)
		{
			Library.SetErrorMessage("The image does not contain a valid section table.");
			return false;
		}
		else if (((ulong)secTabEnd > (ulong)symTabAddr) || ((ulong)strTabAddr > (ulong)dlen))
		{
			Library.SetErrorMessage("The image does not contain a valid symbol table.");
			return false;
		}
		else if ((ulong)strTabEnd > (ulong)dlen)
		{
			Library.SetErrorMessage("The image does not contain a valid string table.");
			return false;
		}

		coff->Data       = data;
		coff->DataLen    = dlen;
		coff->TargetId   = target.Id;
		coff->Entry      = entry;
		coff->SectEnts   = sectEnts;
		coff->StrTabAddr = strTabAddr;

		return true;
	}

	[UnmanagedCallersOnly(EntryPoint = "coff_sects")]
	internal static bool LoadSections(COFFIMAGEENTRY* coff, COFFSECTIONENTRY* sects)
	{
		byte* src      = coff->Data;
		int   srcl     = coff->DataLen;
		int   lenShift = COFFTARGET.GetTargetFromId(coff->TargetId).IsByteAddressable ? 0 : 1;

		COFFSECTIONENTRY* entry = (COFFSECTIONENTRY*)&src[sizeof(COFFHEADERENTRY)];

		for (int idx = 0; idx < coff->SectEnts; idx++, entry++)
		{
			var sect  = &sects[idx];
			var flags = new COFFSECTIONFLAGS(BitUtils.ReadLe(entry->Flags));
			int paddr = BitUtils.ReadLe(entry->PhysAddr) << lenShift;
			int vaddr = BitUtils.ReadLe(entry->VirtAddr) << lenShift;
			int dlen  = BitUtils.ReadLe(entry->DataLen) << (flags.Allocated ? lenShift : 0);
			int daddr = BitUtils.ReadLe(entry->DataAddr);
			int naddr = GetNameAddress(coff, &entry->Name, out int maxNameBytes);

			if ((((ulong)daddr + (ulong)dlen) > (ulong)srcl) || (maxNameBytes == 0))
			{
				Library.SetErrorMessage($"The section at index {idx} within the image is not " +
					"valid.");
				return false;
			}

			sect->Name.NameAddr = naddr;
			sect->Name.NameLen  = Utf8Utils.GetLength(&src[naddr], maxNameBytes);
			sect->PhysAddr      = paddr;
			sect->VirtAddr      = vaddr;
			sect->DataLen       = dlen;
			sect->DataAddr      = daddr;
			sect->Flags         = flags;
		}

		return true;
	}

	[UnmanagedCallersOnly(EntryPoint = "coff_copy_sects")]
	private static void CopySections(
		int addr,
		int len,
		byte* src, 
		byte* dst, 
		COFFSECTIONENTRY* sects,
		int nsects)
	{
		int endAddr = addr + len;

		for (int idx = 0; idx < nsects; idx++)
		{
			var sect  = &sects[idx];
			int daddr = sect->DataAddr;
			int dlen  = sect->DataLen;
			int paddr = sect->PhysAddr;
			int vaddr = sect->VirtAddr;

			if ((paddr >= addr) && ((paddr + dlen) <= endAddr))
			{
				NativeMemory.Copy(&src[daddr], &dst[paddr - addr], (nuint)dlen);
			}
			else if ((vaddr >= addr) && ((vaddr + dlen) <= endAddr))
			{
				NativeMemory.Copy(&src[daddr], &dst[vaddr - addr], (nuint)dlen);
			}
		}
	}

	private static int GetNameAddress(COFFIMAGEENTRY* coff, COFFNAMEENTRY* name, out int maxBytes)
	{
		if (name->StrTabFlag != 0)
		{
			maxBytes = sizeof(COFFNAMEENTRY);
			return (int)((long)name - (long)coff->Data);
		}

		int dlen   = coff->DataLen;
		int offset = BitUtils.ReadLe(name->StrTabOffset);
		int start  = coff->StrTabAddr + offset;
		int max    = dlen - start;

		// Make sure max bytes is valid
		maxBytes = ((ulong)start + (ulong)max) <= (ulong)dlen ? max : 0;

		// Return the offset relative to the start of the image
		return start;
	}
}