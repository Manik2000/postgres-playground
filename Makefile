ruff: 
	ruff check .  --fix
	ruff format .
	
cleanup: rm -rf .ruff_cache