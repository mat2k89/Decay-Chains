# Getting Started

## Setting Up Your Files

To get started, fork this repository. If you're working in a group, only one person should fork this repository and give the others access through making them collaborators. Each team member should clone the repository to their computer so they can work on their own local version. You can use normal collaboration techniques such as branches and merge requests to manage the collaboration of team members.

You should write your code in ```src``` directory.

## Requirements

You are free to use whichever packages you wish to complete this project. However, this project comes with a sample solution in the directory ```sample solution```. To run this code, you will require the following packages:

* Numpy
* SciPy
* Matplotlib

You can install these manually, or through the requirements file.

## Setting up your Editor

This resource was developed using VS Code and the settings file contains a number of setting you may find convenient. If you're using VS Code and want to use different settings, feel free to edit it. If you're using a different editor, feel free to set it up however you wish.

## Setting Up Tests

This resource provides tests to allow you to test your solutions to various tasks. These tests are stored in the ```tests``` directory and are named to correspond to the tasks they relate to. These tests are written using ```unittest```. Because there are tests to every step of the project, even when you complete an earlier activity successfully, there will be tests associated with later activities which will fail.

In order to use these, you will need to edit the file ```src/test_interfaces.py``` file. this contains a number of functions which you should edit to utilise the tools you have written as part of the tasks. These functions will be called by the tests when they are run. You should write the code to complete the tasks however you think makes most sense, then work out how to define the functions in ```src/test_interfaces.py``` to interface with your code.

To run the tests, you can use the command ```python -m unittest``` in the main directory of the repository.

Note: as you develop your project, you may wish to add more tests to check your code is behaving how you expect.

## Task 0

For now, have a go at editing the first two functions ```task_0_always_return_0``` and ```task_0_addition``` in ```src/test_interfaces.py```. When you have done this successfully, you should see that the tests in the file ```tests/test_0.py``` all pass.


