# Metrics Application

## Description

The goal of this milestone overall is to create a simple system that can transport metrics data from a classroom with no Internet connectivity to a remote Internet server, by “hitchhiking” the data on an Android smartphone

## Installation

Before you can run this application, you'll need to install the following dependencies:

1. Python 3.8 or later: You can download it from [the official website](https://www.python.org/downloads/).
2. grpcio-tools: Install it using pip with the command `pip install grpcio-tools`.
3. grpclib: Install it using pip with the command `pip install grpclib`.

## Running the Application

To run this application, follow these steps:

1. Clone the repository: `git clone https://github.com/Nsovo/metrics_data.git`
2. Navigate to the repository directory: `cd metrics-app`
3. Run the application: `python app.py`

## Running the Tests
1. python -m unittest test_app

## Improvement Plan


1. **Error Handling**: Currently, the application does not handle all possible errors gracefully. The code by adding more try/except blocks to catch and handle potential errors.

2. **Testing**: While we have some basic unit tests, we could improve our test coverage. This would help us catch and fix bugs more quickly, and it would make it easier to add new features in the future.

3. **Performance**: There may be some areas where the application's performance could be improved. For example, we could look into optimizing the gRPC calls or the data processing code.

4. **Documentation**: While we have a basic README, we could improve our documentation. This would make it easier for new developers to understand and contribute to the project.

5. **Code Organization**: The code could be better organized. We could look into refactoring the code to make it more modular and easier to maintain.

Please note that these are just suggestions, and the specific improvements needed may vary depending on the specifics of the code and the requirements of the project.
