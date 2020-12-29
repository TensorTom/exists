from typing import AnyStr, Optional, Union, Literal
from datafunc import listlike


def exists(var: Union[AnyStr], scope: Optional[str] = 'any') -> bool:
	"""
	Check for existence of a variable by name.
	:param var: The string representation/name of the variable (Required).
	:param scope: Where to look. Defaults to 'all'/local + global (Optional).
	:return: Boolean - True if var exists, False if not exist.
	"""
	_scope = scope.lower()
	if _scope in ('any', 'local') and var in locals():
		return True
	elif _scope in ('any', 'global') and var in globals():
		return True
	else:
		return False
