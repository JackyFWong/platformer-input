# platformer-input
A Python program to parse a given JSON file to virtualize keyboard inputs.
Designed especially for a platformer running at 60 fps.

Created in January 2019 for 
![CUhackit logo](https://cuhack.it/images/CUhackit_Combined_Logo_RGB_Color_STANDARD.svg "CUhackit 2019")

### Required dependencies
Install [`keyboard`](https://github.com/boppreh/keyboard):
```
pip install keyboard
```

## Formatting
`type` gives the type of data that follows. Can only be either `key` or `comment`.

`cmd` gives the data to be used.
- `comment` types will be printed on the console. It should follow this format:
```
"cmd" : "[your comment goes here]"
```
- `key` type should follow this format:
```
"cmd" : [
	{
		"dur" : [number of frames out of 60],
		"key" : "[key to be pressed]"
	},
	{	[more can be added, following the above format] }
]
```
⋅⋅⋅If more than one pair of `dur` and `key` are added in the same `cmd`, they will be executed
all at once, being de-pressed according to their number of frames respectively.

#### Credits
Jacky Wong, Kaleb Chestnut
