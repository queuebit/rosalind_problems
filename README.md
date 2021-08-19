## Rosalind Problems
This is a location for me to keep track of my attempts to solve the problems of <http://rosalind.info/problems/tree-view/>


## File structure
At a high level files are structured as follows:

* Folder with problem id (e.g. DNA/)
	* ROS_{ID}.rb - Ruby file that does much of the work to solve problem (or other languages)
	* ROS_{ID}.in - optional input file used for testing the script

## Example to run commands

```zsh
% cat rosalind_dna_4_dataset.txt | ./ros_dna.py | tail -1
233 240 272 236
```

## Other Resources
* [Search github](https://github.com/search?l=Ruby&p=1&q=rosalind&ref=commandbar) for other examples of rosalind solutions in Ruby
