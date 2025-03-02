from pathlib import Path
from typing import Iterable

class SourceFile:

	include : bool

	_fpath : Path
	
	def __init__(self, fpath: Path):
		self._fpath  = fpath
		self.include = False

	@property
	def fpath(self) -> Path:
		return self._fpath

class SourceDir:

	_dpath : Path
	_cdirs : list[SourceDir]
	_files : dict[str, SourceFile]
	
	def __init__(self, dpath: Path, fexts: set[str]):
		self._dpath = dpath
		self._cdirs = []
		self._files = dict()
		self._iter_dir(fexts)

	def inc(self, files: list[str] | None, include: bool):
		if files is None:
			self._inc_all(include)
			return
		for file in files:
			if file in self._files:
				self._files[file].include = include

	def r_inc(self, include: bool):
		for file in self._files.values():
			file.include = include
		for cdir in self._cdirs:
			cdir.r_inc(include)

	def _inc_all(self, include: bool):
		for file in self._files.values():
			file.include = include

	def _iter_dir(self, fexts: set[str]):
		for path in self._dpath.iterdir():
			if path.is_file():
				if path.suffix in fexts:
					self._files[path.name] = SourceFile(path)
			elif path.is_dir():
				self._cdirs.append(SourceDir(path, fexts))

	@property
	def dpath(self) -> Path:
		return self._dpath
	
	@property
	def files(self) -> Iterable[SourceFile]:
		return self._files.values()

	@property
	def cdirs(self) -> list[SourceDir]:
		return self._cdirs

class SourceTree:

	_as_fexts  : set[str]
	_c_fexts   : set[str]
	_cpp_fexts : set[str] | None
	_fexts     : set[str]
	_root      : SourceDir
	_dirs      : dict[Path, SourceDir]

	def __init__(self,
		root: Path | None,
		as_fexts: set[str],
		c_fexts: set[str],
		cpp_fexts: set[str] | None):

		self._as_fexts  = as_fexts
		self._c_fexts   = c_fexts
		self._cpp_fexts = cpp_fexts
		self._fexts     = as_fexts | c_fexts | (cpp_fexts if cpp_fexts else set())
		self._root      = SourceDir(root if root else Path.cwd(), self._fexts)
		self._dirs      = self._create_dir_tab()
	
	def inc(self, dir: Path, files: list[str] | None = None, include: bool = True):
		if dir in self._dirs:
			self._dirs[dir].inc(files, include)

	def r_inc(self, dir: Path, include: bool = True):
		if dir in self._dirs:
			self._dirs[dir].r_inc(include)

	def sources(self) -> list[Path]:
		sources = []
		self._update_sources(self._root, sources)
		return sources

	def _create_dir_tab(self) -> dict[Path, SourceDir]:
		table = dict()
		self._update_dirs(self._root, table)
		return table
	
	@staticmethod
	def _update_sources(dir: SourceDir, sources: list[Path]):
		for file in dir.files:
			if file.include:
				sources.append(file.fpath)
		for child in dir.cdirs:
			SourceTree._update_sources(child, sources)
	
	@staticmethod
	def _update_dirs(dir: SourceDir, table: dict[Path, SourceDir]):
		table[dir.dpath] = dir
		for child in dir.cdirs:
			SourceTree._update_dirs(child, table)

	@property
	def root(self) -> Path:
		return self._root.dpath