# texture-synthesis

## How to
To run the texture synthesis program, use Python3 with Matplotlib, Numpy, & Pillow to run main.py.  It is recommended to use Anaconda to ensure that these packages are available.
The demo script provided, examples.sh, runs the main program multiple times; this is a good reference for how to run the main.py script. 
The individual algorithm files are not able to be run by themselves, but can be incoprorated into other scripts using the interface provided by the abstract synthesizer class.

## Implementation
### main.py
This main file runs the texture synthesis and validates all inputs; texture synthesis implementations do not necessarily validate their own inputs and may raise Value Errors if they cannot use the given arguments.
This main file is runnable by the Linux shell assuming your user has Python3 installed. 
To add more synthesis algorithms, simply add an instance to the algorithms dictionary near the top of the file.  
### AbstractSynthesizer.py
This is the abstract base class for texture synthesis algorithms; it was written to make switching between algorithms easier when I fail to implement one.
This class requires that a description and synthesis algorithm be provided.

## References
