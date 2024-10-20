import shutil
import time

def ft_tqdm(lst: range) -> None:

	"""
	ft_tqdm(lst: range) -> None

	A custom implementation of a progress bar similar to tqdm. This function 
	takes an iterable and displays a loading bar in the terminal while iterating 
	through the provided range. It shows the progress percentage, a visual bar, 
	elapsed time, estimated remaining time, and iterations per second.

	Parameters:
	----------
	lst : range
		An iterable range to iterate through. The function will process each item 
		in the range, updating the progress bar accordingly.

	The output is formatted to show:
	- Progress percentage (0-100%)
	- Loading bar visually representing the progress
	- Elapsed time in MM:SS format
	- Estimated remaining time in MM:SS format
	- Iterations per second with two decimal precision
	"""

	l = len(lst)
	terminal_width = shutil.get_terminal_size().columns
	start = time.time()
	update = start
	for i, value in enumerate(lst):
		p = (i+1) / l * 100
		bar_len = terminal_width - 40
		fill = int(bar_len * (i+1) / l)
		loading_bar = '█' * fill + ' ' * (bar_len - fill)

		update = time.time()
		current_duration = update - start
		if p != 0:
			remaining = current_duration / (p/100) - current_duration
		s = int(current_duration % 60)
		m = int(current_duration // 60)
		rs = int(remaining % 60)
		rm = int(remaining // 60)
		itps = 0
		if current_duration > 0.1:
			itps = (i+1) / current_duration
		print(f"\r{int(p):3d}%|{loading_bar}| {i}/{l} [{m:02}:{s:02}<{rm:02}:{rs:02}, {itps:.2f}it/s]", end='')
		yield value
