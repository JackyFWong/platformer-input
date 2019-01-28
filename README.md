# platformer-input
A Python program to parse a given JSON file to virtualize keyboard inputs.  
Designed especially for a platformer running at 60 fps.

Also includes TAS (tool assisted speedrun) json files for various stages in 
[Dessert Dive](https://github.com/HarrisonHall/Dessert_Dive).

Created in January 2019 for 
![CUhackit logo](https://cuhack.it/images/CUhackit_Combined_Logo_RGB_Color_STANDARD.svg "CUhackit 2019")

### Required dependencies
Install [`keyboard`](https://github.com/boppreh/keyboard):
```
pip install keyboard
```

## Execution
* Execute via `sudo python3 virtual_key.py [folder_name/file_name.json]`
* Location for TAS json should go in a user-made appropriate game folder in `games`

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
If more than one pair of `dur` and `key` are added in the same `cmd`, they will be executed
all at once, being de-pressed according to their number of frames respectively.

`num` gives the number of times to execute the given list of keys.

#### Credits
Jacky Wong, Kaleb Chestnut
